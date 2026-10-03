# Stage 0: Personal Portfolio Repository

**Step-by-step on Kumu:** [Stage 0 walkthrough](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage0.html)

**Weight:** 5% of project score
**Format:** Upload-only — no presentation component
**Deliverable:** Public GitHub repository URL submitted via Lamaku

---

## Overview

Create your own public GitHub repository — your **portfolio repo** — that will hold every artifact you produce in this course and serve as a discoverable record of your work for employers and collaborators.

Every later stage adds to it.

> **Never used GitHub before?** This Stage 0 doc is the on-ramp. If you want deeper coverage of any topic below (first commit using GitHub Desktop, the Collaborators panel, pushing larger files), the full reference is at [Kumu onboarding](https://adamwstauffer.github.io/ai-lms/onboarding.html). You don't need to read it cover-to-cover — treat it as the dictionary you keep open in another tab while you follow these five steps.

## Why this is Stage 0

Every later stage delivers into *your* repo. Standing it up now removes a tooling barrier before any analytical work begins, and it forces an early decision: this work will be public-facing and version-controlled, not buried on a personal hard drive.

---

## The five steps

The deck walks through these on one summary slide. This document is the detailed handholding version — read it once, then keep it open as a reference while you work through each step.

| Step | What you do | Time |
|------|-------------|------|
| **1** | Create a GitHub account | 5 min |
| **2** | Install GitHub Desktop (no command line required) | 10 min |
| **3** | Create your repo and directory skeleton with stub READMEs | 15 min |
| **4** | Write your bio (in `README.md`) and `RESUME.md` yourself, have an LLM review them, revise, commit | 30–45 min |
| **5** | Save your changes back to GitHub (Add → Commit → Push) | 2 min per save |

---

## Step 1 — Create a GitHub Account

1. Go to **[github.com](https://github.com)** and click **Sign up**.
2. **Use any email you keep.** Any email works for your GitHub account; for the free GitHub Education benefits, add your school address under Settings › Emails and apply, which is optional and never graded.
3. **Choose a professional username.** Managers, peers, and reviewers will see this — it's effectively a second business card. Good: `firstname-lastname`, `flastname`, `firstinitiallastname`. Avoid gamer tags, joke names, or anything you wouldn't put on a resume.
4. **Verify your email** (check your inbox for the confirmation link).
5. Optional but recommended: upload a **profile photo** (headshot or avatar). It helps your instructor recognize you on the platform.
6. **Share your GitHub username with the instructor** so we can find your repo.

**Optional: GitHub Education benefits.** Add your school address under Settings › Emails, then go to [education.github.com](https://education.github.com) and click **Get benefits**. It is optional and never graded.

---

## Step 2 — Install GitHub Desktop

We use **GitHub Desktop** for this course. It's a free visual app from GitHub that handles everything (clone, commit, push, pull) through buttons and menus — no terminal, no command line, no Git Bash. You install it once and never think about Git internals.

1. Go to **[desktop.github.com](https://desktop.github.com)** and download for your OS.
2. **Windows:** run the installer, click through the prompts (it auto-installs Git in the background — you don't need to install Git separately).
3. **Mac:** open the `.dmg`, drag GitHub Desktop into Applications, then launch it.
4. The first time you open it, it asks you to **sign in to GitHub.com** with the account from Step 1. Sign in.
5. It will ask you to confirm your **Git config** (name and email) — these get attached to every commit. Use your real name and an email you keep.

That's it. You're done with installation.

> **Why we don't use the command line.** Git's CLI (`git add`, `git commit -m "..."`, `git push`) is faster once you know it, but the syntax punishes typos and the error messages aren't friendly. GitHub Desktop wraps the same operations in a UI that's hard to break. If you want to learn the CLI later, the deck's appendix has a Quick Reference Cheat Sheet — but you'll never need it for this course.

---

## Step 3 — Create Your Repo and Directory Skeleton

### 3a. Create the repo on GitHub

1. On [github.com](https://github.com), click the **+** in the top-right corner → **New repository**.
2. **Repository name:** name it after *you*, not this course — `firstname-lastname` (or `firstname-lastname-portfolio` if the plain name is taken; hyphens are conventional). This repo outlives BUS 629: every later course and your career docs land here too, and the name is the first thing an employer reads — so name it for the person, not the subject.
3. **Visibility:** **Public**. This is non-negotiable — the whole point is that managers, collaborators, and reviewers can find it.
4. **Initialize this repository with:** check **Add a README file** (otherwise the repo is empty and you can't clone it).
5. **License:** optional. Pick **MIT** if you want one — it's the most permissive.
6. Click **Create repository**.

### 3b. Clone the repo to your computer with GitHub Desktop

1. Open GitHub Desktop.
2. **File → Clone repository → GitHub.com tab**.
3. Find your new `firstname-lastname` repo in the list, choose where on your computer to save it (e.g., `Documents/GitHub/`), and click **Clone**.
4. GitHub Desktop will tell you "How are you planning to use this fork?" — choose **For my own purposes**.

### 3c. Build the directory skeleton

In your newly cloned folder, create this structure. You can do it in your file explorer (Windows Explorer / Finder), in VS Code, or in any text editor.

```
firstname-lastname/
├── README.md                  # ← Bio (Step 4) — first thing visitors see
├── RESUME.md                  # ← Resume (Step 4)
├── docs/                      # All written deliverables and reference docs
│   ├── README.md              # Explains what lives in docs/
│   ├── decisions/             # Memos and decision documents (Stage 2)
│   │   └── README.md
│   ├── specs/                 # Technical specifications (Stage 4)
│   │   └── README.md
│   ├── plans/                 # Optional project plans / timelines
│   │   └── README.md
│   └── templates/             # Stub README pointing at canonical course templates
│       └── README.md
├── models/                    # All Excel work
│   ├── README.md              # Explains models/ vs. the two subfolders
│   ├── templates/             # Blank model frameworks (Stage 1)
│   │   └── README.md
│   └── builds/                # Populated, working models (Stage 3)
│       └── README.md
├── data/                      # Source financial data + provenance notes
│   └── README.md
├── analysis/                  # Self-audit / validation work
│   ├── README.md
│   └── validation/            # Stage 3 validation reports
│       └── README.md
└── prompt-log.md              # Every AI session that mattered (repo root)
    └── README.md
```

**Every directory gets a `README.md`.** The README explains what belongs in that directory and the naming conventions used. If a new collaborator joins, they should be able to navigate by READMEs alone — no questions asked.

The course repo (`courses/International-Corporate-Finance/projects/performance-ratios/`) is a **living example** — copy and adapt its READMEs.

### 3d. Add a `.gitignore` so junk files stay out

Excel and your OS both create hidden temp files that you do **not** want in your commit history. The fix is a one-time `.gitignore` file at the root of your repo. **Add it now**, before your first Stage 3 workbook commit — once junk files land in the history, getting them back out is painful.

1. In the root of your repo (next to `README.md`), create a new file named **`.gitignore`** (the leading dot is required — on Windows, your file explorer may try to strip it; if so, save the file from a text editor like VS Code or Notepad with quotes around the name: `".gitignore"`).
2. Paste in:

    ```
    # Excel and Office temp files
    ~$*.xlsx
    ~$*.xls
    ~$*.docx
    ~$*.pptx

    # OS junk
    .DS_Store
    Thumbs.db

    # Editor backups
    *.tmp
    *.bak
    ```

3. Save the file.

GitHub Desktop will now silently filter these files out of the **Changes** panel — they won't appear as pending changes the next time you open the workbook in Excel. **If you ever see `~$your-workbook.xlsx` in the Changes panel**, your `.gitignore` is missing or this file isn't matching. Re-check.

### 3e. Save your skeleton back to GitHub

In GitHub Desktop:
1. You'll see all your new files in the **Changes** panel on the left.
2. In the bottom-left, write a **summary** like: `Add directory skeleton`.
3. Click **Commit to main**.
4. Click **Push origin** at the top.

Refresh your repo on GitHub — you should see all the directories.

---

## Step 4 — Write your bio and `RESUME.md`, then iterate with an LLM

The bio is yours: 200–400 words, written by you, and it lives in your `README.md` — never in a separate `BIO.md`. The sequence is human first. You write the first draft; an LLM (ChatGPT or Claude) reviews it; you revise, and the two of you iterate. The resume follows the same sequence: you draft `RESUME.md` from your own source material (LinkedIn, an old resume, a CV), the LLM reviews it, you revise.

### 4a. Pick your LLM

| Tool | Where | Notes |
|------|-------|-------|
| **Claude** | [claude.ai](https://claude.ai) (or download the [desktop app](https://claude.ai/download)) | Anthropic. Strong at structured writing. Free tier sufficient. |
| **ChatGPT** | [chatgpt.com](https://chatgpt.com) | OpenAI. Free tier sufficient. |

Either works. Pick one.

### 4b. Drop in the templates

The course repo contains polished templates — read them first to understand the structure:

- **Bio template** (with 30+ LLM revision prompts): [`../../templates/portfolio/bio-template.md`](../../../../templates/portfolio/bio-template.md)
- **Resume template** (Penn-style): [`../../templates/portfolio/resume-template.md`](../../../../templates/portfolio/resume-template.md)
- **Portfolio README** (workflow guide): [`../../templates/portfolio/README.md`](../../../../templates/portfolio/README.md)

Read the bio template, then write your own 200–400 word draft against its structure. Once you have a draft, paste it into your LLM along with the template and add a prompt like:

> Here is a bio template and a draft bio I wrote. Review the draft against the template's structure and suggest specific improvements — don't rewrite it from scratch. The audience is senior managers, graduate program admissions, and professional collaborators. Make it specific and quantified, not generic.

Then revise it yourself and iterate. The bio template's prompt library has 30+ review angles — try 2 or 3, and keep the changes you agree with in your own words.

Repeat for the resume: write your `RESUME.md` draft against the resume template first, then ask the LLM to review it, then revise.

### 4c. Save the files into your repo

1. In your `firstname-lastname/` folder, replace the auto-generated `README.md` with your bio (200–400 words; no separate `BIO.md`).
2. Create `RESUME.md` with your revised resume.
3. In GitHub Desktop: write a summary like `Add bio and resume`, **Commit to main**, then **Push origin**.

---

## Step 5 — The Save Workflow (Add, Commit, Push)

Every time you finish a piece of work, save it back to GitHub. In GitHub Desktop this is three clicks:

| In Desktop | In CLI (FYI only) | What it does |
|-----------|-------------------|---------------|
| Files appear in the **Changes** panel | `git add .` | Stages your changes |
| Type a summary, click **Commit to main** | `git commit -m "Add bio"` | Creates a permanent snapshot |
| Click **Push origin** | `git push` | Uploads commits to GitHub |

**Commit messages should be descriptive.** Not `update` or `fix` — instead: `Add bio with focus on FX and emerging markets` or `Polish resume formatting for first draft`. Every later stage is graded in part on **commit hygiene**: at least 2 meaningful commits per stage, descriptive messages.

---

## What to submit

Submit the URL of your public GitHub repo via Lamaku. The repo must contain:

- [ ] Public visibility (anyone can view without logging in)
- [ ] `README.md` with your bio
- [ ] `RESUME.md` with your resume
- [ ] Directory skeleton from Step 3 with a `README.md` in every directory
- [ ] At least 2 meaningful commits with descriptive messages

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline can move your score up — the full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (% of Stage 0 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Repo public + accessible | 15% | URL works without login; correctly named |
| Directory skeleton + READMEs | 20% | All required dirs present; every dir has a meaningful README |
| Bio quality | 25% | 200–400 words in `README.md`; structured; judged on your own draft and on how you revised it after the LLM's review |
| Resume quality | 25% | Penn-style format; quantified achievements; concise |
| Commit hygiene | 15% | At least 2 commits; descriptive messages; clean history |

---

## Tips

- **Don't aim for perfection on day one.** Your bio and resume will evolve all semester. Stage 0 is about getting the repo live with a usable skeleton.
- **Draft first, then use the bio template's prompt library.** It includes 30+ LLM review prompts — once your own draft exists, pick 2–3 angles, then revise before settling on the version you commit.
- **Keep it public.** A public repo is the entire point — managers, collaborators, and reviewers need to be able to find it.
- **The course repo is your reference.** When you're not sure what a directory should look like, study how this course repo is organized.
- **Don't commit secrets.** No API keys, no passwords, no personally sensitive financial data. The provided `.gitignore` template handles common cases — see the deck's appendix for more.

---

## If you prefer the command line

GitHub Desktop is the recommended workflow. If you're already comfortable with the CLI and prefer it, the equivalent commands are documented in the **Quick Reference Cheat Sheet** at the end of the deck. The deliverable is identical either way.
