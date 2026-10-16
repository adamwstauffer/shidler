---
template: stage-brief
project: performance-ratios
stage: 6
title: "Modify the DCF Skill"
capability: valuation
deliverables:
  - path: ".claude/skills/dcf-model/SKILL.md"
    format: markdown
  - path: ".claude/skills/dcf-model/LICENSE"
    format: text
  - path: ".claude/skills/audit-xls/SKILL.md"
    format: markdown
  - path: ".claude/skills/audit-xls/LICENSE"
    format: text
  - path: "capabilities/valuation/README.md"
    format: markdown
  - path: "capabilities/valuation/spec.md"
    format: markdown
  - path: "analysis/YYYY-MM-DD-{company-slug}-dcf-skill-diff-analysis.md"
    format: markdown
  - path: "prompt-log.md"
    format: markdown
prerequisites: [1, 3, 5]
---

# Stage 6: Modify the DCF Skill

**Step-by-step on Kumu:** [Stage 6 walkthrough](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage6.html)

**Collaborator penalty:** from Stage 2 on, a stage loses 5 raw points if `adamwstauffer` is not a Write collaborator on your repository at its deadline; fixing it before a stage's deadline lifts the penalty retroactively.

**Format:** Deliverable-only — no in-class presentation
**Deliverable:** A modified professional DCF skill in your repo, committed as a baseline plus edits, with an annotated diff explaining every change

> **Where this fits in the project.**
> **Input:** Your Stage 3 workbook (every identity check passing), the `performance-ratios` skill from Stage 1, and a published DCF skill you copy in at this stage.
> **Output (this stage):** `.claude/skills/dcf-model/` modified for your company, `.claude/skills/audit-xls/` copied as-is, a one-page run brief at `capabilities/valuation/spec.md`, and the annotated diff at `analysis/YYYY-MM-DD-{company-slug}-dcf-skill-diff-analysis.md`.
> **Used by:** Stage 7 (a fresh agent session runs your modified skill, with nothing else but the workbook and the run brief) and Stage 8 (your memo says what the skill got wrong).

> **GitHub only.** Stages 6–8 have no Lamaku fallback: a skill only works from inside your repo.

---

## Overview

**What is the company worth?** A company is worth the present value of the cash it will free, discounted at what its capital costs today. Stages 6–8 answer that for the company you have analyzed since Stage 2 — but you will not build the discounted-cash-flow (DCF) model from scratch, and you will not trust one built for you.

You start from a **published, professional DCF skill**: `dcf-model`, from Anthropic's `financial-services` repository (Apache 2.0 license). It was written for a U.S. company, valued in U.S. dollars, with data pulled from paid market-data connectors and SEC filings. Your company has none of that: it has one workbook of named ranges, in its own currency, and whatever market inputs you can cite.

So the skill will not run correctly on your workbook as shipped. At this stage you make it run: you edit its `SKILL.md` until a fresh agent session, given only the skill, your workbook and a one-paragraph brief, could build the DCF **without asking for data it cannot get, and without a U.S. default silently mis-valuing your company**.

## Why the diff is the spec

At Stage 4 you wrote a spec from a blank page. Here the spec is a **diff against a working professional skill**. Almost every edit you will need is a valuation concept — the tax rate, a discount rate in the right currency, the bounds on terminal growth, what belongs in free cash flow, the bridge from enterprise value to the value of a share. Fixing the skill *is* the finance. The annotated diff is where you show that you understood each change rather than accepted one.

---

## Step 1 — Copy two skills in, unmodified (the baseline commit)

The upstream repository is pinned to one commit so that every student's baseline is the same file:

- `dcf-model`: <https://github.com/anthropics/financial-services/tree/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/model-builder/skills/dcf-model>
- `audit-xls`: <https://github.com/anthropics/financial-services/tree/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/model-builder/skills/audit-xls>
- License: <https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/LICENSE>

Copy the **whole** `dcf-model` folder (`SKILL.md`, `TROUBLESHOOTING.md`, `requirements.txt`, `scripts/`) to `.claude/skills/dcf-model/`, and the `audit-xls` folder to `.claude/skills/audit-xls/`. The skill folders carry no license file of their own — the Apache 2.0 `LICENSE` sits at the root of the upstream repository. Put a copy of it in **each** of the two folders. Use the files from the pinned commit, not the repository's current `main`.

Commit the two folders, unchanged, **on their own**, with the message `Add dcf-model and audit-xls skills, unmodified`. That commit is your baseline: every later edit is measured against it.

**On github.com:**

1. Download the upstream repository at the pinned commit as a zip: <https://github.com/anthropics/financial-services/archive/574ed3624aebd0418c7e96cd101262f30210ab26.zip>. Unzip it on your computer.
2. Inside, find `plugins/agent-plugins/model-builder/skills/`. Copy the repository's root `LICENSE` file into both `dcf-model/` and `audit-xls/`.
3. In your portfolio repo on github.com, open the `.claude/skills/` folder (it exists since Stage 1) → **Add file → Upload files** → drag the `dcf-model` and `audit-xls` folders in → commit with the message above.

**Or ask Claude Code / Codex**, opened in your repo folder:

```
Download https://github.com/anthropics/financial-services/archive/574ed3624aebd0418c7e96cd101262f30210ab26.zip
to a temporary folder outside this repo. Copy
plugins/agent-plugins/model-builder/skills/dcf-model/ to .claude/skills/dcf-model/
and plugins/agent-plugins/model-builder/skills/audit-xls/ to .claude/skills/audit-xls/,
unchanged, and copy the repository's root LICENSE into both folders.
Commit only those two folders, with the message
"Add dcf-model and audit-xls skills, unmodified". Change nothing else.
Show me the commit.
```

Do not modify `audit-xls`. You use it as published, in Stage 7.

## Step 2 — Read the skill against your workbook

Read `dcf-model/SKILL.md` end to end with your Stage 3 workbook and the `performance-ratios` skill open beside it. It is long (well over a thousand lines). For each instruction, ask: *does this hold for my company, in my currency, from my workbook?*

These are the areas where the skill, as shipped, does not fit a workbook like yours. The table says **where** to look and **why** it breaks. What to change it to is your call — and your grade.

| Area of `SKILL.md` | Why it breaks on your workbook |
|---|---|
| Data sources (the opening steps and the workflow's "At Start") | Points at paid data connectors, web search and SEC filings. Your source is a workbook of named ranges plus market inputs you cite yourself. |
| Historical analysis | Wants three to five years of history. Your workbook has one income statement and two balance sheets. |
| Tax validation | The skill's "typical" tax band is a U.S. band. Your company's statutory and effective rates may sit outside it — and the check then fails a correct model. |
| Risk-free rate and equity risk premium | Defaults to a U.S. Treasury yield and a U.S. premium. A U.S.-dollar rate discounting a local-currency cash flow mixes currencies. |
| Units and formats | `$` formats, "$mm" labels, dollars per share. Your statements are in local currency at a scale (Notes tab, Units row); `share_price` is in base units per share; `shares_outstanding` is in millions. |
| Free cash flow build | The skill builds operating profit after tax from EBIT. Your workbook also offers `currentYear_after_tax_operating_income`, which includes after-tax other income — interest earned on cash — which is not an operating cash flow. Decide which one the skill may use, and say so. |
| Equity bridge | Net debt, cash, minority interest. Total debt in your workbook has a short-term and a long-term line; cash may include term deposits; non-controlling interest, if your company reports it, sits inside equity (you recorded the figure on the Notes tab at Stage 3). Neither of the skill's own checks inspects the bridge line by line. |
| Capital-structure weights | Net-debt weights turn negative for a company with more cash than debt. The skill names the case and gives no rule. |
| Scenario layout and sensitivity tables | The skill describes two scenario layouts that cannot both hold, and a sensitivity table (beta × risk-free rate) that means little once the discount rate is set. Your Stage 8 memo needs a **beta × terminal growth** table. |
| Growth, discount-rate and terminal-growth bands | U.S. large-cap and U.S.-tech ranges, and a terminal growth cap tied to a U.S.-dollar risk-free rate. |
| Recalculation and validation | The skill tells the agent to run `recalc.py`, which is **not included in the skill folder** (and is written for Mac/Linux). The bundled `validate_dcf.py` looks for a sheet the skill tells the agent not to build. |

You may decide an area is right for your company as published. That is a legitimate call — defend it in the annotated diff (Step 5). An area you neither change nor defend is a gap.

## Step 3 — Edit the skill (the edit commits)

Edit `.claude/skills/dcf-model/SKILL.md` — in the github.com editor (open the file → pencil icon), or with Claude Code / Codex. Commit in meaningful pieces (one area per commit is a good rhythm), with messages that say what changed and why: `dcf-model: tax check uses statutory local rate, not the U.S. band`.

Two rules while you edit:

- **Every changed input traces to a source.** A historical figure traces to a named range in your workbook (use the `performance-ratios` skill's names — `CASH_capex`, `CASH_working_capital_change` and the rest). A market input (a government bond yield, a risk premium, a beta) is a labeled assumption with a cited source. Write that rule into the skill: the agent never fetches and never invents.
- **Keep the license and say it changed.** Apache 2.0 requires a modified file to carry a notice that it was changed. Add one line directly under the `SKILL.md` frontmatter, for example:

  ```
  > Modified by <your name> from anthropics/financial-services @ 574ed36 for a <currency> named-range workbook. Changes and reasons: analysis/YYYY-MM-DD-{company-slug}-dcf-skill-diff-analysis.md
  ```

  Leave `LICENSE` in both folders.

If an AI helps you edit, it proposes and you decide — the same rule as every stage. "The AI changed it" is not a reason in the annotated diff.

## Step 4 — Write the run brief and the capability README

The Stage 7 session will receive exactly three things: the modified skill, your workbook, and a **run brief**. Write the brief now, at `capabilities/valuation/spec.md`:

- One paragraph: the company, the workbook's path in your repo, the currency and scale, the fiscal year, what the model must produce (value per share, in the same unit as `share_price`, and the sensitivity tables your memo needs) and where to save it (`capabilities/valuation/model.xlsx`).
- A short list of the market inputs you have decided on, each with its value and cited source, or the rule the skill should apply where you have not.

Nothing in the brief may depend on the conversation you had while editing the skill — Stage 7's session will not have it.

Add `capabilities/valuation/README.md`: four to six sentences on what the capability is (a DCF valuation of your company built by your modified skill), what is in the folder, and which stage produces each file — the same shape as `capabilities/performance-ratios/README.md`.

## Step 5 — The annotated diff (the human-in-the-loop artifact)

Create `analysis/YYYY-MM-DD-{company-slug}-dcf-skill-diff-analysis.md`. Take the diff of `SKILL.md` from your baseline commit to your last edit, and for **every hunk** (each block of changed lines) write four lines:

| | |
|---|---|
| **What the original assumed** | Quote or paraphrase the original instruction. |
| **Why that is wrong for this company** | The finance, not the mechanics: currency, jurisdiction, reporting standard, capital structure. |
| **What you changed it to** | The new instruction, in one sentence. |
| **What feeds it now** | The named range, or the cited source for a market input. |

Then one short section, **Areas left as published**, for every area in the Step 2 table you decided not to change, with the reason it holds for your company.

A hunk without a reason is not a modification, it is a guess.

**Getting the diff:**

- *On github.com:* open your repo's commit history (**Commits** link above the file list) → click a commit → the page shows what changed, hunk by hunk. To see all edits since the baseline at once, open `https://github.com/<you>/<your-repo>/compare/<baseline-sha>...main`.
- *Or ask Claude Code / Codex:* `Show the diff of .claude/skills/dcf-model/SKILL.md between the commit "Add dcf-model and audit-xls skills, unmodified" and HEAD, hunk by hunk. Do not change any files.`
- *Optional, for git users:* `git diff <baseline-sha> HEAD -- .claude/skills/dcf-model/SKILL.md`

Log every AI session you used while editing in `prompt-log.md` (repository root).

---

## What to submit

Commit everything to your repo. Stage 6 is graded by inspection of the repo.

- [ ] Baseline commit: `.claude/skills/dcf-model/` and `.claude/skills/audit-xls/` exactly as published at the pinned commit, each with `LICENSE`, committed alone
- [ ] One or more later commits editing `.claude/skills/dcf-model/SKILL.md`, with the change-notice line under its frontmatter
- [ ] `.claude/skills/audit-xls/` unchanged since the baseline
- [ ] `capabilities/valuation/spec.md` (run brief) and `capabilities/valuation/README.md`
- [ ] `analysis/YYYY-MM-DD-{company-slug}-dcf-skill-diff-analysis.md` covering every hunk, plus the areas left as published
- [ ] `prompt-log.md` updated

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — another area addressed, a hunk explained, a source cited — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (% of Stage 6 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Coverage of the skill's assumptions | 30% | Every area in the Step 2 table is either changed or defended as correct for this company |
| Traceability | 20% | Every changed input traces to a named range or a cited source; the skill tells the agent never to fetch or invent |
| Annotated diff | 30% | Every hunk carries all four lines; the reasons explain the finance, not just the edit |
| Run brief | 10% | Stands alone: a session with only the skill, the workbook and this brief has what it needs |
| License and commit hygiene | 10% | Baseline committed alone; `LICENSE` in both folders; change notice present; descriptive commit messages |

---

## Tips

- **Read before you edit.** The first pass through `SKILL.md` is reading, with a list of every line that would not hold for your company. The edits come from the list.
- **Currency consistency is the thread.** A local-currency cash flow takes a local-currency discount rate and a local-currency terminal growth rate. Most of the areas above are that one rule in different places.
- **Fewer, sharper edits beat a rewrite.** You are adapting a professional tool, not replacing it. A reviewer should still recognize the skill.
- **Don't edit around a broken workbook.** If an identity check from Stage 3 still fails, fix the workbook first. A skill tuned to a wrong number is wrong twice.
