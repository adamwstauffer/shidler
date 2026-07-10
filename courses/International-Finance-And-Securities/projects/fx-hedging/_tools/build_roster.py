"""Cross-stage roster for FIN-321 fx-hedging.

Walks the six `STAGE{0..5}_GRADES.md` reports under a graded directory, parses
each student's final score per stage (and repo URL), collapses name-spelling
variants, and writes `roster.md` + `roster.csv` (both gitignored — they live
under an `ignore/` tree).

    python build_roster.py --graded-dir DIR [--out-dir DIR]

`--graded-dir` is the folder that holds (or whose subfolders hold) the
STAGE{N}_GRADES.md files. Each stage report may live in its own
`stage{N}/graded/` subdir; this script searches recursively.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import _repo
from _weights import STAGE_WEIGHTS

STAGE_COUNT = 6
_HEADER_RE = re.compile(
    r"^##\s+\d+\.\s+(?P<name>.+?)\s+—\s+.*?\*\*(?P<score>\d+(?:\.\d+)?)\s*/\s*100\*\*",
    re.MULTILINE,
)
_REPO_RE = re.compile(r"^\*\*Repo:\*\*\s*(?P<url>\S+)", re.MULTILINE)


@dataclass
class StudentRow:
    name: str
    repo: str = ""
    stages: dict[int, float] = field(default_factory=dict)


def _find_stage_report(graded_dir: Path, stage: int) -> Path | None:
    hits = list(graded_dir.rglob(f"STAGE{stage}_GRADES.md"))
    return hits[0] if hits else None


def parse_stage_report(path: Path, stage: int) -> dict[str, tuple[float, str, str]]:
    """key -> (score, repo_url, display_name) for one stage report."""
    out: dict[str, tuple[float, str, str]] = {}
    text = path.read_text(encoding="utf-8", errors="ignore")
    # split into per-student blocks on the `## N.` headers
    blocks = re.split(r"(?=^##\s+\d+\.\s)", text, flags=re.MULTILINE)
    for block in blocks:
        m = _HEADER_RE.search(block)
        if not m:
            continue
        name = m.group("name").strip()
        score = float(m.group("score"))
        repo_m = _REPO_RE.search(block)
        repo = repo_m.group("url") if repo_m else ""
        out[_repo.normalize_name(name)] = (score, repo, name)
    return out


def collect(graded_dir: Path) -> list[StudentRow]:
    rows: dict[str, StudentRow] = {}
    for stage in range(STAGE_COUNT):
        path = _find_stage_report(graded_dir, stage)
        if not path:
            continue
        for key, (score, repo, name) in parse_stage_report(path, stage).items():
            row = rows.get(key)
            if row is None:
                row = rows[key] = StudentRow(name=name)
            row.stages[stage] = score
            if repo and not row.repo:
                row.repo = repo
    return sorted(rows.values(), key=lambda r: r.name.split()[-1].lower() if r.name.split() else r.name)


def _weighted_project_pct(row: StudentRow) -> float:
    """Project-level % = sum(stage_final/100 * stage_weight) over graded stages."""
    return round(sum((row.stages.get(s, 0) / 100) * w for s, w in STAGE_WEIGHTS.items()), 1)


def write_markdown(rows: list[StudentRow], out_path: Path) -> None:
    hdr = ["Student", "Repo"] + [f"S{s}" for s in range(STAGE_COUNT)] + ["Project %"]
    lines = ["# FIN-321 fx-hedging — Roster", "", "| " + " | ".join(hdr) + " |",
             "|" + "|".join(["---"] * len(hdr)) + "|"]
    for r in rows:
        cells = [r.name, r.repo or "—"]
        cells += [f"{r.stages[s]:g}" if s in r.stages else "—" for s in range(STAGE_COUNT)]
        cells.append(f"{_weighted_project_pct(r):g}")
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append(f"*{len(rows)} students. Project % weights stages "
                 + "/".join(f"{STAGE_WEIGHTS[s]}" for s in range(STAGE_COUNT)) + ".*")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def write_csv(rows: list[StudentRow], out_path: Path) -> None:
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["student", "repo"] + [f"stage{s}" for s in range(STAGE_COUNT)] + ["project_pct"])
        for r in rows:
            w.writerow([r.name, r.repo]
                       + [r.stages.get(s, "") for s in range(STAGE_COUNT)]
                       + [_weighted_project_pct(r)])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build the FIN-321 fx-hedging cross-stage roster.")
    ap.add_argument("--graded-dir", type=Path, required=True,
                    help="dir containing (or whose subdirs contain) STAGE{N}_GRADES.md")
    ap.add_argument("--out-dir", type=Path, default=None)
    args = ap.parse_args(argv)
    if not args.graded_dir.exists():
        print(f"error: {args.graded_dir} not found", file=sys.stderr)
        return 1
    rows = collect(args.graded_dir)
    out_dir = args.out_dir or args.graded_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    write_markdown(rows, out_dir / "roster.md")
    write_csv(rows, out_dir / "roster.csv")
    print(f"Wrote roster.md + roster.csv ({len(rows)} students) to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
