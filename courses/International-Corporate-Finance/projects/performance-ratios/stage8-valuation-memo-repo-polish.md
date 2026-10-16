---
template: stage-brief
project: performance-ratios
stage: 8
title: "Valuation Memo & Repo Polish"
capability: valuation
deliverables:
  - path: "docs/decisions/YYYY-MM-DD-{company-slug}-valuation-memo.md"
    format: markdown
  - path: "README.md"
    format: markdown
  - path: "LICENSE"
    format: text
  - path: ".gitignore"
    format: text
  - path: "prompt-log.md"
    format: markdown
prerequisites: [5, 7]
---

# Stage 8: Valuation Memo & Repo Polish

**Step-by-step on Kumu:** [Stage 8 walkthrough](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage8.html)

**Collaborator penalty:** from Stage 2 on, a stage loses 5 raw points if `adamwstauffer` is not a Write collaborator on your repository at its deadline; fixing it before a stage's deadline lifts the penalty retroactively.

**Format:** Deliverable-only — no in-class presentation
**Deliverable:** A valuation memo in your repo, plus the polished GitHub repo — URL submitted via Lamaku

> **Where this fits in the project.**
> **Input:** Your verified DCF (Stage 7), your Stage 5 analysis, and every artifact from Stages 0–7.
> **Output (this stage):** A one-to-two-page valuation memo at `docs/decisions/YYYY-MM-DD-{company-slug}-valuation-memo.md`, and the polished repo itself, its public URL submitted on Lamaku.
> **Used by:** You. The repo is your portfolio piece — share the URL on LinkedIn.

> **About the GitHub-vs-Lamaku question.** Stage 8's deliverable **is** the GitHub repo URL — the repo itself is the artifact. Lamaku is only used to submit the URL pointer. The Lamaku fallback available at earlier stages (memo, workbook, spec uploaded directly) does **not** apply at Stage 8: by this point, all prior-stage artifacts must be consolidated into your public GitHub repo. The polish rubric assumes the full project history lives in the repo. If you used Lamaku for any earlier stage, push those artifacts to the repo before the Stage 8 deadline.

> **Unfamiliar terms?** "PR," "commit history," "named range," "spec," and other recurring terms are defined in the [Project glossary in the BUS-629 README](../../BUS-629-VEMBA/README.md#project-glossary).

---

## Overview

The capstone. Two things happen at this stage:

1. **Write the valuation memo.** Is the market price of your company's shares above or below what the company is worth, by how much, and what does that verdict hang on?
2. **Polish your repository** so the whole project — ratios and valuation — stands as a professional artifact you'd link from your LinkedIn.

Stage 8's deliverable is the repo URL itself — its final state *is* the work product.

## Why this is the capstone

Stages 6 and 7 produced a number and checked it. A number is not a decision. A board does not need to know the value per share to four digits; it needs to know whether the market price is above or below it, how far, and which single input would flip the answer. That is judgment — the part an agent cannot take responsibility for.

The repo polish component recognizes a separate truth: a portfolio artifact a manager, audit reviewer, or future collaborator can find is worth more than a perfect analysis stuck in a personal Dropbox.

---

## Part A — Valuation memo

**File:** `docs/decisions/YYYY-MM-DD-{company-slug}-valuation-memo.md` — all lowercase, hyphen-separated, no last name. Use the repo memo template ([`templates/memo-template.md`](../../../../templates/memo-template.md)) and keep its YAML frontmatter intact.

**Length and audience.** One to two pages, written to the company's board — concise, decision-oriented, evidence-tight. In your voice: the verdict is yours, not the model's and not an LLM's.

### Required content

1. **Intrinsic value against market price.** Your model's value per share beside the market price, and the gap as a percentage of the market price. State the **date and source** of the price (the exchange, the company's investor-relations page, a market-data site), in the currency the shares trade in. You may use `share_price` from your workbook (the fiscal-year-end close) or a more recent close; if you use a recent one, say why and give the fiscal-year-end figure beside it.
2. **The beta × terminal growth sensitivity table.** Beta on one axis, terminal growth rate (g) on the other, an **odd number** of rows and columns (5 × 5 is typical) so there is a true center. Every cell holds value per share, in the same unit as the market price. The **center cell equals your model's value per share** — highlight it. If it does not equal the model, the table is wrong. Build the table from the model (the Stage 6 skill should produce it); paste or reproduce it in the memo.
3. **The flip point, as a number.** Read the table: at what beta (holding g at your base case), or what g (holding beta), does your value per share equal the market price — the point where the verdict flips? Give the number, not "somewhat higher". Interpolate between cells if you have to, and say so.
4. **The one input the verdict hangs on.** Name it, say where its value came from (the named range or the cited source), how confident you are in it, and what the board should find out before acting on the valuation.
5. **What the skill got wrong — and what you would never let it decide alone.** One paragraph drawing on your Stage 6 annotated diff and your Stage 7 audit and verification: where the published skill would have mis-valued your company, and which decision in a valuation you would keep for a human no matter how good the agent gets.

The verdict must follow from the model and the table, not from the market price. If your value is close to the price, say that the table cannot distinguish them, and why.

### Draft first, then use an LLM to review

Draft the memo yourself first and commit the draft — that commit is your evidence of the first draft. Then ask an LLM to review it, not rewrite it:

```
Here is my valuation memo and the sensitivity table from my DCF. Review the memo
against these requirements: value per share against a dated, sourced market
price, with the gap as a percentage; an odd-sized beta × terminal growth table
whose center equals the model's value; the flip point stated as a number; one
named input the verdict hangs on, with its source; a paragraph on what the skill
got wrong. For each problem, quote the line and say what is wrong. Check every
number in the memo against the table. Don't rewrite the memo.

[PASTE MEMO AND TABLE HERE]
```

Work through the review one point at a time and revise the memo yourself; reject points you disagree with. Log the sessions in `prompt-log.md` (repository root).

---

## Part B — Repo polish

By Stage 8, your repo should look like a professional portfolio artifact. **Budget 2–3 hours** for this pass — most of the time is per-directory READMEs and the commit-history cleanup, not the README itself. Don't leave this for the night before.

### Target directory hierarchy

Use this as your reference. A polished Stage 8 repo should look like this (filenames will reflect your own company):

```
firstname-lastname/                         (your portfolio repo root)
├── README.md                               # Project overview, status, "what you'll find here"
├── RESUME.md                               # Your resume (from Stage 0)
├── LICENSE                                 # MIT or Apache-2.0
├── .gitignore                              # Excludes .DS_Store, ~$*.xlsx, *.tmp, etc.
│
├── .claude/
│   └── skills/
│       ├── README.md
│       ├── performance-ratios/SKILL.md                        # Stage 1 (unmodified)
│       ├── dcf-model/                                         # Stage 6 (baseline + your edits, LICENSE)
│       └── audit-xls/                                         # Stage 6 (unmodified, LICENSE)
│
├── docs/
│   ├── README.md                           # Explains what's in docs/
│   └── decisions/
│       ├── README.md
│       ├── YYYY-MM-DD-{company}-selection-memo.md             # Stage 2 memo
│       ├── YYYY-MM-DD-{company}-spec-iteration-memo.md        # (optional) Stage 4 HIL note
│       ├── YYYY-MM-DD-{company}-feedback-response-memo.md     # (optional) Stage 5 follow-up
│       └── YYYY-MM-DD-{company}-valuation-memo.md             # Stage 8 memo
│
├── capabilities/
│   ├── performance-ratios/
│   │   ├── README.md
│   │   └── spec.md                                            # Stage 4 spec
│   └── valuation/
│       ├── README.md                                          # Stage 6
│       ├── spec.md                                            # Stage 6 run brief
│       └── model.xlsx                                         # Stage 7 DCF
│
├── models/
│   ├── README.md
│   ├── templates/
│   │   └── performance-ratios-template.xlsx                   # Stage 1 (unmodified)
│   └── builds/
│       └── YYYY-MM-DD-{company}-financials.xlsx               # Stage 3
│
├── analysis/
│   ├── README.md
│   ├── YYYY-MM-DD-{company}-llm-raw-log.md                    # Stage 5 raw LLM output
│   ├── YYYY-MM-DD-{company}-verification-analysis.md          # Stage 5 verification table
│   ├── YYYY-MM-DD-{company}-analysis.md                       # Stage 5 final analysis
│   ├── YYYY-MM-DD-{company}-spec-retrospective-analysis.md    # Stage 5 retrospective
│   ├── YYYY-MM-DD-{company}-dcf-skill-diff-analysis.md        # Stage 6 annotated diff
│   ├── YYYY-MM-DD-{company}-dcf-raw-log.md                    # Stage 7 session log
│   ├── YYYY-MM-DD-{company}-dcf-audit-analysis.md             # Stage 7 audit-xls + verdicts
│   ├── YYYY-MM-DD-{company}-dcf-verification-analysis.md      # Stage 7 manual verification
│   └── validation/
│       ├── README.md                                          # Stage 3 self-audit notes
│       └── YYYY-MM-DD-{company}-identity-checks-log.md        # Stage 3 identity checks
│
└── prompt-log.md                                              # All AI sessions logged (repo root)
```

### Checklist

Before submitting:

- [ ] Top-level `README.md` updated with project status section listing every stage (0 through 8) and its commit hash
- [ ] Top-of-README "what you'll find here" block — one paragraph orienting a manager, reviewer, or peer who just clicked the repo link
- [ ] **One-line repo description** set in the GitHub repo page header (the field at the top of the repo page, not in the README) — summarizes the project in one sentence
- [ ] **`LICENSE` file** at repo root (MIT or Apache-2.0 recommended — pick one, both signal "this is a portfolio piece you may reference")
- [ ] **`.gitignore`** excluding common scratch files (`.DS_Store`, `~$*.xlsx`, `*.tmp`, etc.) — keeps the repo clean
- [ ] Every directory has a `README.md` explaining what's inside
- [ ] All dated filenames follow `YYYY-MM-DD-{company-slug}-{type}.{ext}` (older names already submitted still count)
- [ ] No orphan files, dead links, or `_temp/` directories
- [ ] Commit history is clean (descriptive messages; no `wip` or `asdf` commits)
- [ ] Repo is **public** and accessible without login

### Pro tip — use an LLM to reorganize and clean up your repo

The polish pass is exactly the kind of routine reorganization an LLM is good at. Two approaches depending on which AI tool you're using:

**Option 1 — Claude Code (in your terminal):**

```
cd ~/path/to/your/firstname-lastname
claude
```

Then prompt:

```
Read every file in this repo. Compare the current structure against the Stage 8
target hierarchy in:
https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/International-Corporate-Finance/projects/performance-ratios/stage8-valuation-memo-repo-polish.md

Identify:
1. Misnamed files (not following YYYY-MM-DD-{company}-{slug}-{type} convention; older names with my last name are fine to leave)
2. Files in the wrong directory
3. Missing per-directory READMEs (every folder should have one)
4. Orphan or temp files that should be deleted

For each issue, propose the exact git mv command or git rm command to fix it.
Do NOT run any commands yourself. Print the list of commands so I can review
each one before executing.

After that list, draft per-directory README.md files for any directory missing one.
Use 4–6 sentences each: what's in the directory, naming conventions used, how it
relates to the project stages.
```

**Option 2 — Claude.ai or ChatGPT (web, no install):**

Compress your repo to a `.zip`, upload it to the LLM, and paste:

```
I have uploaded my portfolio repo as a zip. The Stage 8 target structure is
documented at:
https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/International-Corporate-Finance/projects/performance-ratios/stage8-valuation-memo-repo-polish.md

Audit my repo against that target. Produce:
1. A table of every file currently in the repo, with columns: current path |
   correct path | action needed (rename / move / delete / keep)
2. Draft per-directory README.md text for every directory that needs one
3. A list of any missing artifacts (e.g., LICENSE, .gitignore) with suggested
   minimal content I can copy in

Be specific. Do not say "rename inconsistent files" — list the exact files.
```

**What the LLM should NOT do at Stage 8:** Generate the actual analysis content for you, or rewrite your final analysis or valuation memo to "improve" it. The polish pass is about file organization and presentation, not about the analytical substance — that substance is what the rubric is grading.

**Log the prompt** in `prompt-log.md` (repository root). The repo-cleanup conversation is just as logged-worthy as the analytical ones.

---

## What to submit

- [ ] `docs/decisions/YYYY-MM-DD-{company-slug}-valuation-memo.md` — committed first draft, then revisions
- [ ] Every item on the repo polish checklist above
- [ ] `prompt-log.md` updated with the memo review and the repo-cleanup sessions
- [ ] Public repo URL submitted on Lamaku

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — sharpening the memo, fixing the sensitivity table, finishing the repo polish — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (% of Stage 8 score)

| Criterion | % of Stage 8 | What distinguishes strong work |
|-----------|-------------:|--------------------------------|
| Verdict and gap | 20% | Value per share against a dated, sourced market price; the verdict follows from the model and the table, not from the price |
| Sensitivity table and flip point | 20% | Odd-sized beta × g table, center equal to the model; the flip point stated as a number |
| The hinge input | 15% | Named, sourced, with an honest confidence and an actionable next step for the board |
| What the skill got wrong + executive voice | 15% | Specific, drawn from Stages 6–7; names a decision you would keep for a human; the voice is yours |
| Repo polish (structure, READMEs, naming, commits, license, description) | 30% | Repo presents as a professional artifact; no rough edges; polish checklist satisfied |

---

## Tips

- **Lead with the verdict.** The memo's first sentence says whether the shares trade above or below your value, and by how much.
- **The table is the argument.** A verdict that survives every plausible cell is strong; a verdict that flips one cell from the center is a different memo. Say which one you have.
- **Polish the repo last — but not last-night.** Don't let it become an evening-before scramble. Allocate a dedicated commit pass for READMEs, naming, license, and repo description.
- **Update `capabilities/valuation/README.md`** so a visitor can tell, in four sentences, what the valuation is, how it was built, and how it was checked.
