"""FIN-321 (fx-hedging v2) Stage 2 grader — Model Specification.

The deliverable lives in the student's GitHub repo:
  - spec:       docs/specs/YYYY-MM-DD-{lastname}-{scenario}-spec.md
  - plus an updated prompt-log.md (anywhere in the tree)

The graded skill is *designing a model on paper before any Excel exists* —
precise enough that an AI could build the workbook from the spec alone. So the
headline check reads the spec text: how much of the named-range contract and
tab architecture it pins down, whether all three hedge families are described
in calculation flow, whether it names concrete check figures and a sensitivity
plan, and whether the human-in-the-loop prompt iteration is evidenced. This
scanner is the canonical thin-scanner shape: stage-specific scoring +
suggestions + a `grade(sub)` function, wired to the shared driver.

Rubric (criterion weights = % of the stage, from _weights.CRITERIA_WEIGHTS[2]):
    Named-range contract & tab architecture   30
    Calculation flow (three hedge families)    30
    Validation & sensitivity plan              20
    Reproducibility & prompt log               20

CLI:  python grade_stage2.py <export.zip|dir> [--floor N] [--prior PATH]
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
from _xlsx import NAMED_RANGE_CONTRACT

STAGE_N = 2
STAGE_LABEL = "Model Specification"
CRIT = CRITERIA_WEIGHTS[STAGE_N]
DEFAULT_FLOOR_PCT = STAGE_FLOOR_PCT[STAGE_N]
PRIOR_STAGE = 1
RUBRIC_ROWS = [
    ("Named-range contract & tab architecture", f"{CRIT['named_range_contract']}%"),
    ("Calculation flow (all three hedge families)", f"{CRIT['calculation_flow']}%"),
    ("Validation & sensitivity plan", f"{CRIT['validation_sensitivity']}%"),
    ("Reproducibility & prompt log", f"{CRIT['reproducibility_prompt']}%"),
]

SPEC_RE = re.compile(r"docs/specs/.*spec.*\.md$", re.IGNORECASE)
SPEC_FALLBACK_RE = re.compile(r"docs/specs/.*\.md$", re.IGNORECASE)
PROMPT_LOG_RE = re.compile(r"prompt-log\.md$", re.IGNORECASE)

# Tab / sheet names the brief's architecture section calls for.
TAB_HINTS = ("cover", "legend", "key", "input", "sensitivity", "notes", "assumption")


# ---------------------------------------------------------------- scoring
def _score_named_range(text: str, lowered: str, flags: list[str]) -> tuple[float, int, int]:
    names_found = sum(1 for n in NAMED_RANGE_CONTRACT if n in text)
    tabs_mentioned = sum(1 for t in TAB_HINTS if t in lowered)
    if names_found < 8:
        flags.append("FEW_NAMED_RANGES")
    if tabs_mentioned < 3:
        flags.append("NO_TAB_ARCHITECTURE")
    frac = 0.6 * (names_found / len(NAMED_RANGE_CONTRACT)) + 0.4 * min(1.0, tabs_mentioned / 4)
    return round(frac * CRIT["named_range_contract"], 1), names_found, tabs_mentioned


def _score_calc_flow(lowered: str, flags: list[str]) -> tuple[float, int]:
    forward = "forward" in lowered and (
        "locked" in lowered or re.search(r"fc_amt\s*[*x×]\s*f0_in", lowered) is not None
    )
    money_market = any(w in lowered for w in ("money market", "money-market", "borrow", "invest"))
    options = any(w in lowered for w in ("put", "call", "payoff", "premium"))
    families = sum((bool(forward), bool(money_market), bool(options)))
    if families < 3:
        flags.append("INCOMPLETE_CALC_FLOW")
    return round((families / 3) * CRIT["calculation_flow"], 1), families


def _score_validation(text: str, lowered: str, flags: list[str]) -> tuple[float, bool, bool]:
    checks = any(w in lowered for w in ("parity", "check figure", "validation"))
    sens_plan = "sensitivity" in lowered and any(
        w in lowered for w in ("s_t", "±5", "5%", "1%")
    )
    if not checks:
        flags.append("NO_VALIDATION_RULES")
    if not sens_plan:
        flags.append("NO_SENSITIVITY_PLAN")
    score = (10 if checks else 0) + (10 if sens_plan else 0)
    return float(score), checks, sens_plan


def _score_reproducibility(lowered: str, word_count: int, prompt_log: bool,
                           flags: list[str]) -> tuple[float, bool]:
    if not prompt_log:
        flags.append("NO_PROMPT_LOG")
    thin = word_count < 500
    if thin:
        flags.append("THIN_SPEC")
    iteration = any(w in lowered for w in ("iteration", "before", "after", "revised", "refined"))
    score = (10 if prompt_log else 0) + (0 if thin else 5) + (5 if iteration else 0)
    return float(score), iteration


# ---------------------------------------------------------------- suggestions
def _suggestions_for(flags: set[str], prior_weak: bool):
    s = []
    if "NO_SPEC" in flags:
        s.append(core("No specification found under `docs/specs/`. Commit the spec as "
                      "`docs/specs/YYYY-MM-DD-{lastname}-{scenario}-spec.md` — this stage "
                      "grades the design document, so nothing else can be scored without it."))
    if "FEW_NAMED_RANGES" in flags:
        s.append(core("Fewer than 8 of the 10 contract named ranges appear in the spec. "
                      "Name every input exactly (FC_AMT, S0_in, F0_in, R_USD, R_FC, K_PUT, "
                      "K_CALL, PREM_PUT, PREM_CALL, T_DAYS) in the inputs table so spec, "
                      "workbook, and prompt share one vocabulary."))
    if "NO_TAB_ARCHITECTURE" in flags:
        s.append(core("The tab architecture is thin — name each tab and its purpose "
                      "(Cover, Legend/Key, Inputs, one calculation area per hedge, "
                      "Sensitivity, Notes & Assumptions)."))
    if "INCOMPLETE_CALC_FLOW" in flags:
        s.append(core("The calculation flow doesn't cover all three hedge families. Spell out "
                      "the forward (`FC_AMT × F0_in` → locked proceeds), the money-market "
                      "steps (borrow / convert at S0_in / invest at R_USD, plus the parity "
                      "check), and the options (premium in USD, payoff vs. ending spot)."))
    if "NO_VALIDATION_RULES" in flags:
        s.append(core("List concrete check figures the finished workbook must pass — "
                      "forward ≈ MM parity within rounding, continuous option proceeds, no "
                      "error cells, every output a formula. These become your Stage 3 audit "
                      "checklist."))
    if "NO_SENSITIVITY_PLAN" in flags:
        s.append(core("Specify the sensitivity plan: `S_T` from 0.95×S0_in to 1.05×S0_in in "
                      "1% steps, USD proceeds per strategy at each rate, and one comparison "
                      "chart — say what the chart should let the CFO see."))
    if "NO_PROMPT_LOG" in flags:
        s.append(core("No `prompt-log.md` found. Log the prompts you used to draft the spec "
                      "and commit the file alongside it."))
    if "THIN_SPEC" in flags:
        s.append(core("The spec is short for a context-free reader to build from. The brief "
                      "asks for 2–3 pages — flesh out inputs, assumptions, and calculation "
                      "flow so an AI wouldn't have to guess."))
    if "NOT_PUBLIC" in flags:
        s.append(core("The repo isn't public yet — make it public so the spec and prompt "
                      "log are visible for review."))
    if "INSTRUCTOR_NOT_COLLABORATOR" in flags:
        s.append(core("I'm not a collaborator on the repo yet — add `adamwstauffer` so I "
                      "can leave inline review comments."))
    if "STRONG" in flags:
        s.append(core("Strong spec — named-range contract and tab architecture complete, all "
                      "three hedge families in the calculation flow, concrete check figures "
                      "and a full sensitivity plan, with the prompt iteration logged. An AI "
                      "could build straight from this."))
    if prior_weak:
        s.append(backward("Your Stage 1 memo scored below the floor — the exposure framing "
                          "you sharpen here (currency, amount, settlement timing) is the same "
                          "material the memo needed. Tightening it can still lift the Stage 1 "
                          "score at the post-deadline revision sweep."))
    nxt = next_stage_pointer(STAGE_N)
    if nxt:
        s.append(nxt)
    return s


# ---------------------------------------------------------------- PR sections
def _tick(b) -> str:
    return "✓" if b else "—"


def _pr_sections(spec_path: str, names_found: int, tabs_mentioned: int, families: int,
                 checks: bool, sens_plan: bool, prompt_log: bool):
    checklist = [
        "| Check | Status |", "|-------|--------|",
        f"| Spec committed (`docs/specs/`) | {_tick(bool(spec_path))} |",
        f"| Named ranges named | {names_found}/10 |",
        f"| Tab architecture | {_tick(tabs_mentioned >= 3)} ({tabs_mentioned} tabs) |",
        f"| Three hedge families in calc flow | {_tick(families >= 3)} ({families}/3) |",
        f"| Validation rules / check figures | {_tick(checks)} |",
        f"| Sensitivity plan | {_tick(sens_plan)} |",
        f"| Prompt log committed | {_tick(prompt_log)} |",
    ]
    return [("Specification checklist", checklist)]


# ---------------------------------------------------------------- grading
def grade(sub: Submission, prior_weak: bool = False) -> StudentReport:
    flags: list[str] = []
    meta: list[str] = []
    if sub.github_url:
        meta.append(f"**Repo:** {sub.github_url}")
    if sub.submitted_at:
        meta.append(f"**Submitted:** {sub.submitted_at:%Y-%m-%d %H:%M}")

    def report(raw, crit, accessible, spec_path="", names_found=0, tabs_mentioned=0,
               families=0, checks=False, sens_plan=False, prompt_log=False):
        return StudentReport(
            name=sub.name, stage_n=STAGE_N, raw_pct=round(raw, 1), accessible=accessible,
            criteria=crit, suggestions=_suggestions_for(set(flags), prior_weak),
            flags=flags, meta_lines=meta,
            pr_sections=_pr_sections(spec_path, names_found, tabs_mentioned, families,
                                     checks, sens_plan, prompt_log),
        )

    empty_crit = [
        Criterion("Named-range contract & tab architecture", 0, CRIT["named_range_contract"],
                  "no gradable spec"),
        Criterion("Calculation flow", 0, CRIT["calculation_flow"], "—"),
        Criterion("Validation & sensitivity plan", 0, CRIT["validation_sensitivity"], "—"),
        Criterion("Reproducibility & prompt log", 0, CRIT["reproducibility_prompt"], "—"),
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
    spec_paths = [p for p in st.tree if SPEC_RE.search(p)]
    if not spec_paths:
        spec_paths = [p for p in st.tree if SPEC_FALLBACK_RE.search(p)]
    prompt_log = any(PROMPT_LOG_RE.search(p) for p in st.tree)

    if not spec_paths:
        flags.append("NO_SPEC")
        return report(0, empty_crit, accessible=True, prompt_log=prompt_log)

    spec_path = sorted(spec_paths, key=len)[0]
    meta.append(f"**Spec:** `{spec_path}`")
    text = _repo.download_text(owner, repo, spec_path, branch) or ""
    lowered = text.lower()
    word_count = len(text.split())

    nr, names_found, tabs_mentioned = _score_named_range(text, lowered, flags)
    cf, families = _score_calc_flow(lowered, flags)
    vs, checks, sens_plan = _score_validation(text, lowered, flags)
    rp, iteration = _score_reproducibility(lowered, word_count, prompt_log, flags)
    raw_pct = nr + cf + vs + rp
    if raw_pct >= 92 and not flags:
        flags.append("STRONG")

    criteria = [
        Criterion("Named-range contract & tab architecture", nr, CRIT["named_range_contract"],
                  f"{names_found}/10 named ranges; {tabs_mentioned} tab names mentioned."),
        Criterion("Calculation flow", cf, CRIT["calculation_flow"],
                  f"{families}/3 hedge families described (forward / money-market / options)."),
        Criterion("Validation & sensitivity plan", vs, CRIT["validation_sensitivity"],
                  f"check figures {'yes' if checks else 'no'}; "
                  f"sensitivity plan {'yes' if sens_plan else 'no'}."),
        Criterion("Reproducibility & prompt log", rp, CRIT["reproducibility_prompt"],
                  f"prompt-log {'present' if prompt_log else 'missing'}; "
                  f"~{word_count} words; iteration {'shown' if iteration else 'not shown'}."),
    ]
    return report(raw_pct, criteria, accessible=True, spec_path=spec_path,
                  names_found=names_found, tabs_mentioned=tabs_mentioned, families=families,
                  checks=checks, sens_plan=sens_plan, prompt_log=prompt_log)


if __name__ == "__main__":
    sys.exit(run_scanner(STAGE_N, STAGE_LABEL, RUBRIC_ROWS, grade,
                         default_floor=DEFAULT_FLOOR_PCT, prior_stage=PRIOR_STAGE))
