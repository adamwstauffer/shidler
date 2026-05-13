---
title: "GitHub Guide for MBA Students"
audience: Students (BUS 629 VEMBA and other Shidler courses with portfolio repos)
status: required reading for Stage 0–5 GitHub mechanics
last_updated: 2026-05-13
related:
  - claude-code-install-for-non-technical-users.md
  - student-ai-enhancements.md
---

# GitHub Guide for MBA Students
## Forks, Commits, Branches, Pull Requests, and Collaboration

### Purpose

GitHub is a collaboration platform for managing files, code, data, documentation, and project work. For MBA students, think of GitHub as:

> Google Docs version history + project management + formal change approval + public/professional portfolio.

This guide is a complete walkthrough — from creating your first account to responding to instructor feedback on a pull request. Read Section 1 (vocabulary) once, then jump to the section you need. No prior technical experience assumed.

---

# 1. Core Vocabulary

## Repository, or "repo"

A repository is the project folder. It can contain code, spreadsheets, data files, notes, assignments, documentation, images, or a website.

Example:

    mba-currency-crisis-project/
      README.md
      data/
      analysis/
      charts/
      final-report.md

---

## Commit

A commit is a saved checkpoint.

Plain English:

> A commit is like saying: "Save this specific set of changes, label it, and keep it in the history forever."

Good commit messages:

    Add exchange rate data for Thailand
    Fix typo in executive summary
    Update README with project instructions
    Add charts for currency crisis analysis

---

## Branch

A branch is a separate workspace inside a repository.

Plain English:

> A branch is a "safe copy of the work-in-progress area."

---

## Main branch

The `main` branch is usually the official version of the project.

---

## Fork

A fork is your own copy of someone else's repository.

Plain English:

> A fork is like making your own editable copy of someone else's project.

---

## Pull Request, or PR

A pull request is a formal proposal to merge your changes into another branch or repo.

Plain English:

> A pull request says: "Here are my changes. Please review them and decide whether to accept them."

---

# 2. The Big Picture

## Simple workflow

Edit → Commit → Push

## External contributor workflow

Fork → Branch → Commit → Pull Request

---

# 3. Key Takeaway

If you own the repo:

branch → commit → pull request → merge

If you do not own the repo:

fork → branch → commit → pull request

---

# 4. From zero: create your GitHub account and your first repo

*If you've already completed Stage 0 (created a portfolio repo), skip to Section 5.*

## Step 1 — Create a GitHub account

Go to [github.com](https://github.com) and click **Sign up**. Use a **professional username** — this name appears on every commit you make and is visible to anyone who looks at your repos. It is part of your professional identity for the rest of your career.

| Good usernames | Avoid |
|---|---|
| `firstname-lastname`, `lastname-firstname`, `flastname`, `firstinitiallastname` | `tigerfan99`, your favorite band, inside jokes, anything you wouldn't put on a resume |

Verify your email after sign-up. Without verification you can't make commits.

## Step 2 — Create your portfolio repo

From your GitHub home page:

1. Click the **+** icon (top-right) → **New repository**.
2. **Repository name:** `Corporate-Finance` (or another professional name appropriate to the course).
3. **Description:** one sentence — e.g., *"AI-assisted ratio analysis and corporate-finance portfolio for Shidler BUS 629."*
4. **Visibility:** **Public.** Your repo is a portfolio piece you'll share with recruiters and on LinkedIn.
5. **Initialize with:** check `README`, `.gitignore` (pick any template from the dropdown — `Node` is a safe default), and `LICENSE` (MIT recommended).
6. Click **Create repository**.

You now have a repo at `https://github.com/{your-username}/Corporate-Finance` with three files (README.md, .gitignore, LICENSE).

## Step 3 — Make your first edit (in the browser)

The web UI is the simplest path for a one-off edit:

1. On your repo page, click `README.md`.
2. Click the **pencil icon** (top-right of the file view).
3. Replace the placeholder text with two or three sentences about who you are and what's in this repo.
4. Scroll down to the **Commit changes** panel.
5. Commit message: *"Update README with portfolio overview"*.
6. Choose **Commit directly to the main branch**.
7. Click **Commit changes**.

You just made your first commit. The repo now shows two entries in its commit history.

---

# 5. Pick a lane: the three ways to commit

Once your repo exists, you can edit and commit files three different ways. **Pick one and stick with it.** Mixing them creates confusion (different tools, different defaults, different error messages).

| Lane | Best for | Setup time | Daily friction | Visual? |
|---|---|---|---|---|
| **GitHub web UI** | Editing a single file occasionally | 0 min | Slow for many changes | Yes (in browser) |
| **GitHub Desktop** ⭐ recommended | All-around use; never used Git before | 10 min | Lowest | Yes (desktop app) |
| **Git CLI** (terminal) | Students who already use Claude Code or are comfortable in a terminal | 30+ min | Highest, but most powerful | No |

**Strong recommendation: GitHub Desktop.**

It's a free desktop app from GitHub that shows your repo as a graphical interface — file changes appear as a list, commits are buttons, branches are dropdowns. It hides Git's complexity behind clear English. If you've never used Git, this is the lane.

**Pick the CLI if and only if** you already have Claude Code installed (see [`claude-code-install-for-non-technical-users.md`](claude-code-install-for-non-technical-users.md)). Claude Code runs in the same terminal as Git, so you'd already be there.

**The web UI is fine** for occasional one-off edits — quick fixes to a README, dropping in a new memo. It becomes tedious for multi-file work.

---

# 6. Your first commit using GitHub Desktop (~15 min)

This is the GitHub Desktop walkthrough. Use it if you picked that lane in Section 5.

## Step 1 — Install GitHub Desktop

1. Go to [desktop.github.com](https://desktop.github.com) → **Download for {Windows / macOS}**.
2. Run the installer with default settings.
3. Open GitHub Desktop. Sign in with the GitHub account you created in Section 4.

## Step 2 — Clone your repo to your computer

1. **File → Clone repository**.
2. Pick your portfolio repo from the list (it appears because you're signed in).
3. **Local path:** accept the default (typically `~/Documents/GitHub/{repo-name}` on Mac or `C:\Users\YourName\Documents\GitHub\{repo-name}` on Windows) or pick a folder you'll remember.
4. Click **Clone**.

GitHub Desktop downloads your repo and opens it. You can now see the repo folder in your file explorer.

## Step 3 — Make a change

1. Open your file explorer (Finder on Mac, File Explorer on Windows) and navigate to the repo folder.
2. Open `README.md` in your text editor (TextEdit, Notepad, VS Code, or any plain-text editor — **not Word**, which adds invisible formatting).
3. Edit and save.

## Step 4 — Commit and push

1. Return to GitHub Desktop.
2. The left pane now shows your edited file under **Changes**. Click it to see the diff (red = removed, green = added).
3. At the bottom-left, type a summary in **Summary (required)** — e.g., *"Update README"*.
4. Click **Commit to main**.
5. At the top, click **Push origin** to send your commit to GitHub.

Verify by visiting your repo on github.com — your change is there with your commit message.

**That's the full edit → commit → push loop in GitHub Desktop.** You'll repeat it dozens of times this semester.

---

# 7. Adding a collaborator (granting the instructor Write access)

**Required for Stage 2 onward.** The instructor opens pull requests with feedback on your work; PRs can't happen without Write access. Stage 5 grades 5% on how you incorporated PR feedback — that 5% is unearnable without this step.

## Step 1 — Open your repo's settings

1. Go to your repo page on github.com.
2. Click the **Settings** tab (top-right of the repo navigation — you may need to scroll the tab row right).

## Step 2 — Open the Collaborators panel

1. In the left sidebar, under **Access**, click **Collaborators**.
2. GitHub may ask you to re-enter your password — type it.

## Step 3 — Add the instructor

1. Click **Add people**.
2. Type the instructor's GitHub handle: **`adamwstauffer`**
3. Select the entry that appears in the dropdown (verify it's the right one — full name "Adam Stauffer").
4. Choose role: **Write**. **Not** Read (instructor can't open PRs), **not** Maintain (more than needed), **not** Admin (way too much). Write is exactly right.
5. Click **Add adamwstauffer to this repository**.

## Step 4 — Confirm acceptance

The instructor receives an email invitation and must accept it. **Until accepted, no PRs can be opened.**

To check status:

- Return to **Settings → Collaborators**.
- You should see `adamwstauffer` listed with a **Write** role badge and a status of **Active** (not **Pending**).
- If still **Pending** after a few days, follow up via email (subject line: `BUS 629 — instructor write access pending`).

## Common slip

Some students grant **Read** by accident (it's the default in the dropdown). The instructor can see the repo but cannot open PRs. **The role must be Write.**

---

# 8. Reading and responding to a pull request (PR)

**This section is load-bearing for Stage 5.** PRs are how the instructor delivers feedback on your Stage 2 memo. The Stage 5 rubric grades 5% on how visibly you responded to that feedback.

## How you'll find out a PR was opened

1. GitHub emails you (to the address on your GitHub account).
2. The repo page shows a **Pull requests** tab with a number badge (e.g., `Pull requests 1`).
3. Click **Pull requests** → click the title of the PR.

## The three tabs on a PR

| Tab | What's there | When to look |
|---|---|---|
| **Conversation** | Overall comments, replies, and the merge button | First, to read the high-level summary; last, to merge |
| **Commits** | The list of changes the instructor is proposing (often empty if the instructor only wrote comments) | If you want to see what's actually being changed |
| **Files changed** | Line-by-line diff with inline comments attached to specific lines | **This is where most feedback lives.** Spend the most time here |

## Three kinds of comment you'll see

| Comment style | What it looks like | How to respond |
|---|---|---|
| **General comment** | A paragraph in the Conversation tab without a line attached | Reply in the Conversation tab. State whether you'll act on it. |
| **Inline comment** | A speech-bubble icon attached to a specific line in **Files changed**; the comment text appears under that line | Click **Reply** on that line. State whether you accepted, rejected, or modified the suggestion. |
| **Suggested change** | An inline comment with a code/text block marked **Suggestion** and a green **Commit suggestion** button | One click accepts the change as a new commit. Or reply and write your own version. |

## How to accept a suggested change

If the instructor proposes "Change `growing market` to `growth-stage market`" via a suggestion block:

1. On that line in **Files changed**, click **Commit suggestion**.
2. Optional: edit the commit message (e.g., *"Tighten hypothesis 2 per instructor PR comment #3"*).
3. Click **Commit changes**.

GitHub adds the change as a new commit on the PR branch. The commit ends up in your repo history.

This is the fastest path. **It also leaves a clear audit trail** — the rubric explicitly rewards commit messages that reference PR comments.

## How to modify a suggested change

If the instructor's suggestion is close to what you want but not quite right, type a reply with your own version:

1. Reply to the comment with your alternative phrasing.
2. Manually make the edit to the file (via web UI, GitHub Desktop, or CLI — whichever lane you picked).
3. Push the commit.
4. Mention the commit hash in your reply (e.g., *"Done in commit `a3f9c12` — kept the company's own 10-K phrasing for the second clause."*).
5. Click **Resolve conversation** on the comment thread.

## How to reject a suggested change

**You are allowed to disagree with the instructor.** Stage 5's rubric explicitly says: *"If you received feedback and disagreed with it, that is fine — but the disagreement must be visible."*

To reject:

1. Reply in the comment thread with **one or two sentences** explaining why you kept the original. Examples:
    - *"Holding the original framing — `growing market` is the language used in the company's own 10-K, and matching that wording is intentional."*
    - *"Disagreeing on this one. The revised hypothesis you suggested narrows the scope to consumer staples; I'm keeping the multi-sector framing because the memo's whole point is sector-comparison."*
2. Click **Resolve conversation** so it's clear you addressed it (not ignored it).

**Silence is worse than disagreement.** The rubric reads silence as oversight, not judgment.

## How to merge the PR (when you're done)

After you've responded to every comment:

1. Click the **Conversation** tab.
2. Scroll to the bottom.
3. Click the green **Merge pull request** button.
4. Optional: edit the merge commit message to summarize what changed (e.g., *"Apply Stage 2 instructor feedback — tighten hypotheses, fix citation, hold scope per reply"*).
5. Click **Confirm merge**.

Your repo's `main` branch now contains all the changes. The PR is closed.

## Tracking your responses for the rubric

Stage 5 grades "visible response" to PR feedback. After merging, write a one-line note in your final analysis (or in your prompt log) that points the grader at the evidence:

> *"Stage 2 PR feedback (commits `abc1234`, `def5678`) tightened hypothesis 2 and corrected the source citation in para 4. PR comment #3 (re-scope to one industry) was held — see the reply on that thread for the rationale."*

**That single sentence is worth more than a thousand-word reflection.** It points the grader at the evidence and shows you read every comment. The rubric grades visibility, not effort.

If your scope/framing changed substantially based on the feedback, you can also ship a `docs/decisions/YYYY-MM-DD-{lastname}-stage2-feedback-response.md` memo describing the change — but the in-PR comments + commit-message references are usually enough.

---

# 9. Working with larger files (.xlsx, .pdf, .png)

GitHub has a **50 MB soft limit** and a **100 MB hard limit** per file. For this course, every artifact is well under those limits — the populated workbook from Stage 3 is typically 100–500 KB, the spec at Stage 4 is < 50 KB, slides are 1–5 MB. **You will not need Git LFS** (a paid add-on for very large files).

Two gotchas show up regardless:

## Gotcha 1 — Excel temp files

When you have a workbook open in Excel, Excel creates a hidden file alongside it named `~$YourFile.xlsx`. If you commit this file by accident, GitHub Desktop will show "Working tree has changes" every time you open the workbook. It's harmless but noisy.

**Fix:** add a `.gitignore` file at the root of your repo (if it doesn't already exist) with these contents:

    ~$*.xlsx
    ~$*.xls
    ~$*.docx
    .DS_Store
    *.tmp
    Thumbs.db

GitHub Desktop will respect this automatically and stop showing those files in the **Changes** pane.

If your repo was initialized with a `.gitignore` template in Section 4, you already have a file at the root — just append the lines above to it.

## Gotcha 2 — The first commit of a workbook is slower

If your Stage 3 workbook is 1–2 MB, the **first** push of that file may take 30–60 seconds on a slow connection. This is normal. Subsequent pushes are fast because Git only transfers the changed bytes, not the whole file.

If a push is taking more than **5 minutes** with no apparent progress, cancel it (in GitHub Desktop click **Cancel push**; in the CLI press Ctrl-C) and check your internet connection.

## Gotcha 3 — A file accidentally pushed that shouldn't be there

If you committed a sensitive file (e.g., a draft with personal info) or a huge binary that shouldn't be in version control, **don't panic** — but **don't just delete and re-commit either**. Git keeps the old version in history.

The clean fix involves rewriting history (`git filter-repo` or BFG) which is risky to do by hand. Paste your situation into [claude.ai](https://claude.ai):

> *"I accidentally committed a file called `private-notes.md` to a public GitHub repo and pushed it. I want to remove the file AND its history so it's not visible. What's the safest way to do this?"*

Claude will walk you through it. Don't improvise — it's the kind of operation where a wrong command can lose work.

---

# 10. Common gotchas

| Symptom | Likely cause | Fix |
|---|---|---|
| "Updates were rejected because the remote contains work that you do not have locally" | Someone else (or another machine of yours) pushed to your repo since you last pulled | In GitHub Desktop: click **Fetch origin**, then **Pull origin**, resolve any conflicts the dialog shows, then push again |
| Your name shows up wrong in commits (or `[no email]`) | Git is configured with a stale or empty username/email | GitHub Desktop → **Preferences / Settings** → **Git** → set **Name** and **Email** to match your GitHub account |
| You accidentally committed a file you didn't mean to (e.g., a Word temp file) | Missing `.gitignore` entry | Add the pattern to `.gitignore` (see Section 9), then in GitHub Desktop right-click the file → **Discard changes** before the next commit |
| You can't push because of "credentials" or "authentication failure" | First-time push from a new machine | GitHub Desktop prompts you to sign in via the browser — sign in, return to Desktop, retry |
| The instructor can't see your repo | Repo is private | Repo **Settings** → scroll to **Danger Zone** → **Change repository visibility** → **Public** |
| The instructor opened a PR but you can't find it | You missed the email notification | Visit your repo on github.com → **Pull requests** tab |
| Your repo on github.com shows old content even though you committed | You committed locally but didn't push | In GitHub Desktop click **Push origin** (or check the top bar — if it says "1 commit to push," that's the issue) |
| You see a screen full of git error text you don't understand | Could be anything | Copy the entire error text, paste into [claude.ai](https://claude.ai), prefix with: *"I'm using GitHub Desktop on {Windows / Mac}. I got this error trying to {what you were doing}. What does it mean and how do I fix it?"* |

---

# 11. Where to go next

- **Never installed Claude Code?** See [`claude-code-install-for-non-technical-users.md`](claude-code-install-for-non-technical-users.md).
- **Want to try a Claude Skill or a finance plugin?** See [`student-ai-enhancements.md`](student-ai-enhancements.md).
- **Need help on a specific git error?** Copy the full error text into [claude.ai](https://claude.ai) and ask: *"I'm using GitHub Desktop (or the web UI / the terminal). I got this error. What does it mean and how do I fix it?"* Claude is excellent at diagnosing git errors and will give you a step-by-step fix.

The single best habit for the semester: **commit small, commit often, write a clear commit message every time.** A repo with 30 small commits, each labeled meaningfully, is a better portfolio artifact than one with 3 giant commits labeled `wip`.
