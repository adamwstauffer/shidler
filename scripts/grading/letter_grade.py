#!/usr/bin/env python3
"""Convert a numeric score to a letter grade on Adam W. Stauffer's standard scale.

Single source of truth for the thresholds: docs/grading-scale.md.
Do not hard-code letter grades elsewhere; import or shell out to this.

    from letter_grade import letter_grade
    letter_grade(92)      # -> "A-"

    python letter_grade.py 92 88.5 64.9   # prints each score with its letter
"""
from __future__ import annotations
import sys

# (minimum score, letter) — highest first. Mirrors docs/grading-scale.md exactly.
SCALE = [
    (97, "A+"),
    (93, "A"),
    (90, "A-"),
    (87, "B+"),
    (83, "B"),
    (80, "B-"),
    (77, "C+"),
    (73, "C"),
    (70, "C-"),
    (67, "D+"),
    (65, "D"),
]


def letter_grade(score: float) -> str:
    """Return the letter grade for a numeric score. Below 65 is F."""
    for minimum, letter in SCALE:
        if score >= minimum:
            return letter
    return "F"


def _main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    for raw in argv:
        try:
            score = float(raw)
        except ValueError:
            print(f"{raw}: not a number", file=sys.stderr)
            return 2
        print(f"{raw} -> {letter_grade(score)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
