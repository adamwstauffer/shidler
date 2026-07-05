"""BUS-629 post-deadline revision sweep.

One driver, one run per stage. Reads the existing `STAGE{N}_GRADES.md`,
re-inspects each student's current repo state, re-runs the same rubric
scoring, and **appends** `### Updated YYYY-MM-DD (re-grade)` blocks for
students whose raw score improved. Generosity-only — a score can only go
up, never down.

Policy: see `docs/decisions/bus629/2026-05-15-bus629-regrade-feedback-delivery.md`.
Sweep dates (Spring 2026):
    Stage 0     deadline 2026-05-16 → sweep 2026-05-17
    Stages 1–3  deadline 2026-05-23 → sweep 2026-05-24
    Stages 4–5  deadline 2026-05-30 → sweep 2026-05-31

Top-of-file lock:
    On first run, the driver inserts `**Sweep performed:** YYYY-MM-DD — stage
    locked.` into the preamble. Re-running against a locked report is
    refused unless `--force` is passed.

Re-grade block format (append-only beneath the original student section):

    ### Updated YYYY-MM-DD (re-grade)

    The post-deadline revision sweep picked up the following improvements:

    | Criterion | Before | After | Δ |
    |---|---|---|---|
    | Criterion A | 25 / 30 | 30 / 30 | +5 |
    | ... |
    | **Raw total** | **NN / 100** | **MM / 100** | **+X** |

    **Re-graded final:** MM / 100 (effective YYYY-MM-DD)

The canonical `**Re-graded final:**` marker is what `build_roster.py` reads
to flag a re-grade with `†` on the roster.

USAGE:
    python sweep_stage.py --stage 0
    python sweep_stage.py --stage 0 --dry-run
    python sweep_stage.py --stage 0 --force
    python sweep_stage.py --stage 0 --student "Ryan Markeiz"   # just one
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

# Force UTF-8 stdout so arrows / em-dashes don't crash on Windows cp1252.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

# Per-stage scorers expose `rescore_from_repo(name, repo_url, ...) -> Grade`.
import grade_stage0
import grade_stage1
import grade_stage2
import grade_stage3
import grade_stage4
import grade_stage5


COURSE_ROOT = Path(__file__).resolve().parent.parent
TOTAL_POINTS = 100


# ------------------------------------------------------------------
# Per-stage configuration
# ------------------------------------------------------------------

@dataclass
class StageConfig:
    n: int
    module: object
    report_path: Path
    floor_pct: int
    criterion_columns: list[tuple[str, str, int]]   # (label, grade-attr, max)
    extra_priors: list[Path] = field(default_factory=list)


def stage_config(n: int) -> StageConfig:
    if n == 0:
        return StageConfig(
            n=0, module=grade_stage0, floor_pct=90,
            report_path=COURSE_ROOT / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md",
            criterion_columns=[
                ("Repo public + accessible", "score_public", 15),
                ("Directory skeleton + READMEs", "score_skeleton", 20),
                ("Bio quality", "score_bio", 25),
                ("Resume quality", "score_resume", 25),
                ("Commit hygiene", "score_commits", 15),
            ],
        )
    if n == 1:
        return StageConfig(
            n=1, module=grade_stage1, floor_pct=80,
            report_path=COURSE_ROOT / "ignore" / "stage1" / "graded" / "STAGE1_GRADES.md",
            criterion_columns=[
                ("Template uploaded correctly", "score_template", 30),
                ("Directory structure", "score_dirs", 40),
                ("README quality", "score_readmes", 20),
                ("Commit hygiene", "score_commits", 10),
            ],
            extra_priors=[
                COURSE_ROOT / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md",
            ],
        )
    if n == 2:
        return StageConfig(
            n=2, module=grade_stage2, floor_pct=80,
            report_path=COURSE_ROOT / "ignore" / "stage2" / "graded" / "STAGE2_GRADES.md",
            criterion_columns=[
                ("Company Selection & Rationale", "score_selection", 25),
                ("Analytical Framing & Hypotheses", "score_hypotheses", 25),
                ("Data Source Identification", "score_sources", 25),
                ("Professionalism & Communication", "score_professionalism", 25),
            ],
            extra_priors=[
                COURSE_ROOT / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md",
                COURSE_ROOT / "ignore" / "stage1" / "graded" / "STAGE1_GRADES.md",
            ],
        )
    if n == 3:
        return StageConfig(
            n=3, module=grade_stage3, floor_pct=75,
            report_path=COURSE_ROOT / "ignore" / "stage3" / "graded" / "STAGE3_GRADES.md",
            criterion_columns=[
                ("Data accuracy", "score_accuracy", 40),
                ("Completeness", "score_completeness", 25),
                ("Source documentation", "score_sources", 20),
                ("Auto-computed ratios", "score_ratios", 15),
            ],
            extra_priors=[
                COURSE_ROOT / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md",
                COURSE_ROOT / "ignore" / "stage1" / "graded" / "STAGE1_GRADES.md",
                COURSE_ROOT / "ignore" / "stage2" / "graded" / "STAGE2_GRADES.md",
            ],
        )
    if n == 4:
        return StageConfig(
            n=4, module=grade_stage4, floor_pct=70,
            report_path=COURSE_ROOT / "ignore" / "stage4" / "graded" / "STAGE4_GRADES.md",
            criterion_columns=[
                ("Data & Structure", "score_data_structure", 25),
                ("Ratios & Validation", "score_ratios_validation", 25),
                ("Analysis spec", "score_analysis", 25),
                ("Spec craft", "score_craft_hil", 25),
            ],
            extra_priors=[
                COURSE_ROOT / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md",
                COURSE_ROOT / "ignore" / "stage1" / "graded" / "STAGE1_GRADES.md",
                COURSE_ROOT / "ignore" / "stage2" / "graded" / "STAGE2_GRADES.md",
                COURSE_ROOT / "ignore" / "stage3" / "graded" / "STAGE3_GRADES.md",
            ],
        )
    if n == 5:
        return StageConfig(
            n=5, module=grade_stage5, floor_pct=70,
            report_path=COURSE_ROOT / "ignore" / "stage5" / "graded" / "STAGE5_GRADES.md",
            criterion_columns=[
                ("Analytical correctness", "score_analytical", 25),
                ("Manual verification", "score_verification", 10),
                ("LLM eval", "score_evaluation", 25),
                ("Strategic recs", "score_strategic", 20),
                ("Stage 2 feedback", "score_s2_feedback", 5),
                ("Repo polish", "score_polish", 15),
            ],
            extra_priors=[
                COURSE_ROOT / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md",
                COURSE_ROOT / "ignore" / "stage2" / "graded" / "STAGE2_GRADES.md",
                COURSE_ROOT / "ignore" / "stage3" / "graded" / "STAGE3_GRADES.md",
                COURSE_ROOT / "ignore" / "stage4" / "graded" / "STAGE4_GRADES.md",
            ],
        )
    raise ValueError(f"unknown stage {n}")


# ------------------------------------------------------------------
# Parse STAGE{N}_GRADES.md into structured records
# ------------------------------------------------------------------

@dataclass
class StudentEntry:
    name: str
    section_start: int          # index into `lines` where `## N. Name…` lives
    section_end: int            # index of the next `---` or `## ` boundary
    header_score: int           # the score shown in the `## N. Name — **NN / 100**` header
    repo_url: str
    submitted_at: str
    floor_applied: bool
    last_regrade_score: int | None = None  # if there's already a re-grade block
    last_regrade_date: str = ""


# Matches both a fresh header (`## N. Name — **NN / 100**`) and a re-graded
# header carrying a struck original score (`## N. Name — ~~XX / 100~~ →
# **YY / 100**`). In the re-graded case `score` captures the post-arrow
# *effective* score (YY), so a student who was bumped in an earlier sweep is
# still parsed and re-considered here.
STUDENT_HEADER_RE = re.compile(
    r"^## \d+\.\s*(?P<name>[^—\n]+?)\s*—\s*"
    r"(?:~~[^~]*~~\s*(?:→|->)\s*)?"
    r"\*\*(?P<score>\d+)\s*/\s*100\*\*"
    r"(?P<rest>[^\n]*)$",
    re.MULTILINE,
)
REPO_LINE_RE = re.compile(r"^\*\*Repo:\*\*\s*(?P<url>https?://github\.com/\S+)", re.MULTILINE)
SUBMITTED_LINE_RE = re.compile(r"^\*\*Submitted:\*\*\s*(?P<ts>[^\n]+)", re.MULTILINE)
REGRADE_FINAL_RE = re.compile(
    r"\*\*Re-graded final:\*\*\s*(?P<score>\d+)\s*/\s*100"
    r"[^\n]*?effective\s*(?P<date>\d{4}-\d{2}-\d{2})"
)
SWEEP_LOCK_RE = re.compile(r"\*\*Sweep performed:\*\*\s*(?P<date>\d{4}-\d{2}-\d{2})")


def parse_report(text: str) -> tuple[list[StudentEntry], list[str]]:
    """Parse a STAGE{N}_GRADES.md into (entries, lines)."""
    lines = text.splitlines()
    entries: list[StudentEntry] = []

    # Find all student section starts.
    starts: list[tuple[int, str, int, str]] = []   # (line_idx, name, score, rest)
    for i, line in enumerate(lines):
        m = re.match(
            r"## \d+\.\s*(?P<name>[^—\n]+?)\s*—\s*"
            r"(?:~~[^~]*~~\s*(?:→|->)\s*)?"
            r"\*\*(?P<score>\d+)\s*/\s*100\*\*"
            r"(?P<rest>[^\n]*)$",
            line,
        )
        if m:
            starts.append((i, m.group("name").strip(), int(m.group("score")), m.group("rest")))

    # Find boundaries.
    for idx, (line_idx, name, score, rest) in enumerate(starts):
        if idx + 1 < len(starts):
            end_idx = starts[idx + 1][0] - 1
        else:
            # Last student section — end at the "## Class summary" or end of file.
            end_idx = len(lines) - 1
            for j in range(line_idx + 1, len(lines)):
                if lines[j].startswith("## ") and "class summary" in lines[j].lower():
                    end_idx = j - 1
                    break

        section_text = "\n".join(lines[line_idx:end_idx + 1])

        repo_m = REPO_LINE_RE.search(section_text)
        sub_m = SUBMITTED_LINE_RE.search(section_text)
        rg = list(REGRADE_FINAL_RE.finditer(section_text))
        latest_rg = max(rg, key=lambda x: x.group("date")) if rg else None

        floor_applied = "floor applied" in rest.lower()

        entries.append(StudentEntry(
            name=name,
            section_start=line_idx,
            section_end=end_idx,
            header_score=score,
            repo_url=repo_m.group("url") if repo_m else "",
            submitted_at=sub_m.group("ts").strip() if sub_m else "",
            floor_applied=floor_applied,
            last_regrade_score=int(latest_rg.group("score")) if latest_rg else None,
            last_regrade_date=latest_rg.group("date") if latest_rg else "",
        ))

    return entries, lines


# ------------------------------------------------------------------
# Prior-stage record loader (matches what each grader does internally)
# ------------------------------------------------------------------

def load_priors(cfg: StageConfig, student_name: str):
    """Build the per-stage prior record this grader expects, by parsing
    each prior-stage report and looking the student up."""
    if cfg.n == 0:
        return None
    module = cfg.module
    if not hasattr(module, "parse_prior_report") or not hasattr(module, "lookup_prior"):
        return None
    merged: dict = {}
    for prior_path in cfg.extra_priors:
        if not prior_path.exists():
            continue
        records = module.parse_prior_report(prior_path)
        # Different stages have different merge semantics; stage 2/3 expose
        # `merge_prior()` to combine. Stage 1 takes the single prior dict.
        if hasattr(module, "merge_prior"):
            merged = module.merge_prior(merged, records) if merged else records
        else:
            merged = records
    return module.lookup_prior(merged, student_name)


# ------------------------------------------------------------------
# Re-grade detection + block building
# ------------------------------------------------------------------

@dataclass
class SweepResult:
    student: StudentEntry
    new_raw: int
    breakdown: list[tuple[str, int, int]]   # (label, prior_score, new_score)
    prior_effective: int                     # the current effective score
    prior_collab_penalty: int = 0            # collab penalty in original entry (Stage 2)
    new_collab_penalty: int = 0              # collab penalty in current rescore (Stage 2)
    skipped_reason: str = ""                 # if non-empty, no diff applied


def _parse_before_score(section_text: str, label_substring: str, max_pts: int) -> int | None:
    """Pull the 'NN / max' value from a `| Criterion | NN / max | ... |` row.

    Looks for the row whose first cell contains `label_substring` (case-insensitive).
    """
    pat = re.compile(
        rf"\|\s*[^|\n]*{re.escape(label_substring)}[^|\n]*\|\s*(\d+)\s*/\s*{max_pts}\s*\|",
        re.IGNORECASE,
    )
    m = pat.search(section_text)
    if not m:
        return None
    return int(m.group(1))


def run_sweep_for_student(
    cfg: StageConfig, entry: StudentEntry, full_text: str
) -> SweepResult | None:
    """Rescore one student and return the diff vs. their current entry."""
    module = cfg.module
    prior = load_priors(cfg, entry.name)

    grade = module.rescore_from_repo(
        student_name=entry.name,
        repo_url=entry.repo_url,
        submitted_at=None,
        prior=prior,
    ) if cfg.n > 0 else module.rescore_from_repo(
        student_name=entry.name,
        repo_url=entry.repo_url,
    )

    if grade is None:
        return SweepResult(
            student=entry, new_raw=0, breakdown=[],
            prior_effective=entry.last_regrade_score or entry.header_score,
            skipped_reason="unparseable repo URL",
        )

    new_raw = grade.raw_total
    # Find the section text for this student to scrape 'before' scores.
    section_text = "\n".join(
        full_text.splitlines()[entry.section_start:entry.section_end + 1]
    )

    breakdown: list[tuple[str, int, int]] = []
    for label, attr, max_pts in cfg.criterion_columns:
        before = _parse_before_score(section_text, label, max_pts)
        if before is None:
            before = 0
        after = getattr(grade, attr, 0)
        breakdown.append((label, before, after))

    prior_effective = entry.last_regrade_score if entry.last_regrade_score is not None else entry.header_score

    # Collaborator penalty — Stage 2 only. Parse 'Collaborator-status penalty | **−N**'
    # (or '−N' / '-N' variants) from the section text for the 'before' value; pull
    # the 'after' value off the Grade object.
    new_collab_penalty = int(getattr(grade, "collab_penalty", 0) or 0)
    prior_collab_penalty = 0
    m = re.search(
        r"Collaborator[- ]status penalty[^|]*\|\s*\**\s*[−\-]?\s*(\d+)\s*\**\s*\|",
        section_text, re.IGNORECASE,
    )
    if m:
        prior_collab_penalty = int(m.group(1))

    return SweepResult(
        student=entry, new_raw=new_raw,
        breakdown=breakdown, prior_effective=prior_effective,
        prior_collab_penalty=prior_collab_penalty,
        new_collab_penalty=new_collab_penalty,
    )


def _effective_for(raw: int, floor_pct: int) -> int:
    """Apply the working-repo floor: effective = max(raw, floor) when raw > 0."""
    if raw <= 0:
        return raw
    floor_val = round(TOTAL_POINTS * floor_pct / 100)
    return max(raw, floor_val)


def build_regrade_block(
    cfg: StageConfig, result: SweepResult, today: datetime
) -> list[str]:
    """Render the markdown lines for a `### Updated YYYY-MM-DD (re-grade)` block.

    Includes raw-criterion deltas AND (when relevant) a Floor-adjustment row
    so the reader can reconcile the rubric breakdown against the recorded
    effective score.
    """
    date_str = today.strftime("%Y-%m-%d")
    floor_val = round(TOTAL_POINTS * cfg.floor_pct / 100)

    lines: list[str] = []
    lines.append(f"### Updated {date_str} (re-grade)")
    lines.append("")
    lines.append("The post-deadline revision sweep picked up the following changes:")
    lines.append("")
    lines.append("| Criterion | Before | After | Δ |")
    lines.append("|---|---|---|---|")

    sub_before = 0
    sub_after = 0
    for label, max_pts in [(c[0], c[2]) for c in cfg.criterion_columns]:
        row = next((r for r in result.breakdown if r[0] == label), None)
        if row is None:
            continue
        _, before, after = row
        delta = after - before
        sign = "+" if delta > 0 else ("±" if delta == 0 else "")
        lines.append(
            f"| {label} | {before} / {max_pts} | {after} / {max_pts} | "
            f"{sign}{delta} |"
        )
        sub_before += before
        sub_after += after

    # Rubric subtotal row (sum of criterion scores — pre-penalty).
    sub_delta = sub_after - sub_before
    sub_sign = "+" if sub_delta > 0 else ("±" if sub_delta == 0 else "")
    lines.append(
        f"| **Rubric subtotal** | **{sub_before} / 100** | **{sub_after} / 100** | "
        f"**{sub_sign}{sub_delta}** |"
    )

    # Collaborator penalty row (Stage 2) — only when relevant.
    pen_before = result.prior_collab_penalty
    pen_after = result.new_collab_penalty
    if pen_before or pen_after:
        # Δ for penalty: a *reduced* penalty improves the score, so the
        # visible delta should be positive when the penalty drops.
        pen_delta = pen_before - pen_after
        pen_sign = "+" if pen_delta > 0 else ("±" if pen_delta == 0 else "")
        before_cell = f"−{pen_before}" if pen_before > 0 else "0"
        after_cell = f"−{pen_after}" if pen_after > 0 else "0"
        lines.append(
            f"| Collaborator penalty | {before_cell} | {after_cell} | "
            f"{pen_sign}{pen_delta} |"
        )

    # Raw total row (subtotal − penalties; this is what the floor compares against).
    raw_before = max(0, sub_before - pen_before)
    raw_after = max(0, sub_after - pen_after)
    eff_before = result.prior_effective
    eff_after = _effective_for(raw_after, cfg.floor_pct)
    if pen_before or pen_after:
        raw_delta = raw_after - raw_before
        raw_sign = "+" if raw_delta > 0 else ("±" if raw_delta == 0 else "")
        lines.append(
            f"| **Raw total** | **{raw_before} / 100** | **{raw_after} / 100** | "
            f"**{raw_sign}{raw_delta}** |"
        )

    # Floor adjustment row — only when the floor was/is doing work (raw < floor).
    floor_before = eff_before - raw_before
    floor_after = eff_after - raw_after
    if floor_before > 0 or floor_after > 0:
        before_cell = f"+{floor_before}" if floor_before > 0 else "—"
        after_cell = f"+{floor_after}" if floor_after > 0 else "—"
        f_delta = floor_after - floor_before
        f_sign = "+" if f_delta > 0 else ("±" if f_delta == 0 else "")
        lines.append(
            f"| Floor adjustment ({cfg.floor_pct}% floor) | {before_cell} | "
            f"{after_cell} | {f_sign}{f_delta} |"
        )

    # Final effective row.
    eff_delta = eff_after - eff_before
    eff_sign = "+" if eff_delta > 0 else ("±" if eff_delta == 0 else "")
    lines.append(
        f"| **Final (effective)** | **{eff_before} / 100** | "
        f"**{eff_after} / 100** | **{eff_sign}{eff_delta}** |"
    )
    lines.append("")
    lines.append(
        f"**Re-graded final:** {eff_after} / 100 (effective {date_str})"
    )
    lines.append("")
    return lines


# ------------------------------------------------------------------
# Report patching
# ------------------------------------------------------------------

def insert_regrade_blocks(
    text: str, entries: list[StudentEntry], blocks_by_student: dict[str, list[str]]
) -> str:
    """Walk students in reverse so line indices stay valid as we splice."""
    lines = text.splitlines()
    for entry in reversed(entries):
        blk = blocks_by_student.get(entry.name)
        if not blk:
            continue
        # Insert just before the section's trailing `---` (if present)
        # or at section_end + 1.
        insert_at = entry.section_end + 1
        # Walk back from section_end to find the trailing `---`.
        for j in range(entry.section_end, entry.section_start, -1):
            if lines[j].strip() == "---":
                insert_at = j
                break
            if lines[j].strip():
                break
        # If there's not a trailing `---`, insert right after the section.
        lines[insert_at:insert_at] = blk
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def add_sweep_lock(text: str, today: datetime) -> str:
    """Insert `**Sweep performed:** YYYY-MM-DD — stage locked.` into the preamble."""
    if SWEEP_LOCK_RE.search(text):
        return text  # already locked — caller checks; this is defensive
    date_str = today.strftime("%Y-%m-%d")
    lock_line = (
        f"**Sweep performed:** {date_str} — stage locked. Per the "
        "[BUS-629 revision-sweep policy]"
        "(../../../../docs/decisions/bus629/"
        "2026-05-15-bus629-regrade-feedback-delivery.md), "
        "no further re-grades for this stage."
    )
    # Place it right above the first horizontal rule (the one before `## Rubric (recap)`).
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "---":
            lines.insert(i, lock_line)
            lines.insert(i, "")
            break
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def _name_matches_row(student_cell: str, name: str) -> bool:
    """Match a class-summary row by name, tolerating an existing `(re-graded ...)` suffix.

    Returns True iff `name` appears as the literal name token at the start of
    the row (i.e., the cell is the student's name optionally followed by a
    `(re-graded ...)` parenthetical), so we don't match partial substrings
    from a second row that happens to contain the same name fragment.
    """
    cell = student_cell.strip()
    name = name.strip()
    if cell == name:
        return True
    # Allow `Name (re-graded ...)` or `Name (re-graded)`.
    if cell.lower().startswith(name.lower()):
        tail = cell[len(name):].lstrip()
        if tail.startswith("(") and "re-grad" in tail.lower():
            return True
    return False


def update_class_summary(
    text: str,
    today: datetime,
    bumped_by_sweep: dict[str, int],
    floor_pct: int,
) -> str:
    """Annotate just-swept rows + recompute Mean / Floor-applied aggregates.

    `bumped_by_sweep` maps student name → new effective score; only rows
    matching those names get a `(re-graded YYYY-MM-DD)` annotation, so any
    pre-existing manual re-grade rows are left untouched.
    """
    date_str = today.strftime("%Y-%m-%d")
    floor_val = round(TOTAL_POINTS * floor_pct / 100)
    lines = text.splitlines()
    in_summary = False
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## class summary"):
            in_summary = True
            continue
        if in_summary and line.startswith("## "):
            break
        if not in_summary or not line.startswith("|"):
            continue
        if "---" in line or line.lower().startswith("| student"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        student_cell = cells[0]
        for name, new_score in bumped_by_sweep.items():
            if _name_matches_row(student_cell, name):
                # Only annotate THIS row; skip if already annotated for today.
                if f"re-graded {date_str}" in student_cell.lower():
                    break
                # Strip any prior `(re-graded ...)` parenthetical and re-add today's.
                base = re.sub(r"\s*\(re-graded[^)]*\)\s*$", "", student_cell).strip()
                cells[0] = f"{base} (re-graded {date_str})"
                cells[1] = re.sub(r"\d+\s*/\s*100", f"{new_score} / 100", cells[1], count=1)
                lines[i] = "| " + " | ".join(cells) + " |"
                break

    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    # Recompute aggregates from the effective scores of each student section.
    effective_scores: list[tuple[str, int]] = []
    floored_names: list[str] = []
    for sec_m in STUDENT_HEADER_RE.finditer(text):
        name = sec_m.group("name").strip()
        sec_start = sec_m.start()
        next_m = STUDENT_HEADER_RE.search(text, sec_m.end())
        sec_end = next_m.start() if next_m else len(text)
        section = text[sec_start:sec_end]
        header_score = int(sec_m.group("score"))
        rg = list(REGRADE_FINAL_RE.finditer(section))
        latest = max(rg, key=lambda x: x.group("date")) if rg else None
        effective = int(latest.group("score")) if latest else header_score
        if effective == 0:
            # Non-submission — skip from aggregates.
            continue
        effective_scores.append((name, effective))
        # A student is on the floor iff effective == floor_val AND there's a
        # `Floor adjustment` line in the section. (Re-graded students who
        # left the floor won't have it in their re-grade block.)
        on_floor = (
            effective == floor_val
            and "Floor adjustment" in section.split("### Updated")[0]
            and (latest is None or "Floor adjustment" in section.split("### Updated")[-1])
        )
        if on_floor:
            floored_names.append(name)

    if effective_scores:
        mean = sum(s for _, s in effective_scores) / len(effective_scores)
        floor_str = (
            f"{len(floored_names)} of {len(effective_scores)} submissions"
            + (f" ({', '.join(floored_names)})" if floored_names else "")
        )
        text = re.sub(
            r"\*\*Mean(?:\s*\([^)]*\))?:\*\*[^\n]*",
            f"**Mean (submissions only):** {mean:.1f}",
            text, count=1,
        )
        text = re.sub(
            r"\*\*Floor applied:\*\*[^\n]*",
            f"**Floor applied:** {floor_str}",
            text, count=1,
        )

    return text


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Post-deadline revision sweep for BUS-629 stages."
    )
    p.add_argument("--stage", type=int, required=True, choices=[0, 1, 2, 3, 4, 5])
    p.add_argument("--dry-run", action="store_true",
                   help="Print what would change; don't write.")
    p.add_argument("--force", action="store_true",
                   help="Override the top-of-file sweep lock.")
    p.add_argument("--student", default="",
                   help="Limit sweep to one student (case-insensitive substring).")
    p.add_argument("--today", default="",
                   help="Override 'today' (ISO YYYY-MM-DD); defaults to system date.")
    p.add_argument("--report", type=Path, default=None,
                   help="Override the STAGE{N}_GRADES.md path (for testing).")
    args = p.parse_args(argv)

    cfg = stage_config(args.stage)
    if args.report is not None:
        cfg.report_path = args.report
    if not cfg.report_path.exists():
        print(f"error: {cfg.report_path} not found", file=sys.stderr)
        return 1

    today = (
        datetime.strptime(args.today, "%Y-%m-%d") if args.today else datetime.now()
    )
    text = cfg.report_path.read_text(encoding="utf-8")

    lock = SWEEP_LOCK_RE.search(text)
    if lock and not args.force and not args.dry_run:
        print(
            f"Stage {args.stage} is locked — sweep already performed "
            f"({lock.group('date')}). Use --force to override "
            f"or --dry-run to preview.",
            file=sys.stderr,
        )
        return 2
    if lock and args.dry_run:
        print(
            f"(stage is locked; --dry-run shows what a re-sweep would do)"
        )

    entries, _ = parse_report(text)
    if args.student:
        needle_tokens = set(re.split(r"\s+", args.student.lower().strip()))
        def _matches(name: str) -> bool:
            name_tokens = set(re.split(r"\s+", name.lower().strip()))
            # Match if the smaller token set is a subset of the larger,
            # OR if there's a substring containment either direction.
            if not needle_tokens or not name_tokens:
                return False
            if needle_tokens <= name_tokens or name_tokens <= needle_tokens:
                return True
            return args.student.lower() in name.lower() or name.lower() in args.student.lower()
        entries = [e for e in entries if _matches(e.name)]
        if not entries:
            print(f"No matching student for --student '{args.student}'.", file=sys.stderr)
            return 1

    print(f"\nSweep for Stage {args.stage} — {len(entries)} student(s) to check.")
    print(f"Report: {cfg.report_path}")
    print(f"Effective date: {today.strftime('%Y-%m-%d')}")
    if args.dry_run:
        print("(DRY RUN — no writes)")
    print()

    blocks: dict[str, list[str]] = {}
    bumped_effective: dict[str, int] = {}
    bumps = 0
    no_change = 0
    skipped = 0
    for entry in entries:
        try:
            result = run_sweep_for_student(cfg, entry, text)
        except Exception as e:
            print(f"  {entry.name}: ERROR {e}", file=sys.stderr)
            skipped += 1
            continue
        if result is None or result.skipped_reason:
            reason = result.skipped_reason if result else "no result"
            print(f"  {entry.name}: SKIP ({reason})")
            skipped += 1
            continue
        new_effective = _effective_for(result.new_raw, cfg.floor_pct)
        delta = new_effective - result.prior_effective
        if delta > 0:
            print(
                f"  {entry.name}: BUMP {result.prior_effective} → "
                f"{new_effective} (+{delta}) [raw {result.new_raw}]"
            )
            blocks[entry.name] = build_regrade_block(cfg, result, today)
            bumped_effective[entry.name] = new_effective
            bumps += 1
        else:
            print(
                f"  {entry.name}: no change ({result.prior_effective}; "
                f"new effective {new_effective}, raw {result.new_raw})"
            )
            no_change += 1

    print()
    print(f"Summary — bumps: {bumps}, no-change: {no_change}, skipped: {skipped}")

    if args.dry_run:
        # Optional: print the blocks that would be inserted.
        for name, blk in blocks.items():
            print(f"\n--- would insert for {name} ---")
            print("\n".join(blk))
        return 0

    if not blocks and not args.force:
        # Still apply the lock so re-runs are refused.
        new_text = add_sweep_lock(text, today)
        cfg.report_path.write_text(new_text, encoding="utf-8")
        print(f"\nNo bumps to apply. Lock written to {cfg.report_path.name}.")
        return 0

    new_text = insert_regrade_blocks(text, entries, blocks)
    new_text = update_class_summary(
        new_text, today,
        bumped_by_sweep=bumped_effective,
        floor_pct=cfg.floor_pct,
    )
    new_text = add_sweep_lock(new_text, today)
    cfg.report_path.write_text(new_text, encoding="utf-8")
    print(f"\nWrote updates to {cfg.report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
