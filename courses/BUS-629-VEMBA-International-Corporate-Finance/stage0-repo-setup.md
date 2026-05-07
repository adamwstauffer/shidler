# Stage 0: Personal Portfolio Repository

**Weight:** 5% of project score
**Format:** Upload-only — no presentation component
**Deliverable:** Public GitHub repository URL submitted via Lamaku

---

## Overview

Create your own public GitHub repository — your **portfolio repo** — that will hold every artifact you produce in this course and serve as a discoverable record of your work for employers and collaborators.

A polished public repo is one of the highest-leverage career artifacts you can build. Every subsequent stage adds to it.

## Why this is Stage 0

Every later stage delivers into *your* repo. Standing it up now removes a tooling barrier before any analytical work begins, and it forces an early decision: this work will be public-facing and version-controlled, not buried on a personal hard drive.

---

## What you must create

A public repository named **`Corporate Finance`** (or `corporate-finance` — your choice) with these files at the root:

| File | What it is |
|------|------------|
| `README.md` | Your professional bio (the first thing visitors see) |
| `RESUME.md` | Markdown resume |
| `BIO.md` | Optional longer-form bio if you want to keep your resume separate from your README narrative |

The repo will grow throughout the semester to add `docs/`, `models/`, `data/`, `analysis/`, and `deliverables/` directories. You don't need to create those today — just the repo and the three root files.

### Templates to start from

The course repo already contains polished templates you should copy:

- **Bio template** (with LLM revision prompts): [`../../docs/templates/portfolio/bio-template.md`](../../docs/templates/portfolio/bio-template.md)
- **Resume template** (Penn-style): [`../../docs/templates/portfolio/resume-template.md`](../../docs/templates/portfolio/resume-template.md)
- **Portfolio README** (workflow guide): [`../../docs/templates/portfolio/README.md`](../../docs/templates/portfolio/README.md)

---

## Three ways to do it

You can use any of these workflows — pick the one you're most comfortable with. The deliverable is the same.

### Option A — GitHub web UI (no installs needed)

1. Go to **github.com** → sign in or create an account.
2. Click **+** (top right) → **New repository**.
3. Name it `Corporate Finance`. Set visibility to **Public**. Check **Add a README file**. Click **Create repository**.
4. In the repo, click **Add file → Create new file** to add `RESUME.md` and `BIO.md`.
5. Paste content from the templates above and edit with your details.
6. Each save is a "commit" — write a short message explaining the change.

### Option B — Claude desktop app (chat interface, file uploads)

1. Open the [Claude desktop app](https://claude.ai/download).
2. Upload the bio and resume templates (drag-and-drop the `.md` files).
3. Ask Claude to help you draft your bio and resume against the template structure.
4. Copy the output into GitHub via Option A's workflow.

### Option C — Claude Code CLI (terminal)

1. Install [Claude Code](https://claude.ai/code).
2. From your terminal: `git clone https://github.com/[your-username]/Corporate-Finance.git` then `cd Corporate-Finance`.
3. Launch `claude` and ask it to populate your `README.md`, `RESUME.md`, and `BIO.md` from the templates at:
   - `https://github.com/adamwstauffer/shidler/blob/main/docs/templates/portfolio/bio-template.md`
   - `https://github.com/adamwstauffer/shidler/blob/main/docs/templates/portfolio/resume-template.md`
4. Use `git add . && git commit -m "Add bio and resume" && git push` to publish.

---

## Git basics — what `commit`, `push`, and `pull` mean

Don't worry about mastering Git in Stage 0. You only need to understand what these three commands do conceptually:

| Command | Plain English |
|---------|---------------|
| `git add` | "Stage this change to be saved." Like marking which files go into the next save-point. |
| `git commit` | "Save this set of changes locally with a description." Creates a snapshot. |
| `git push` | "Send my saved changes from my computer up to GitHub so others can see them." |
| `git pull` | "Bring down any changes from GitHub that I don't have locally yet." |

In the GitHub web UI, every "Commit changes" button does **add + commit + push** in one click.

**Commit messages should be descriptive.** Not `update` or `fix` — instead: `Add bio with focus on FX and emerging markets` or `Polish resume formatting for first draft`.

---

## What to submit

Submit the URL of your public GitHub repo via Lamaku. The repo must contain:

- [ ] Public visibility (anyone can view without logging in)
- [ ] `README.md` with your bio
- [ ] `RESUME.md` with your resume
- [ ] `BIO.md` (optional but recommended)
- [ ] At least 2 meaningful commits with descriptive messages

---

## Rubric (% of Stage 0 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Repo public + accessible | 20% | URL works without login; correctly named |
| Bio quality | 30% | 150–200 words; structured; iteratively revised |
| Resume quality | 30% | Penn-style format; quantified achievements; concise |
| Commit hygiene | 20% | At least 2 commits; descriptive messages; clean history |

---

## Tips

- **Don't aim for perfection on day one.** Your bio and resume will evolve all semester. Stage 0 is about getting the repo live.
- **Use the bio template's prompt library.** It includes 30+ LLM prompts for iterative revision — pick 2–3 angles and run them.
- **Keep it public.** A public repo is the entire point — recruiters and collaborators need to be able to find it.
- **The course repo is your reference.** When you're not sure what a directory should look like, study how this course repo is organized.
