"""One-shot: add an adjusted Team Project column to BUS-313 S26 score CSVs.

Adjusted score is on a 20-point scale. Curve is a class-relative linear
stretch: per file, the lowest raw_pct in the section maps exactly to FLOOR
and 100% stays at 100%. Nobody's percentage drops.

    slope         = (1 - FLOOR) / (1 - min_pct)
    adjusted_pct  = max(FLOOR, FLOOR + (raw_pct - min_pct) * slope)
    adjusted_/20  = ceil(adjusted_pct * NEW_MAX * 100) / 100   # ceil at 2dp
                                                               # for safety

New column header follows the existing Brightspace convention:
    Team Project Adjusted Points Grade <Numeric MaxPoints:20>
"""
from __future__ import annotations

import csv
from math import ceil
from pathlib import Path

BASE = Path(
    r"C:\GitHub\shidler\courses\BUS-313-Economic-And-Financial-Environment-Global-Business"
    r"\ignore\2026 Spring"
)
FILES = [
    "BUS-313-001 S26 Team Project - Scores Master - Roster.csv",
    "BUS-313-002 S26 Team Project - Scores Master - Roster.csv",
]
RAW_COL = "Team Project Points Grade <Numeric MaxPoints:15>"
NEW_COL = "Team Project Adjusted Points Grade <Numeric MaxPoints:20>"
RAW_MAX = 15
NEW_MAX = 20
FLOOR = 0.75


def adjust(raw: str, min_pct: float) -> str:
    if raw is None or raw.strip() == "":
        return ""
    raw_pct = float(raw) / RAW_MAX
    slope = (1 - FLOOR) / (1 - min_pct) if min_pct < 1 else 0
    new_pct = max(FLOOR, FLOOR + (raw_pct - min_pct) * slope)
    return f"{ceil(new_pct * NEW_MAX * 100) / 100:g}"


def section_min_pct(rows, raw_idx):
    raws = [r[raw_idx] for r in rows if r[raw_idx].strip() != ""]
    return min(float(v) for v in raws) / RAW_MAX


for name in FILES:
    path = BASE / name
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    raw_idx = header.index(RAW_COL)
    min_pct = section_min_pct(rows[1:], raw_idx)
    if NEW_COL in header:
        new_idx = header.index(NEW_COL)
        new_header = header
        new_rows = [new_header]
        for row in rows[1:]:
            row = list(row)
            row[new_idx] = adjust(row[raw_idx], min_pct)
            new_rows.append(row)
    else:
        insert_at = raw_idx + 1
        new_header = header[:insert_at] + [NEW_COL] + header[insert_at:]
        new_rows = [new_header]
        for row in rows[1:]:
            adj = adjust(row[raw_idx], min_pct)
            new_rows.append(row[:insert_at] + [adj] + row[insert_at:])

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(new_rows)

    print(f"Updated {name}: {len(new_rows) - 1} rows, min raw_pct={min_pct:.4f}")
