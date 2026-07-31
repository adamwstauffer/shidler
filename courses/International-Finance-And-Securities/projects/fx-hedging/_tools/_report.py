"""Shared report + PR-feedback writers for the FIN-321 fx-hedging graders.

Every stage emits the same two artifacts, so the layout lives here once:

  - `build_report(...)`  -> internal STAGE{N}_GRADES.md (HAS scores):
        header + rubric recap + one numbered section per student
        (curved final, criterion table, floor adjustment when applied,
        flags, and the CORE/BACKWARD/FORWARD suggestion block) + class summary.

  - `build_pr_feedback(...)` -> _pr_feedback/{lastname}/feedback-file.md:
        a Criterion / Score / Notes rubric table (per-criterion scores, so the
        student sees exactly where points were earned or lost) wrapped around
        the same suggestion block and stage-specific detector sections.
        (Score visibility in student feedback is an experiment per Adam,
        2026-07 — revert to score-free if it doesn't land well.)

Each scanner builds a list of `StudentReport` (rubric-agnostic) and hands it
here. The curve/letter/floor logic is centralized (via _curve), not repeated.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Callable

import _repo
from _curve import curved_score, floor_applied
from _weights import stage_pct, STAGE_FLOOR_PCT
from _grading_comments import render_suggestions, Suggestion

LETTER_SCALE = [
    ("A", 93), ("A-", 90), ("B+", 87), ("B", 83), ("B-", 80),
    ("C+", 77), ("C", 73), ("C-", 70), ("D+", 67), ("D", 63), ("D-", 60), ("F", 0),
]


def letter(pct: float) -> str:
    for name, lo in LETTER_SCALE:
        if pct >= lo:
            return name
    return "F"


@dataclass
class Criterion:
    label: str
    earned: float      # points earned
    max: float         # criterion max (% of the stage)
    note: str = ""     # detector note for the internal report


@dataclass
class StudentReport:
    name: str
    stage_n: int
    raw_pct: float
    accessible: bool
    criteria: list[Criterion]
    suggestions: list[Suggestion]
    flags: list[str] = field(default_factory=list)
    meta_lines: list[str] = field(default_factory=list)          # **Repo:** etc.
    pr_sections: list[tuple[str, list[str]]] = field(default_factory=list)  # (heading, md lines)
    adjustment: float = 0.0          # instructor discretion, applied AFTER the curve
    adjustment_note: str = ""        # shown in the rubric row explaining the adjustment

    @property
    def final(self) -> float:
        base = curved_score(self.raw_pct, self.stage_n, accessible=self.accessible)
        # An instructor bump never resurrects a non-submission (base 0).
        if not self.adjustment or base <= 0:
            return base
        return float(max(0.0, min(100.0, base + self.adjustment)))

    @property
    def floored(self) -> bool:
        return floor_applied(self.raw_pct, self.stage_n, accessible=self.accessible)


def _criterion_table(s: StudentReport, floor_pct: int, score_header: str = "Earned") -> list[str]:
    """Criterion / <score_header> / Notes table shared by the internal report and
    the student PR feedback. Shows raw + floor adjustment rows when the floor lifts
    the score, so the per-criterion numbers still reconcile to the final."""
    final = s.final
    base = curved_score(s.raw_pct, s.stage_n, accessible=s.accessible)  # curved, pre-adjustment
    rows = [f"| Criterion | {score_header} | Notes |", "|-----------|--------|-------|"]
    for c in s.criteria:
        rows.append(f"| {c.label} | {c.earned:g} / {c.max:g} | {c.note} |")
    if s.floored or base != s.raw_pct or s.adjustment:
        rows.append(f"| **Raw total** | **{s.raw_pct:g} / 100** | — |")
    if s.floored:
        rows.append(f"| **Floor adjustment** | **+{base - s.raw_pct:g}** | lifted to {floor_pct}% floor, rounded up |")
    elif base != s.raw_pct:
        rows.append(f"| **Rounded up** | **+{base - s.raw_pct:g}** | up to the nearest whole % |")
    if s.adjustment:
        rows.append(f"| **Instructor adjustment** | **{s.adjustment:+g}** | {s.adjustment_note or 'instructor discretion'} |")
    final_note = ("no gradable submission" if final == 0
                  else "instructor-adjusted" if s.adjustment
                  else "floor applied" if s.floored else "earned on merit")
    rows.append(f"| **Final** | **{final:g} / 100** | {final_note} |")
    return rows


def _pr_process_note(stage_n: int) -> list[str]:
    """Student-facing callout (Stage 2+ only): the primary feedback is the PR
    review on their repo; this LMS copy is the short version. Explains the how
    and the why so a student who has never opened a Pull Request can find it."""
    return [
        "### 📌 How your feedback is delivered",
        "",
        "Your primary feedback for this stage is a **detailed review posted as a Pull "
        "Request (PR) on your GitHub repository** — that is where the substantive, "
        "section-by-section guidance lives. The grade and notes above are the short version.",
        "",
        f"**To view it:** open your repo on GitHub → the **Pull requests** tab → the review "
        f"titled *“Stage {stage_n} review — … Treasury sign-off”*. Read it there, "
        "**reply in the thread** with questions or push-back, and use it to revise before the "
        "deadline (revisions can still lift this grade at the post-deadline sweep).",
        "",
        "*Why a PR?* It is how professional teams review work — feedback attached to the actual "
        "files, discussed in context, and closed out once addressed. Getting fluent in that loop "
        "is part of the skill this course builds.",
        "",
    ]


def _student_section(n: int, s: StudentReport, floor_pct: int) -> list[str]:
    final = s.final
    if final == 0:
        tag = " (no gradable submission)"
    elif s.floored:
        tag = f" ({letter(final)}, floor applied)"
    else:
        tag = f" ({letter(final)})"

    lines = [f"## {n}. {s.name} — **{final:g} / 100**{tag}", ""]
    lines.extend(s.meta_lines)
    if s.meta_lines:
        lines.append("")

    lines.extend(_criterion_table(s, floor_pct))
    lines.append("")
    if s.stage_n >= 2:
        lines.extend(_pr_process_note(s.stage_n))
    if s.flags:
        lines.append(f"*Flags: {', '.join(s.flags)}*")
        lines.append("")
    lines.extend(render_suggestions(s.suggestions, stage_n=s.stage_n))
    lines.append("---")
    return lines


def build_report(
    stage_n: int,
    stage_label: str,
    rubric_rows: list[tuple[str, str]],
    students: list[StudentReport],
    floor_pct: int,
    today: date,
) -> str:
    lines = [
        f"# FIN-321 Stage {stage_n} — Grade Report",
        "",
        f"**Stage:** {stage_label} ({stage_pct(stage_n)}% of project score)",
        f"**Graded:** {today:%Y-%m-%d}",
        f"**Submissions reviewed:** {len(students)}",
        f"**Floor policy:** {floor_pct}% floor for any accessible repo with the stage deliverable present.",
        "**Scores:** the per-criterion rubric (with scores) now also appears in the "
        "student PR feedback, so students can see where points were earned or lost "
        "(experiment, 2026-07 — revert to score-free feedback if it doesn't land).",
    ]
    if stage_n >= 2:
        lines.append(
            "**Delivery:** primary feedback for this stage is a PR review on each student's "
            "repo; the per-student feedback file (copy/pasted into the LMS) points students "
            "there and explains how to view and respond to it."
        )
    lines += [
        "",
        "---",
        "## Rubric (recap)",
        "",
        "| Criterion | Weight |",
        "|-----------|--------|",
    ]
    lines += [f"| {label} | {weight} |" for label, weight in rubric_rows]
    lines += ["", "---"]

    ordered = sorted(students, key=lambda s: s.name.split()[-1].lower() if s.name.split() else s.name)
    summary: list[tuple[str, float, str]] = []
    for i, s in enumerate(ordered, 1):
        lines.extend(_student_section(i, s, floor_pct))
        note = ("no submission" if s.final == 0
                else "floor applied" if s.floored else "earned")
        summary.append((s.name, s.final, note))

    lines += ["## Class summary", "", "| Student | Score | Notes |", "|---------|-------|-------|"]
    for name, sc, note in summary:
        lines.append(f"| {name} | {sc:g} / 100 | {note} |")
    submitted = [sc for _, sc, n in summary if n != "no submission"]
    if submitted:
        floored_n = sum(1 for _, _, n in summary if n == "floor applied")
        lines += [
            "",
            f"**Mean (submissions only):** {sum(submitted) / len(submitted):.1f}",
            f"**Submission rate:** {len(submitted)} of {len(summary)}",
            f"**Floor applied:** {floored_n} of {len(submitted)} submissions",
        ]
    lines.append("")
    return "\n".join(lines)


def build_pr_feedback(stage_n: int, s: StudentReport, today: date, floor_pct: int) -> str:
    """Student-facing grade + feedback block (the copy handed to the student).

    Leads with the name and grade — no internal labels (`floor applied`, flag
    codes) — then a descriptive criterion table and the step-by-step
    improvement suggestions. Mirrors `_tools/feedback-template.md`.
    """
    lines = [f"## {s.name} — **{s.final:g} / 100** ({letter(s.final)})", ""]
    lines.extend(s.meta_lines)
    if s.meta_lines:
        lines.append("")
    lines.extend(_criterion_table(s, floor_pct, score_header="Earned"))
    lines.append("")
    # Stage 2+ feedback is delivered primarily via a PR review on the student's
    # repo; the LMS copy points there. Stages 0–1 are file-only, no PR.
    if stage_n >= 2:
        lines.extend(_pr_process_note(stage_n))
    lines.extend(render_suggestions(s.suggestions, stage_n=s.stage_n))
    return "\n".join(lines).rstrip() + "\n"


# --- shared CLI driver (identical across all six scanners) -----------------
_PRIOR_HEADER_RE = re.compile(
    r"^##\s+\d+\.\s+(?P<name>.+?)\s+—\s+.*?\*\*(?P<score>\d+(?:\.\d+)?)\s*/\s*100\*\*",
    re.MULTILINE,
)


def parse_prior_report(path: Path | None) -> dict[str, float]:
    """Map normalized student name -> a prior stage's final score (0-100)."""
    out: dict[str, float] = {}
    if not path or not Path(path).exists():
        return out
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    for m in _PRIOR_HEADER_RE.finditer(text):
        out[_repo.normalize_name(m.group("name"))] = float(m.group("score"))
    return out


def resolve_out_dir(export: Path, out_dir: str | None) -> Path:
    if out_dir:
        return Path(out_dir)
    if export.parent.name.lower() == "ungraded":
        return export.parent.parent / "graded"
    base = export.parent if export.is_file() else export
    return base / "graded"


def clean_ungraded(export: Path) -> int:
    """Tidy the ungraded directory after a successful run: remove the extracted
    temp folders (always regenerable) and the processed zip(s) — the graded
    export and any older ones. A *newer* zip that appeared since is preserved so
    a later export isn't lost. Returns the count removed.

    These files are gitignored and not otherwise backed up, so this only runs
    when the caller passes --clean-ungraded.
    """
    ung = export.parent if export.is_file() else export
    cutoff = export.stat().st_mtime if export.is_file() else None
    removed = 0
    for p in sorted(ung.iterdir()):
        try:
            if p.is_dir() and p.name.startswith("_") and p.name.endswith("_extracted"):
                shutil.rmtree(p, ignore_errors=True)
                removed += 1
            elif (p.is_file() and p.suffix.lower() == ".zip"
                  and (cutoff is None or p.stat().st_mtime <= cutoff)):
                p.unlink()
                removed += 1
        except OSError as e:
            print(f"  (could not remove {p.name}: {e})", file=sys.stderr)
    print(f"Cleaned ungraded/: removed {removed} processed item(s) from {ung}")
    return removed


def run_scanner(
    stage_n: int,
    stage_label: str,
    rubric_rows: list[tuple[str, str]],
    grade_fn: Callable[..., StudentReport],
    *,
    default_floor: int,
    prior_stage: int | None = None,
    argv: list[str] | None = None,
) -> int:
    """CLI entry shared by grade_stage{0..5}.py.

    `grade_fn(sub, prior_weak=bool)` returns a StudentReport for one submission.
    `prior_stage` (if set) enables carry-forward recognition: a student whose
    score in that prior stage's report was below its floor gets `prior_weak=True`.
    """
    ap = argparse.ArgumentParser(description=f"FIN-321 Stage {stage_n} grader ({stage_label}).")
    ap.add_argument("export", type=Path, help="Lamaku export .zip or extracted dir")
    ap.add_argument("--floor", type=int, default=default_floor)
    ap.add_argument("--prior", type=Path, default=None,
                    help="prior stage STAGE_GRADES.md for carry-forward recognition")
    ap.add_argument("--out-dir", default=None)
    ap.add_argument("--today", default=None, help="YYYY-MM-DD (defaults to today)")
    ap.add_argument("--clean-ungraded", action="store_true",
                    help="after writing grades, delete the processed zip(s) and extracted "
                         "temp folders from the ungraded directory (keeps it organized)")
    args = ap.parse_args(argv)

    if not args.export.exists():
        print(f"error: export not found: {args.export}", file=sys.stderr)
        return 1
    today = (datetime.strptime(args.today, "%Y-%m-%d").date()
             if args.today else datetime.now().date())

    subs = _repo.discover_submissions(args.export)
    print(f"Discovered {len(subs)} submissions.")
    prior = parse_prior_report(args.prior)

    reports: list[StudentReport] = []
    for sub in subs:
        print(f"  grading {sub.student_id} {sub.name} ...", end=" ", flush=True)
        prior_weak = (
            prior_stage is not None
            and _repo.normalize_name(sub.name) in prior
            and prior[_repo.normalize_name(sub.name)] < STAGE_FLOOR_PCT[prior_stage]
        )
        r = grade_fn(sub, prior_weak=prior_weak)
        reports.append(r)
        print(f"raw={r.raw_pct:g}/100 final={r.final:g} flags={','.join(r.flags) or '-'}")

    out_dir = resolve_out_dir(args.export, args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / f"STAGE{stage_n}_GRADES.md"
    report_path.write_text(
        build_report(stage_n, stage_label, rubric_rows, reports, args.floor, today),
        encoding="utf-8")
    print(f"Wrote {report_path}")

    fb_root = out_dir / "_pr_feedback"
    for r in reports:
        d = fb_root / _repo.lastname_slug(r.name)
        d.mkdir(parents=True, exist_ok=True)
        (d / "feedback-file.md").write_text(build_pr_feedback(stage_n, r, today, args.floor), encoding="utf-8")
    print(f"Wrote {len(reports)} PR-feedback files under {fb_root}")

    if args.clean_ungraded:
        clean_ungraded(args.export)
    return 0
