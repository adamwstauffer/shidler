"""BUS-629 master student roster builder.

Walks every `STAGEN_GRADES.md` under `ignore/stage{N}/graded/`, parses
per-student entries (name, score, repo URL, submitted timestamp), then
queries the GitHub API via `gh` for live repo state: visibility, last
commit date + message, and whether the instructor is a Write collaborator.

Outputs:

  - ignore/roster.md   — human-readable markdown table
  - ignore/roster.csv  — same data, machine-readable

Both outputs are gitignored (`**/ignore/` rule in the root `.gitignore`).

Run from the course directory:

    python _tools/build_roster.py

Options:

    --no-gh        Skip live GitHub API calls (offline mode — only uses
                   data already in the STAGEN_GRADES.md files).
    --out-dir DIR  Override the output directory (default: ignore/).
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

INSTRUCTOR_GITHUB_HANDLE = "adamwstauffer"
STAGE_COUNT = 6  # stages 0–5

GITHUB_URL_RE = re.compile(
    r"https?://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)"
)

# ------------------------------------------------------------------
# Per-student data model
# ------------------------------------------------------------------

@dataclass
class StageRecord:
    stage: int
    score: int | None = None
    submitted_at: str = ""
    floor_applied: bool = False
    workbook_or_memo: str = ""
    original_score: int | None = None
    regrade_date: str = ""


@dataclass
class StudentRow:
    name: str
    repo_url: str = ""
    owner: str = ""
    repo: str = ""
    stages: dict[int, StageRecord] = field(default_factory=dict)

    # Live GitHub state (populated by _enrich_with_gh)
    gh_queried: bool = False
    gh_accessible: bool = False
    gh_private: bool = False
    gh_default_branch: str = ""
    gh_last_commit_at: str = ""
    gh_last_commit_msg: str = ""
    gh_instructor_collaborator: bool = False
    gh_error: str = ""


# ------------------------------------------------------------------
# Parse STAGEN_GRADES.md files
# ------------------------------------------------------------------

def _normalize_name(name: str) -> str:
    tokens = re.findall(r"[A-Za-z]+", name.lower())
    return " ".join(sorted(tokens))


def parse_stage_report(path: Path, stage: int) -> dict[str, StageRecord]:
    """Return {normalized_name: StageRecord} for one stage's report.

    Also captures repo URL (per-student) so the caller can fold it back
    into the StudentRow.
    """
    out: dict[str, tuple[StageRecord, str, str]] = {}
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    header_re = re.compile(
        r"^## (?P<n>\d+)\. (?P<name>.+?) — \*\*(?P<score>\d+) / 100\*\*"
        r"(?P<modifiers>[^\n]*)",
        re.MULTILINE,
    )
    headers = [(m.start(), m) for m in header_re.finditer(text)]
    headers.append((len(text), None))
    parsed: dict[str, StageRecord] = {}
    repo_by_key: dict[str, str] = {}
    for i in range(len(headers) - 1):
        start, m = headers[i]
        end, _ = headers[i + 1]
        section = text[start:end]
        name = m.group("name").strip()
        score = int(m.group("score"))
        modifiers = m.group("modifiers").lower()
        floor = "floor applied" in modifiers

        sub_match = re.search(
            r"\*\*Submitted:\*\*\s*([^\n]+)", section
        )
        submitted_at = sub_match.group(1).strip() if sub_match else ""

        url_match = GITHUB_URL_RE.search(section)
        repo_url = url_match.group(0) if url_match else ""

        artifact_match = re.search(
            r"\*\*(?:Memo filename|Workbook|Stage \d+ file)[:*]+\s*`?([^\n`]+)`?",
            section,
        )
        artifact = artifact_match.group(1).strip() if artifact_match else ""

        regrade_matches = list(re.finditer(
            r"\*\*Re-graded final:\*\*\s*(?P<rg_score>\d+)\s*/\s*100"
            r"[^\n]*?effective\s*(?P<rg_date>\d{4}-\d{2}-\d{2})",
            section,
        ))
        regrade_score = None
        regrade_date = ""
        if regrade_matches:
            latest = max(regrade_matches, key=lambda m: m.group("rg_date"))
            regrade_score = int(latest.group("rg_score"))
            regrade_date = latest.group("rg_date")

        key = _normalize_name(name)
        effective_score = regrade_score if regrade_score is not None else score
        rec = StageRecord(
            stage=stage, score=effective_score, submitted_at=submitted_at,
            floor_applied=floor if regrade_score is None else False,
            workbook_or_memo=artifact,
        )
        rec.original_score = score
        rec.regrade_date = regrade_date
        parsed[key] = rec
        if repo_url:
            repo_by_key[key] = repo_url

    return {k: (rec, repo_by_key.get(k, ""), name_for_key(k, text))
            for k, rec in parsed.items()}


def name_for_key(key: str, text: str) -> str:
    """Re-find the display-name spelling for a normalized key inside text.

    We pull display names from the markdown so the roster shows the spelling
    each student used at submission time (e.g. "Phan Khanh" vs "Khanh Phan").
    """
    for m in re.finditer(r"^## \d+\. (.+?) —", text, re.MULTILINE):
        if _normalize_name(m.group(1)) == key:
            return m.group(1).strip()
    return key.title()


def _find_matching_key(key: str, existing: dict[str, StudentRow]) -> str | None:
    """Match `key` against existing student keys using subset-token logic.

    Returns the matched key if `key`'s tokens are a subset of an existing
    student's tokens (or vice versa), so that "Luong Phuong" and
    "Luong Duy Phuong" collapse to the same student.
    """
    if key in existing:
        return key
    new_tokens = set(key.split())
    if not new_tokens:
        return None
    best_match: str | None = None
    best_overlap = 0
    for ekey in existing.keys():
        e_tokens = set(ekey.split())
        if not e_tokens:
            continue
        # Require at least 2 shared tokens AND subset in either direction —
        # avoids spurious "single-shared-token" matches between unrelated
        # students who happen to share a common family name component.
        overlap = len(new_tokens & e_tokens)
        if overlap >= 2 and (new_tokens.issubset(e_tokens)
                              or e_tokens.issubset(new_tokens)):
            if overlap > best_overlap:
                best_overlap = overlap
                best_match = ekey
    return best_match


def collect_students(stage_root: Path) -> list[StudentRow]:
    students: dict[str, StudentRow] = {}
    for n in range(STAGE_COUNT):
        report = stage_root / f"stage{n}" / "graded" / f"STAGE{n}_GRADES.md"
        if not report.exists():
            continue
        parsed = parse_stage_report(report, n)
        for key, (rec, repo_url, display_name) in parsed.items():
            matched = _find_matching_key(key, students)
            if matched is None:
                row = StudentRow(name=display_name)
                students[key] = row
            else:
                row = students[matched]
                # If the incoming display name has more tokens than the
                # stored one (e.g. "Luong Duy Phuong" beats "Luong Phuong"),
                # prefer the more-formal/complete spelling.
                if len(display_name.split()) > len(row.name.split()):
                    row.name = display_name
            row.stages[n] = rec
            if repo_url and not row.repo_url:
                row.repo_url = repo_url
    for row in students.values():
        if row.repo_url:
            m = GITHUB_URL_RE.search(row.repo_url)
            if m:
                row.owner = m.group("owner")
                row.repo = m.group("repo")
    return sorted(students.values(),
                  key=lambda r: (r.name.split()[-1].lower(), r.name.lower()))


# ------------------------------------------------------------------
# GitHub API enrichment
# ------------------------------------------------------------------

def _gh(*args: str) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            ["gh", *args], check=False, capture_output=True, text=True,
            encoding="utf-8", errors="replace",
        )
    except FileNotFoundError:
        return 127, "", "gh CLI not found"
    return proc.returncode, proc.stdout or "", proc.stderr or ""


def enrich_with_gh(row: StudentRow) -> None:
    row.gh_queried = True
    if not (row.owner and row.repo):
        row.gh_error = "no repo URL"
        return
    rc, out, err = _gh("api", f"repos/{row.owner}/{row.repo}")
    if rc != 0 or not out:
        row.gh_error = (err.strip().splitlines()[-1]
                        if err else f"gh api repo returned rc={rc}")
        return
    try:
        meta = json.loads(out)
    except json.JSONDecodeError:
        row.gh_error = "could not parse repo metadata"
        return
    row.gh_accessible = True
    row.gh_private = bool(meta.get("private"))
    row.gh_default_branch = meta.get("default_branch") or "main"

    rc, out, _ = _gh(
        "api",
        f"repos/{row.owner}/{row.repo}/commits?per_page=1&sha={row.gh_default_branch}",
    )
    if rc == 0 and out:
        try:
            commits = json.loads(out)
        except json.JSONDecodeError:
            commits = []
        if commits:
            c = commits[0].get("commit", {})
            author = c.get("author", {}) or c.get("committer", {})
            row.gh_last_commit_at = author.get("date", "")
            msg = (c.get("message") or "").split("\n", 1)[0]
            row.gh_last_commit_msg = msg[:80]

    rc, out, _ = _gh(
        "api",
        f"repos/{row.owner}/{row.repo}/collaborators/{INSTRUCTOR_GITHUB_HANDLE}/permission",
    )
    if rc == 0 and out:
        try:
            perm = json.loads(out).get("permission", "")
        except json.JSONDecodeError:
            perm = ""
        row.gh_instructor_collaborator = perm in {"admin", "write", "maintain"}


# ------------------------------------------------------------------
# Output
# ------------------------------------------------------------------

def _fmt_score_cell(rec: StageRecord | None) -> str:
    if not rec or rec.score is None:
        return "—"
    if rec.regrade_date:
        return f"{rec.score}†"
    suffix = "*" if rec.floor_applied else ""
    return f"{rec.score}{suffix}"


def _fmt_last_commit(row: StudentRow) -> str:
    if not row.gh_queried:
        return "—"
    if row.gh_error:
        return f"⚠ {row.gh_error[:40]}"
    if not row.gh_last_commit_at:
        return "—"
    # ISO-z format from GitHub: "2026-05-14T16:13:10Z" → friendlier display
    try:
        dt = datetime.strptime(row.gh_last_commit_at, "%Y-%m-%dT%H:%M:%SZ")
        days_ago = (datetime.now(timezone.utc) - dt.replace(tzinfo=timezone.utc)).days
        if days_ago == 0:
            ago = "today"
        elif days_ago == 1:
            ago = "1d ago"
        else:
            ago = f"{days_ago}d ago"
        return f"{dt.strftime('%Y-%m-%d')} ({ago})"
    except ValueError:
        return row.gh_last_commit_at


def _current_stage(row: StudentRow) -> str:
    if not row.stages:
        return "—"
    highest = max(row.stages.keys())
    rec = row.stages[highest]
    suffix = " (floor)" if rec.floor_applied else ""
    return f"Stage {highest}{suffix}"


def _next_stage_signal(row: StudentRow) -> str:
    """Are there commits since the latest graded stage's submission?"""
    if not row.stages or not row.gh_last_commit_at:
        return ""
    highest = max(row.stages.keys())
    sub_str = row.stages[highest].submitted_at
    try:
        sub_dt = datetime.strptime(sub_str.split(" ")[0], "%Y-%m-%d")
    except (ValueError, IndexError):
        return ""
    try:
        commit_dt = datetime.strptime(row.gh_last_commit_at, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return ""
    if commit_dt.date() > sub_dt.date():
        return f"working on Stage {highest + 1}?"
    return ""


def write_markdown(rows: list[StudentRow], out_path: Path, *, used_gh: bool) -> None:
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# BUS-629 VEMBA — Student Roster",
        "",
        f"_Generated by `_tools/build_roster.py` at {today}._  ",
        ("_Live GitHub state included (visibility, last commit, collaborator status)._"
         if used_gh else
         "_Offline mode — GitHub state not refreshed; only data from grade reports._"),
        "",
        "Scores marked with `*` indicate the floor was applied at that stage.  ",
        "Scores marked with `†` indicate a re-grade (see `STAGE{N}_GRADES.md` for the `### Updated` block).  ",
        "**Collab ✓** = instructor `@" + INSTRUCTOR_GITHUB_HANDLE + "` is a "
        "Write collaborator on the repo.  ",
        "**Current stage** = highest stage the student has been graded on.  ",
        "**Last commit** = age of HEAD on the default branch.  ",
        "**Signal** = repo activity after the latest graded stage's submission "
        "(suggests work on the next stage).",
        "",
        "| Student | GitHub | Public | Collab ✓ | S0 | S1 | S2 | S3 | S4 | S5 | "
        "Current stage | Last commit | Signal |",
        "|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|---|",
    ]
    for row in rows:
        gh_link = f"`{row.owner}/{row.repo}`" if row.owner else "—"
        public = ("⚠ private" if row.gh_private else
                  ("Y" if row.gh_accessible else "—"))
        collab = ("Y" if row.gh_instructor_collaborator else
                  ("**N**" if row.gh_accessible else "—"))
        cells = [_fmt_score_cell(row.stages.get(n)) for n in range(STAGE_COUNT)]
        lines.append(
            f"| {row.name} | {gh_link} | {public} | {collab} | "
            + " | ".join(cells)
            + f" | {_current_stage(row)} | {_fmt_last_commit(row)} | "
            f"{_next_stage_signal(row)} |"
        )
    lines.append("")
    # Aggregates
    lines.append("## Aggregates")
    lines.append("")
    total = len(rows)
    collab_yes = sum(1 for r in rows if r.gh_instructor_collaborator)
    private = sum(1 for r in rows if r.gh_private)
    by_stage = {n: sum(1 for r in rows if n in r.stages) for n in range(STAGE_COUNT)}
    lines.append(f"- **Total students tracked:** {total}")
    lines.append(f"- **Instructor added as collaborator:** {collab_yes} / {total}")
    if private:
        lines.append(f"- **Private repos:** {private} ⚠ (should be public)")
    lines.append(f"- **Submission counts by stage:** "
                 + ", ".join(f"S{n}={c}" for n, c in by_stage.items() if c))
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Output regenerated on each run — do not edit by hand.")
    lines.append(
        f"- Re-run with `python _tools/build_roster.py` (add `--no-gh` to skip "
        "live API calls)."
    )
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def write_csv(rows: list[StudentRow], out_path: Path) -> None:
    cols = [
        "name", "github_owner", "github_repo", "repo_url",
        "public", "private", "default_branch",
        "instructor_collaborator", "last_commit_at", "last_commit_msg",
    ] + [f"stage{n}_score" for n in range(STAGE_COUNT)] + [
        f"stage{n}_floor" for n in range(STAGE_COUNT)
    ] + ["current_stage", "next_stage_signal", "gh_error"]
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for row in rows:
            stage_scores = [
                row.stages[n].score if n in row.stages else "" for n in range(STAGE_COUNT)
            ]
            stage_floors = [
                ("Y" if (n in row.stages and row.stages[n].floor_applied) else "")
                for n in range(STAGE_COUNT)
            ]
            current = max(row.stages) if row.stages else ""
            w.writerow([
                row.name, row.owner, row.repo, row.repo_url,
                "Y" if row.gh_accessible and not row.gh_private else "",
                "Y" if row.gh_private else "",
                row.gh_default_branch,
                "Y" if row.gh_instructor_collaborator else "",
                row.gh_last_commit_at, row.gh_last_commit_msg,
                *stage_scores, *stage_floors,
                f"Stage {current}" if current != "" else "",
                _next_stage_signal(row), row.gh_error,
            ])


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--no-gh", action="store_true",
                   help="Skip live GitHub API calls; use only data already "
                        "in the STAGEN_GRADES.md files.")
    p.add_argument("--out-dir", type=Path, default=None,
                   help="Output directory (default: ignore/ in the course root)")
    args = p.parse_args(argv)

    course_root = Path(__file__).resolve().parent.parent
    stage_root = course_root / "ignore"
    out_dir = args.out_dir or (course_root / "ignore")

    if not stage_root.exists():
        print(f"No stage root at {stage_root} — nothing to do.")
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = collect_students(stage_root)
    if not rows:
        print("No student records found in any STAGEN_GRADES.md — exiting.")
        return 1
    print(f"Found {len(rows)} student(s) across stage reports.")

    if not args.no_gh:
        for row in rows:
            if not row.owner:
                continue
            print(f"  refreshing {row.name} ({row.owner}/{row.repo}) ...",
                  end=" ", flush=True)
            enrich_with_gh(row)
            if row.gh_error:
                print(f"⚠ {row.gh_error}")
            else:
                collab = "Y" if row.gh_instructor_collaborator else "N"
                print(f"ok (collab={collab}, last commit "
                      f"{row.gh_last_commit_at or 'unknown'})")
    else:
        print("Skipping GitHub API calls (--no-gh).")

    md_path = out_dir / "roster.md"
    csv_path = out_dir / "roster.csv"
    write_markdown(rows, md_path, used_gh=not args.no_gh)
    write_csv(rows, csv_path)
    print(f"\nWrote {md_path}")
    print(f"Wrote {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
