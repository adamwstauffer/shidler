"""FIN-321 (fx-hedging v2) Stage 4 grader — Market Data + Population.

Deliverables live in the student's GitHub repo:
  - market-data memo: data/YYYY-MM-DD-{lastname}-market-data.md
  - workbook (re-committed): models/builds/YYYY-MM-DD-{lastname}-{scenario}-model.xlsx

Stage 4 is where the workbook stops being a classroom exercise and becomes a
dated, sourced, defensible analysis. Two things are graded: whether every live
input is *sourced and timestamped* (the provenance memo), and whether the model
*still resolves* once real quotes flow through the named ranges. Stage 4 re-uses
the Stage 3 workbook audit (from `_xlsx`) to re-check that the model holds under
live data.

Rubric (criterion weights = % of the stage, from _weights.CRITERIA_WEIGHTS[4]):
    Data quality & provenance   50   (source + timestamp per input, proxies documented)
    Model resolves cleanly      33   (live data flows through named ranges; checks pass)
    Lab cross-check             17   (FX Hedging Lab comparison performed + resolved)

CLI:  python grade_stage4.py <export.zip|dir> [--floor N] [--prior PATH]
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
from _xlsx import audit_workbook, WorkbookAudit, NAMED_RANGE_CONTRACT

STAGE_N = 4
STAGE_LABEL = "Market Data + Population"
CRIT = CRITERIA_WEIGHTS[STAGE_N]
DEFAULT_FLOOR_PCT = STAGE_FLOOR_PCT[STAGE_N]
PRIOR_STAGE = 3
RUBRIC_ROWS = [
    ("Data quality & provenance (source + timestamp per input, proxies documented)", f"{CRIT['data_provenance']}%"),
    ("Model resolves cleanly (live data through named ranges; checks pass)", f"{CRIT['model_resolves']}%"),
    ("Lab cross-check (FX Hedging Lab comparison performed + resolved)", f"{CRIT['lab_crosscheck']}%"),
]

WORKBOOK_RE = re.compile(r"models/builds/.*\.xlsx?$", re.IGNORECASE)
MEMO_RE = re.compile(r"data/.*market.?data.*\.md$", re.IGNORECASE)
MEMO_FALLBACK_RE = re.compile(r"data/.*\.md$", re.IGNORECASE)

# --- provenance heuristics on the lowercased memo -------------------------
_TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
_SOURCE_KEYWORDS = ("source", "bloomberg", "yahoo", "ecb", "fred", "reference rate")
_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_TIMESTAMP_KEYWORDS = ("retriev", "as of", "timestamp")
_PROXY_KEYWORDS = ("cip", "covered interest", "implied forward", "proxy")
_LAB_COMPARE_KEYWORDS = ("cross-check", "crosscheck", "compare", "comparison")


# ---------------------------------------------------------------- scoring
def _score_provenance(memo: str, present: bool, flags: list[str]) -> float:
    if not present:
        flags.append("NO_DATA_MEMO")
        return 0.0
    low = memo.lower()

    table_rows = sum(1 for ln in memo.splitlines() if _TABLE_ROW_RE.match(ln))
    has_table = table_rows >= 3
    if not has_table:
        flags.append("NO_PROVENANCE_TABLE")

    source_hits = sum(1 for kw in _SOURCE_KEYWORDS if kw in low)
    if source_hits == 0:
        flags.append("NO_SOURCES")

    has_dates = bool(_DATE_RE.search(memo)) or any(kw in low for kw in _TIMESTAMP_KEYWORDS)
    if not has_dates:
        flags.append("NO_TIMESTAMPS")

    has_proxy = any(kw in low for kw in _PROXY_KEYWORDS)

    frac = (0.40 * has_table
            + 0.30 * min(1.0, source_hits / 3)
            + 0.20 * has_dates
            + 0.10 * has_proxy)
    return round(frac * CRIT["data_provenance"], 1)


def _score_model_resolves(a: WorkbookAudit, wb_present: bool, flags: list[str]) -> float:
    if not wb_present:
        flags.append("NO_WORKBOOK")
        return 0.0
    if not a.opened:
        flags.append("MODEL_BROKEN")
        return 0.0
    formula_score = min(1.0, a.formula_ratio / 0.9) if a.formula_ratio else 0.0
    frac = (0.5 * formula_score
            + 0.3 * (len(a.named_ranges_present) / 10)
            + 0.2 * (1.0 if a.sensitivity_detected else 0.0))
    return round(frac * CRIT["model_resolves"], 1)


def _score_lab_crosscheck(memo: str, present: bool, flags: list[str]) -> float:
    low = memo.lower() if present else ""
    has_lab = "lab" in low
    has_compare = any(kw in low for kw in _LAB_COMPARE_KEYWORDS)
    if has_lab and has_compare:
        return float(CRIT["lab_crosscheck"])
    if has_lab or has_compare:
        return round(0.5 * CRIT["lab_crosscheck"], 1)
    flags.append("NO_LAB_CROSSCHECK")
    return 0.0


# ---------------------------------------------------------------- suggestions
def _suggestions_for(flags: set[str], prior_weak: bool):
    s = []
    if "NO_DATA_MEMO" in flags:
        s.append(core("No market-data memo found under `data/`. Commit "
                      "`data/YYYY-MM-DD-{lastname}-market-data.md` with a provenance "
                      "table for every input."))
    if "NO_PROVENANCE_TABLE" in flags:
        s.append(core("The memo has no readable provenance table. Use a markdown table "
                      "with one row per input: value, source, retrieval timestamp, and "
                      "any proxy/computation used."))
    if "NO_SOURCES" in flags:
        s.append(core("No sources are cited. For each input name where the number came "
                      "from (Yahoo Finance, Bloomberg, ECB reference rate, FRED) — an "
                      "auditor should be able to re-pull every quote."))
    if "NO_TIMESTAMPS" in flags:
        s.append(core("No retrieval timestamps/dates found. Record when each number was "
                      "pulled (a YYYY-MM-DD date or an \"as of\" market-close time); "
                      "everyone's data is date-stamped and unique."))
    if "NO_WORKBOOK" in flags:
        s.append(core("No workbook found under `models/builds/`. Re-commit the populated "
                      "`.xlsx` with your live inputs entered into the named-range cells."))
    if "MODEL_BROKEN" in flags:
        s.append(core("The workbook couldn't be opened/re-audited with live data — "
                      "re-export it as a valid .xlsx and re-commit. If a formula broke on "
                      "population, fix the structure and note what you fixed (that's the "
                      "exercise, not a penalty)."))
    if "NO_LAB_CROSSCHECK" in flags:
        s.append(core("No FX Hedging Lab cross-check is documented. Enter your live inputs "
                      "into the lab, compare its forward / money-market / option outputs to "
                      "your workbook, and record the resolution in the memo."))
    if "INSTRUCTOR_NOT_COLLABORATOR" in flags:
        s.append(core("I'm not a collaborator on the repo yet — add `adamwstauffer` so I "
                      "can leave inline review comments."))
    if "STRONG" in flags:
        s.append(core("Fully sourced and dated — provenance table complete, live data flows "
                      "through the named ranges, and the lab cross-check is resolved. "
                      "Defensible, auditable work."))
    if prior_weak:
        s.append(backward("Your Stage 3 build scored below the floor — a workbook whose "
                          "outputs are all formulas on named ranges is exactly what lets "
                          "live data drop in without breaking. Tightening the build can "
                          "still lift the Stage 3 score at the revision sweep."))
    nxt = next_stage_pointer(STAGE_N)
    if nxt:
        s.append(nxt)
    return s


# ---------------------------------------------------------------- PR sections
def _tick(b) -> str:
    return "✓" if b else "—"


def _pr_sections(memo: str, memo_present: bool, a: WorkbookAudit, wb_path: str):
    low = memo.lower() if memo_present else ""
    table_rows = sum(1 for ln in memo.splitlines() if _TABLE_ROW_RE.match(ln)) if memo_present else 0
    source_hits = sum(1 for kw in _SOURCE_KEYWORDS if kw in low)
    has_dates = bool(_DATE_RE.search(memo)) or any(kw in low for kw in _TIMESTAMP_KEYWORDS) if memo_present else False
    has_proxy = any(kw in low for kw in _PROXY_KEYWORDS)
    has_lab = "lab" in low and any(kw in low for kw in _LAB_COMPARE_KEYWORDS)

    checklist = [
        "| Check | Status |", "|-------|--------|",
        f"| Market-data memo committed (`data/`) | {_tick(memo_present)} |",
        f"| Provenance table (rows) | {table_rows} |",
        f"| Sources cited | {_tick(source_hits)} |",
        f"| Retrieval timestamps/dates | {_tick(has_dates)} |",
        f"| CIP/proxy documented | {_tick(has_proxy)} |",
        f"| FX Hedging Lab cross-check | {_tick(has_lab)} |",
    ]
    resolves = [
        "| Check | Status |", "|-------|--------|",
        f"| Workbook committed (`models/builds/`) | {_tick(bool(wb_path))} |",
        f"| Named ranges attached | {len(a.named_ranges_present)}/10 |",
        f"| Calculated cells are formulas | {a.formula_ratio * 100:.0f}% |",
        f"| Sensitivity recalculates | {_tick(a.sensitivity_detected)} |",
    ]
    return [("Market-data checklist", checklist),
            ("Model still resolves", resolves)]


# ---------------------------------------------------------------- grading
def grade(sub: Submission, prior_weak: bool = False) -> StudentReport:
    flags: list[str] = []
    meta: list[str] = []
    if sub.github_url:
        meta.append(f"**Repo:** {sub.github_url}")
    if sub.submitted_at:
        meta.append(f"**Submitted:** {sub.submitted_at:%Y-%m-%d %H:%M}")

    def report(raw, crit, accessible, memo="", memo_present=False, wb_path="", audit=None):
        return StudentReport(
            name=sub.name, stage_n=STAGE_N, raw_pct=round(raw, 1), accessible=accessible,
            criteria=crit, suggestions=_suggestions_for(set(flags), prior_weak),
            flags=flags, meta_lines=meta,
            pr_sections=_pr_sections(memo, memo_present, audit or WorkbookAudit(), wb_path),
        )

    empty_crit = [
        Criterion("Data quality & provenance", 0, CRIT["data_provenance"], "no gradable submission"),
        Criterion("Model resolves cleanly", 0, CRIT["model_resolves"], "—"),
        Criterion("Lab cross-check", 0, CRIT["lab_crosscheck"], "—"),
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
        memo_paths = [p for p in st.tree if MEMO_FALLBACK_RE.search(p)]
    wb_paths = [p for p in st.tree if WORKBOOK_RE.search(p)]

    memo, memo_present = "", False
    if memo_paths:
        memo_path = sorted(memo_paths, key=len)[0]
        meta.append(f"**Market-data memo:** `{memo_path}`")
        memo = _repo.download_text(owner, repo, memo_path, branch) or ""
        memo_present = bool(memo.strip())

    audit = WorkbookAudit(error="no workbook in models/builds/")
    wb_path = ""
    if wb_paths:
        wb_path = sorted(wb_paths, key=len)[0]
        meta.append(f"**Workbook:** `{wb_path}`")
        raw = _repo.download_bytes(owner, repo, wb_path, branch)
        audit = audit_workbook(raw) if raw else WorkbookAudit(error="download failed")

    dp = _score_provenance(memo, memo_present, flags)
    mr = _score_model_resolves(audit, bool(wb_path), flags)
    lc = _score_lab_crosscheck(memo, memo_present, flags)
    raw_pct = dp + mr + lc
    if raw_pct >= 92 and not flags:
        flags.append("STRONG")

    criteria = [
        Criterion("Data quality & provenance", dp, CRIT["data_provenance"],
                  f"{'memo present' if memo_present else 'memo missing'}; "
                  f"{sum(1 for kw in _SOURCE_KEYWORDS if kw in memo.lower())} source signal(s); "
                  f"{'dated' if (_DATE_RE.search(memo) or any(k in memo.lower() for k in _TIMESTAMP_KEYWORDS)) else 'undated'}; "
                  f"{'proxy noted' if any(k in memo.lower() for k in _PROXY_KEYWORDS) else 'no proxy note'}."),
        Criterion("Model resolves cleanly", mr, CRIT["model_resolves"],
                  f"{len(audit.named_ranges_present)}/10 named ranges; "
                  f"{audit.formula_ratio * 100:.0f}% of calc cells are formulas; "
                  f"sensitivity {'yes' if audit.sensitivity_detected else 'no'}."),
        Criterion("Lab cross-check", lc, CRIT["lab_crosscheck"],
                  f"{'lab comparison documented' if ('lab' in memo.lower() and any(k in memo.lower() for k in _LAB_COMPARE_KEYWORDS)) else 'not documented'}."),
    ]
    return report(raw_pct, criteria, accessible=True, memo=memo, memo_present=memo_present,
                  wb_path=wb_path, audit=audit)


if __name__ == "__main__":
    sys.exit(run_scanner(STAGE_N, STAGE_LABEL, RUBRIC_ROWS, grade,
                         default_floor=DEFAULT_FLOOR_PCT, prior_stage=PRIOR_STAGE))
