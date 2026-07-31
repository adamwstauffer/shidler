# Mini 1 · Stage 1a — Repo + Brief

**Mini weight:** 10% of course grade — this stage: 3 of 20 pts
**Format:** Upload-only — no presentation component
**Deliverable:** Public GitHub repository URL (repo contains skeleton + `projects/farm-profit/brief.md`) submitted via Lamaku
**Due:** end of Week 1 — exact dates on the course calendar (Mini 1 spans Weeks 1–2, Aug 24–Sep 4)

> **Status:** Kumu-authored draft (2026-07-31) — pending Adam's review before students see it.

---

## Overview

Two things happen in this stage, and both are deliberately small: you stand up a **public GitHub portfolio repo**, and you write a one-page **brief** stating the farm problem in your own words — including a hypothesis about the answer *before you've run anything*.

The repo is not busywork. It accretes across all three minis and the Policy Shock project — every artifact you produce this semester lands in it, and by December it's a public, version-controlled record of your work that an employer can actually read. Stand it up now, before any analytical work begins, and the tooling never blocks you again.

The brief matters for a different reason: a hypothesis written *before* Solver runs is falsifiable. One written after is a summary. Stage 1c asks you to compare what you expected against what the model found — that comparison only exists if you commit to a guess now.

We walk through repo setup at the in-class kickoff; DLEMBA students get a screencast kickoff instead — same steps, same deliverables.

> **Never used GitHub before?** This doc is the on-ramp — it's enough. For deeper coverage of anything below (first commit, larger files, troubleshooting), the full reference is [`docs/guides/github-mba-guide.md`](../../../../../docs/guides/github-mba-guide.md) in the course repo. Keep it open in another tab; don't read it cover-to-cover.

---

## The four steps

| Step | What you do | Time |
|------|-------------|------|
| **1** | Create a GitHub account | 5 min |
| **2** | Install GitHub Desktop | 10 min |
| **3** | Create your public repo + minimal skeleton | 15 min |
| **4** | Write `projects/farm-profit/brief.md` and push it | 30–45 min |

---

## Step 1 — Create a GitHub account

1. Go to [github.com](https://github.com) and click **Sign up**.
2. **Use your `@hawaii.edu` email.** It makes you eligible for [GitHub Education](https://education.github.com) — free GitHub Pro, free Copilot, instant approval in most cases.
3. **Choose a professional username.** This is effectively a second business card — reviewers, managers, and admissions committees will see it. Good: `firstname-lastname`, `flastname`. Avoid gamer tags, joke names, anything you wouldn't put on a resume.
4. Verify your email, and (recommended) upload a profile photo so your instructor can recognize you on the platform.

## Step 2 — Install GitHub Desktop

We use **GitHub Desktop** — a free visual app that handles clone, commit, and push through buttons. No terminal, no command line, ever.

1. Download from [desktop.github.com](https://desktop.github.com) and run the installer (Windows auto-installs Git in the background; Mac: drag to Applications).
2. On first launch, **sign in** with the account from Step 1.
3. Confirm your **Git config** — real name, `@hawaii.edu` email. These get stamped on every commit.

If you're already comfortable with the Git CLI, use it — the deliverable is identical either way.

## Step 3 — Create your repo + minimal skeleton

### 3a. Create the repo on GitHub

1. On [github.com](https://github.com): **+** (top-right) → **New repository**.
2. **Name it after *you*, not this course:** `firstname-lastname` (or `firstname-lastname-portfolio` if taken). This repo outlives BUS 620 — all three minis, the Policy Shock project, and later courses land here. Name it for the person.
3. **Visibility: Public.** Non-negotiable — a portfolio nobody can see isn't one.
4. Check **Add a README file** (an empty repo can't be cloned).
5. Click **Create repository**.

### 3b. Clone it locally

In GitHub Desktop: **File → Clone repository → GitHub.com tab** → pick your new repo → choose a local folder (e.g., `Documents/GitHub/`) → **Clone**.

### 3c. Build the skeleton

Keep it minimal — this is a portfolio scaffold, not an org chart:

```
firstname-lastname/
├── README.md            # ← short professional bio (3–6 sentences)
├── .gitignore           # ← Office/OS junk filter (Step 3d)
└── projects/
    └── farm-profit/
        └── brief.md     # ← Step 4
```

Replace the auto-generated `README.md` with a short bio: who you are, background, what you're working toward. 3–6 sentences is plenty — it will evolve all semester. Drafting it with an LLM is fine; committing generic filler is not.

### 3d. Add a `.gitignore`

Excel and your OS both spawn hidden temp files you do **not** want in your history — and once junk lands in commits, getting it out is painful. Before your first workbook commit (Stage 1b), create a file named `.gitignore` at the repo root (the leading dot is required; on Windows, save it from a text editor with quotes around the name: `".gitignore"`) containing:

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

If you ever see `~$farm-model.xlsx` in GitHub Desktop's Changes panel, your `.gitignore` is missing or misnamed — re-check.

### 3e. Commit and push

In GitHub Desktop: your new files appear in the **Changes** panel → write a summary (`Add skeleton and gitignore` — descriptive, not `update`) → **Commit to main** → **Push origin**. Refresh the repo on github.com and confirm everything is there.

## Step 4 — Write the brief

Create `projects/farm-profit/brief.md`. Read the [case README](README.md) first — the scenario, the assumptions table, the constraints. Then, **before touching Solver or the workbook**, write roughly half a page to a page:

1. **The problem in your own words.** What is the farm deciding, what's fixed, what's chosen, what limits the choice? If you can't state it without re-reading the case, you don't have it yet.
2. **Your hypothesis:** *"I expect the optimal mix to be X because Y."* Actual numbers — beds of tomatoes, carrots, mesclun — and actual reasoning (prices? labor intensity? the diminishing-returns percentages? the bed caps?). You will not be graded on being *right*; you will be graded on whether the guess is genuine and the reasoning is economic. "I expect a balanced mix because diversification" earns nothing.

Commit and push it: `Add farm-profit brief with hypothesis`.

**AI note for this stage:** AI may critique your reasoning or explain concepts from the case — it may not write the brief. The hypothesis has to be yours; a hypothesis you didn't generate can't be honestly compared against results in Stage 1c.

---

## What to submit

Submit your repo URL via Lamaku. The repo must contain:

- [ ] Public visibility (URL opens without logging in)
- [ ] `README.md` with a short professional bio
- [ ] `.gitignore` covering Office/OS temp files
- [ ] `projects/farm-profit/brief.md` — problem restatement + genuine "X because Y" hypothesis
- [ ] At least 2 commits with descriptive messages

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit — a sharper hypothesis, a real bio, a fixed `.gitignore` — can move your score up; the full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (3 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| Repo live + public, professionally named | 1 | URL works without login; `firstname-lastname` naming; bio README isn't placeholder text |
| Skeleton + `.gitignore` + commit hygiene | 1 | `projects/farm-profit/` in place; junk files filtered; ≥2 descriptive commits |
| Brief quality — genuine hypothesis | 1 | Problem restated accurately in your own voice; hypothesis names a specific mix with economic reasoning, written before any Solver work |

---

## Tips

- **Don't polish the bio.** It evolves all semester — Stage 1a is about getting the repo live.
- **A wrong hypothesis is a good hypothesis.** The gap between your guess and Solver's answer is the raw material for Stage 1c. The only bad hypothesis is a hedged one.
- **Commit messages are graded habit.** Not `update` or `stuff` — say what changed: `Add brief: predicting tomato-heavy mix on price per bed`.
- **Stuck on setup?** The [MBA GitHub guide](../../../../../docs/guides/github-mba-guide.md) covers every failure mode we've seen; check it before emailing.
