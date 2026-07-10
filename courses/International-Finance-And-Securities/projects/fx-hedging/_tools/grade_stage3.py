"""FIN-321 (fx-hedging v2) Stage 3 grader — AI-Assisted Build + Audit.

Deliverables live in the student's GitHub repo:
  - workbook:   models/builds/YYYY-MM-DD-{lastname}-{scenario}-model.xlsx
  - audit note: analysis/YYYY-MM-DD-{lastname}-build-audit.md

The graded skill is *specifying precisely and auditing ruthlessly*, so the
headline check is the mechanical formula-presence audit in `_xlsx` (every
calculated cell a formula referencing named ranges; hardcoded outputs earn
nothing). This scanner is the canonical thin-scanner shape: stage-specific
scoring + suggestions + a `grade(sub)` function, wired to the shared driver.

Rubric (criterion weights = % of the stage, from _weights.CRITERIA_WEIGHTS[3]):
    Contract compliance        50   (named ranges + formulas-only + hedges + sensitivity)
    Structure & presentation   25   (cover, legend/key, color convention, layout)
    Audit note                 25   (>=3 substantive findings, committed)

CLI:  python grade_stage3.py <export.zip|dir> [--floor N] [--prior PATH]
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
from _xlsx import audit_workbook, WorkbookAudit, NAMED_RANGE_CONTRACT, count_audit_findings

STAGE_N = 3
STAGE_LABEL = "AI-Assisted Build + Audit"
CRIT = CRITERIA_WEIGHTS[STAGE_N]
DEFAULT_FLOOR_PCT = STAGE_FLOOR_PCT[STAGE_N]
PRIOR_STAGE = 2
RUBRIC_ROWS = [
    ("Contract compliance (named ranges, formulas-only, hedges, sensitivity)", f"{CRIT['contract_compliance']}%"),
    ("Structure & presentation (cover, legend/key, color convention)", f"{CRIT['structure_presentation']}%"),
    ("Audit note (>=3 findings)", f"{CRIT['audit_note']}%"),
]

WORKBOOK_RE = re.compile(r"models/builds/.*\.xlsx?$", re.IGNORECASE)
AUDIT_NOTE_RE = re.compile(r"analysis/.*(?:audit|build-audit).*\.md$", re.IGNORECASE)


# ---------------------------------------------------------------- scoring
def _score_contract(a: WorkbookAudit, flags: list[str]) -> float:
    nr_frac = len(a.named_ranges_present) / len(NAMED_RANGE_CONTRACT)
    if len(a.named_ranges_present) < 8:
        flags.append("FEW_NAMED_RANGES")
    formula_score = min(1.0, a.formula_ratio / 0.9) if a.formula_ratio else 0.0
    if a.formula_cells and a.formulas_using_named_ranges == 0:
        formula_score = min(formula_score, 0.5)
        flags.append("FORMULAS_NOT_USING_NAMES")
    if a.formula_ratio < 0.8:
        flags.append("HARDCODED_OUTPUTS")
    have = set(a.hedges_found)
    hedge_frac = (0.5 * (len({"Forward", "MoneyMarket"} & have) / 2)
                  + 0.5 * (1.0 if a.has_option_hedge else 0.0))
    for h in ("Forward", "MoneyMarket"):
        if h not in have:
            flags.append(f"MISSING_{h.upper()}")
    if not a.has_option_hedge:
        flags.append("MISSING_OPTION")
    sens = 1.0 if (a.sensitivity_detected and a.chart_count > 0) else (
        0.5 if a.sensitivity_detected else 0.0)
    if not a.sensitivity_detected:
        flags.append("NO_SENSITIVITY")
    if a.chart_count == 0:
        flags.append("NO_CHART")
    frac = 0.40 * nr_frac + 0.35 * formula_score + 0.15 * hedge_frac + 0.10 * sens
    return round(frac * CRIT["contract_compliance"], 1)


def _score_structure(a: WorkbookAudit, flags: list[str]) -> float:
    if not a.has_cover_tab:
        flags.append("NO_COVER")
    if not a.has_legend_tab:
        flags.append("NO_LEGEND")
    color_ok = a.distinct_fill_colors >= 3
    if not color_ok:
        flags.append("WEAK_COLOR_CONVENTION")
    frac = (0.35 * a.has_cover_tab + 0.35 * a.has_legend_tab
            + 0.20 * color_ok + 0.10 * a.has_notes_tab)
    return round(frac * CRIT["structure_presentation"], 1)


def _score_audit_note(present: bool, findings: int, flags: list[str]) -> float:
    if not present:
        flags.append("AUDIT_NOTE_MISSING")
        return 0.0
    if findings >= 3:
        return float(CRIT["audit_note"])
    flags.append("AUDIT_NOTE_THIN")
    return round(0.5 * CRIT["audit_note"], 1)


# ---------------------------------------------------------------- suggestions
def _suggestions_for(flags: set[str], prior_weak: bool):
    s = []
    if "NO_WORKBOOK" in flags:
        s.append(core("No workbook found under `models/builds/`. Commit the generated "
                      "`.xlsx` there with the convention-compliant filename."))
    if "WORKBOOK_OPEN_FAILED" in flags:
        s.append(core("The workbook couldn't be opened — re-export it as a valid .xlsx "
                      "and re-commit."))
    if "FEW_NAMED_RANGES" in flags:
        s.append(core("Fewer than 8 of the 10 contract named ranges were found. Attach "
                      "every one (FC_AMT, S0_in, F0_in, R_USD, R_FC, K_PUT, K_CALL, "
                      "PREM_PUT, PREM_CALL, T_DAYS) to its input cell."))
    if "HARDCODED_OUTPUTS" in flags:
        s.append(core("Several calculated cells hold typed numbers rather than formulas. "
                      "Every output must be a formula referencing named ranges — pasted "
                      "results don't earn contract credit."))
    if "FORMULAS_NOT_USING_NAMES" in flags:
        s.append(core("Your formulas use cell addresses (e.g. `$F$7`) instead of named "
                      "ranges. Swap in the contract names so spec, workbook, and prompt "
                      "share one vocabulary."))
    for h, msg in (("MISSING_FORWARD", "forward hedge"),
                   ("MISSING_MONEYMARKET", "money-market hedge"),
                   ("MISSING_OPTION", "option (put/call) hedge")):
        if h in flags:
            s.append(core(f"The {msg} isn't detectable — make sure it's built and labelled."))
    if "NO_CHART" in flags:
        s.append(core("Add the sensitivity line chart (USD outcome vs. ending spot, one "
                      "series per strategy)."))
    if "NO_LEGEND" in flags:
        s.append(core("Add a Legend/Key tab documenting the color convention (yellow "
                      "inputs, blue assumptions, green formulas, gray outputs)."))
    if "AUDIT_NOTE_MISSING" in flags:
        s.append(core("The build-audit note is missing. Add `analysis/…-build-audit.md` "
                      "with at least three findings you checked or fixed."))
    if "AUDIT_NOTE_THIN" in flags:
        s.append(core("The audit note has fewer than three substantive findings. For each: "
                      "what you checked, what you found, what you did."))
    if "INSTRUCTOR_NOT_COLLABORATOR" in flags:
        s.append(core("I'm not a collaborator on the repo yet — add `adamwstauffer` so I "
                      "can leave inline review comments."))
    if "STRONG" in flags:
        s.append(core("Clean build — named ranges complete, outputs formula-driven, hedges "
                      "and sensitivity all present. Nicely audited."))
    if prior_weak:
        s.append(backward("Your Stage 2 spec scored below the floor — the clearer the spec's "
                          "named-range contract and calculation flow, the less the build has "
                          "to guess. Tightening it can still lift the Stage 2 score at the "
                          "revision sweep."))
    nxt = next_stage_pointer(STAGE_N)
    if nxt:
        s.append(nxt)
    return s


# ---------------------------------------------------------------- PR sections
def _tick(b) -> str:
    return "✓" if b else "—"


def _pr_sections(a: WorkbookAudit, wb_path: str, note_present: bool, findings: int):
    contract = [
        "| Check | Status |", "|-------|--------|",
        f"| Workbook committed (`models/builds/`) | {_tick(bool(wb_path))} |",
        f"| Named ranges attached | {len(a.named_ranges_present)}/10 |",
        f"| Calculated cells are formulas | {a.formula_ratio * 100:.0f}% |",
        f"| Formulas use named ranges | {_tick(a.formulas_using_named_ranges)} |",
        f"| Forward hedge | {_tick('Forward' in a.hedges_found)} |",
        f"| Money-market hedge | {_tick('MoneyMarket' in a.hedges_found)} |",
        f"| Option hedge (put/call) | {_tick(a.has_option_hedge)} |",
        f"| Sensitivity table | {_tick(a.sensitivity_detected)} |",
        f"| Sensitivity chart | {_tick(a.chart_count)} |",
    ]
    presentation = [
        "| Element | Status |", "|---------|--------|",
        f"| Cover tab | {_tick(a.has_cover_tab)} |",
        f"| Legend/Key tab | {_tick(a.has_legend_tab)} |",
        f"| Color convention (distinct fills) | {a.distinct_fill_colors} |",
        f"| Notes/Assumptions tab | {_tick(a.has_notes_tab)} |",
    ]
    audit_note = [
        f"- Present: **{'yes' if note_present else 'no'}**",
        f"- Substantive findings counted: **{findings}** (brief asks for ≥3)",
    ]
    return [("Build contract checklist", contract),
            ("Presentation", presentation),
            ("Audit note", audit_note)]


# ---------------------------------------------------------------- grading
def grade(sub: Submission, prior_weak: bool = False) -> StudentReport:
    flags: list[str] = []
    meta: list[str] = []
    if sub.github_url:
        meta.append(f"**Repo:** {sub.github_url}")
    if sub.submitted_at:
        meta.append(f"**Submitted:** {sub.submitted_at:%Y-%m-%d %H:%M}")

    def report(raw, crit, accessible, wb_path="", audit=None, note_present=False, findings=0):
        return StudentReport(
            name=sub.name, stage_n=STAGE_N, raw_pct=round(raw, 1), accessible=accessible,
            criteria=crit, suggestions=_suggestions_for(set(flags), prior_weak),
            flags=flags, meta_lines=meta,
            pr_sections=_pr_sections(audit or WorkbookAudit(), wb_path, note_present, findings),
        )

    empty_crit = [
        Criterion("Contract compliance", 0, CRIT["contract_compliance"], "no gradable workbook"),
        Criterion("Structure & presentation", 0, CRIT["structure_presentation"], "—"),
        Criterion("Audit note", 0, CRIT["audit_note"], "—"),
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
    wb_paths = [p for p in st.tree if WORKBOOK_RE.search(p)]
    note_paths = [p for p in st.tree if AUDIT_NOTE_RE.search(p)]

    audit = WorkbookAudit(error="no workbook in models/builds/")
    wb_path = ""
    if wb_paths:
        wb_path = sorted(wb_paths, key=len)[0]
        meta.append(f"**Workbook:** `{wb_path}`")
        raw = _repo.download_bytes(owner, repo, wb_path, branch)
        audit = audit_workbook(raw) if raw else WorkbookAudit(error="download failed")
    else:
        flags.append("NO_WORKBOOK")

    note_present, findings = False, 0
    if note_paths:
        note_path = sorted(note_paths, key=len)[0]
        meta.append(f"**Audit note:** `{note_path}`")
        text = _repo.download_text(owner, repo, note_path, branch) or ""
        note_present = bool(text.strip())
        findings = count_audit_findings(text)

    cc = sp = 0.0
    if audit.opened:
        cc = _score_contract(audit, flags)
        sp = _score_structure(audit, flags)
    elif audit.error.startswith("open failed"):
        flags.append("WORKBOOK_OPEN_FAILED")
    an = _score_audit_note(note_present, findings, flags)
    raw_pct = cc + sp + an
    if raw_pct >= 92 and not flags:
        flags.append("STRONG")

    criteria = [
        Criterion("Contract compliance", cc, CRIT["contract_compliance"],
                  f"{len(audit.named_ranges_present)}/10 named ranges; "
                  f"{audit.formula_ratio * 100:.0f}% of calc cells are formulas; "
                  f"hedges: {', '.join(audit.hedges_found) or 'none'}; "
                  f"{'chart + ' if audit.chart_count else 'no chart, '}sensitivity "
                  f"{'yes' if audit.sensitivity_detected else 'no'}."),
        Criterion("Structure & presentation", sp, CRIT["structure_presentation"],
                  f"cover {'Y' if audit.has_cover_tab else 'N'}, legend "
                  f"{'Y' if audit.has_legend_tab else 'N'}, {audit.distinct_fill_colors} "
                  f"fill colors, notes {'Y' if audit.has_notes_tab else 'N'}."),
        Criterion("Audit note", an, CRIT["audit_note"],
                  f"{'present' if note_present else 'missing'}, ~{findings} findings."),
    ]
    return report(raw_pct, criteria, accessible=True, wb_path=wb_path, audit=audit,
                  note_present=note_present, findings=findings)


if __name__ == "__main__":
    sys.exit(run_scanner(STAGE_N, STAGE_LABEL, RUBRIC_ROWS, grade,
                         default_floor=DEFAULT_FLOOR_PCT, prior_stage=PRIOR_STAGE))
