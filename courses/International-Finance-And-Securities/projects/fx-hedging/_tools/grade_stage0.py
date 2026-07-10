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


def _has_dir(tree: list[str], prefix: str) -> bool:
    return any(p.startswith(prefix) for p in tree)


# ---------------------------------------------------------------- scoring
def _score_public(st, flags: list[str]) -> float:
    if st.public:
        return float(CRIT["public_accessible"])
    # accessible but private
    flags.append("NOT_PUBLIC")
    return round(0.5 * CRIT["public_accessible"], 1)


def _score_skeleton(tree: list[str], flags: list[str]) -> tuple[float, int, int]:
    expected = len(SKELETON_FILES) + len(SKELETON_DIRS)
    present = sum(_has_file(tree, f) for f in SKELETON_FILES)
    present += sum(_has_dir(tree, d) for d in SKELETON_DIRS)
    if not _has_file(tree, "prompt-log.md"):
        flags.append("MISSING_PROMPT_LOG")
    frac = present / expected if expected else 0.0
    if frac < 0.5:
        flags.append("NO_SKELETON")
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
        return round(0.5 * CRIT["commit_hygiene"], 1)
    flags.append("FEW_COMMITS")
    return 0.0


# ---------------------------------------------------------------- suggestions
def _suggestions_for(flags: set[str], prior_weak: bool):
    s = []
    if "NO_GITHUB_LINK" in flags:
        s.append(core("No GitHub URL was found in your submission. Submit the repository "
                      "URL via Lamaku so the repo can be inspected."))
    if "REPO_404" in flags:
        s.append(core("The repository couldn't be reached — confirm it exists, is public, "
                      "and the submitted URL is correct."))
    if "NOT_PUBLIC" in flags:
        s.append(core("The repository is private. Make it public so it reads as a portfolio "
                      "piece a recruiter can open, and re-confirm the URL."))
    if "NO_SKELETON" in flags:
        s.append(core("The canonical skeleton is mostly missing. Build the full structure "
                      "(`docs/`, `models/`, `data/`, `analysis/` with their subfolders) and "
                      "drop a one- or two-line stub `README.md` in every folder."))
    if "MISSING_PROMPT_LOG" in flags:
        s.append(core("`prompt-log.md` isn't at the repo root. Add it now and log the "
                      "prompts you used to draft your bio and resume — you'll append to it "
                      "every stage."))
    if "THIN_BIO" in flags:
        s.append(core("Your bio `README.md` is thin (under ~100 words). It's the first thing "
                      "a recruiter sees — expand it and edit it well beyond raw LLM output."))
    if "NO_RESUME" in flags:
        s.append(core("`RESUME.md` is missing or empty. Add a real resume; use an LLM as the "
                      "drafter and yourself as the editor, and log the prompts."))
    if "FEW_COMMITS" in flags:
        s.append(core("The rubric expects at least two meaningful commits with descriptive "
                      "messages (e.g. `Add repo skeleton with directory READMEs`, "
                      "`Add bio and resume`), not a single `update`."))
    if "INSTRUCTOR_NOT_COLLABORATOR" in flags:
        s.append(core("I'm not a collaborator on the repo yet — add `adamwstauffer` so I can "
                      "leave inline review comments on later stages."))
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


def _pr_sections(st, present: int, expected: int,
                 bio_words: int, resume_words: int):
    tree = st.tree if st else []
    checklist = [
        "| Check | Status |", "|-------|--------|",
        f"| Public / accessible | {_tick(bool(st and st.public))} |",
        f"| Skeleton dirs & READMEs | {present}/{expected} |",
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
        Criterion("Public & accessible", 0, CRIT["public_accessible"], "no reachable repo"),
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

    pa = _score_public(st, flags)
    sk, present, expected = _score_skeleton(st.tree, flags)

    bio_words = 0
    if _has_file(st.tree, "README.md"):
        bio_words = _word_count(_repo.download_text(owner, repo, "README.md", branch) or "")
    resume_words = 0
    if _has_file(st.tree, "RESUME.md"):
        resume_words = _word_count(_repo.download_text(owner, repo, "RESUME.md", branch) or "")
    br = _score_bio_resume(bio_words, resume_words, flags)

    ch = _score_commits(st, flags)

    raw_pct = pa + sk + br + ch
    if raw_pct >= 92 and not flags:
        flags.append("STRONG")

    criteria = [
        Criterion("Public & accessible", pa, CRIT["public_accessible"],
                  f"{'public' if st.public else 'private' if st.accessible else 'unreachable'}, "
                  f"default branch `{st.default_branch}`."),
        Criterion("Skeleton & READMEs", sk, CRIT["skeleton_readmes"],
                  f"{present}/{expected} canonical paths present; "
                  f"prompt-log {'Y' if _has_file(st.tree, 'prompt-log.md') else 'N'}."),
        Criterion("Bio & resume", br, CRIT["bio_resume"],
                  f"bio ~{bio_words} words, resume ~{resume_words} words."),
        Criterion("Commit hygiene", ch, CRIT["commit_hygiene"],
                  f"{st.commit_count} commits, {st.descriptive_commit_count} descriptive."),
    ]
    return report(raw_pct, criteria, accessible=True, st=st,
                  present=present, expected=expected,
                  bio_words=bio_words, resume_words=resume_words)


if __name__ == "__main__":
    sys.exit(run_scanner(STAGE_N, STAGE_LABEL, RUBRIC_ROWS, grade,
                         default_floor=DEFAULT_FLOOR_PCT, prior_stage=PRIOR_STAGE))
