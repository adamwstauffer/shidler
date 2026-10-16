---
template: stage-brief
project: performance-ratios
stage: 1
title: "Provided Ratios Template"
capability: performance-ratios
deliverables:
  - path: "models/templates/performance-ratios-template.xlsx"
    format: xlsx
  - path: ".claude/skills/performance-ratios/SKILL.md"
    format: markdown
prerequisites: [0]
---

# Stage 1: Provided Ratios Template

**Step-by-step on Kumu:** [Stage 1 walkthrough](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage1.html)

**Format:** Upload-only — no presentation component
**Deliverable:** `performance-ratios-template.xlsx` uploaded to your repo, plus the `performance-ratios` skill installed in `.claude/skills/`

---

## Overview

Use the provided Excel ratios template — built by your instructor — as the foundation for the rest of the project. Download it, study its structure, and upload your own copy to your portfolio repo.

You will not modify the template at this stage. The point of Stage 1 is to make sure every student is working from the same architecture and named-range conventions before any company data lands in the model.

## Why we provide the template

Some courses have students design their own templates from scratch, which is a useful exercise for first-time modelers. Here the learning happens further down the pipeline: in *populating* a model under real reporting standards (Stage 3), in *specifying* analytical work precisely enough that an LLM can execute it (Stage 4), in *evaluating* AI-generated analysis against your own judgment (Stage 5), and in *valuing* the company with a professional DCF skill you adapt, run and audit yourself (Stages 6–8). Standardizing the template at Stage 1 protects the time those later stages need.

---

## The provided template

**File:** [`../../templates/spreadsheets/performance-ratios-template.xlsx`](../../../../templates/spreadsheets/performance-ratios-template.xlsx)

**Tabs included:**

| Tab | Contents |
|-----|----------|
| **Cover** | Project overview, how to use the template, and the color legend (yellow = data inputs, blue = assumptions, green = formulas, gray = ratio outputs) |
| **Balance Sheet** | Skeleton with current and prior year columns (`BAL_*`, `startYear_*`) |
| **Income Statement** | Skeleton with line items and named-range placeholders (`INC_*`) |
| **Cash Flow Statement** | Skeleton for operating, investing, financing activities (`CASH_*`, including `CASH_capex` and `CASH_working_capital_change`) |
| **Ratios** | All six categories with formulas pre-filled in named-range notation (`RATIO_*`) — auto-populates once Stage 3 financials are entered |
| **Notes** | Space for your source and method notes |

The Ratios tab is **fully formulaic** — no hardcoded numbers. When you populate the financial statements at Stage 3, ratios compute automatically.

### Two names the valuation stages need

Most `CASH_*` names are subtotals the ratios use. Two more exist for the DCF in Stages 6–8, which needs a base-year free cash flow:

| Name | Points at | Sign convention |
|---|---|---|
| `CASH_capex` | Cash Flow Statement, **Capital expenditures** line | Recorded negative (cash out) |
| `CASH_working_capital_change` | Cash Flow Statement, **Total change in working capital** line | Positive = cash released; a build in working capital is negative |

Check that they are there: open your copy → **Formulas → Name Manager** → both names listed. If they are missing, your copy predates them — download the template again from the link above and replace your copy (it is still blank at this stage, so nothing is lost).

The statement tabs show figures in **the currency and scale you enter on the Notes tab (Units row)** — "VND billion", "EUR million", "USD thousand". Nothing in the template assumes U.S. dollars.

---

## Install the `performance-ratios` skill

A **skill** is a folder of instructions an AI agent (Claude Code, Codex, and others) loads on demand. The `performance-ratios` skill is the workbook's named-range contract: what each name means, which valuation inputs can be derived from the names, and the identity checks any model built on the workbook must pass. You run its checks at Stage 3, and the DCF agent in Stages 6–8 reads the workbook through it.

Install it unmodified at:

```
[your-repo]/.claude/skills/performance-ratios/SKILL.md
```

The source is the sample portfolio repo: [`templates/portfolio/firstname-lastname/.claude/skills/performance-ratios/SKILL.md`](../../../../templates/portfolio/firstname-lastname/.claude/skills/performance-ratios/SKILL.md).

**On github.com (no install needed):**

1. Open the source link above → click **Raw** → select all and copy.
2. In your portfolio repo on github.com → **Add file → Create new file**.
3. In the name box type `.claude/skills/performance-ratios/SKILL.md` — each `/` creates a folder.
4. Paste, then **Commit changes** with the message `Add performance-ratios skill`.

**Or ask Claude Code / Codex**, opened in your repo folder:

```
Copy the file at
https://raw.githubusercontent.com/adamwstauffer/shidler/main/templates/portfolio/firstname-lastname/.claude/skills/performance-ratios/SKILL.md
into .claude/skills/performance-ratios/SKILL.md in this repo, unchanged,
and commit it alone with the message "Add performance-ratios skill".
Show me the commit when you are done.
```

Read the skill once after installing it. You will not change it at this stage.

---

## Deliverable

Upload your own copy of `performance-ratios-template.xlsx` to:

```
[your-repo]/models/templates/performance-ratios-template.xlsx
```

You should also create the following directory skeleton in your repo (if you haven't already):

```
your-repo/
├── README.md            # Bio (from Stage 0)
├── RESUME.md            # Resume (from Stage 0)
├── .claude/
│   └── skills/
│       └── performance-ratios/  # SKILL.md (Stage 1, unmodified)
├── capabilities/
│   └── performance-ratios/  # README.md, and spec.md at Stage 4
├── docs/
│   ├── decisions/       # Memos and decision documents (Stage 2)
│   │   └── README.md
│   └── plans/           # Optional project plans
├── models/
│   ├── templates/       # ← Place performance-ratios-template.xlsx here
│   └── builds/          # Populated model lands here at Stage 3
├── data/                # Source financial data (Stage 3)
├── analysis/
│   └── validation/      # Self-audit reports
└── prompt-log.md        # AI session log (repo root)
```

Each directory should have a short `README.md` explaining what belongs there. The course repo (`courses/International-Corporate-Finance/projects/performance-ratios/`) is a living example — copy and adapt its READMEs.

---

## What to submit

Submit nothing separately — just commit the template and the directory structure to your repo. Stage 1 is graded by inspection of the repo URL you submitted at Stage 0.

The repo must contain:

- [ ] `models/templates/performance-ratios-template.xlsx` (unmodified copy of the provided template, with `CASH_capex` and `CASH_working_capital_change` in Name Manager)
- [ ] `.claude/skills/performance-ratios/SKILL.md` (unmodified copy of the skill)
- [ ] Directory skeleton above with a `README.md` in each directory
- [ ] At least 2 new commits since Stage 0 with descriptive messages

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline can move your score up — the full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (% of Stage 1 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Template and skill installed correctly | 30% | Template unmodified, in the right directory, with the correct filename; `performance-ratios` skill at `.claude/skills/performance-ratios/SKILL.md`, unmodified |
| Directory structure | 40% | All required directories present; README.md in each; logical organization |
| README quality | 20% | READMEs explain purpose and conventions; not just placeholders |
| Commit hygiene | 10% | Meaningful commit messages; clean history |

---

## Tips

- **Open the template before uploading.** Click through every tab. Read the Cover & Instructions tab. Skim the Ratios tab — note how every formula is in named-range notation. You'll need this familiarity at Stages 3 and 4.
- **Don't modify the template at this stage.** If you spot something you'd want to change, write it down — it'll be useful for your Stage 4 spec.
- **Use the templates README as your reference.** [`../../templates/README.md`](../../../../templates/README.md) documents the file naming convention (`YYYY-MM-DD-{slug}.md`) you'll use for memos and specs in later stages.
