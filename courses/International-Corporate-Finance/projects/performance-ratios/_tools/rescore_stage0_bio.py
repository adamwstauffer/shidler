"""One-off: rescore all Stage 0 students under the updated bio policy.

Parses STAGE0_GRADES.md for (name, repo URL, current rubric scores), then
re-runs `grade_stage0.rescore_from_repo` against the live repo state and
prints a side-by-side comparison. Does NOT modify the report file.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

import grade_stage0

REPORT = (
    Path(__file__).resolve().parent.parent.parent / "BUS-629-VEMBA"
    / "ignore" / "stage0" / "graded" / "STAGE0_GRADES.md"
)

HEADER_RE = re.compile(
    r"^## (\d+)\. (.+?) — \*\*(\d+) / 100\*\*",
    re.MULTILINE,
)
URL_RE = re.compile(r"https?://github\.com/[A-Za-z0-9_./-]+")
BIO_ROW_RE = re.compile(
    r"\| Bio quality \| (\d+) / 25 \|", re.MULTILINE
)
RAW_TOTAL_RE = re.compile(r"\*\*Raw total\*\* \| \*\*(\d+) / 100\*\*")
FLOOR_APPLIED_RE = re.compile(r"floor applied", re.IGNORECASE)


def parse_students(text: str) -> list[dict]:
    out = []
    headers = list(HEADER_RE.finditer(text))
    headers_with_end = [(m, headers[i + 1].start() if i + 1 < len(headers) else len(text))
                        for i, m in enumerate(headers)]
    for m, end in headers_with_end:
        section = text[m.start():end]
        url_match = URL_RE.search(section)
        if not url_match:
            continue
        bio_match = BIO_ROW_RE.search(section)
        raw_match = RAW_TOTAL_RE.search(section)
        old_final = int(m.group(3))
        old_bio = int(bio_match.group(1)) if bio_match else None
        old_raw = int(raw_match.group(1)) if raw_match else old_final
        out.append({
            "n": int(m.group(1)),
            "name": m.group(2).strip(),
            "url": url_match.group(0),
            "old_bio": old_bio,
            "old_raw": old_raw,
            "old_final": old_final,
            "floor_applied": bool(FLOOR_APPLIED_RE.search(section.split("\n", 1)[0])),
        })
    return out


def main() -> int:
    text = REPORT.read_text(encoding="utf-8")
    students = parse_students(text)
    print(f"Parsed {len(students)} students from {REPORT.name}")
    print()
    print(f"{'#':>2}  {'Student':<26}  "
          f"{'Bio old':>8}  {'Bio new':>8}  {'Δbio':>5}  "
          f"{'Raw old':>8}  {'Raw new':>8}  {'Final old':>9}  {'Final new':>9}  {'ΔFinal':>7}")
    print("-" * 130)

    floor_pct = 90
    floor_value = round(100 * floor_pct / 100)
    deltas = []

    for s in students:
        print(f"{s['n']:>2}  {s['name'][:26]:<26}  ", end="", flush=True)
        g = grade_stage0.rescore_from_repo(student_name=s["name"], repo_url=s["url"])
        if g is None:
            print("rescore failed")
            continue
        new_bio = g.score_bio
        new_raw = g.raw_total
        floor_now = g.inspection.accessible and not g.inspection.private and new_raw < floor_value
        new_final = floor_value if floor_now else new_raw
        d_bio = (new_bio - s["old_bio"]) if s["old_bio"] is not None else 0
        d_final = new_final - s["old_final"]
        deltas.append((s["name"], s["old_final"], new_final, d_bio, d_final))
        print(
            f"{(s['old_bio'] or 0):>8}  {new_bio:>8}  {d_bio:+5d}  "
            f"{s['old_raw']:>8}  {new_raw:>8}  {s['old_final']:>9}  {new_final:>9}  {d_final:+7d}"
        )

    print()
    print("=== Summary ===")
    bumped = [d for d in deltas if d[4] > 0]
    print(f"Students whose final score increased: {len(bumped)}")
    for name, old, new, dbio, dfinal in bumped:
        print(f"  {name:<28} {old} → {new}  (Δbio={dbio:+d}, ΔFinal={dfinal:+d})")
    if not bumped:
        print("  (none — bio policy change didn't change any final score)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
