"""FIN-321 (fx-hedging v2) Stage 5 grader — LLM Analysis & Validation (capstone).

Deliverables live in the student's GitHub repo:
  - validation doc:   analysis/YYYY-MM-DD-{lastname}-{scenario}-validation.md
  - recommendation:   docs/decisions/YYYY-MM-DD-{lastname}-{scenario}-hedge-recommendation.md

The capstone graded skill is *validating a model you did not run yourself* —
feed the spec + market-data memo to a fresh LLM, then compare its output to the
workbook, diagnose every discrepancy, recompute the key outcomes by hand, and
only then recommend. So the headline checks are textual: a comparison table
with a diagnosis, a hand-verification table with real arithmetic, a CFO-voiced
recommendation, an honest spec retrospective, and a portfolio-polished repo.

This scanner is the canonical thin-scanner shape: stage-specific scoring +
suggestions + a `grade(sub)` function, wired to the shared driver. There is no
"looking ahead" block — Stage 5 is the final stage.

Rubric (criterion weights = % of the stage, from _weights.CRITERIA_WEIGHTS[5]):
    LLM execution & comparison   25   (two-doc run, comparison table, diagnosis)
    Hand verification            25   (>=3 outcomes recomputed with arithmetic)
    Recommendation & voice       25   (A-E structure, CFO-appropriate length)
    Spec retrospective           17   (specific, honest, ties failures to spec)
    Repo polish                   8   (LICENSE, description, READMEs, public, commits)

CLI:  python grade_stage5.py <export.zip|dir> [--floor N] [--prior PATH]
                             [--out-dir DIR] [--today YYYY-MM-DD]
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass

import _repo
from _repo import Submission
from _weights import CRITERIA_WEIGHTS, STAGE_FLOOR_PCT
from _grading_comments import core, backward, next_stage_pointer
from _report import Criterion, StudentReport, run_scanner
from _xlsx import count_audit_findings

STAGE_N = 5
STAGE_LABEL = "LLM Analysis & Validation"
CRIT = CRITERIA_WEIGHTS[STAGE_N]
DEFAULT_FLOOR_PCT = STAGE_FLOOR_PCT[STAGE_N]
PRIOR_STAGE = 4
RUBRIC_ROWS = [
    ("LLM execution & comparison (two-doc run, comparison table, diagnosis)", f"{CRIT['llm_execution_comparison']}%"),
    ("Hand verification (>=3 outcomes recomputed with arithmetic)", f"{CRIT['hand_verification']}%"),
    ("Recommendation & executive voice (A-E structure, CFO voice)", f"{CRIT['recommendation_voice']}%"),
    ("Spec retrospective (specific, honest, ties failures to spec gaps)", f"{CRIT['spec_retrospective']}%"),
    ("Repo polish (LICENSE, description, READMEs, public, commits)", f"{CRIT['repo_polish']}%"),
]

VALIDATION_RE = re.compile(r"analysis/.*validation.*\.md$", re.IGNORECASE)
RECOMMENDATION_RE = re.compile(r"docs/decisions/.*recommendation.*\.md$", re.IGNORECASE)

# --- textual signals ------------------------------------------------------
_LLM_SIGNALS = ("llm", "comparison", "compare")
_DIAGNOSIS_SIGNALS = ("discrepan", "diagnos", "llm error", "workbook error", "spec ambig")
_HAND_SIGNALS = ("by hand", "hand-verification", "hand verification", "recompute", "verification", "hand")
_RETRO_SIGNALS = ("retrospective", "spec gap", "would say differently", "the spec")
# A-E recommendation sections (exposure, outcomes, sensitivity, recommendation, justification).
_REC_SECTION_SIGNALS = ("exposure", ("hedge outcome", "outcomes"), "sensitivity",
                        "recommend", ("justification", "justif"))

_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
_ARITH_RE = re.compile(r"\d[\d,\.]*\s*[×xX*+\-/=]\s*\d")


def _is_sep_row(line: str) -> bool:
    s = line.strip()
    return bool(s) and set(s) <= set("|:- ")


def _count_table_rows(text: str) -> int:
    """Count markdown table content rows (>=2 pipes, excluding separator rows)."""
    return sum(1 for ln in text.splitlines()
               if ln.count("|") >= 2 and not _is_sep_row(ln))


def _section_words(text: str, keyword: str) -> int:
    """Word count of the first heading section whose title contains `keyword`."""
    collecting = False
    words = 0
    for ln in text.splitlines():
        m = _HEADING_RE.match(ln)
        if m:
            if collecting:
                break
            if keyword in m.group(1).lower():
                collecting = True
            continue
        if collecting:
            words += len(ln.split())
    return words


def _has_signal(low: str, signal) -> bool:
    if isinstance(signal, tuple):
        return any(s in low for s in signal)
    return signal in low


# ---------------------------------------------------------------- detection
@dataclass
class Detect:
    val_present: bool = False
    rec_present: bool = False
    # validation doc
    has_llm: bool = False
    table_rows: int = 0
    has_diagnosis: bool = False
    has_hand: bool = False
    hand_outcomes: int = 0
    has_arithmetic: bool = False
    retro_mentioned: bool = False
    retro_words: int = 0
    # recommendation memo
    rec_sections: int = 0
    rec_words: int = 0

    @property
    def has_comparison(self) -> bool:
        return self.has_llm and self.table_rows >= 3

    @property
    def rec_length_ok(self) -> bool:
        return 500 <= self.rec_words <= 2500


def _analyze(vtext: str, rtext: str) -> Detect:
    d = Detect()
    d.val_present = bool(vtext.strip())
    d.rec_present = bool(rtext.strip())

    if d.val_present:
        low = vtext.lower()
        d.table_rows = _count_table_rows(vtext)
        d.has_llm = any(s in low for s in _LLM_SIGNALS)
        d.has_diagnosis = any(s in low for s in _DIAGNOSIS_SIGNALS)
        d.has_hand = any(s in low for s in _HAND_SIGNALS)
        d.hand_outcomes = max(count_audit_findings(vtext), d.table_rows)
        d.has_arithmetic = bool(_ARITH_RE.search(vtext))
        d.retro_mentioned = any(s in low for s in _RETRO_SIGNALS)
        d.retro_words = _section_words(vtext, "retrospective")

    if d.rec_present:
        low = rtext.lower()
        d.rec_sections = sum(1 for sig in _REC_SECTION_SIGNALS if _has_signal(low, sig))
        d.rec_words = len(rtext.split())
    return d


# ---------------------------------------------------------------- scoring
def _score_comparison(d: Detect, flags: list[str]) -> float:
    if not d.val_present:
        return 0.0
    has_table = d.table_rows >= 3
    if not (d.has_llm and has_table):
        flags.append("NO_COMPARISON")
    frac = 0.34 * d.has_llm + 0.33 * has_table + 0.33 * d.has_diagnosis
    return round(frac * CRIT["llm_execution_comparison"], 1)


def _score_hand(d: Detect, flags: list[str]) -> float:
    if not d.val_present:
        return 0.0
    if d.hand_outcomes < 3:
        flags.append("WEAK_HAND_VERIFICATION")
    has_table = d.table_rows >= 3
    frac = (0.25 * d.has_hand
            + 0.35 * (min(d.hand_outcomes, 3) / 3)
            + 0.20 * has_table
            + 0.20 * d.has_arithmetic)
    return round(frac * CRIT["hand_verification"], 1)


def _score_recommendation(d: Detect, flags: list[str]) -> float:
    if not d.rec_present:
        return 0.0
    if d.rec_sections < 4 or not d.rec_length_ok:
        flags.append("THIN_RECOMMENDATION")
    frac = 0.7 * (d.rec_sections / 5) + 0.3 * (1.0 if d.rec_length_ok else 0.0)
    return round(frac * CRIT["recommendation_voice"], 1)


def _score_retrospective(d: Detect, flags: list[str]) -> float:
    if not d.val_present:
        return 0.0
    if not d.retro_mentioned:
        flags.append("NO_RETROSPECTIVE")
        return 0.0
    if d.retro_words >= 50:
        return float(CRIT["spec_retrospective"])
    return round(0.5 * CRIT["spec_retrospective"], 1)


def _repo_polish_items(st) -> list[tuple[str, bool]]:
    readmes = sum(1 for p in st.tree if p.lower().endswith("readme.md"))
    return [
        ("LICENSE present", bool(st.license)),
        ("Repo description set", bool(st.description)),
        ("Per-directory READMEs (>=3)", readmes >= 3),
        ("Repo public", st.public),
        ("Descriptive commit history (>=2)", st.descriptive_commit_count >= 2),
    ]


def _score_repo_polish(items: list[tuple[str, bool]], flags: list[str]) -> float:
    present = sum(1 for _, ok in items if ok)
    if present < len(items):
        flags.append("REPO_UNPOLISHED")
    return round(present / len(items) * CRIT["repo_polish"], 1)


# ---------------------------------------------------------------- suggestions
def _suggestions_for(flags: set[str], prior_weak: bool):
    s = []
    if "NO_VALIDATION_DOC" in flags:
        s.append(core("No validation doc found under `analysis/`. Commit "
                      "`analysis/…-validation.md` with the comparison table, hand "
                      "verification, and spec retrospective (Parts 1–2 + retrospective)."))
    if "NO_RECOMMENDATION" in flags:
        s.append(core("No recommendation memo found under `docs/decisions/`. Commit "
                      "`docs/decisions/…-hedge-recommendation.md` — the 2–4 page CFO memo "
                      "with the A–E structure."))
    if "NO_COMPARISON" in flags:
        s.append(core("The comparison of the fresh LLM run against your workbook isn't "
                      "detectable. Add a table with the LLM result vs. workbook result per "
                      "strategy at 2–3 `S_T` points, and diagnose each discrepancy (LLM "
                      "error, workbook error, or spec ambiguity)."))
    if "WEAK_HAND_VERIFICATION" in flags:
        s.append(core("Fewer than three outcomes are recomputed by hand. Show the arithmetic "
                      "for at least three — forward proceeds (`FC_AMT × F0_in`), the "
                      "money-market hedge (all three steps), and one option outcome — with "
                      "the numbers at each step. This table is the single strongest evidence "
                      "you understand the model."))
    if "THIN_RECOMMENDATION" in flags:
        s.append(core("The recommendation memo is thin — aim for the full A–E arc (exposure "
                      "summary, hedge outcomes, sensitivity interpretation, a single "
                      "recommendation, and executive justification) in a 2–4 page CFO voice, "
                      "supported by your live-data numbers."))
    if "NO_RETROSPECTIVE" in flags:
        s.append(core("Add the spec retrospective (½–1 page in the validation doc): what did "
                      "the LLM get wrong or have to guess, and what does that reveal about "
                      "your spec? \"The spec was perfect\" is not a retrospective — candor is "
                      "graded."))
    if "REPO_UNPOLISHED" in flags:
        s.append(core("Finish the repo-polish checklist: a LICENSE, a one-line repo "
                      "description, accurate per-directory READMEs, a public repo, and a "
                      "clean commit history make this a portfolio piece."))
    if "INSTRUCTOR_NOT_COLLABORATOR" in flags:
        s.append(core("I'm not a collaborator on the repo yet — add `adamwstauffer` so I "
                      "can leave inline review comments."))
    if "NOT_PUBLIC" in flags:
        s.append(core("The repo is private. Make it public so it works as the portfolio "
                      "artifact this project has been building toward."))
    if "STRONG" in flags:
        s.append(core("Capstone landed — clean two-document LLM run with diagnosed "
                      "discrepancies, hand verification that shows the arithmetic, a "
                      "decision-ready CFO recommendation, a candid spec retrospective, and a "
                      "genuinely portfolio-ready repo. Excellent close to the project."))
    if prior_weak:
        s.append(backward("Your Stage 4 market-data work scored below the floor — the cleaner "
                          "the live-data provenance and resolved checks, the more your "
                          "capstone numbers can lean on them. Tightening it can still lift the "
                          "Stage 4 score at the revision sweep."))
    nxt = next_stage_pointer(STAGE_N)
    if nxt:
        s.append(nxt)
    return s


# ---------------------------------------------------------------- PR sections
def _tick(b) -> str:
    return "✓" if b else "—"


def _pr_sections(d: Detect, polish_items: list[tuple[str, bool]]):
    validation = [
        "| Check | Status |", "|-------|--------|",
        f"| Validation doc committed (`analysis/`) | {_tick(d.val_present)} |",
        f"| Comparison table (LLM vs. workbook) | {_tick(d.has_comparison)} |",
        f"| Discrepancy diagnosis | {_tick(d.has_diagnosis)} |",
        f"| Hand-verification outcomes | {d.hand_outcomes} (brief asks for ≥3) |",
        f"| Arithmetic shown | {_tick(d.has_arithmetic)} |",
        f"| Spec retrospective | {_tick(d.retro_mentioned)} |",
    ]
    recommendation = [
        "| Element | Status |", "|---------|--------|",
        f"| Memo committed (`docs/decisions/`) | {_tick(d.rec_present)} |",
        f"| A–E sections present | {d.rec_sections}/5 |",
        f"| Length in CFO band (500–2500 words) | {_tick(d.rec_length_ok)} ({d.rec_words} words) |",
    ]
    polish = ["| Element | Status |", "|---------|--------|"]
    polish += [f"| {label} | {_tick(ok)} |" for label, ok in polish_items]
    return [("Validation checklist", validation),
            ("Recommendation", recommendation),
            ("Repo polish", polish)]


# ---------------------------------------------------------------- grading
def grade(sub: Submission, prior_weak: bool = False) -> StudentReport:
    flags: list[str] = []
    meta: list[str] = []
    if sub.github_url:
        meta.append(f"**Repo:** {sub.github_url}")
    if sub.submitted_at:
        meta.append(f"**Submitted:** {sub.submitted_at:%Y-%m-%d %H:%M}")

    def report(raw, crit, accessible, d=None, polish_items=None):
        return StudentReport(
            name=sub.name, stage_n=STAGE_N, raw_pct=round(raw, 1), accessible=accessible,
            criteria=crit, suggestions=_suggestions_for(set(flags), prior_weak),
            flags=flags, meta_lines=meta,
            pr_sections=_pr_sections(d or Detect(), polish_items or _repo_polish_items(_EMPTY_ST)),
        )

    empty_crit = [
        Criterion("LLM execution & comparison", 0, CRIT["llm_execution_comparison"], "no gradable submission"),
        Criterion("Hand verification", 0, CRIT["hand_verification"], "—"),
        Criterion("Recommendation & executive voice", 0, CRIT["recommendation_voice"], "—"),
        Criterion("Spec retrospective", 0, CRIT["spec_retrospective"], "—"),
        Criterion("Repo polish", 0, CRIT["repo_polish"], "—"),
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
    val_paths = [p for p in st.tree if VALIDATION_RE.search(p)]
    rec_paths = [p for p in st.tree if RECOMMENDATION_RE.search(p)]

    vtext = ""
    if val_paths:
        vpath = sorted(val_paths, key=len)[0]
        meta.append(f"**Validation doc:** `{vpath}`")
        vtext = _repo.download_text(owner, repo, vpath, branch) or ""
    else:
        flags.append("NO_VALIDATION_DOC")

    rtext = ""
    if rec_paths:
        rpath = sorted(rec_paths, key=len)[0]
        meta.append(f"**Recommendation:** `{rpath}`")
        rtext = _repo.download_text(owner, repo, rpath, branch) or ""
    else:
        flags.append("NO_RECOMMENDATION")

    d = _analyze(vtext, rtext)
    polish_items = _repo_polish_items(st)

    lc = _score_comparison(d, flags)
    hv = _score_hand(d, flags)
    rv = _score_recommendation(d, flags)
    sr = _score_retrospective(d, flags)
    rp = _score_repo_polish(polish_items, flags)
    raw_pct = lc + hv + rv + sr + rp
    if raw_pct >= 92 and not flags:
        flags.append("STRONG")

    criteria = [
        Criterion("LLM execution & comparison", lc, CRIT["llm_execution_comparison"],
                  f"comparison {'present' if d.has_comparison else 'missing'} "
                  f"({d.table_rows} table rows); "
                  f"diagnosis {'yes' if d.has_diagnosis else 'no'}."),
        Criterion("Hand verification", hv, CRIT["hand_verification"],
                  f"~{d.hand_outcomes} outcomes; "
                  f"arithmetic {'shown' if d.has_arithmetic else 'not shown'}."),
        Criterion("Recommendation & executive voice", rv, CRIT["recommendation_voice"],
                  f"{'present' if d.rec_present else 'missing'}, {d.rec_sections}/5 A–E "
                  f"sections, {d.rec_words} words."),
        Criterion("Spec retrospective", sr, CRIT["spec_retrospective"],
                  f"{'section ~' + str(d.retro_words) + ' words' if d.retro_words else ('mentioned' if d.retro_mentioned else 'missing')}."),
        Criterion("Repo polish", rp, CRIT["repo_polish"],
                  ", ".join(f"{label.split('(')[0].strip()} {'Y' if ok else 'N'}"
                            for label, ok in polish_items) + "."),
    ]
    return report(raw_pct, criteria, accessible=True, d=d, polish_items=polish_items)


# A zeroed RepoState so `report(...)` can build empty PR sections before `st` exists.
_EMPTY_ST = _repo.RepoState(owner="", repo="")


if __name__ == "__main__":
    sys.exit(run_scanner(STAGE_N, STAGE_LABEL, RUBRIC_ROWS, grade,
                         default_floor=DEFAULT_FLOOR_PCT, prior_stage=PRIOR_STAGE))
