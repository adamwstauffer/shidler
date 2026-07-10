"""Shared student-facing feedback scaffolding for grade_stage{0..5}.py.

Ported from the BUS-629 performance-ratios toolchain — same three-bucket
model, same public API, same emitted headings (so any downstream parser that
keys on `### Kindly-worded suggestions for improvement` keeps working). Only
the per-stage `FORWARD_GUIDANCE` text is rewritten for the fx-hedging arc.

Three buckets:

  1. CORE     — observations about THIS stage's rubric (earned / missed).
  2. BACKWARD — carry-forwards from prior stages and recognition of fixes.
                Flagged with NO point loss at this stage (no-double-deduction
                policy); closing them before the deadline can still bump the
                prior stage's score at the post-deadline revision sweep.
  3. FORWARD  — guidance toward the next stage, so every block ends on what
                comes next, not what's broken.

Usage in a per-stage script:

    from _grading_comments import core, backward, forward, render_suggestions, FORWARD_GUIDANCE
    def _suggestions_for(g):
        s = []
        if "NO_CHART" in g.flags:
            s.append(core("Add the sensitivity line chart — the rubric expects it."))
        if _carry(g, "FEW_NAMED_RANGES"):
            s.append(backward("Named-range coverage was thin last stage too ..."))
        s.append(forward(FORWARD_GUIDANCE[STAGE_N]))
        return s
    # ...
    lines.extend(render_suggestions(_suggestions_for(g), stage_n=STAGE_N))
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

# --- Bucket constants -----------------------------------------------------
CORE = "core"
BACKWARD = "backward"
FORWARD = "forward"

_BUCKET_ORDER = (CORE, BACKWARD, FORWARD)

_BUCKET_HEADERS = {
    CORE: "**Stage {stage_n} rubric notes**",
    BACKWARD: (
        "**Carry-forwards & prior-stage recognition** "
        "*(no points lost here — closing these before the deadline can "
        "bump the prior stage's score at the post-deadline revision sweep)*"
    ),
    FORWARD: "**Looking ahead to Stage {next_n}**",
}

_HEADING = "### Kindly-worded suggestions for improvement"


@dataclass(frozen=True)
class Suggestion:
    bucket: str
    text: str


def _clean(text: str) -> str:
    return " ".join(text.split())


def core(text: str) -> Suggestion:
    return Suggestion(CORE, _clean(text))


def backward(text: str) -> Suggestion:
    return Suggestion(BACKWARD, _clean(text))


def forward(text: str) -> Suggestion:
    return Suggestion(FORWARD, _clean(text))


# --- Semantic helpers (canned framing) ------------------------------------
def recognize_prior_fix(prior_stage_n: int, what_improved: str) -> Suggestion:
    return backward(
        f"**Recognized improvement since Stage {prior_stage_n}:** {what_improved} "
        f"This can move your Stage {prior_stage_n} score up at the post-deadline "
        f"revision sweep."
    )


def carry_forward_open(prior_stage_n: int, what_remains: str) -> Suggestion:
    return backward(
        f"**Still open from Stage {prior_stage_n}:** {what_remains} "
        f"Not re-deducted here (no double-dock) — worth closing before the sweep."
    )


def next_stage_pointer(stage_n: int) -> Suggestion | None:
    guidance = FORWARD_GUIDANCE.get(stage_n)
    return forward(guidance) if guidance else None


# --- Per-stage forward-guidance defaults (fx-hedging arc) -----------------
# FORWARD_GUIDANCE[N] points toward Stage N+1. No entry for the final stage.
FORWARD_GUIDANCE: dict[int, str] = {
    0: (
        "**Stage 1 — commit your executive memo.** Save it to `docs/decisions/` "
        "using the decision-memo template and name the exposure precisely "
        "(currency, amount, settlement timing). From here on, \"submit\" means "
        "\"commit and push.\""
    ),
    1: (
        "**Stage 2 — turn the memo into a model specification.** In `docs/specs/`, "
        "write the named-range contract, tab architecture, calculation flow, and "
        "validation checks — precise enough that an AI could build the workbook "
        "from the spec alone."
    ),
    2: (
        "**Stage 3 — build from your spec and audit it.** Hand the spec to an AI to "
        "generate the workbook, then audit: every calculated cell a formula "
        "referencing named ranges, all three hedge families, a sensitivity table + "
        "chart, and a build-audit note with at least three findings."
    ),
    3: (
        "**Stage 4 — load live market data.** Replace placeholder inputs with real "
        "quotes, document provenance (source + timestamp) in `data/`, re-run the "
        "parity and sensitivity checks, and cross-check the FX Hedging Lab."
    ),
    4: (
        "**Stage 5 — validate and recommend.** Feed your spec and market-data memo "
        "(and nothing else) to a fresh LLM, hand-verify at least three outcomes, "
        "write the executive recommendation and a candid spec retrospective, and "
        "polish the repo into a portfolio piece."
    ),
}


# --- Renderer -------------------------------------------------------------
def render_suggestions(
    suggestions: Iterable[Suggestion],
    *,
    stage_n: int,
    heading: str = _HEADING,
) -> list[str]:
    """Render suggestions into markdown lines under the canonical heading.

    Returns [] when there are no suggestions. Buckets render in fixed order
    (CORE, BACKWARD, FORWARD); empty buckets are dropped silently. Ends with
    a trailing blank line so the caller can append a `---` rule.
    """
    items = [s for s in suggestions if s and s.text]
    if not items:
        return []
    by_bucket: dict[str, list[str]] = {b: [] for b in _BUCKET_ORDER}
    for s in items:
        by_bucket.setdefault(s.bucket, []).append(s.text)

    lines = [heading, ""]
    for bucket in _BUCKET_ORDER:
        texts = by_bucket.get(bucket)
        if not texts:
            continue
        header = _BUCKET_HEADERS[bucket].format(stage_n=stage_n, next_n=stage_n + 1)
        lines.append(header)
        lines.extend(f"- {t}" for t in texts)
        lines.append("")
    return lines


__all__ = [
    "Suggestion", "CORE", "BACKWARD", "FORWARD", "FORWARD_GUIDANCE",
    "core", "backward", "forward",
    "recognize_prior_fix", "carry_forward_open", "next_stage_pointer",
    "render_suggestions",
]


if __name__ == "__main__":
    demo = [
        core("All ten named ranges present and every output cell is a formula — clean build."),
        carry_forward_open(2, "The spec left the day-count basis implicit."),
        next_stage_pointer(3),
    ]
    print("\n".join(render_suggestions(demo, stage_n=3)))
