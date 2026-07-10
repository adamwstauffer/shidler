"""Post-deadline generosity re-grade sweep for one FIN-321 fx-hedging stage.

Re-runs the stage scanner against the (updated) submission export. Because the
curve is generosity-only, a student's swept score can only rise: any student
whose fresh grade would fall below their pre-sweep result keeps the prior
score. The sweep reports who improved, rebuilds the internal report with the
protected scores, and **locks** the stage so it is not swept twice.

    python sweep_stage.py --stage N <export.zip|dir> [--report PATH]
        [--floor N] [--today YYYY-MM-DD] [--dry-run] [--force]

Policy (Adam): one batch sweep per stage after the deadline; no cap on the
bump; the stage locks once the sweep runs. Students just revise files in the
repo — no re-submission needed.

Note: for a student whose prior score already exceeds a fresh re-grade, the
Final row is protected to the prior value while the criterion rows reflect the
current repo; that intended divergence is what "generosity-only" means here.
"""
from __future__ import annotations

import argparse
import importlib
import re
import sys
from datetime import datetime
from pathlib import Path

import _repo
from _report import parse_prior_report, resolve_out_dir, build_report, build_pr_feedback

SWEEP_LOCK_RE = re.compile(r"^\*\*Sweep performed:\*\*", re.MULTILINE)


def _insert_lock(report: str, lock_line: str) -> str:
    """Insert the lock line into the preamble, just before the first `---`."""
    marker = "\n---\n"
    idx = report.find(marker)
    if idx == -1:
        return lock_line + "\n" + report
    return report[:idx] + "\n" + lock_line + report[idx:]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Generosity re-grade sweep for one stage.")
    ap.add_argument("--stage", type=int, required=True, choices=range(6))
    ap.add_argument("export", type=Path, help="Lamaku export .zip or extracted dir")
    ap.add_argument("--report", type=Path, default=None,
                    help="STAGE{N}_GRADES.md (defaults to <graded>/STAGE{N}_GRADES.md)")
    ap.add_argument("--floor", type=int, default=None)
    ap.add_argument("--today", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="sweep again despite the lock")
    args = ap.parse_args(argv)

    if not args.export.exists():
        print(f"error: export not found: {args.export}", file=sys.stderr)
        return 1
    mod = importlib.import_module(f"grade_stage{args.stage}")
    floor = args.floor if args.floor is not None else mod.DEFAULT_FLOOR_PCT
    today = (datetime.strptime(args.today, "%Y-%m-%d").date()
             if args.today else datetime.now().date())

    out_dir = resolve_out_dir(args.export, None)
    report_path = args.report or (out_dir / f"STAGE{args.stage}_GRADES.md")

    if report_path.exists() and SWEEP_LOCK_RE.search(
            report_path.read_text(encoding="utf-8")) and not args.force:
        print(f"Stage {args.stage} already swept (locked): {report_path}")
        print("Re-run with --force to override.")
        return 2

    prior = parse_prior_report(report_path if report_path.exists() else None)
    subs = _repo.discover_submissions(args.export)
    print(f"Sweeping Stage {args.stage}: {len(subs)} submissions.")

    reports, bumps = [], []
    for sub in subs:
        r = mod.grade(sub, prior_weak=False)
        p = prior.get(_repo.normalize_name(sub.name))
        new_final = r.final
        if p is not None:
            if new_final > p:
                bumps.append((sub.name, p, new_final))
            if r.raw_pct < p:            # protect prior score (generosity-only)
                r.raw_pct = p
        reports.append(r)
        print(f"  {sub.name}: prior={p if p is not None else '-'} new={new_final:g} "
              f"-> {r.final:g}")

    print(f"\n{len(bumps)} score(s) improved:")
    for name, before, after in sorted(bumps, key=lambda b: b[0]):
        print(f"  {name}: {before:g} -> {after:g}  (+{after - before:g})")

    if args.dry_run:
        print("\n[dry-run] no files written.")
        return 0

    body = build_report(args.stage, mod.STAGE_LABEL, mod.RUBRIC_ROWS, reports, floor, today)
    lock = (f"**Sweep performed:** {today:%Y-%m-%d} — stage locked. Generosity-only "
            f"re-grade; no further sweeps for this stage.")
    body = _insert_lock(body, lock)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(body, encoding="utf-8")
    print(f"\nWrote {report_path} (locked).")

    fb_root = out_dir / "_pr_feedback"
    for r in reports:
        d = fb_root / _repo.lastname_slug(r.name)
        d.mkdir(parents=True, exist_ok=True)
        (d / "feedback-file.md").write_text(build_pr_feedback(args.stage, r, today), encoding="utf-8")
    print(f"Refreshed {len(reports)} PR-feedback files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
