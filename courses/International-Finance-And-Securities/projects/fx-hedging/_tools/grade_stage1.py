"""FIN-321 (fx-hedging v2) Stage 1 grader — Executive Memo.

The deliverable is a single decision memo committed to the student's GitHub repo:
  - memo: docs/decisions/YYYY-MM-DD-{lastname}-{scenario}-hedge-framing.md

The graded skill is *framing an FX exposure for a CFO and staging the work* —
name the currency/amount/timing, weigh the three hedge families honestly, and
lay out the Stage 2–5 arc. This scanner is the canonical thin-scanner shape:
stage-specific scoring + suggestions + a `grade(sub)` function, wired to the
shared driver.

Rubric (criterion weights = % of the stage, from _weights.CRITERIA_WEIGHTS[1]):
    Exposure framing            25   (currency, amount, timing)
    Hedge families & trade-offs 25   (forward / money-market / options)
    Next steps                  25   (frames the Stage 2–5 arc)
    Professionalism             25   (length, frontmatter, location/filename)

CLI:  python grade_stage1.py <export.zip|dir> [--floor N] [--prior PATH]
                             [--out-dir DIR] [--today YYYY-MM-DD]
"""
from __future__ import annotations

import re
import sys

import _repo
from _repo import Submission
from _weights import CRITERIA_WEIGHTS, STAGE_FLOOR_PCT
from _grading_comments import core, backward, next_stage_pointer
from _report import Criterion, StudentReport, run_scanner

STAGE_N = 1
STAGE_LABEL = "Executive Memo"
CRIT = CRITERIA_WEIGHTS[STAGE_N]
DEFAULT_FLOOR_PCT = STAGE_FLOOR_PCT[STAGE_N]
PRIOR_STAGE = 0
RUBRIC_ROWS = [
    ("Exposure framing (currency, amount, timing)", f"{CRIT['exposure_framing']}%"),
    ("Hedge families & trade-offs (forward / money-market / options)", f"{CRIT['hedge_families']}%"),
    ("Next steps (frames the Stage 2–5 arc)", f"{CRIT['next_steps']}%"),
    ("Professionalism (length, frontmatter, location/filename)", f"{CRIT['professionalism']}%"),
]

# Memo discovery is deliberately lenient on *filing* (extension / exact location)
# so a real, substantive memo still gets graded on its content — the canonical
# path is nudged via the Professionalism `correct_location` check, not a zero.
# Preferred: a memo-named file directly under docs/decisions/ (any/no extension).
MEMO_RE = re.compile(r"docs/decisions/[^/]*(?:hedge|framing|memo)[^/]*$", re.IGNORECASE)
# Fallback: any single file directly in docs/decisions/ (including a README the
# student used as the memo file), a top-level docs/decisions.md committed in
# place of the folder, or a bare extensionless `docs/decisions` file the student
# wrote the memo into (in place of the folder placeholder). The directly-under
# anchor keeps a deep stub like docs/decisions/specs/.../README.md from matching;
# a short stub sitting at any of these paths is rejected later by the word-count
# guard, not by name.
FALLBACK_RE = re.compile(r"^docs/decisions(?:/[^/]+|\.md)?$", re.IGNORECASE)
# Last resort: a memo-named markdown file *anywhere* in the repo — a student who
# filed the memo under `Docs/`, `memos/`, or the repo root has submitted it, and
# the two patterns above would score that a zero on filing alone, which is the
# opposite of this section's stated intent. Deliberately last so a canonical memo
# always wins; `pick_text` drops template stubs and prefers the longest file, and
# the word-count guard below still rejects a short stub that happens to match.
ANYWHERE_RE = re.compile(r"(?:^|/)[^/]*(?:hedge|framing|memo)[^/]*\.md$", re.IGNORECASE)
# ...but never an unfilled template. `strip_templates` only catches the
# placeholder tokens (`lastname`, `yyyy-mm-dd`); a student who copied
# `template-decision-memo.md` into their repo verbatim has not submitted a memo,
# and repo-wide matching would otherwise grade them on the template's own prose.
TEMPLATE_MEMO_RE = re.compile(r"(?:^|/)_?templates?/|(?:^|/)template[-_]", re.IGNORECASE)
MEMO_MIN_WORDS = 40  # below this a "memo" is a placeholder/stub, not a submission

# --- text-detection patterns ----------------------------------------------
CURRENCY_WORDS = ("eur", "gbp", "jpy", "usd", "euro", "pound", "yen", "dollar")
FX_PAIR_RE = re.compile(r"\b[a-z]{3}/[a-z]{3}\b")
BIGNUM_RE = re.compile(r"\d[\d,]{3,}")
TIMING_WORDS = ("day", "month", "settle", "maturity", "due", "receiv")
DATE_RE = re.compile(
    r"\b\d{4}-\d{1,2}-\d{1,2}\b"
    r"|\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d",
    re.IGNORECASE,
)


# ---------------------------------------------------------------- scoring
def _score_exposure(has_currency: bool, has_amount: bool, has_timing: bool,
                    flags: list[str]) -> float:
    hits = sum((has_currency, has_amount, has_timing))
    if hits < 2:
        flags.append("WEAK_EXPOSURE")
    return round(CRIT["exposure_framing"] * hits / 3, 1)


def _score_hedges(families: set[str], flags: list[str]) -> float:
    n = len(families)
    if n < 3:
        flags.append("MISSING_HEDGE_FAMILIES")
    return round(CRIT["hedge_families"] * n / 3, 1)


def _score_next_steps(signals: int, flags: list[str]) -> float:
    if signals >= 3:
        frac = 1.0
    elif signals == 2:
        frac = 0.6
    else:
        frac = 0.25
        flags.append("WEAK_NEXT_STEPS")
    return round(CRIT["next_steps"] * frac, 1)


def _score_professionalism(wc: int, has_frontmatter: bool, correct_location: bool,
                           flags: list[str]) -> float:
    length_score = 1.0 if 200 <= wc <= 700 else 0.5
    if wc < 150 or wc > 900:
        flags.append("MEMO_LENGTH")
    if not has_frontmatter:
        flags.append("NO_FRONTMATTER")
    frac = (0.5 * length_score
            + 0.25 * (1.0 if has_frontmatter else 0.0)
            + 0.25 * (1.0 if correct_location else 0.0))
    return round(CRIT["professionalism"] * frac, 1)


# ---------------------------------------------------------------- suggestions
def _suggestions_for(flags: set[str], prior_weak: bool):
    s = []
    if "NO_MEMO" in flags:
        s.append(core("No executive memo was found in your repo. To submit it: "
                      "**(1)** open the decision-memo template in the course repo; "
                      "**(2)** fill in the exposure (currency, amount, settlement timing), "
                      "the three hedge families, and your Stage 2–5 plan; "
                      "**(3)** save it in your repo as "
                      "`docs/decisions/YYYY-MM-DD-{lastname}-{scenario}-hedge-framing.md`; "
                      "**(4)** commit and push. The committed file *is* your submission."))
    if "WEAK_EXPOSURE" in flags:
        s.append(core("State the exposure precisely in your Background section — all three of: "
                      "**the currency** (e.g. EUR), **the amount** (e.g. €20,000,000), and "
                      "**the settlement timing** (e.g. due in 12 months). See the criterion "
                      "note above for which you're missing. A CFO sizing this risk — and your "
                      "own Stage 2 spec — needs each one stated outright, not implied."))
    if "MISSING_HEDGE_FAMILIES" in flags:
        s.append(core("Cover all three hedge families in your Methods section, each as its own "
                      "short paragraph with one honest pro and one honest con: "
                      "**(1)** a forward contract, **(2)** a money-market hedge, and "
                      "**(3)** options (a EUR put or collar). The criterion note above shows "
                      "which you're missing. The rubric wants all three on the table even if "
                      "you ultimately favor one."))
    if "WEAK_NEXT_STEPS" in flags:
        s.append(core("In your Limitations & Next Steps section, lay out the Stage 2–5 arc as "
                      "a short plan the CFO can approve — one sentence each: "
                      "**Stage 2** model specification, **Stage 3** AI-assisted build + audit, "
                      "**Stage 4** live market data, **Stage 5** validation + recommendation. "
                      "The point is to show where this memo is heading."))
    if "MEMO_LENGTH" in flags:
        s.append(core("The memo is outside the one-page executive band (aim for ~300–400 words). "
                      "Tighten or expand so it covers exposure, the three families, and next "
                      "steps — long enough to be complete, short enough to read in one pass."))
    if "NO_FRONTMATTER" in flags:
        s.append(core("Add the template's YAML frontmatter — the `---` fenced block at the very "
                      "top of the file (above the `#` title) holding `title`, `author`, `date`, "
                      "and `version`. Yours jumps straight into the heading; copy that block "
                      "back in from the decision-memo template and fill it in."))
    if "MEMO_LOCATION" in flags:
        s.append(core("Your memo was found and graded on its content, but it isn't at the "
                      "canonical path. To fix: rename/move it to "
                      "`docs/decisions/YYYY-MM-DD-{lastname}-{scenario}-hedge-framing.md` — "
                      "**inside** the `docs/decisions/` folder, dated, and ending in `.md`. "
                      "Small professionalism deduction only, no content penalty."))
    if "NOT_PUBLIC" in flags:
        s.append(core("Your repo is private, so the memo can't be reviewed. Make it public: "
                      "on GitHub, **Settings → General → Danger Zone → Change visibility → "
                      "Public**, then re-confirm."))
    if "INSTRUCTOR_NOT_COLLABORATOR" in flags:
        s.append(core("Add me as a collaborator so I can leave inline comments on your memo: "
                      "**(1)** on GitHub, open your repo's **Settings → Collaborators**; "
                      "**(2)** click **Add people**; **(3)** enter `adamwstauffer` and confirm."))
    if "STRONG" in flags:
        s.append(core("Sharp memo — exposure named precisely, all three hedge families with "
                      "honest trade-offs, and a clear Stage 2–5 plan. Great foundation for "
                      "the spec."))
    if prior_weak:
        s.append(backward("Your Stage 0 repository setup scored below the floor — a quick "
                          "cleanup (canonical folders, stub READMEs, a public repo, the URL "
                          "submitted) before the post-deadline sweep can still lift that "
                          "Stage 0 score."))
    nxt = next_stage_pointer(STAGE_N)
    if nxt:
        s.append(nxt)
    return s


# ---------------------------------------------------------------- PR sections
def _tick(b) -> str:
    return "✓" if b else "—"


def _pr_sections(c: dict):
    checklist = [
        "| Check | Status |", "|-------|--------|",
        f"| Memo committed (`docs/decisions/`) | {_tick(c.get('memo'))} |",
        f"| Exposure — currency named | {_tick(c.get('currency'))} |",
        f"| Exposure — amount named | {_tick(c.get('amount'))} |",
        f"| Exposure — timing named | {_tick(c.get('timing'))} |",
        f"| Three hedge families | {c.get('families', 0)}/3 |",
        f"| Next-steps arc (Stage 2–5) | {_tick(c.get('next_steps'))} |",
        f"| YAML frontmatter | {_tick(c.get('frontmatter'))} |",
        f"| Length in band (200–700 words) | {_tick(c.get('length_ok'))} |",
    ]
    return [("Memo checklist", checklist)]


# ---------------------------------------------------------------- grading
def grade(sub: Submission, prior_weak: bool = False) -> StudentReport:
    flags: list[str] = []
    meta: list[str] = []
    if sub.github_url:
        meta.append(f"**Repo:** {sub.github_url}")
    if sub.submitted_at:
        meta.append(f"**Submitted:** {sub.submitted_at:%Y-%m-%d %H:%M}")

    def report(raw, crit, accessible, checks=None):
        return StudentReport(
            name=sub.name, stage_n=STAGE_N, raw_pct=round(raw, 1), accessible=accessible,
            criteria=crit, suggestions=_suggestions_for(set(flags), prior_weak),
            flags=flags, meta_lines=meta, pr_sections=_pr_sections(checks or {}),
        )

    empty_crit = [
        Criterion("Exposure framing", 0, CRIT["exposure_framing"], "no gradable memo"),
        Criterion("Hedge families & trade-offs", 0, CRIT["hedge_families"], "—"),
        Criterion("Next steps", 0, CRIT["next_steps"], "—"),
        Criterion("Professionalism", 0, CRIT["professionalism"], "—"),
    ]

    parsed = sub.repo
    if not parsed:
        flags.append("NO_GITHUB_LINK")
        return report(0, empty_crit, accessible=False)
    owner, repo = parsed
    st = _repo.repo_state(owner, repo)
    if not st.accessible:
        flags.append("REPO_404")
        return report(0, empty_crit, accessible=False)
    if not st.public:
        flags.append("NOT_PUBLIC")
    if not st.instructor_is_collaborator:
        flags.append("INSTRUCTOR_NOT_COLLABORATOR")

    branch = st.default_branch
    memo_paths = [p for p in st.tree if MEMO_RE.search(p)]
    if not memo_paths:
        memo_paths = [p for p in st.tree if FALLBACK_RE.search(p)]
    if not memo_paths:
        memo_paths = [p for p in st.tree
                      if ANYWHERE_RE.search(p) and not TEMPLATE_MEMO_RE.search(p)]

    if not memo_paths:
        flags.append("NO_MEMO")
        return report(0, empty_crit, accessible=True)

    memo_path, text = _repo.pick_text(owner, repo, branch, memo_paths)
    meta.append(f"**Memo:** `{memo_path}`")
    if not text.strip():
        flags.append("NO_MEMO")
        return report(0, empty_crit, accessible=True, checks={"memo": True})

    text_lower = text.lower()
    wc = len(re.findall(r"\b\w+\b", text))
    if wc < MEMO_MIN_WORDS:  # a stub README / placeholder sitting where a memo would be
        flags.append("NO_MEMO")
        return report(0, empty_crit, accessible=True, checks={"memo": True})

    has_currency = (any(w in text_lower for w in CURRENCY_WORDS)
                    or bool(FX_PAIR_RE.search(text_lower)))
    has_amount = ("million" in text_lower
                  or any(sym in text for sym in ("€", "£", "$"))
                  or bool(BIGNUM_RE.search(text)))
    has_timing = (any(w in text_lower for w in TIMING_WORDS)
                  or bool(DATE_RE.search(text)))

    families: set[str] = set()
    if "forward" in text_lower:
        families.add("forward")
    if "money market" in text_lower or "money-market" in text_lower:
        families.add("money market")
    if any(w in text_lower for w in ("option", "put", "call")):
        families.add("options")

    signals = sum((
        ("specification" in text_lower or "spec" in text_lower),
        ("build" in text_lower),
        ("market data" in text_lower or "data" in text_lower),
        ("validation" in text_lower or "recommendation" in text_lower),
    ))

    has_frontmatter = text.lstrip().startswith("---")
    # Canonical filing = a dedicated .md file inside docs/decisions/. A memo
    # committed without the extension (docs/decisions/…-hedge-framing), in place
    # of the folder (docs/decisions.md), or stuffed into the folder's own
    # README.md still grades on content but forfeits this slice.
    correct_location = bool(
        re.match(r"docs/decisions/(?!README\.md$)[^/]+\.md$", memo_path, re.IGNORECASE))
    if not correct_location:
        flags.append("MEMO_LOCATION")

    ef = _score_exposure(has_currency, has_amount, has_timing, flags)
    hf = _score_hedges(families, flags)
    ns = _score_next_steps(signals, flags)
    pr = _score_professionalism(wc, has_frontmatter, correct_location, flags)
    raw_pct = ef + hf + ns + pr
    if raw_pct >= 92 and not flags:
        flags.append("STRONG")

    checks = {
        "memo": True, "currency": has_currency, "amount": has_amount,
        "timing": has_timing, "families": len(families), "next_steps": signals >= 2,
        "frontmatter": has_frontmatter, "length_ok": 200 <= wc <= 700,
    }

    # --- descriptive criterion notes (brief; the suggestions expand on them) ---
    _ex = (("currency", has_currency), ("amount", has_amount), ("settlement timing", has_timing))
    ex_missing = [n for n, ok in _ex if not ok]
    ex_note = ("All three named: currency, amount, settlement timing." if not ex_missing
               else f"Named: {', '.join(n for n, ok in _ex if ok) or 'none'}; "
                    f"missing: {', '.join(ex_missing)}.")
    fam_missing = [f for f in ("forward", "money-market", "options")
                   if f.replace("-", " ") not in families]
    fam_note = (f"All three families with trade-offs: {', '.join(sorted(families))}."
                if not fam_missing
                else f"{len(families)}/3 families — covered: {', '.join(sorted(families)) or 'none'}; "
                     f"missing: {', '.join(fam_missing)}.")
    ns_note = ("Next steps map the full Stage 2–5 arc." if signals >= 3
               else f"Next steps only partly map the Stage 2–5 plan ({signals}/4 stages referenced).")
    prof_note = "; ".join([
        f"{wc} words ({'in band' if 200 <= wc <= 700 else 'outside the 200–700 band'})",
        "YAML frontmatter present" if has_frontmatter else "no YAML frontmatter",
        "canonical path" if correct_location else "non-canonical path/filename",
    ]) + "."

    criteria = [
        Criterion("Exposure framing", ef, CRIT["exposure_framing"], ex_note),
        Criterion("Hedge families & trade-offs", hf, CRIT["hedge_families"], fam_note),
        Criterion("Next steps", ns, CRIT["next_steps"], ns_note),
        Criterion("Professionalism", pr, CRIT["professionalism"], prof_note),
    ]
    return report(raw_pct, criteria, accessible=True, checks=checks)


if __name__ == "__main__":
    sys.exit(run_scanner(STAGE_N, STAGE_LABEL, RUBRIC_ROWS, grade,
                         default_floor=DEFAULT_FLOOR_PCT, prior_stage=PRIOR_STAGE))
