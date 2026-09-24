---
template: stage-brief
project: fx-hedging
stage: 0
title: "Portfolio Repository"
capability: fx-hedging
deliverables:
  - path: "(repository) firstname-lastname"
    format: repo
    ai_boundary: ai-first-verified
prerequisites: []
weight: "8% of project"
estimated_time: "40-50 min"
---

# Stage 0 — Portfolio Repository (8% of project)

**Deliverable:** the public portfolio repository, built to the standard, with the instructor invited
**Submission:** committed and pushed to your public repository; the repository URL goes to Lamaku; graded by inspection
**Estimated time:** 40–50 minutes

> **Stage 0 belongs to the course, not to the FX hedging project** (reframed 2026-09-24, matching
> the course site and BUS 620 Micro & Macro Economics, which is the guidepost for this course's
> conventions). It is done once, before any project work, and every course here reads the same
> result. It comes in **two parts**: **part 1** — the GitHub account and the three verbs
> (add → commit → push), on the
> [onboarding page](https://adamwstauffer.github.io/ai-lms/onboarding.html#github-account);
> **part 2** — the workspace, which is this brief. Its interactive companion is
> [github-stage0.html](https://adamwstauffer.github.io/ai-lms/github-stage0.html) *(the old
> `fx-hedging-stage0.html` URL redirects there)*. The weight is unchanged: it is still recorded as
> the project's Stage 0.
>
> **What moved (2026-09-24).** This brief used to prescribe a project-shaped skeleton —
> `docs/specs/`, `docs/plans/`, `docs/templates/`, `models/templates/`, `models/builds/`, and a
> separate `BIO.md`. That skeleton is **superseded** by the course-independent portfolio repo
> standard below. The two folders this project actually commits into, `docs/specs/` and
> `models/builds/`, are now added at **Stage 1** (see
> [`stage1-executive-memo.md`](stage1-executive-memo.md) § Set up this project's folders), the
> way the course site has taught it since 2026-08-20. The earlier text is in this file's git
> history. The frozen legacy grader `_tools/grade_stage0.py` still checks the old skeleton — do not
> use it against this brief.

---

## 1. Purpose

This stage produces the workspace, and nothing else. One public repository, named for you, holding
the structure that every stage of this project — and every project after it — lands in. No finance
happens here; the point is that from Stage 1 on, the work is about currency risk rather than Git.

It is a stage of its own because it has to be finished before the memo is committed, and because it
is the one artifact in this course that outlives the course. A repository stood up properly in week
one is a portfolio by the end of the term; one thrown together on the way to a deadline is a folder
of homework.

**Already have a portfolio repo from BUS 313/314 or another course?** You don't start over. Bring it
up to the standard below and add anything missing. Same rubric.

## 2. Prerequisites

None. This is the entry point for the project and for the repository.

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
| The skeleton | `capabilities/`, `docs/briefs/`, `docs/decisions/`, `data/`, `analysis/figures/` — each with a one-line `README.md` | folders |

The skeleton is the course-independent standard (reference copy, with this project's Stage 1
folders already added: [`../../sample/`](../../sample/)):

```
firstname-lastname/
├── README.md          bio + engagement index — the first thing a visitor reads
├── RESUME.md
├── AGENTS.md          your AI conventions; CLAUDE.md is a one-line pointer to it
├── CLAUDE.md
├── prompt-log.md      one entry per AI session, kept all term
├── .gitignore
├── capabilities/      one folder per thing you can do — capabilities/fx-hedging/ for this project
├── docs/
│   ├── briefs/        the question, before the work
│   └── decisions/     the answer, after the work — memos land here
├── data/              sourced inputs, with provenance
└── analysis/
    └── figures/       the findings, and their charts
```

## 4. Background

The repository is organized by **capability** and **engagement**, never by course. A folder named
for a class stops meaning anything the moment the class ends, and a reader who opens
`fin321/final_v2.xlsx` learns nothing about what you can do. `capabilities/fx-hedging/` names a
capability; `docs/`, `data/`, and `analysis/` hold the work that proves you exercised it.

Two consequences worth knowing before you start rather than after:

**Git tracks files, not folders.** An empty directory does not survive a push. Every directory in
the skeleton needs at least one file in it — a one-line `README.md` saying what belongs there is
enough, and is more useful to a reader than an empty folder anyway.

**History is permanent.** A file committed once stays in the repository's history even after it is
deleted. That is why `.gitignore` goes in *before* the first workbook, not after the first
accidental commit of a `~$` temp file.

## 5. Procedure

1. **Create the GitHub account** (part 1). Use your `@hawaii.edu` address — it qualifies for
   [GitHub Education](https://education.github.com). **Already have a GitHub account? Use it** — do
   not create a second one; add your `hawaii.edu` address under *Settings → Emails*.
   *Confirm:* you can sign in, and the email is verified.

2. **Install GitHub Desktop**, or use the command line if you already prefer it. The deliverable is
   identical either way.
   *Confirm:* your Git config carries your real name and `.edu` address — both are stamped on every commit.

3. **Create the repository.** Name it `firstname-lastname` (or `firstname-lastname-portfolio` if the
   plain name is taken), set visibility to **public**, and initialize it with a README. Resist a
   course- or finance-scoped name: this repo outlives any one class, and its name is the first thing
   an employer reads.
   *Confirm:* the repository URL opens in a private browser window without a login prompt.

4. **Clone it, then hand the mechanics to an AI.** The
   [setup prompt](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html#build-with-llm) on the
   portfolio repo standard builds the skeleton, drafts `AGENTS.md` tailored to you from your resume,
   writes the one-line `CLAUDE.md`, starts `prompt-log.md` with its first entry, and adds
   `.gitignore`. **Read every file before you commit.**
   *Confirm:* every directory holds at least one file; `AGENTS.md` says something only you could have said.

5. **Write the bio yourself.** Replace the placeholder `README.md` with three to six sentences on who
   you are, followed by an engagement index. The bio lives in `README.md`, not in a separate `BIO.md`.
   *Confirm:* nothing in these files is placeholder text you would not want read.

6. **Add `.gitignore`** before any workbook is committed, using the starter block in
   [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#gitignore).
   *Confirm:* `~$`-prefixed files never appear in your Changes panel.

7. **Add your instructor as a collaborator** — **Settings → Collaborators → Add people**, then
   `adamwstauffer`.
   *Confirm:* the invitation shows as pending. You do not need to wait for it.

8. **Commit and push**, then submit the repository URL on Lamaku. At least two commits, each with a
   message saying what changed — `Add portfolio skeleton and gitignore`, not `update`.
   *Confirm:* the files are visible on github.com, not only on your machine.

## 6. AI use

| Artifact | Draft order |
|---|---|
| Repository skeleton, `.gitignore`, `AGENTS.md` tailored from your resume, `CLAUDE.md`, the first `prompt-log.md` entry | AI-first, verified — the setup prompt does all of it |
| `README.md` bio, `RESUME.md` | AI-first, verified — then edited until it sounds like you |
| `prompt-log.md` after day one | Kept under the standing rule in `AGENTS.md`: one entry per session, never backfilled |

Everything here is a means to the work rather than the work itself, so AI may build all of it and
you verify. Three things to check: no folder is named after a course or a term, every directory
contains something, and the placeholder files are actually placeholders rather than invented
biography.

## 7. Verification

- [ ] Repository is **public** — the URL opens in a private browser window without logging in
- [ ] Named for you (`firstname-lastname`), not for a course
- [ ] `README.md` holds a real bio and the start of an engagement index
- [ ] `AGENTS.md` tailored to you; `CLAUDE.md` is the one-line pointer
- [ ] `RESUME.md` at the root; `prompt-log.md` has its first entry
- [ ] `.gitignore` filters Office and OS temp files
- [ ] Every skeleton directory holds at least one file
- [ ] `adamwstauffer` invited as a collaborator
- [ ] At least two commits, each with a message that says what changed; URL submitted on Lamaku

## 8. Rubric (8% of project)

| Criterion | Weight | What distinguishes strong work |
|---|---:|---|
| Public & accessible | 25% | Repo is public, professionally named, URL submitted |
| Skeleton & READMEs | 25% | The standard skeleton above; a stub `README.md` in every folder; `AGENTS.md`, `CLAUDE.md`, `prompt-log.md`, `.gitignore` present |
| Bio & resume | 25% | Clear, professional, recruiter-ready; evidence of editing beyond raw LLM output |
| Commit hygiene | 25% | ≥2 meaningful commits with descriptive messages |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| The repository is private | Settings → General → Change visibility → Public, then test the URL in a private window |
| The repository is named after the course | Rename it now, while nothing links to it |
| Empty directories disappear on push | Git tracks files, not folders; put a one-line `README.md` in each |
| Building `docs/specs/` and `models/` now | Not yet — those are this project's folders, added at Stage 1 |
| `.gitignore` added after the first workbook commit | The junk is already in the history. Add it now anyway |

## 10. How this leads to Stage 1

Stage 1 adds this project's two folders (`docs/specs/`, `models/builds/`) and commits the
exposure memo to `docs/decisions/`. From here on, "submit" means "commit and push" — version
control is a professional skill you practice by default, not a submission mechanism.

## 11. References

- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [`.gitignore`](https://adamwstauffer.github.io/ai-lms/onboarding.html#gitignore) and [how work is submitted](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
- The same stage in BUS 620: [`../../../Micro-And-Macro-Economics/projects/perfect-competition-marginal-costs/stage0-portfolio-repo.md`](../../../Micro-And-Macro-Economics/projects/perfect-competition-marginal-costs/stage0-portfolio-repo.md)
