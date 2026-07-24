"""Grade ONE student's repo against ONE stage — spot-check / makeup helper.

Builds a synthetic submission from a repo URL and runs that stage's scanner,
printing the student's grade section to the terminal. Does NOT modify any
class report (use the stage scanner or sweep_stage for that).

    python grade_one.py --stage N --name "First Last" --repo URL [--today YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import importlib
import sys
from datetime import datetime

from datetime import date

from _repo import Submission
from _report import letter, build_pr_feedback
from _weights import STAGE_FLOOR_PCT


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Grade one repo against one stage.")
    ap.add_argument("--stage", type=int, required=True, choices=range(6))
    ap.add_argument("--name", required=True)
    ap.add_argument("--repo", required=True, help="student repo URL")
    ap.add_argument("--today", default=None)
    ap.add_argument("--feedback", action="store_true",
                    help="also print the student-facing PR feedback file")
    args = ap.parse_args(argv)

    # Feedback/report text uses ✓ and em-dashes; force UTF-8 stdout so a
    # Windows cp1252 console doesn't choke when printing them.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    mod = importlib.import_module(f"grade_stage{args.stage}")
    sub = Submission(student_id="", name=args.name, submitted_at=None,
                     folder=None, github_url=args.repo)
    r = mod.grade(sub, prior_weak=False)

    print(f"\nStage {args.stage} — {r.name}")
    print(f"  Final: {r.final:g} / 100 ({letter(r.final)})"
          + ("  [floor applied]" if r.floored else "")
          + ("  [raw " + f"{r.raw_pct:g}]" if r.floored else ""))
    print("  Criteria:")
    for c in r.criteria:
        print(f"    - {c.label}: {c.earned:g} / {c.max:g}  ({c.note})")
    print(f"  Flags: {', '.join(r.flags) or '-'}")

    if args.feedback:
        today = date.fromisoformat(args.today) if args.today else date.today()
        print("\n" + "=" * 72 + "\nSTUDENT-FACING FEEDBACK FILE\n" + "=" * 72)
        print(build_pr_feedback(args.stage, r, today, STAGE_FLOOR_PCT[args.stage]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
