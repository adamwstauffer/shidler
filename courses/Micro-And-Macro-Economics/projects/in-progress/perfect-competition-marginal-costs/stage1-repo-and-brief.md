# Case 1 · Stage 1 — Repo + Brief

**Case weight:** 10% of course grade — this stage: 3 of 20 pts
**Format:** Upload-only — no presentation component
**Deliverable:** Public GitHub repository URL (repo contains the portfolio skeleton + `docs/briefs/perfect-competition-brief.md`) submitted via Lamaku
**Due:** end of Week 1 — exact dates on the course calendar (Case 1 spans Weeks 1–2, Aug 24–Sep 4)

---

## Overview

You are a farmer on a 1.5-acre market garden, and in a few weeks you have to commit the whole season to a planting plan you cannot undo. Over the next two weeks you will work out what that plan should be — and you will document it the way a consultant documents work for a client who has to live with the answer, because that client is your own operation. Everything you produce lands in one place: a **public GitHub portfolio repo** that you stand up in this stage and never rebuild.

Two things happen here, and both are deliberately small: the repo goes live, and you write a one-page **engagement brief** stating the problem in your own words — including a hypothesis about the answer *before you have run anything*.

The repo is not busywork, and it is not a course folder. It is structured the way a working analyst's practice is structured — **capabilities you can do**, and **engagements that prove you did them** — so it keeps working after this class, after this degree, and into a job. Three engagements this semester land in it; so does everything you do in later courses.

The brief matters for a different reason: a hypothesis written *before* Solver runs is falsifiable. One written after is a summary. Stage 3 asks you to compare what you expected against what the model found — that comparison only exists if you commit to a guess now.

We walk through repo setup at the in-class kickoff; DLEMBA students get a screencast kickoff instead — same steps, same deliverables.

> **Never used GitHub before?** This doc is the on-ramp — it's enough. For deeper coverage of anything below (first commit, larger files, troubleshooting), the full reference is [`docs/guides/github-mba-guide.md`](../../../../../docs/guides/github-mba-guide.md) in the course repo, and the [Kumu Start Here page](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics) covers the add → commit → push loop with screenshots. Keep one open in another tab; don't read either cover-to-cover.

---

## The four steps

| Step | What you do | Time |
|------|-------------|------|
| **1** | Create a GitHub account | 5 min |
| **2** | Install GitHub Desktop | 10 min |
| **3** | Create your public repo + portfolio skeleton | 20 min |
| **4** | Write `docs/briefs/perfect-competition-brief.md` and push it | 30–45 min |

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

## Step 3 — Create your repo + portfolio skeleton

### 3a. Create the repo on GitHub

1. On [github.com](https://github.com): **+** (top-right) → **New repository**.
2. **Name it after *you*, not this course:** `firstname-lastname` (or `firstname-lastname-portfolio` if taken). This repo outlives BUS 620 — all three engagements, later courses, and work you do after graduation land here. Name it for the person.
3. **Visibility: Public.** Non-negotiable — a portfolio nobody can see isn't one.
4. Check **Add a README file** (an empty repo can't be cloned).
5. Click **Create repository**.

### 3b. Clone it locally

In GitHub Desktop: **File → Clone repository → GitHub.com tab** → pick your new repo → choose a local folder (e.g., `Documents/GitHub/`) → **Clone**.

### 3c. Build the skeleton

This is the structure you keep. Nothing in it is named after a class:

```
firstname-lastname/
├── README.md                 # ← who you are + your index of engagements
├── RESUME.md                 # ← Markdown resume; rough is fine on day one
├── AGENTS.md                 # ← your AI conventions (canonical)
├── CLAUDE.md                 # ← one line: "See AGENTS.md."
├── prompt-log.md             # ← running record of AI sessions that mattered
├── .gitignore                # ← Office/OS junk filter (Step 3d)
├── skills/                   # ← THE QUIVER: one folder per capability (Stage 2 fills the first)
├── docs/
│   ├── briefs/               # ← BEFORE the work: scope + hypothesis
│   │   └── perfect-competition-brief.md   # ← Step 4
│   └── decisions/            # ← AFTER the work: recommendations to an audience
└── analysis/                 # ← findings + figures/ (Stage 3 fills these)
```

Two distinctions make the whole thing legible, and they are worth ten seconds each:

- **Briefs ask; memos answer.** `docs/briefs/` holds the engagement letter you write before you know anything. `docs/decisions/` holds what you hand the client at the end.
- **Skills are capabilities; engagements are evidence.** `skills/marginal-analysis/` (built next stage) is a thing you can *do*. `docs/`, `analysis/`, and `data/` hold the work that proves you did it. Each skill folder's README names the engagements that exercised it — that link, claim to proof, is the line a reader actually follows.

**About `skills/` vs `.claude/skills/`:** top-level `skills/` is *your* word, the one that goes on a resume — capabilities, written for humans. `.claude/skills/` is a tool-specific folder some AI tools read; you may create it and experiment freely, and nothing in this course grades it. They look similar on purpose: a capability folder is close enough to that convention that you can drop one in later almost unchanged.

Replace the auto-generated `README.md` with a short professional bio — who you are, background, what you're working toward. 3–6 sentences is plenty, and it evolves all semester. Below it, start an **engagement index**: a short list linking each piece of work to its brief, analysis, and memo. That index is the by-subject view of your repo; it lives in the README, never in the folder paths.

`CLAUDE.md` is literally one line: `See AGENTS.md.` One source of truth, two filenames.

`AGENTS.md` is where you write down how you want AI to work with you. A workable start — edit until it's yours:

```markdown
# AI conventions

## How I work
- Explain concepts fully; walk the worked example. Don't hand me conclusions.
- Critique my reasoning hard. I'd rather be corrected than agreed with.

## Boundaries
- You may explain, critique, debug, and quiz me.
- You may NOT write my briefs, analyses, memos, or reflections.
- Every statistic or figure you give me is a draft until I verify it against a source.

## Records
- Sessions that mattered go in prompt-log.md: date, tool, what I asked,
  what I got, what I did with it.
```

Drafting the bio, resume, or `AGENTS.md` with an LLM is fine; committing generic filler is not.

> Git will not track an empty folder. To create `skills/` and `analysis/` now, drop a one-line `README.md` in each (`Capability folders live here.`) — or wait and create them in Stages 2 and 3, when they get real contents. Either is fine.

### 3d. Add a `.gitignore`

Excel and your OS both spawn hidden temp files you do **not** want in your history — and once junk lands in commits, getting it out is painful. Before your first workbook commit (Stage 2), create a file named `.gitignore` at the repo root (the leading dot is required; on Windows, save it from a text editor with quotes around the name: `".gitignore"`) containing:

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

If you ever see `~$model.xlsx` in GitHub Desktop's Changes panel, your `.gitignore` is missing or misnamed — re-check.

### 3e. Add your instructor as a collaborator

The repo is public, so anyone can read it. Collaborator access is a different thing: it lets me push a review branch or open a pull request against your work instead of emailing you a paragraph.

On your repo page: **Settings → Collaborators → Add people** → add **`adamwstauffer`**. The invitation shows as pending until it's accepted; you don't need to wait on it.

### 3f. Commit and push

In GitHub Desktop: your new files appear in the **Changes** panel → write a summary (`Add portfolio skeleton and gitignore` — descriptive, not `update`) → **Commit to main** → **Push origin**. Refresh the repo on github.com and confirm everything is there.

## Step 4 — Write the brief

Create `docs/briefs/perfect-competition-brief.md`. Read the [case README](README.md) first — the scenario, the assumptions table, the constraints. Then, **before touching Solver or the workbook**, write roughly half a page to a page:

1. **The problem in your own words.** What is the farm deciding, what's fixed, what's chosen, what limits the choice? If you can't state it without re-reading the case, you don't have it yet.
2. **Your hypothesis:** *"I expect the optimal mix to be X because Y."* Actual numbers — beds of tomatoes, carrots, mesclun — and actual reasoning (prices? labor intensity? the diminishing-returns percentages? the bed caps?). You will not be graded on being *right*; you will be graded on whether the guess is genuine and the reasoning is economic. "I expect a balanced mix because diversification" earns nothing.

Commit and push it: `Add perfect-competition brief with mix hypothesis`.

**AI note for this stage:** AI may critique your reasoning or explain concepts from the case — it may not write the brief. The hypothesis has to be yours; a hypothesis you didn't generate can't be honestly compared against results in Stage 3.

---

## What to submit

Submit your repo URL via Lamaku. The repo must contain:

- [ ] Public visibility (URL opens without logging in)
- [ ] `README.md` with a short professional bio + the start of an engagement index
- [ ] `AGENTS.md` with your own conventions, and `CLAUDE.md` pointing at it
- [ ] `.gitignore` covering Office/OS temp files
- [ ] `docs/briefs/perfect-competition-brief.md` — problem restatement + genuine "X because Y" hypothesis
- [ ] `adamwstauffer` invited as a collaborator
- [ ] At least 2 commits with descriptive messages

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit — a sharper hypothesis, a real bio, a fixed `.gitignore` — can move your score up; the full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (3 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| Repo live + public, professionally named | 1 | URL works without login; `firstname-lastname` naming; bio README isn't placeholder text |
| Skeleton + `.gitignore` + commit hygiene | 1 | `docs/briefs/` in place and the root files present (`AGENTS.md`, `CLAUDE.md`, `RESUME.md`, `prompt-log.md`); junk files filtered; ≥2 descriptive commits |
| Brief quality — genuine hypothesis | 1 | Problem restated accurately in your own voice; hypothesis names a specific mix with economic reasoning, written before any Solver work |

---

## Tips

- **Don't polish the bio.** It evolves all semester — Stage 1 is about getting the repo live.
- **A wrong hypothesis is a good hypothesis.** The gap between your guess and Solver's answer is the raw material for Stage 3. The only bad hypothesis is a hedged one.
- **Commit messages are graded habit.** Not `update` or `stuff` — say what changed: `Add brief: predicting tomato-heavy mix on price per bed`.
- **Name files for the engagement, not the week.** `perfect-competition-brief.md` will still make sense to a stranger in three years. `week1.md` won't.
- **Stuck on setup?** The [MBA GitHub guide](../../../../../docs/guides/github-mba-guide.md) covers every failure mode we've seen; check it before emailing.
