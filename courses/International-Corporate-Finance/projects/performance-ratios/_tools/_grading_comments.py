"""Shared scaffolding for student-facing comments across grade_stage{0..N}.py.

The goal is a *consistent* per-student feedback block across every stage's
grade report, organized into three buckets:

  1. CORE     — observations about THIS stage's rubric (what was earned / missed)
  2. BACKWARD — carry-forwards from prior stages and recognition of fixes the
                student made between submissions. Carry-forwards are flagged
                with no point loss at this stage (the no-double-deduction
                policy); they *can* still move the prior stage's score up at
                the post-deadline revision sweep.
  3. FORWARD  — forward-looking guidance for the next stage. Keeps every
                feedback block ending on what comes next, not what's broken.

Each per-stage script should:

    from _grading_comments import core, backward, forward, render_suggestions
    # ...
    def _suggestions_for(g) -> list[Suggestion]:
        s: list[Suggestion] = []
        if "SOMETHING_WRONG" in g.flags:
            s.append(core("Stage-specific rubric tip..."))
        if _carry(g, "X"):
            s.append(backward("Carry-forward note about Stage N-1 issue..."))
        s.append(forward(FORWARD_GUIDANCE[STAGE_N]))
        return s

    # ...in _student_section:
    lines.extend(render_suggestions(_suggestions_for(g), stage_n=STAGE_N))

The renderer always emits `### Kindly-worded suggestions for improvement` so
existing parsers (`build_roster.py`, the section regex in each script's
report-merge logic) keep working unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

# --- Bucket constants -----------------------------------------------------
CORE = "core"
BACKWARD = "backward"
FORWARD = "forward"

_BUCKET_ORDER = (CORE, BACKWARD, FORWARD)

# Sub-headings rendered under the main `### Kindly-worded suggestions for
# improvement` block. The `{stage_n}` / `{next_n}` placeholders are resolved
# by `render_suggestions`.
_BUCKET_HEADERS = {
    CORE: "**Stage {stage_n} rubric notes**",
    BACKWARD: (
        "**Carry-forwards & prior-stage recognition** "
        "*(no points lost here — closing these before the deadline can "
        "bump the prior stage's score at the post-deadline revision sweep)*"
    ),
    FORWARD: "**Looking ahead to Stage {next_n}**",
}


# --- Per-stage forward-guidance defaults ----------------------------------
# Short, generic pointers to the next stage. Per-student forward tips can
# override or supplement these by appending another `forward(...)` entry.
FORWARD_GUIDANCE: dict[int, str] = {
    0: (
        "**Stage 1 — drop the master ratios template into your repo.** "
        "Download `performance-ratios-template.xlsx` from "
        "`docs/templates/spreadsheets/` (or the link in the Stage 1 brief) "
        "and place it at `models/templates/performance-ratios-template.xlsx`. "
        "Enhancements to the formulas are welcome; an unmodified upload is "
        "also full credit."
    ),
    1: (
        "**Stage 2 — company-selection memo.** Pick a publicly listed firm "
        "whose 10-K (or VAS annual report / IFRS 20-F) is easy to source, so "
        "Stage 3 doesn't get stuck on missing data. The memo is mostly "
        "writing — favor a name where you have either career-angle or "
        "regional familiarity. Don't forget to add `@adamwstauffer` as a "
        "**Write** collaborator on your repo (Settings → Collaborators); "
        "the Stage 2 checklist asks for this so feedback PRs can land."
    ),
    2: (
        "**Stage 3 — populate the workbook with real financials.** Income "
        "Statement, Balance Sheet, and Cash Flow for current year + prior "
        "year, sourced from your company's most recent 10-K (or VAS / IFRS "
        "equivalent). The Ratios tab auto-computes once the statement tabs "
        "are filled — your Stage 3 job is to tie each line to the audited "
        "source, not to interpret the numbers."
    ),
    3: (
        "**Stage 4 — technical specification for the LLM analysis.** The "
        "spec is the input that drives Stage 5's automated ratio review. "
        "Reference named ranges directly (e.g., `BAL_assets_total_curr`, "
        "`RATIO_roe`) so the LLM can find the right cells. Use the Stage 4 "
        "HIL iteration pass to catch spec gaps before they bake into Stage 5."
    ),
    4: (
        "**Stage 5 — LLM analysis + manual verification.** Run your Stage 4 "
        "spec through the LLM of your choice, then verify at least five of "
        "its ratio outputs against the workbook by hand. The polish rubric "
        "grades how cleanly the prior four stages tie together as a single "
        "deliverable, so revisit your earlier files with fresh eyes."
    ),
    5: (
        "**Project wrap-up — capture lessons learned.** A short retrospective "
        "in `docs/decisions/` (what worked, what didn't, what you'd change) "
        "turns the project into a portfolio asset rather than a coursework "
        "artifact. Future hiring managers, auditors, or graduate-program "
        "reviewers find written reflection more credible than polish alone."
    ),
}


# --- Data structure -------------------------------------------------------
@dataclass(frozen=True)
class Suggestion:
    """A single feedback bullet, tagged by bucket.

    Use `core()`, `backward()`, `forward()` factory functions rather than
    constructing this directly — they normalize whitespace and make call
    sites read as labeled prose.
    """

    bucket: str
    text: str


# --- Factories ------------------------------------------------------------
def core(text: str) -> Suggestion:
    """A tip about this stage's rubric performance."""
    return Suggestion(CORE, " ".join(text.split()))


def backward(text: str) -> Suggestion:
    """A carry-forward note from a prior stage (no point loss this stage)."""
    return Suggestion(BACKWARD, " ".join(text.split()))


def forward(text: str) -> Suggestion:
    """Forward-looking guidance toward the next stage."""
    return Suggestion(FORWARD, " ".join(text.split()))


# --- Semantic helpers -----------------------------------------------------
def recognize_prior_fix(prior_stage_n: int, what_improved: str) -> Suggestion:
    """Backward-bucket bullet recognizing a fix between stages.

    Use when the grader detects that a Stage N-1 deduction item is now
    resolved (e.g., placeholder README replaced with real content, BIO
    stub expanded, capitalized paths renamed lowercase). This is the
    explicit cue students need to see to understand the post-deadline
    sweep can move their prior-stage score up.
    """
    text = what_improved.rstrip(".") + "."
    return backward(
        f"**Recognized improvement since Stage {prior_stage_n}:** {text} "
        f"This can move your Stage {prior_stage_n} score up at the "
        f"post-deadline revision sweep — no action needed beyond what's "
        f"already in your repo."
    )


def carry_forward_open(prior_stage_n: int, what_remains: str) -> Suggestion:
    """Backward-bucket bullet for a still-open prior-stage carry-forward."""
    text = what_remains.rstrip(".") + "."
    return backward(
        f"**Still open from Stage {prior_stage_n}:** {text} Not re-deducted "
        f"here (no double-dock), but closing it before the deadline can "
        f"bump your Stage {prior_stage_n} score at the revision sweep."
    )


def next_stage_pointer(stage_n: int) -> Suggestion | None:
    """Forward-bucket bullet with the canned next-stage pointer.

    Returns None if `stage_n` has no defined forward pointer (e.g., final
    stage). Append additional `forward(...)` calls for student-specific
    forward guidance.
    """
    if stage_n + 1 not in FORWARD_GUIDANCE and stage_n not in FORWARD_GUIDANCE:
        return None
    # Use the *current* stage's entry, which already describes "what comes
    # next" by convention. (FORWARD_GUIDANCE[N] = guidance toward Stage N+1.)
    text = FORWARD_GUIDANCE.get(stage_n)
    if not text:
        return None
    return forward(text)


# --- Renderer -------------------------------------------------------------
def render_suggestions(
    suggestions: Iterable[Suggestion],
    *,
    stage_n: int,
    heading: str = "### Kindly-worded suggestions for improvement",
) -> list[str]:
    """Render bucketed suggestions to markdown lines.

    Always emits `heading` (keeps `build_roster.py`'s parser stable).
    Empty buckets are silently dropped so the output stays tight.

    Returns a list of strings ready to be `lines.extend(...)`-ed into the
    student section. The final line is empty (trailing blank) so the
    caller can append `"---"` immediately afterward.
    """
    items = list(suggestions)
    if not items:
        return []

    lines: list[str] = [heading, ""]

    for bucket in _BUCKET_ORDER:
        bucket_items = [s for s in items if s.bucket == bucket]
        if not bucket_items:
            continue
        header = _BUCKET_HEADERS[bucket].format(
            stage_n=stage_n, next_n=stage_n + 1
        )
        lines.append(header)
        lines.append("")
        for s in bucket_items:
            lines.append(f"- {s.text}")
        lines.append("")

    return lines


__all__ = [
    "Suggestion",
    "CORE",
    "BACKWARD",
    "FORWARD",
    "FORWARD_GUIDANCE",
    "core",
    "backward",
    "forward",
    "recognize_prior_fix",
    "carry_forward_open",
    "next_stage_pointer",
    "render_suggestions",
]
