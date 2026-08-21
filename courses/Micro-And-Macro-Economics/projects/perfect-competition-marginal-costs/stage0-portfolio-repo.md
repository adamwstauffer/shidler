---
template: stage-brief
project: perfect-competition-marginal-costs
stage: 0
title: "Portfolio Repository"
capability: marginal-analysis
deliverables:
  - path: "(repository) firstname-lastname"
    format: repo
    ai_boundary: ai-first-verified
prerequisites: []
points: 2
estimated_time: "40-50 min"
---

# Stage 0 — Portfolio Repository

**Deliverable:** the public portfolio repository, built to the standard, with the instructor invited
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 40–50 minutes

> **Stage 0 belongs to the course, not to Case 1** (reframed 2026-08-17, matching the course site).
> It is done once, before any engagement, and every course here reads the same result. It comes in
> **two parts**: **part 1** — the GitHub account and the three verbs (add → commit → push), on the
> [onboarding page](https://adamwstauffer.github.io/ai-lms/onboarding.html#github-account); **part 2**
> — the workspace, which is this brief. Its interactive companion is
> [github-stage0.html](https://adamwstauffer.github.io/ai-lms/github-stage0.html) *(renamed from
> `case-perfect-competition-stage0.html`; the old URL redirects)*. Grading is unchanged: it is still
> recorded as Case 1's item 1.0.

---

## 1. Purpose

This stage produces the workspace, and nothing else. One public repository, named for you, holding
the structure that every engagement in this course and every engagement after it lands in. No
analysis happens here.

It is a stage of its own rather than a preamble to the brief because it has to be finished before
the brief is written, and because it is the one artifact in this course that outlives the course. A
repository stood up properly in week one is a portfolio by December; one thrown together on the way
to a deadline is a folder of homework.

## 2. Prerequisites

None. This is the entry point for the engagement and for the repository.

Read before starting:

- [The portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) — the structure, the four starter files, and a prompt that builds the skeleton
- [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html) — what goes in `AGENTS.md`, and what must never be committed
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics) — local versus remote, add → commit → push, `.gitignore`, and how work is submitted

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| Public portfolio repository, named for you | `github.com/{you}/firstname-lastname` | repository |
| Bio and engagement index | `README.md` | markdown |
| AI conventions, and the pointer to them | `AGENTS.md`, `CLAUDE.md` | markdown |
| Resume and prompt log, started | `RESUME.md`, `prompt-log.md` | markdown |
| Exclusion rules | `.gitignore` | text |

## 4. Background

The repository is organized by **capability** and **engagement**, never by course. A folder named
for a class stops meaning anything the moment the class ends, and a reader who opens
`week3/final_v2.xlsx` learns nothing about what you can do. `capabilities/marginal-analysis/` names a
capability; `docs/`, `data/`, and `analysis/` hold the work that proves you exercised it.

Two consequences worth knowing before you start rather than after:

**Git tracks files, not folders.** An empty directory does not survive a push. Every directory in
the skeleton needs at least one file in it — a one-line `README.md` saying what belongs there is
enough, and is more useful to a reader than an empty folder anyway.

**History is permanent.** A file committed once stays in the repository's history even after it is
deleted. That is why `.gitignore` goes in *before* the first workbook, not after the first
accidental commit of a `~$` temp file.

## 5. Procedure

1. **Create the GitHub account.** Use your `@hawaii.edu` address — it qualifies for
   [GitHub Education](https://education.github.com). Choose a professional username; it appears
   beside every piece of work you publish. **Already have a GitHub account? Use it** — do not create
   a second one; add your `hawaii.edu` address under *Settings → Emails* and the education benefits
   attach to the account you keep after graduation.
   *Confirm:* you can sign in, and the email is verified.

2. **Install GitHub Desktop**, or use the command line if you already prefer it. The deliverable is
   identical either way.
   *Confirm:* the app is signed in, and your Git config carries your real name and `.edu` address —
   both are stamped on every commit.

3. **Create the repository.** Name it `firstname-lastname`, set visibility to **public**, and
   initialize it with a README so it can be cloned.
   *Confirm:* the repository URL opens in a private browser window without a login prompt.

4. **Clone it, then build the skeleton** to the structure in the portfolio repo standard. Creating
   directories is mechanical work — use the starter prompt on that page and check the result rather
   than typing it out.
   *Confirm:* every directory holds at least one file, or Git will not track it.

5. **Write the four root files.** Replace the generated `README.md` with three to six sentences on
   who you are, followed by an engagement index. Add `RESUME.md`, `AGENTS.md` (start from the
   baseline on the AI conventions page and edit until it describes you), and the one-line
   `CLAUDE.md` pointing at it.
   *Confirm:* nothing in these files is placeholder text you would not want read.

6. **Add `.gitignore`** before any workbook is committed, using the starter block in
   [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#gitignore).
   *Confirm:* `~$`-prefixed files never appear in your Changes panel.

7. **Add your instructor as a collaborator** — repository **Settings → Collaborators → Add people**,
   then `adamwstauffer`. Collaborator access is what allows a review branch or a pull request against
   your work instead of an emailed paragraph.
   *Confirm:* the invitation shows as pending. You do not need to wait for it.

8. **Commit and push.** At least two commits, each with a message saying what changed —
   `Add portfolio skeleton and gitignore` rather than `update`.
   *Confirm:* the files are visible on github.com, not only on your machine.

## 6. AI use

| Artifact | Draft order |
|---|---|
| Repository skeleton, `.gitignore`, the `AGENTS.md` starting point | AI-first, verified |
| `README.md` bio, `RESUME.md` | AI-first, verified — then edited until it sounds like you |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** everything here is a means to the work rather than the work itself,
so AI may build all of it and you verify. Three things to check in what it produces: no folder is
named after a course or a term, every directory contains something, and the placeholder files are
actually placeholders rather than invented biography. That last one is the failure that matters —
committing generic AI-written filler as your bio is obvious to any reader, and it is the first thing
anyone sees.

## 7. Verification

- [ ] Repository is **public** — the URL opens in a private browser window without logging in
- [ ] Named for you (`firstname-lastname`), not for a course
- [ ] `README.md` holds a real three-to-six-sentence bio and the start of an engagement index
- [ ] `AGENTS.md` written in your own words; `CLAUDE.md` is the one-line pointer
- [ ] `RESUME.md` and `prompt-log.md` exist at the root — rough is acceptable
- [ ] `.gitignore` filters Office and OS temp files
- [ ] Every skeleton directory holds at least one file
- [ ] `adamwstauffer` invited as a collaborator
- [ ] At least two commits, each with a message that says what changed

## 8. Rubric (2 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Repo live and public, professionally named | 1 | URL works without login; `firstname-lastname` naming; the bio in `README.md` is not placeholder text |
| Skeleton, `.gitignore`, and commit hygiene | 1 | `docs/briefs/` in place and the root files present (`AGENTS.md`, `CLAUDE.md`, `RESUME.md`, `prompt-log.md`); junk files filtered; at least two descriptive commits |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| The repository is private, so nothing in it can be read | Settings → General → Change visibility → Public, then test the URL in a private window |
| The repository is named after the course | Rename it now, while nothing links to it — a course-shaped repository stops meaning anything at graduation |
| Empty directories disappear on push | Git tracks files, not folders; put a one-line `README.md` in each |
| An hour spent polishing the bio on day one | It evolves all term. Get the repository live |
| Commit messages read `update` | Say what changed: `Add portfolio skeleton and gitignore` |
| `.gitignore` added after the first workbook commit | The junk is already in the history. Add it now anyway, and know that history is permanent |

## 10. References

- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [`.gitignore`](https://adamwstauffer.github.io/ai-lms/onboarding.html#gitignore) and [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
- [`docs/guides/github-mba-guide.md`](../../../../../docs/guides/github-mba-guide.md) — the long-form Git reference, for troubleshooting
