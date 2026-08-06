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
from urllib.parse import quote

INSTRUCTOR_GITHUB_HANDLE = "adamwstauffer"

# --- argv-safety validators ----------------------------------------------
_SAFE_OWNER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
_SAFE_REPO_RE = re.compile(r"^[A-Za-z0-9._-]{1,100}$")
_SAFE_BRANCH_RE = re.compile(r"^[A-Za-z0-9._/-]{1,255}$")
# Repo paths are deliberately permissive: GitHub accepts almost any character in
# a filename, and students routinely commit memos with `:`, `{}`, or parentheses
# in the name (a mangled `docs:decisions:…md`, an unreplaced `{scenario-slug}`).
# The old `[A-Za-z0-9 ._/-]` allow-list rejected those, so `download_text`
# returned None and a real, substantive submission scored a silent 0. `gh` is
# invoked with an argv list (never a shell), so the only things that actually
# need excluding are control characters, backslashes, and a leading `-` (which
# `gh` would parse as a flag). The path is percent-encoded in `_contents_ref`
# before it reaches the API, which handles `#`, `?`, and `%` safely.
_SAFE_PATH_RE = re.compile(r"^(?!-)[^\x00-\x1f\\]{1,300}$")
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


def lamaku_display_name(raw: str) -> str:
    """Flip a Lamaku folder name from `Lastname Firstname[ Middle]` to natural
    `Firstname[ Middle] Lastname` order.

    Lamaku exports the surname first (`Gallano Clarence`), which reads backwards
    in a student-facing header and throws off `lastname_slug`. The surname is the
    leading token, so we move it to the end. Order-independent matching
    (`normalize_name`) is unaffected either way; single-token names pass through.
    """
    toks = raw.split()
    if len(toks) < 2:
        return raw
    return " ".join(toks[1:] + toks[:1])


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


def _contents_ref(owner: str, repo: str, path: str) -> str:
    """Build the `contents` API endpoint with the path percent-encoded.

    Path separators stay literal; everything else (spaces, `#`, `?`, `%`, `:`)
    is escaped so an unusual-but-legal filename resolves instead of silently
    404-ing partway through the path.
    """
    return f"repos/{owner}/{repo}/contents/{quote(path, safe='/')}"


def download_bytes(owner: str, repo: str, path: str, branch: str) -> bytes | None:
    """Fetch a file blob from the repo; None on failure. Handles base64."""
    if not (_SAFE_OWNER_RE.match(owner) and _SAFE_REPO_RE.match(repo)
            and _SAFE_PATH_RE.match(path) and _SAFE_BRANCH_RE.match(branch)):
        return None
    data = _gh_json(
        "api", _contents_ref(owner, repo, path), "-X", "GET", "-f", f"ref={branch}",
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


# --- deliverable selection ------------------------------------------------
# Students routinely leave the assignment's unfilled template in the repo next
# to their real work (`…-lastname-…`, `YYYY-MM-DD-…`, `scenario-slug`). Both match
# a stage's deliverable pattern, and picking the shorter path grabs the stub — a
# real, canonically-filed submission then scores ~0. Every stage selects through
# the helpers below so that failure mode can't recur.
TEMPLATE_PATH_RE = re.compile(r"lastname|yyyy-mm-dd|scenario-slug", re.IGNORECASE)


def strip_templates(paths: list[str]) -> list[str]:
    """Drop unfilled-template paths. If every candidate looks like a template,
    keep them all so a lone stub still flows to the stage's own word-count guard
    (which reports it as missing) rather than vanishing here."""
    real = [p for p in paths if not TEMPLATE_PATH_RE.search(p)]
    return real or list(paths)


def pick_text(owner: str, repo: str, branch: str, paths: list[str]) -> tuple[str, str]:
    """Choose the real text deliverable among candidate paths → (path, text).

    Drops template stubs, then — if more than one plausible file remains —
    fetches each and keeps the one with the most words (the actual submission,
    not a short stub) instead of guessing by path length. ('', '') if no paths.
    """
    pool = strip_templates(paths)
    if not pool:
        return "", ""
    if len(pool) == 1:
        return pool[0], download_text(owner, repo, pool[0], branch) or ""
    best_path, best_text, best_wc = pool[0], "", -1
    for p in sorted(pool, key=len):
        t = download_text(owner, repo, p, branch) or ""
        wc = len(re.findall(r"\b\w+\b", t))
        if wc > best_wc:
            best_path, best_text, best_wc = p, t, wc
    return best_path, best_text


def pick_path(paths: list[str]) -> str | None:
    """Pick a single non-template path (shortest) — for binary deliverables
    (e.g. .xlsx) that can't be ranked by word count. None if no candidates."""
    pool = strip_templates(paths)
    return sorted(pool, key=len)[0] if pool else None


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
            name=lamaku_display_name(m.group("name").strip()),
            submitted_at=_parse_folder_time(m),
            folder=child,
            github_url=_scan_html_for_url(child),
        )
        prev = by_id.get(sub.student_id)
        if (prev is None or sub.submitted_at is None or prev.submitted_at is None
                or sub.submitted_at > prev.submitted_at):
            by_id[sub.student_id] = sub
    return sorted(by_id.values(), key=lambda s: normalize_name(s.name))
