"""Fetch each FIN-321 Stage 4 student GitHub deliverable.

Reads the Stage 4 submission HTML files in
ignore-term/2026-Spring/stage4/, extracts the GitHub link from each, and
downloads the referenced file (or the most likely stage4 file in the repo)
into _grading/_fetched/<student>.md so the grader can score them locally.

Strategy:
  1. Parse each HTML file for href="https://github.com/...".
  2. Convert blob/tree URLs to raw.githubusercontent.com URLs.
     - blob/<branch>/<path>      -> raw.githubusercontent.com/<user>/<repo>/<branch>/<path>
     - tree/<branch>/<path>      -> use GitHub API to find a stage4 .md|.pdf
     - bare repo URL             -> use API to find a stage4 .md|.pdf
  3. Download via requests.
  4. Write a manifest CSV recording the (id, name, url, status, local_path).
"""
from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlparse, quote

import requests

STAGE4_DIR = Path(
    r"C:\GitHub\shidler\courses\FIN-321-International-Finance-And-Securities"
    r"\ignore-term\2026-Spring\stage4"
)
OUT_DIR = STAGE4_DIR / "_grading" / "_fetched"
MANIFEST = STAGE4_DIR / "_grading" / "stage4-fetch-manifest.csv"
OUT_DIR.mkdir(parents=True, exist_ok=True)
MANIFEST.parent.mkdir(parents=True, exist_ok=True)

FOLDER_RE = re.compile(r"^(?P<sid>\d+)-\d+\s*-\s*(?P<name>.+?)\s*-\s*")
HREF_RE = re.compile(r'href="(https://github\.com/[^"]+)"', re.IGNORECASE)


@dataclass
class Item:
    sid: str
    name: str
    folder: Path
    url: str = ""
    raw_url: str = ""
    local: Path | None = None
    inline_html: Path | None = None  # for students who pasted inline
    status: str = ""
    notes: str = ""


def list_submissions() -> list[Item]:
    items: list[Item] = []
    for child in sorted(STAGE4_DIR.iterdir()):
        if not child.is_dir() or child.name.startswith("_"):
            continue
        m = FOLDER_RE.match(child.name)
        if not m:
            continue
        items.append(Item(sid=m.group("sid"), name=m.group("name").strip(),
                          folder=child))
    return items


def find_html(folder: Path) -> Path | None:
    htmls = list(folder.glob("*.html"))
    return htmls[0] if htmls else None


def extract_github_url(html_path: Path) -> str:
    text = html_path.read_text(encoding="utf-8", errors="ignore")
    m = HREF_RE.search(text)
    return m.group(1).strip() if m else ""


def github_to_raw(url: str) -> tuple[str, str]:
    """Return (raw_url, kind). kind in {file, tree, repo, commit}."""
    p = urlparse(url)
    parts = [x for x in p.path.split("/") if x]
    # parts: [user, repo, ('blob'|'tree'|'commit'), branch, *path]
    if len(parts) < 2:
        return "", "unknown"
    repo_part = parts[1]
    if repo_part.endswith(".git"):
        repo_part = repo_part[:-4]
    user, repo = parts[0], repo_part
    if len(parts) >= 4 and parts[2] == "blob":
        branch = parts[3]
        path = "/".join(parts[4:])
        raw = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path}"
        return raw, "file"
    if len(parts) >= 3 and parts[2] == "tree":
        branch = parts[3] if len(parts) >= 4 else "main"
        sub = "/".join(parts[4:])
        return f"https://api.github.com/repos/{user}/{repo}/contents/{sub}?ref={branch}", "tree"
    if len(parts) >= 3 and parts[2] == "commit":
        sha = parts[3]
        return f"https://api.github.com/repos/{user}/{repo}/commits/{sha}", "commit"
    return f"https://api.github.com/repos/{user}/{repo}", "repo"


STAGE4_KEYWORDS = ("stage4", "stage-4", "stage_4", "final", "memo", "recommend",
                   "executive")

# Hostnames that are allowed to receive the GitHub PAT. The regex at the top of
# the file constrains inputs to github.com URLs, but URL parsing/transformation
# downstream is non-trivial — gate the Authorization header at request time so
# a future regression in URL handling can't exfiltrate the token to an
# attacker-controlled host.
_GITHUB_HOSTS = frozenset({"api.github.com", "raw.githubusercontent.com"})


def _auth_headers_for(url: str, token: str) -> dict[str, str]:
    if not token:
        return {}
    host = (urlparse(url).hostname or "").lower()
    if host in _GITHUB_HOSTS:
        return {"Authorization": f"Bearer {token}"}
    return {}


def list_repo_tree(user: str, repo: str, branch: str,
                   sess: requests.Session, token: str) -> list[str]:
    """Recursively list all file paths in a repo via the git-tree API."""
    api = f"https://api.github.com/repos/{user}/{repo}/git/trees/{branch}?recursive=1"
    headers = {"Accept": "application/vnd.github+json", **_auth_headers_for(api, token)}
    r = sess.get(api, headers=headers)
    if r.status_code != 200:
        return []
    return [t["path"] for t in r.json().get("tree", []) if t.get("type") == "blob"]


def pick_best_file(api_url: str, sess: requests.Session, token: str) -> str:
    headers = {"Accept": "application/vnd.github+json", **_auth_headers_for(api_url, token)}
    r = sess.get(api_url, headers=headers)
    if r.status_code != 200:
        return ""
    data = r.json()
    if isinstance(data, dict):
        # commit endpoint - check modified files
        files = data.get("files") or []
        candidates = [f.get("filename", "") for f in files]
    else:
        candidates = [f.get("path", "") for f in data if f.get("type") == "file"]
    return _rank_candidates(candidates)


def _rank_candidates(paths: list[str]) -> str:
    md = [c for c in paths if c.lower().endswith((".md", ".pdf", ".txt", ".docx"))]
    md.sort(key=lambda c: (
        not any(k in c.lower() for k in STAGE4_KEYWORDS),
        "stage4" not in c.lower() and "stage-4" not in c.lower(),
        len(c),
    ))
    return md[0] if md else ""


def fetch(url: str, dest: Path, sess: requests.Session, token: str) -> tuple[bool, str]:
    try:
        r = sess.get(url, timeout=30, headers=_auth_headers_for(url, token))
    except Exception as e:
        return False, f"error:{e}"
    if r.status_code != 200:
        return False, f"http {r.status_code}"
    dest.write_bytes(r.content)
    return True, f"ok ({len(r.content)} bytes)"


def main() -> int:
    items = list_submissions()
    print(f"Found {len(items)} submissions")
    sess = requests.Session()
    token = ""
    token_path = Path.home() / ".gh-token.txt"
    if token_path.exists():
        token = token_path.read_text().strip()

    for it in items:
        html = find_html(it.folder)
        if not html:
            it.status = "no_html"
            continue
        url = extract_github_url(html)
        if not url:
            it.status = "no_link"
            it.inline_html = html
            it.notes = "submitted inline / no GitHub link"
            continue
        it.url = url

        raw, kind = github_to_raw(url)
        it.raw_url = raw

        # Sanitize filename
        safe = re.sub(r"[^A-Za-z0-9_-]+", "_", it.name)[:60]

        if kind == "file":
            ext = Path(unquote(urlparse(raw).path)).suffix or ".md"
            local = OUT_DIR / f"{it.sid}_{safe}{ext}"
            ok, msg = fetch(raw, local, sess, token)
            if ok:
                it.local = local
                it.status = "ok"
                it.notes = msg
            else:
                it.status = "fetch_failed"
                it.notes = msg
        else:
            best = pick_best_file(raw, sess, token)
            if not best and kind in ("repo", "tree"):
                # Fall back: list the whole tree recursively
                p = urlparse(url)
                parts = [x for x in p.path.split("/") if x]
                repo_part = parts[1]
                if repo_part.endswith(".git"):
                    repo_part = repo_part[:-4]
                user2 = parts[0]
                repo2 = repo_part
                # Find default branch
                meta_url = f"https://api.github.com/repos/{user2}/{repo2}"
                rmeta = sess.get(meta_url,
                                 headers={"Accept": "application/vnd.github+json",
                                          **_auth_headers_for(meta_url, token)})
                branch2 = "main"
                if rmeta.status_code == 200:
                    branch2 = rmeta.json().get("default_branch") or "main"
                tree_paths = list_repo_tree(user2, repo2, branch2, sess, token)
                best = _rank_candidates(tree_paths)
                if best:
                    raw_path = (f"https://raw.githubusercontent.com/"
                                f"{user2}/{repo2}/{branch2}/{quote(best)}")
                    ext = Path(best).suffix or ".md"
                    local = OUT_DIR / f"{it.sid}_{safe}{ext}"
                    ok, msg = fetch(raw_path, local, sess, token)
                    if ok:
                        it.local = local
                        it.status = "ok_via_tree"
                        it.notes = f"resolved {best} via recursive tree; {msg}"
                        continue
            if not best:
                it.status = "no_match_in_repo"
                it.notes = f"could not find stage4 file via {kind}"
                continue
            # Now fetch the raw file
            p = urlparse(url)
            parts = [x for x in p.path.split("/") if x]
            repo_part = parts[1]
            if repo_part.endswith(".git"):
                repo_part = repo_part[:-4]
            user, repo = parts[0], repo_part
            if kind == "commit":
                sha = parts[3]
                raw_path = f"https://raw.githubusercontent.com/{user}/{repo}/{sha}/{best}"
            else:
                # tree or repo: assume main branch unless tree url specified one
                branch = parts[3] if (kind == "tree" and len(parts) >= 4) else "main"
                raw_path = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{quote(best)}"
            ext = Path(best).suffix or ".md"
            local = OUT_DIR / f"{it.sid}_{safe}{ext}"
            ok, msg = fetch(raw_path, local, sess, token)
            if ok:
                it.local = local
                it.status = "ok_via_api"
                it.notes = f"resolved {best} via {kind}; {msg}"
            else:
                it.status = "fetch_failed"
                it.notes = f"resolved {best} via {kind}; {msg}"

    # Write manifest
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sid", "name", "github_url", "raw_url", "local_file",
                    "inline_html", "status", "notes"])
        for it in items:
            w.writerow([
                it.sid, it.name, it.url, it.raw_url,
                str(it.local) if it.local else "",
                str(it.inline_html) if it.inline_html else "",
                it.status, it.notes,
            ])
    print(f"Wrote manifest: {MANIFEST}")
    print()
    by_status: dict[str, int] = {}
    for it in items:
        by_status[it.status] = by_status.get(it.status, 0) + 1
    for k, v in sorted(by_status.items()):
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
