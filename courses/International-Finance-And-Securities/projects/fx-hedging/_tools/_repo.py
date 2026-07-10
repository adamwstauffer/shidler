"""Shared GitHub-inspection + submission-discovery layer for FIN-321 graders.

BUS-629 duplicated its `gh` helpers, Lamaku folder parsing, and name
normalization into every `grade_stage*.py`. This module centralizes them so
each fx-hedging scanner stays focused on its rubric.

All `gh` arguments are regex-validated before they reach `subprocess` so a
malformed owner/repo/path from a student HTML file can't inject argv. Every
`gh` failure degrades to "" / [] / None rather than raising, so one dead repo
never aborts a batch.

Requires the GitHub CLI (`gh`) to be installed and authenticated. Offline /
no-`gh` callers should catch the empty results.
"""
from __future__ import annotations

import base64
import json
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

INSTRUCTOR_GITHUB_HANDLE = "adamwstauffer"

# --- argv-safety validators ----------------------------------------------
_SAFE_OWNER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
_SAFE_REPO_RE = re.compile(r"^[A-Za-z0-9._-]{1,100}$")
_SAFE_BRANCH_RE = re.compile(r"^[A-Za-z0-9._/-]{1,255}$")
_SAFE_PATH_RE = re.compile(r"^[A-Za-z0-9 ._/-]{1,300}$")
_SAFE_HANDLE_RE = re.compile(r"^[A-Za-z0-9-]{1,39}$")

GITHUB_URL_RE = re.compile(
    r"https?://github\.com/(?P<owner>[A-Za-z0-9-]+)/(?P<repo>[A-Za-z0-9._-]+)",
    re.IGNORECASE,
)

# Lamaku export folder: "<sid>-<n> - <Name> - <Mon> <Day>, <Year> <H><AM/PM>"
FOLDER_NAME_RE = re.compile(
    r"^(?P<sid>\d+)-\d+\s*-\s*(?P<name>.+?)\s*-\s*"
    r"(?P<month>[A-Za-z]+)\s+(?P<day>\d+),\s*(?P<year>\d{4})\s+"
    r"(?P<h>\d{1,4})\s*(?P<ampm>AM|PM)\s*$"
)


# --- name utilities -------------------------------------------------------
def normalize_name(name: str) -> str:
    """Canonical name key: lowercase alpha tokens, sorted, space-joined.

    "Nguyen, Anh" / "Anh Nguyen" -> "anh nguyen". Used to match a student
    across stages regardless of spelling/order.
    """
    tokens = sorted(t.lower() for t in re.findall(r"[A-Za-z]+", name))
    return " ".join(tokens)


def lastname_slug(name: str) -> str:
    """Directory slug for _pr_feedback/, from the last name token."""
    tokens = re.findall(r"[A-Za-z]+", name)
    last = tokens[-1] if tokens else "student"
    return re.sub(r"[^a-z0-9-]", "", last.lower()) or "student"


def parse_repo_url(url: str) -> tuple[str, str] | None:
    """Extract (owner, repo) from a github URL; strip a trailing .git."""
    if not url:
        return None
    m = GITHUB_URL_RE.search(url)
    if not m:
        return None
    owner, repo = m.group("owner"), m.group("repo")
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not (_SAFE_OWNER_RE.match(owner) and _SAFE_REPO_RE.match(repo)):
        return None
    return owner, repo


# --- gh plumbing ----------------------------------------------------------
def gh(*args: str) -> str:
    """Run `gh <args>`; return stdout, or "" on any failure."""
    try:
        proc = subprocess.run(
            ["gh", *args], capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return proc.stdout if proc.returncode == 0 else ""


def _gh_json(*args: str):
    out = gh(*args)
    if not out.strip():
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


@dataclass
class RepoState:
    owner: str
    repo: str
    accessible: bool = False
    private: bool = True
    description: str = ""
    default_branch: str = "main"
    license: str = ""
    tree: list[str] = field(default_factory=list)
    commit_count: int = 0
    descriptive_commit_count: int = 0
    instructor_is_collaborator: bool = False

    @property
    def public(self) -> bool:
        return self.accessible and not self.private


VAGUE_MESSAGE_RE = re.compile(
    r"^\s*(update|edit|change|fix|stuff|wip|misc|\.+|commit|final|test)\s*$",
    re.IGNORECASE,
)


def _is_descriptive(msg: str) -> bool:
    first = (msg or "").splitlines()[0] if msg else ""
    return len(first.split()) >= 3 and not VAGUE_MESSAGE_RE.match(first)


def repo_state(owner: str, repo: str) -> RepoState:
    """One-shot repo inspection: metadata + recursive tree + commit hygiene."""
    st = RepoState(owner=owner, repo=repo)
    if not (_SAFE_OWNER_RE.match(owner) and _SAFE_REPO_RE.match(repo)):
        return st
    meta = _gh_json("api", f"repos/{owner}/{repo}")
    if not isinstance(meta, dict):
        return st  # 404 / private / no access
    st.accessible = True
    st.private = bool(meta.get("private", True))
    st.description = meta.get("description") or ""
    st.default_branch = meta.get("default_branch") or "main"
    lic = meta.get("license")
    st.license = (lic or {}).get("spdx_id", "") if isinstance(lic, dict) else ""

    if _SAFE_BRANCH_RE.match(st.default_branch):
        tree = _gh_json(
            "api", f"repos/{owner}/{repo}/git/trees/{st.default_branch}",
            "-X", "GET", "-f", "recursive=1",
        )
        if isinstance(tree, dict):
            st.tree = [
                e["path"] for e in tree.get("tree", [])
                if e.get("type") == "blob" and "path" in e
            ]

    for page in (1, 2, 3):
        commits = _gh_json(
            "api", f"repos/{owner}/{repo}/commits",
            "-X", "GET", "-f", "per_page=100", "-f", f"page={page}",
        )
        if not isinstance(commits, list) or not commits:
            break
        st.commit_count += len(commits)
        for c in commits:
            msg = (c.get("commit") or {}).get("message", "")
            if _is_descriptive(msg):
                st.descriptive_commit_count += 1
        if len(commits) < 100:
            break

    st.instructor_is_collaborator = _check_collaborator(
        owner, repo, INSTRUCTOR_GITHUB_HANDLE
    )
    return st


def _check_collaborator(owner: str, repo: str, handle: str) -> bool:
    if not _SAFE_HANDLE_RE.match(handle):
        return False
    data = _gh_json(
        "api", f"repos/{owner}/{repo}/collaborators/{handle}/permission",
    )
    if not isinstance(data, dict):
        return False
    return data.get("permission") in ("write", "admin", "maintain")


def download_bytes(owner: str, repo: str, path: str, branch: str) -> bytes | None:
    """Fetch a file blob from the repo; None on failure. Handles base64."""
    if not (_SAFE_OWNER_RE.match(owner) and _SAFE_REPO_RE.match(repo)
            and _SAFE_PATH_RE.match(path) and _SAFE_BRANCH_RE.match(branch)):
        return None
    data = _gh_json(
        "api", f"repos/{owner}/{repo}/contents/{path}", "-X", "GET", "-f", f"ref={branch}",
    )
    if not isinstance(data, dict) or data.get("encoding") != "base64":
        return None
    try:
        return base64.b64decode(data.get("content", ""))
    except (ValueError, TypeError):
        return None


def download_text(owner: str, repo: str, path: str, branch: str) -> str | None:
    raw = download_bytes(owner, repo, path, branch)
    if raw is None:
        return None
    return raw.decode("utf-8", errors="ignore")


# --- submission discovery -------------------------------------------------
@dataclass
class Submission:
    student_id: str
    name: str
    submitted_at: datetime | None
    folder: Path
    github_url: str = ""

    @property
    def repo(self) -> tuple[str, str] | None:
        return parse_repo_url(self.github_url)


def _parse_folder_time(m: re.Match) -> datetime | None:
    h = m.group("h")
    if len(h) == 3:
        hour, minute = int(h[0]), int(h[1:])
    elif len(h) == 4:
        hour, minute = int(h[:2]), int(h[2:])
    else:
        hour, minute = int(h), 0
    if m.group("ampm").upper() == "PM" and hour != 12:
        hour += 12
    elif m.group("ampm").upper() == "AM" and hour == 12:
        hour = 0
    try:
        return datetime.strptime(
            f"{m.group('month')} {m.group('day')} {m.group('year')}", "%b %d %Y"
        ).replace(hour=hour, minute=minute)
    except ValueError:
        return None


def _scan_html_for_url(folder: Path) -> str:
    """First github URL found in any *.html / *.txt pointer file in folder."""
    for p in sorted(folder.iterdir()):
        if p.is_file() and p.suffix.lower() in (".html", ".txt"):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            m = GITHUB_URL_RE.search(text)
            if m:
                return m.group(0)
    return ""


def discover_submissions(export: Path, scratch_suffix: str = "_extracted") -> list[Submission]:
    """Discover per-student submissions from a Lamaku export (zip or dir).

    A `.zip` is extracted (zipslip-safe) to a sibling `_{stem}{suffix}` dir.
    Each top-level per-student folder is parsed for id/name/timestamp and
    scanned for a GitHub URL. Deduped by student id (latest timestamp wins).
    """
    import zipfile
    from _safe_zip import safe_extractall

    export = Path(export)
    if export.is_file() and export.suffix.lower() == ".zip":
        dest = export.parent / f"_{export.stem}{scratch_suffix}"
        dest.mkdir(exist_ok=True)
        with zipfile.ZipFile(export) as zf:
            safe_extractall(zf, dest)
        root = dest
    else:
        root = export

    by_id: dict[str, Submission] = {}
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name.startswith("_"):
            continue
        m = FOLDER_NAME_RE.match(child.name)
        if not m:
            continue
        sub = Submission(
            student_id=m.group("sid"),
            name=m.group("name").strip(),
            submitted_at=_parse_folder_time(m),
            folder=child,
            github_url=_scan_html_for_url(child),
        )
        prev = by_id.get(sub.student_id)
        if (prev is None or sub.submitted_at is None or prev.submitted_at is None
                or sub.submitted_at > prev.submitted_at):
            by_id[sub.student_id] = sub
    return sorted(by_id.values(), key=lambda s: normalize_name(s.name))
