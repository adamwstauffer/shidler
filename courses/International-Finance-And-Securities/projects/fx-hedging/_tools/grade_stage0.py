"""FIN-321 (fx-hedging v2) Stage 0 grader — Portfolio Repository.

Stage 0 has no workbook and no analytical deliverable: it grades the *repo
itself*. The graded skill is *standing up a clean, public, professionally
structured portfolio repository* — so every check runs off `repo_state`
(metadata + recursive tree + commit hygiene) plus a couple of blob downloads
for the bio and resume. This scanner is the canonical thin-scanner shape:
stage-specific scoring + suggestions + a `grade(sub)` function, wired to the
shared driver.

Rubric (criterion weights = % of the stage, from _weights.CRITERIA_WEIGHTS[0]):
    Public & accessible   25   (repo public, reachable, URL submitted)
    Skeleton & READMEs    25   (canonical dirs + stub READMEs + prompt-log)
    Bio & resume          25   (README bio + RESUME.md, edited beyond raw LLM)
    Commit hygiene        25   (>=2 meaningful commits)

CLI:  python grade_stage0.py <export.zip|dir> [--floor N] [--prior PATH]
                             [--out-dir DIR] [--today YYYY-MM-DD]
"""
from __future__ import annotations

import re
import sys

import _repo
from _repo import Submission
from _weights import CRITERIA_WEIGHTS, STAGE_FLOOR_PCT
from _grading_comments import core, next_stage_pointer
from _report import Criterion, StudentReport, run_scanner

STAGE_N = 0
STAGE_LABEL = "Portfolio Repository"
CRIT = CRITERIA_WEIGHTS[STAGE_N]
DEFAULT_FLOOR_PCT = STAGE_FLOOR_PCT[STAGE_N]
PRIOR_STAGE = None
RUBRIC_ROWS = [
    ("Public & accessible (public, professionally named, URL submitted)", f"{CRIT['public_accessible']}%"),
    ("Skeleton & READMEs (canonical structure, stub READMEs, prompt-log)", f"{CRIT['skeleton_readmes']}%"),
    ("Bio & resume (recruiter-ready, edited beyond raw LLM)", f"{CRIT['bio_resume']}%"),
    ("Commit hygiene (>=2 meaningful commits)", f"{CRIT['commit_hygiene']}%"),
]

# Canonical skeleton the stage doc asks for: stub-README files (exact paths)
# and directories (present if any tree path sits under them).
SKELETON_FILES = [
    "README.md", "RESUME.md", "prompt-log.md",
    "docs/README.md", "models/README.md", "data/README.md", "analysis/README.md",
]
SKELETON_DIRS = [
    "docs/decisions/", "docs/specs/", "models/templates/", "models/builds/",
]


# ---------------------------------------------------------------- helpers
def _word_count(text: str) -> int:
    return len(re.findall(r"\S+", text or ""))


def _has_file(tree: list[str], path: str) -> bool:
    return path in tree


def _find_ci(tree: list[str], path: str) -> str | None:
    """Return the actual tree path matching `path` case-insensitively, else None.

    GitHub's tree/contents API is case-sensitive, so a student who commits
    `Resume.md` won't match an exact `RESUME.md` lookup. We resolve the real
    casing here so the file is still found and read; the *policy* on whether a
    given casing costs points is decided by the caller.
    """
    low = path.lower()
    for p in tree:
        if p.lower() == low:
            return p
    return None


def _detect_wrapper_prefix(tree: list[str]) -> str:
    """Detect a single wrapper folder the whole submission was committed inside.

    Students sometimes drag the *extracted download folder* into the repo whole,
    so the canonical tree lands under `<repo>-phase0/<repo>/…` instead of at the
    root. If `README.md` already sits at the root there is no wrapper (return "").
    Otherwise find the shortest directory that looks like the real portfolio root
    — a `README.md` alongside a `RESUME.md`, `BIO.md`, or a `docs/` subtree — and
    return it so the canonical lookups can rebase onto it. The student is still
    nudged to move everything to the root (NESTED_SUBMISSION).
    """
    if _find_ci(tree, "README.md") is not None:
        return ""
    candidates = []
    for p in tree:
        if "/" not in p or p.rsplit("/", 1)[-1].lower() != "readme.md":
            continue
        d = p.rsplit("/", 1)[0]
        siblings = {q[len(d) + 1:].lower() for q in tree if q.startswith(d + "/")}
        if ("resume.md" in siblings or "bio.md" in siblings
                or any(s.startswith("docs/") for s in siblings)):
            candidates.append(d)
    if not candidates:
        return ""
    return min(candidates, key=lambda d: (d.count("/"), len(d)))


def _strip_prefix(tree: list[str], prefix: str) -> list[str]:
    n = len(prefix) + 1
    return [p[n:] for p in tree if p.startswith(prefix + "/")]


def _join(prefix: str, path: str) -> str:
    return f"{prefix}/{path}" if prefix else path


def _has_dir(tree: list[str], prefix: str) -> bool:
    return any(p.startswith(prefix) for p in tree)


def _dir_attempted(tree: list[str], prefix: str) -> bool:
    """A folder the student *tried* to stand up but left without a stub README.

    GitHub can't store an empty directory, so students often commit a bare
    placeholder named after the folder (`docs/specs` or `docs/specs.md`)
    instead of `docs/specs/README.md`. That's a real structural attempt worth
    half credit — recognized here, matched case-insensitively.
    """
    base = prefix.rstrip("/")
    return _find_ci(tree, base) is not None or _find_ci(tree, base + ".md") is not None


# ---------------------------------------------------------------- scoring
def _score_public(st, flags: list[str]) -> float:
    if st.public:
        return float(CRIT["public_accessible"])
    # accessible but private
    flags.append("NOT_PUBLIC")
    return round(0.5 * CRIT["public_accessible"], 1)


def _score_skeleton(tree: list[str], flags: list[str]) -> tuple[float, float, int]:
    expected = len(SKELETON_FILES) + len(SKELETON_DIRS)
    present = 0.0
    for f in SKELETON_FILES:
        actual = _find_ci(tree, f)
        if actual is None:
            continue
        # README is an industry convention: the *filename* must be canonical
        # ALL-CAPS `README.md` to earn the point. A miscased filename
        # (`readme.md`, `ReadMe.md`) is flagged and doesn't count. A miscased
        # parent directory (`Docs/README.md`) is NOT a README-casing miss —
        # the README itself is fine — so it still counts. Every other skeleton
        # file matches case-insensitively (casing there is personal formatting).
        if f.rsplit("/", 1)[-1] == "README.md" and actual.rsplit("/", 1)[-1] != "README.md":
            if "README_CASING" not in flags:
                flags.append("README_CASING")
            continue
        present += 1
    # Full credit for a real folder with content; half credit for a folder the
    # student attempted via a bare placeholder file but never gave a stub README.
    partial = 0
    for d in SKELETON_DIRS:
        if _has_dir(tree, d):
            present += 1
        elif _dir_attempted(tree, d):
            present += 0.5
            partial += 1
    if _find_ci(tree, "prompt-log.md") is None:
        flags.append("MISSING_PROMPT_LOG")
    frac = present / expected if expected else 0.0
    if frac < 0.4:
        flags.append("NO_SKELETON")
    elif frac < 0.9 and (partial or present < expected):
        flags.append("THIN_SKELETON")
    return round(frac * CRIT["skeleton_readmes"], 1), present, expected


def _score_bio_resume(bio_words: int, resume_words: int, flags: list[str]) -> float:
    bio_ok = bio_words >= 100
    resume_ok = resume_words >= 30
    if not bio_ok:
        flags.append("THIN_BIO")
    if resume_words == 0:
        flags.append("NO_RESUME")
    if bio_ok and resume_ok:
        return float(CRIT["bio_resume"])
    if bio_ok or resume_ok:
        return round(0.5 * CRIT["bio_resume"], 1)
    return 0.0


def _score_commits(st, flags: list[str]) -> float:
    if st.commit_count >= 2 and st.descriptive_commit_count >= 2:
        return float(CRIT["commit_hygiene"])
    if st.commit_count >= 2:
        flags.append("VAGUE_COMMITS")
        return round(0.5 * CRIT["commit_hygiene"], 1)
    flags.append("FEW_COMMITS")
    return 0.0


# ---------------------------------------------------------------- suggestions
def _suggestions_for(flags: set[str], prior_weak: bool):
    s = []
    if "NO_GITHUB_LINK" in flags:
        s.append(core("No GitHub URL was found in your submission. Paste your full "
                      "`https://github.com/<you>/<repo>` link into Lamaku so the repo can be "
                      "inspected — the repo itself is what's graded."))
    if "REPO_404" in flags:
        s.append(core("The repository couldn't be reached. Confirm that: **(1)** it exists at "
                      "the submitted URL; **(2)** the URL is spelled correctly; **(3)** it's "
                      "public (steps below)."))
    if "NOT_PUBLIC" in flags:
        s.append(core("Your repo is private, so it can't be opened as a portfolio piece. Make "
                      "it public: on GitHub, **Settings → General → Danger Zone → Change "
                      "visibility → Public**, then re-confirm the URL in Lamaku."))
    if "NESTED_SUBMISSION" in flags:
        s.append(core("Your whole portfolio is committed one folder deep — everything lives "
                      "inside a wrapper folder (looks like you dragged the extracted download "
                      "in whole) instead of at the repo root. Graded on content, so no penalty "
                      "here, but move it up: **(1)** open the repo, drag the *contents* of the "
                      "wrapper folder up to the root (or `git mv` them) so `README.md`, "
                      "`RESUME.md`, and `docs/` sit at the top level; **(2)** delete the now-empty "
                      "wrapper folder; **(3)** commit. A visitor should land on your bio, not on "
                      "a single folder to click into."))
    if "NO_SKELETON" in flags:
        s.append(core("The canonical folder skeleton is mostly missing. Build it now: "
                      "**(1)** create the folders — `docs/` (with `decisions/`, `specs/`, "
                      "`plans/`, `templates/`), `models/` (with `templates/`, `builds/`), "
                      "`data/`, and `analysis/`; **(2)** put a one- or two-line `README.md` "
                      "*inside each* saying what belongs there (GitHub won't keep an empty "
                      "folder, so the README is what makes it stick); **(3)** commit. The "
                      "Stage 0 handout has the exact tree to copy."))
    if "THIN_SKELETON" in flags:
        s.append(core("You've laid out most of the structure — nice. The gap: several folders "
                      "are bare placeholder files (e.g. `docs/specs`) instead of folders with "
                      "a stub inside. For each, **(1)** add a one-line `README.md` in the "
                      "folder (`docs/specs/README.md`, `models/builds/README.md`, …) and "
                      "**(2)** delete the bare placeholder file. That makes the folders render "
                      "on GitHub and documents what each holds."))
    if "MISSING_PROMPT_LOG" in flags:
        s.append(core("Add `prompt-log.md` at the repo root: **(1)** create the file; "
                      "**(2)** paste in the prompts you used to draft your bio and resume, each "
                      "with a one-line note on what you kept or changed; **(3)** commit. You'll "
                      "append to this every stage, so starting it now pays off."))
    if "README_CASING" in flags:
        s.append(core("Rename your README to the canonical all-caps `README.md`. On GitHub, "
                      "open the file → **pencil (Edit)** → change the name in the path box → "
                      "**Commit**. All-caps README is the universal convention GitHub and "
                      "reviewers expect, and it's the one skeleton file where casing counts."))
    if "RESUME_CASING" in flags:
        s.append(core("Minor, no points off: GitHub is case-sensitive and the canonical "
                      "filename is `RESUME.md` (all caps). Rename `Resume.md` → `RESUME.md` "
                      "(edit the file, change the name in the path box, commit) to stay "
                      "consistent with the rest of the skeleton."))
    if "THIN_BIO" in flags:
        s.append(core("Your root `README.md` bio is thin (under ~100 words). Expand it to "
                      "100–150: **(1)** open `README.md`; **(2)** write 2–3 short paragraphs — "
                      "who you are (year + major at Shidler), a few skills or interests, and "
                      "what you're working toward; **(3)** if you draft with an LLM, rewrite it "
                      "in your own voice; **(4)** commit. It's the first thing a hiring manager "
                      "or reviewer sees."))
    if "BIO_IN_BIO_MD" in flags:
        s.append(core("Nice bio — but it's in `BIO.md`, and the file a visitor lands on first is "
                      "`README.md`. Make `README.md` your primary bio: **(1)** copy your bio text "
                      "into `README.md`; **(2)** keep `BIO.md` for the optional longer-form version "
                      "(or trim it to a short pointer); **(3)** commit. Full bio credit either way — "
                      "this is about putting your best foot forward on the landing page."))
    if "NO_RESUME" in flags:
        s.append(core("`RESUME.md` is missing or empty. Add a real resume *in the file* (a "
                      "linked `.pdf`/`.docx` attachment doesn't count): **(1)** create "
                      "`RESUME.md`; **(2)** include a contact line, a short summary, "
                      "experience, education, and skills; **(3)** draft with an LLM if you "
                      "like, but edit it yourself and log the prompt; **(4)** commit."))
    if "FEW_COMMITS" in flags:
        s.append(core("The rubric expects at least two meaningful commits. Commit in stages as "
                      "you work — e.g. `Add repo skeleton with directory READMEs`, then "
                      "`Add bio and resume` — rather than one bulk `update`. Separate, "
                      "descriptive commits show your process."))
    if "VAGUE_COMMITS" in flags:
        s.append(core("You have enough commits, but the messages aren't descriptive "
                      "(e.g. `Create README.md`, `Initial commit`). Going forward, write "
                      "messages that say *what changed* — `Add bio and resume`, `Add repo "
                      "skeleton with directory READMEs` — to earn full commit-hygiene credit."))
    if "INSTRUCTOR_NOT_COLLABORATOR" in flags:
        s.append(core("Add me as a collaborator so I can leave inline comments on later "
                      "stages: **(1)** on GitHub, open your repo's **Settings → Collaborators**; "
                      "**(2)** click **Add people**; **(3)** enter `adamwstauffer` and confirm."))
    if "STRONG" in flags:
        s.append(core("Clean setup — public repo, full skeleton with stub READMEs, a solid "
                      "bio and resume, and descriptive commits. A strong foundation for the "
                      "rest of the project."))
    nxt = next_stage_pointer(STAGE_N)
    if nxt:
        s.append(nxt)
    return s


# ---------------------------------------------------------------- PR sections
def _tick(b) -> str:
    return "✓" if b else "—"


def _pr_sections(st, present: float, expected: int,
                 bio_words: int, resume_words: int):
    tree = st.tree if st else []
    checklist = [
        "| Check | Status |", "|-------|--------|",
        f"| Public / accessible | {_tick(bool(st and st.public))} |",
        f"| Skeleton dirs & READMEs | {present:g}/{expected} |",
        f"| `prompt-log.md` present | {_tick(_has_file(tree, 'prompt-log.md'))} |",
        f"| Bio (`README.md`) | {_tick(bio_words >= 100)} |",
        f"| Resume (`RESUME.md`) | {_tick(resume_words >= 30)} |",
        f"| Commit hygiene (>=2 descriptive) | "
        f"{_tick(st and st.commit_count >= 2 and st.descriptive_commit_count >= 2)} |",
    ]
    commits = [
        f"- Commits: **{st.commit_count if st else 0}** "
        f"({st.descriptive_commit_count if st else 0} with descriptive messages; "
        f"brief asks for ≥2).",
    ]
    return [("Repository checklist", checklist),
            ("Commits", commits)]


# ---------------------------------------------------------------- grading
def grade(sub: Submission, prior_weak: bool = False) -> StudentReport:
    # Stage 0 has no prior stage, so prior_weak is ignored.
    flags: list[str] = []
    meta: list[str] = []
    if sub.github_url:
        meta.append(f"**Repo:** {sub.github_url}")
    if sub.submitted_at:
        meta.append(f"**Submitted:** {sub.submitted_at:%Y-%m-%d %H:%M}")

    def report(raw, crit, accessible, st=None,
               present=0, expected=len(SKELETON_FILES) + len(SKELETON_DIRS),
               bio_words=0, resume_words=0):
        return StudentReport(
            name=sub.name, stage_n=STAGE_N, raw_pct=round(raw, 1), accessible=accessible,
            criteria=crit, suggestions=_suggestions_for(set(flags), False),
            flags=flags, meta_lines=meta,
            pr_sections=_pr_sections(st, present, expected, bio_words, resume_words),
        )

    empty_crit = [
        Criterion("Public & accessible", 0, CRIT["public_accessible"], "Your repo couldn't be reached."),
        Criterion("Skeleton & READMEs", 0, CRIT["skeleton_readmes"], "—"),
        Criterion("Bio & resume", 0, CRIT["bio_resume"], "—"),
        Criterion("Commit hygiene", 0, CRIT["commit_hygiene"], "—"),
    ]

    parsed = sub.repo
    if not parsed:
        flags.append("NO_GITHUB_LINK")
        return report(0, empty_crit, accessible=False)
    owner, repo = parsed
    st = _repo.repo_state(owner, repo)
    if not st.accessible:
        flags.append("REPO_404")
        return report(0, empty_crit, accessible=False)
    if not st.instructor_is_collaborator:
        flags.append("INSTRUCTOR_NOT_COLLABORATOR")

    branch = st.default_branch

    # If the whole submission was committed inside a wrapper folder, rebase the
    # canonical lookups onto it so the real skeleton/bio/resume still resolve;
    # the tree used for scoring becomes the wrapper-relative view, and blob
    # downloads re-prepend the prefix. The student is nudged to move to root.
    prefix = _detect_wrapper_prefix(st.tree)
    tree = _strip_prefix(st.tree, prefix) if prefix else st.tree
    if prefix:
        flags.append("NESTED_SUBMISSION")

    pa = _score_public(st, flags)
    sk, present, expected = _score_skeleton(tree, flags)

    readme_path = _find_ci(tree, "README.md")
    readme_bio_words = (_word_count(
        _repo.download_text(owner, repo, _join(prefix, readme_path), branch) or "")
        if readme_path else 0)
    bio_words = readme_bio_words
    # The handout puts the bio in README.md and reserves BIO.md for an optional
    # longer-form version. When README.md is thin, fall back to BIO.md: a real
    # bio filed there is the content done — just not where a visitor lands first.
    # Grade it on merit and nudge on placement (same policy as a memo found off
    # its canonical path), rather than reporting a "~2-word" bio the student
    # plainly wrote.
    if readme_bio_words < 100:
        bio_path = _find_ci(tree, "BIO.md")
        bio_md_words = (_word_count(
            _repo.download_text(owner, repo, _join(prefix, bio_path), branch) or "")
            if bio_path else 0)
        if bio_md_words > readme_bio_words:
            bio_words = bio_md_words
            if bio_md_words >= 100:
                flags.append("BIO_IN_BIO_MD")
    resume_path = _find_ci(tree, "RESUME.md")
    resume_words = (_word_count(
        _repo.download_text(owner, repo, _join(prefix, resume_path), branch) or "")
        if resume_path else 0)
    # A resume that exists but isn't named the canonical `RESUME.md` still gets
    # full credit — casing here is personal formatting, worth a nudge, not points.
    if resume_path and resume_path != "RESUME.md":
        flags.append("RESUME_CASING")
    br = _score_bio_resume(bio_words, resume_words, flags)

    ch = _score_commits(st, flags)

    raw_pct = pa + sk + br + ch
    if raw_pct >= 92 and not flags:
        flags.append("STRONG")

    prompt_log_ok = bool(_find_ci(st.tree, "prompt-log.md"))
    if "BIO_IN_BIO_MD" in flags:
        bio_desc = f"~{bio_words} words (in `BIO.md`; move it into `README.md`)"
    else:
        bio_desc = f"~{bio_words} words" + ("" if bio_words >= 100 else " (thin — aim for 100–150)")
    resume_desc = f"~{resume_words} words" if resume_words >= 30 else "missing or placeholder"
    commit_desc = (f"{st.commit_count} commits, {st.descriptive_commit_count} with descriptive "
                   f"messages" + ("" if st.descriptive_commit_count >= 2 else " (need ≥2)"))
    criteria = [
        Criterion("Public & accessible", pa, CRIT["public_accessible"],
                  f"{'Public and reachable' if st.public else 'Private' if st.accessible else 'Unreachable'}; "
                  f"default branch `{st.default_branch}`."),
        Criterion("Skeleton & READMEs", sk, CRIT["skeleton_readmes"],
                  f"{present:g}/{expected} canonical paths in place (½ credit for placeholder "
                  f"folders); prompt-log {'present' if prompt_log_ok else 'missing'}."),
        Criterion("Bio & resume", br, CRIT["bio_resume"], f"Bio {bio_desc}; resume {resume_desc}."),
        Criterion("Commit hygiene", ch, CRIT["commit_hygiene"], commit_desc + "."),
    ]
    return report(raw_pct, criteria, accessible=True, st=st,
                  present=present, expected=expected,
                  bio_words=bio_words, resume_words=resume_words)


if __name__ == "__main__":
    sys.exit(run_scanner(STAGE_N, STAGE_LABEL, RUBRIC_ROWS, grade,
                         default_floor=DEFAULT_FLOOR_PCT, prior_stage=PRIOR_STAGE))
