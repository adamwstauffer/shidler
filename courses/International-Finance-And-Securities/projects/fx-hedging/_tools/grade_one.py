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

from _repo import Submission
from _report import letter


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Grade one repo against one stage.")
    ap.add_argument("--stage", type=int, required=True, choices=range(6))
    ap.add_argument("--name", required=True)
    ap.add_argument("--repo", required=True, help="student repo URL")
    ap.add_argument("--today", default=None)
    args = ap.parse_args(argv)

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
    return 0


if __name__ == "__main__":
    sys.exit(main())
