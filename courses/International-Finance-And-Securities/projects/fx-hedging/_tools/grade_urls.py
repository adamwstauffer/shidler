"""Grade a LIST of repos (by URL) against one stage and WRITE the grade files.

Fills the gap between the two existing entry points: `grade_one.py` spot-checks
a single repo and writes nothing, while the per-stage scanners discover
submissions from a Lamaku export zip. This one grades an explicit `Name=URL`
list — the shape of an ad-hoc pass where students just handed over repo URLs —
and writes the same two artifacts the scanners do: the internal
`STAGE{N}_GRADES.md` and the per-student PR feedback files.

    python grade_urls.py --stage 0 --out-dir DIR [--floor N] [--today YYYY-MM-DD] \
        "Joy Scofield=https://github.com/joys7-ai/Scofield-Joy" \
        "Kiley Gennerman=https://github.com/Kileyge/Kiley-Gennerman"
"""
from __future__ import annotations

import argparse
import importlib
import sys
from datetime import datetime
from pathlib import Path

import _repo
from _repo import Submission
from _report import build_report, build_pr_feedback
from _grading_comments import core
from _weights import STAGE_FLOOR_PCT


def _parse_student(spec: str) -> tuple[str, str]:
    name, _, url = spec.partition("=")
    name, url = name.strip(), url.strip()
    if not name or not url:
        raise argparse.ArgumentTypeError(f"expected 'Name=URL', got: {spec!r}")
    return name, url


def _parse_named(spec: str, what: str) -> tuple[str, str]:
    """Split a `Name=value` flag into (normalized-name-key, value)."""
    name, _, val = spec.partition("=")
    name, val = name.strip(), val.strip()
    if not name or not val:
        raise argparse.ArgumentTypeError(f"expected 'Name={what}', got: {spec!r}")
    return _repo.normalize_name(name), val


def main(argv: list[str] | None = None) -> int:
    # Feedback text uses ✓ and em-dashes; force UTF-8 stdout for the progress log.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    ap = argparse.ArgumentParser(
        description="Grade a Name=URL list against one stage and write the grade files.")
    ap.add_argument("--stage", type=int, required=True, choices=range(6))
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--floor", type=int, default=None,
                    help="override the stage's default floor %")
    ap.add_argument("--today", default=None, help="YYYY-MM-DD (defaults to today)")
    ap.add_argument("--adjust", action="append", default=[], metavar="Name=+N",
                    help="instructor score adjustment applied AFTER the curve (repeatable)")
    ap.add_argument("--adjust-note", action="append", default=[], metavar="Name=text",
                    help="rubric-row note explaining a student's adjustment (repeatable)")
    ap.add_argument("--comment", action="append", default=[], metavar="Name=text",
                    help="extra feedback bullet appended to that student's review (repeatable)")
    ap.add_argument("students", nargs="+", type=_parse_student, metavar="Name=URL")
    args = ap.parse_args(argv)

    mod = importlib.import_module(f"grade_stage{args.stage}")
    floor = args.floor if args.floor is not None else STAGE_FLOOR_PCT[args.stage]
    today = (datetime.strptime(args.today, "%Y-%m-%d").date()
             if args.today else datetime.now().date())

    adjustments = dict(_parse_named(a, "+N") for a in args.adjust)
    adjust_notes = dict(_parse_named(a, "text") for a in args.adjust_note)
    comments: dict[str, list[str]] = {}
    for c in args.comment:
        key, txt = _parse_named(c, "text")
        comments.setdefault(key, []).append(txt)

    reports = []
    for name, url in args.students:
        print(f"  grading {name} ...", end=" ", flush=True)
        sub = Submission(student_id="", name=name, submitted_at=None,
                         folder=None, github_url=url)
        r = mod.grade(sub, prior_weak=False)
        key = _repo.normalize_name(name)
        if key in adjustments:
            r.adjustment = float(adjustments[key])
            r.adjustment_note = adjust_notes.get(key, "instructor discretion")
        for txt in comments.get(key, []):
            r.suggestions.append(core(txt))
        reports.append(r)
        print(f"raw={r.raw_pct:g} final={r.final:g} flags={','.join(r.flags) or '-'}")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / f"STAGE{args.stage}_GRADES.md"
    report_path.write_text(
        build_report(args.stage, mod.STAGE_LABEL, mod.RUBRIC_ROWS, reports, floor, today),
        encoding="utf-8")
    print(f"Wrote {report_path}")

    fb_root = out_dir / "_pr_feedback"
    for r in reports:
        d = fb_root / _repo.lastname_slug(r.name)
        d.mkdir(parents=True, exist_ok=True)
        (d / "feedback-file.md").write_text(
            build_pr_feedback(args.stage, r, today, floor), encoding="utf-8")
    print(f"Wrote {len(reports)} PR-feedback files under {fb_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
