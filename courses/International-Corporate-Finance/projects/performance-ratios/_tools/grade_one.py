"""One-off grading driver: grade a single student against stages 0/1/2 by
repo URL, then append the new entries to each STAGE{N}_GRADES.md report.

Re-uses the per-stage `rescore_from_repo` entry points so the scoring logic
is identical to the bulk grading runs. Skips a stage cleanly when the
student hasn't submitted that stage's artifact yet.

USAGE:
    python grade_one.py --name "First Last" --repo https://github.com/<owner>/<repo>
                        [--stages 0,1,2] [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

import grade_stage0
import grade_stage1
import grade_stage2

COURSE_ROOT = Path(__file__).resolve().parent.parent.parent / "BUS-629-VEMBA"

STAGE_REPORTS = {
    0: COURSE_ROOT / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md",
    1: COURSE_ROOT / "ignore" / "stage1" / "graded" / "STAGE1_GRADES.md",
    2: COURSE_ROOT / "ignore" / "stage2" / "graded" / "STAGE2_GRADES.md",
}
STAGE_FLOORS = {0: 90, 1: 80, 2: 80}


def grade_stage(stage_n: int, name: str, repo_url: str) -> object:
    if stage_n == 0:
        return grade_stage0.rescore_from_repo(student_name=name, repo_url=repo_url)
    if stage_n == 1:
        prior = grade_stage1.lookup_prior(
            grade_stage1.parse_prior_report(STAGE_REPORTS[0]), name
        )
        return grade_stage1.rescore_from_repo(
            student_name=name, repo_url=repo_url, prior=prior,
        )
    if stage_n == 2:
        merged = grade_stage2.merge_prior(
            grade_stage2.parse_prior_report(STAGE_REPORTS[0]),
            grade_stage2.parse_prior_report(STAGE_REPORTS[1]),
        )
        prior = grade_stage2.lookup_prior(merged, name)
        return grade_stage2.rescore_from_repo(
            student_name=name, repo_url=repo_url, prior=prior,
        )
    raise ValueError(f"unknown stage {stage_n}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--name", required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--stages", default="0,1,2",
                   help="Comma-separated stage numbers, default 0,1,2")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    stages = [int(s.strip()) for s in args.stages.split(",") if s.strip()]
    today = datetime.now()

    for n in stages:
        print(f"\n=== Stage {n} ===")
        grade = grade_stage(n, args.name, args.repo)
        if grade is None:
            print(f"  Stage {n}: rescore_from_repo returned None — skipping.")
            continue
        raw = grade.raw_total
        print(f"  raw={raw}/100 flags={','.join(grade.flags) or '-'}")

        module = {0: grade_stage0, 1: grade_stage1, 2: grade_stage2}[n]
        report_path = STAGE_REPORTS[n]
        floor_pct = STAGE_FLOORS[n]

        if args.dry_run:
            section = module._student_section(999, grade, floor_pct)
            print("--- preview ---")
            print(section)
            print("--- /preview ---")
            continue

        new_entries = module.write_or_update_grade_report(
            [grade], floor_pct, report_path, today=today,
        )
        if new_entries:
            print(f"  Appended {len(new_entries)} new entry to {report_path.name}")
        else:
            print(f"  No new entry (already recorded) in {report_path.name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
