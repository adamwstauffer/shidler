"""Generosity-only grade curve for the FIN-321 fx-hedging graders.

Each stage is scored on a **0-100 scale** — the percent of that stage the
student earned (criterion fractions x criterion weights from `_weights.py`,
which sum to 100). The stage's project weight (`STAGE_WEIGHTS`) is applied
later, in the gradebook; the graders work entirely in "% of the stage."

The curve NEVER lowers a score. It only lifts a *working, accessible*
submission up to the stage's floor (`STAGE_FLOOR_PCT`). This is the same
generosity-only floor BUS-629 uses, but centralized here instead of
copy-pasted into every scanner, and reading the floor from the single source
of truth in `_weights.py`.

    curved = curved_score(raw_pct, stage, accessible=repo_ok)   # 0..100
    floored = floor_applied(raw_pct, stage, accessible=repo_ok) # bool

Policy (Adam): "For curved grades, Curved = MAX(raw, floor); never lower a
student's raw score." A non-submission (raw == 0) stays 0. The final score is
then **rounded up to the nearest whole percent** (ceiling) — same generosity
direction as the floor: rounding never costs a student a fraction of a point.
"""
from __future__ import annotations

import math

from _weights import STAGE_FLOOR_PCT


def stage_floor(stage: int) -> int:
    """The floor (0-100, % of stage) a working submission is lifted to."""
    return STAGE_FLOOR_PCT[stage]


def curved_score(raw_pct: float, stage: int, *, accessible: bool = True) -> float:
    """Effective stage score in 0-100, rounded UP to the nearest whole percent.

    - raw_pct <= 0 (nothing submitted / inaccessible-and-empty) -> 0.
    - accessible submission below the floor -> lifted to the floor.
    - otherwise -> the raw score, unchanged (never lowered).
    The surviving value is then ceiling-rounded to a whole number.
    """
    if raw_pct <= 0:
        return 0.0
    floor = STAGE_FLOOR_PCT[stage]
    effective = float(floor) if (accessible and raw_pct < floor) else float(raw_pct)
    return float(math.ceil(effective))


def floor_applied(raw_pct: float, stage: int, *, accessible: bool = True) -> bool:
    """True iff the floor actually lifted this score (for reporting)."""
    return accessible and 0 < raw_pct < STAGE_FLOOR_PCT[stage]


if __name__ == "__main__":
    for st in sorted(STAGE_FLOOR_PCT):
        f = STAGE_FLOOR_PCT[st]
        demo = [0, f - 10, f, f + 8, 100]
        print(f"Stage {st} (floor {f}): " + ", ".join(
            f"{r}->{curved_score(r, st):g}" + ("*" if floor_applied(r, st) else "")
            for r in demo
        ))
