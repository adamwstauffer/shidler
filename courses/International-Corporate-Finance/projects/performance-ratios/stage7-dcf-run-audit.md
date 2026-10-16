---
template: stage-brief
project: performance-ratios
stage: 7
title: "Run & Audit the DCF"
capability: valuation
deliverables:
  - path: "capabilities/valuation/model.xlsx"
    format: xlsx
  - path: "analysis/YYYY-MM-DD-{company-slug}-dcf-raw-log.md"
    format: markdown
  - path: "analysis/YYYY-MM-DD-{company-slug}-dcf-audit-analysis.md"
    format: markdown
  - path: "analysis/YYYY-MM-DD-{company-slug}-dcf-verification-analysis.md"
    format: markdown
  - path: "prompt-log.md"
    format: markdown
prerequisites: [3, 6]
---

# Stage 7: Run & Audit the DCF

**Step-by-step on Kumu:** [Stage 7 walkthrough](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage7.html)

**Collaborator penalty:** from Stage 2 on, a stage loses 5 raw points if `adamwstauffer` is not a Write collaborator on your repository at its deadline; fixing it before a stage's deadline lifts the penalty retroactively.

**Format:** Deliverable-only — no in-class presentation
**Deliverable:** The DCF model your modified skill produced, its unedited session log, an `audit-xls` findings table with your verdicts, and a manual verification table

> **Where this fits in the project.**
> **Input:** Your modified `dcf-model` skill and run brief (Stage 6), your Stage 3 workbook, and the unmodified `audit-xls` skill.
> **Output (this stage):** `capabilities/valuation/model.xlsx`, the raw session log, the audit, and the manual verification table — all in your repo.
> **Used by:** Stage 8 (your valuation memo reads this model, and only after you have verified it).

> **GitHub only.** No Lamaku fallback for Stages 6–8.

---

## Overview

At Stage 6 you made a professional DCF skill fit your company. Now you find out whether it does. A **fresh** agent session runs your modified skill with nothing but your workbook and your run brief, and builds the model. Then you audit what it built, twice: once with a second professional skill (`audit-xls`), and once by hand.

## Why audit twice

An automated audit catches formula errors, broken links and inconsistent signs quickly and thoroughly. It does not know what your company reports. A DCF can pass every automated check and still misstate the value of a share, because no automated check knows what your company's filing says. The manual table is where you check the few numbers the valuation hangs on, against your own arithmetic. It has the same shape as the Stage 5 verification table, for the same reason.

---

## Step 1 — Run the skill in a genuinely fresh session

"Fresh" means the session knows nothing you did not hand it: **only** the modified `dcf-model` skill, your workbook, and `capabilities/valuation/spec.md`. No chat history, no web search, no data connectors, no "as we discussed".

- **Claude Code:** open a new conversation in your repo folder (or type `/clear` first).
- **Codex:** start a new task on your repo.
- **Neither installed?** Start a new chat in Claude.ai with file uploads and code execution on; upload `SKILL.md`, the workbook and `spec.md`, paste the prompt below, and say in the log that this is how you ran it.

Prompt:

```
Use the dcf-model skill in .claude/skills/dcf-model/ to build a DCF from the
workbook at models/builds/<your-file>.xlsx. The only other input is the run
brief at capabilities/valuation/spec.md. Read the performance-ratios skill in
.claude/skills/performance-ratios/ for what the workbook's names mean. Do not
search the web and do not use any data connector. Do not read any other file
in this repo. Save the model to capabilities/valuation/model.xlsx. Wherever
you have to stop, guess, or work around something, say so plainly.
```

Let it run. Answer a question only if the session cannot continue without you — and every answer you give goes in the log.

**Recalculation.** The skill tells the agent to run `recalc.py` before delivery. That script is not included in the skill folder (it belongs to a different skill, and is written for Mac/Linux), so the command fails unless your Stage 6 edits replaced it. A formula-written workbook has no computed values until a spreadsheet program calculates it. Two paths that work on any machine:

- **Excel recalculates on open.** After you commit the model as produced (Step 2), open it in Excel (desktop or Excel for the web), check that no cell shows `#REF!`, `#NAME?`, `#DIV/0!` or `#VALUE!`, and save. Commit the saved file separately: `Recalculate model.xlsx in Excel, no edits`.
- **Ask the agent to scan the formulas** instead of running a script: `Read every formula in capabilities/valuation/model.xlsx. List any that refers to a sheet, cell or name that does not exist, and any that would divide by an empty cell. Do not change the file.`

If the skill still calls `validate_dcf.py`, record its output in the log like any other output. A pass from it is not a verification.

## Step 2 — Commit the model before you touch it

Commit `capabilities/valuation/model.xlsx` exactly as the session produced it, before you open it, recalculate it or fix anything: `Add DCF model as produced by the modified dcf-model skill`. That commit is the evidence of what your skill did on its own. Every change after it is yours, and visible.

Save the complete, unedited session transcript (or its export) as `analysis/YYYY-MM-DD-{company-slug}-dcf-raw-log.md`. Then mark — with a short bold note on its own line, never by editing the transcript — every place where the session **stopped to ask**, **guessed**, or **worked around** something. Those marks are the list of what your Stage 6 edits did not yet cover.

**If the run failed** — the session could not finish, or built something plainly wrong because of the skill — fix the skill with another Stage 6-style commit to `.claude/skills/dcf-model/SKILL.md` (add the hunk to your annotated diff), then run Step 1 again in a new fresh session. Keep both runs in the raw log (*Run 1*, *Run 2*), commit the first model before the second overwrites it, and say in one paragraph what failed and what you changed. A failed run plus a fix and a rerun is evidence, not a penalty.

## Step 3 — Audit with `audit-xls`

In a session of your choice (it need not be fresh), prompt:

```
Run the audit-xls skill in .claude/skills/audit-xls/ at model scope on
capabilities/valuation/model.xlsx. Write the findings table, unedited, to
analysis/<YYYY-MM-DD>-<company-slug>-dcf-audit-analysis.md. Do not change the
workbook.
```

Naming the scope matters: without it the skill stops to ask.

Below the findings table, in the same file, add **your verdict on every finding**:

| Finding | Verdict | Why |
|---|---|---|
| (from the table) | Real / False positive / Real but acceptable | One or two sentences: what you checked and what you found |

A "false positive" needs the evidence that it is false. A "real but acceptable" needs the reason it does not move the value per share materially.

## Step 4 — Verify by hand

Create `analysis/YYYY-MM-DD-{company-slug}-dcf-verification-analysis.md`. Recompute at least these eight checks from your workbook and the model's own assumptions, show the arithmetic, and compare with the model:

| Check | Formula (named-range notation) | Manual value (show arithmetic) | Model's value | Match? | One-line note |
|---|---|---|---|---|---|
| Base-year revenue | `INC_sales` | | | | |
| Base-year NOPAT | `INC_ebit × (1 − tax_rate)` | | | | |
| Base-year FCF | NOPAT + `INC_depreciation` + `CASH_capex` + `CASH_working_capital_change` | | | | |
| Net debt | `BAL_debt_short_term_curr + BAL_debt_long_term_curr − BAL_cash_marketable_securities_curr` | | | | |
| After-tax cost of debt | pre-tax cost of debt × (1 − `tax_rate`) | | | | |
| WACC | E/V × cost of equity + D/V × pre-tax cost of debt × (1 − `tax_rate`), market weights | | | | |
| PV of terminal value | FCF in the year after the forecast ÷ (WACC − g), discounted to today | | | | |
| Equity value per share | (enterprise value − net debt − non-controlling interest) ÷ `shares_outstanding` | | | | |

Notes on the table:

- **Units.** Your statements are in the currency and scale on the Notes tab; `share_price` is in base units per share; `shares_outstanding` is in millions. State the unit in every row, and make the last row come out in the same unit as `share_price`.
- **Your definitions may differ.** If your Stage 6 skill defines net debt to include lease liabilities, or to treat term deposits differently, use your definition and say so in the note. The check is that the model does what your skill says.
- **Non-controlling interest** comes from the figure you recorded on the Notes tab at Stage 3. If your company reports none, write 0 and say so.

Discrepancies are not failures — they are the most informative rows. For every mismatch, trace the cause and name it: **the skill** (an instruction your Stage 6 edits missed), **the workbook** (a Stage 3 entry), or **the session** (the agent departed from the skill). A mismatch with its cause named earns full credit; an unflagged one does not.

Log every session in `prompt-log.md` (repository root).

---

## What to submit

- [ ] `capabilities/valuation/model.xlsx`, first committed exactly as produced; any recalculation or fix in later commits
- [ ] `analysis/YYYY-MM-DD-{company-slug}-dcf-raw-log.md` — unedited transcript, every ask / guess / workaround marked
- [ ] `analysis/YYYY-MM-DD-{company-slug}-dcf-audit-analysis.md` — `audit-xls` findings table plus a verdict on every finding
- [ ] `analysis/YYYY-MM-DD-{company-slug}-dcf-verification-analysis.md` — at least the eight checks, arithmetic shown, every mismatch traced
- [ ] If the run failed: the fix commit to the skill, the new hunk in your Stage 6 annotated diff, and both runs in the log
- [ ] `prompt-log.md` updated

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — a verdict added, a mismatch traced, another check recomputed — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (% of Stage 7 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Fresh, honest run | 20% | The log shows a genuinely fresh session with only the three inputs; the model is committed before any change; asks, guesses and workarounds are marked |
| Automated audit with verdicts | 25% | Every `audit-xls` finding has a verdict and a reason; false positives come with evidence |
| Manual verification | 40% | At least the eight checks, arithmetic shown, units stated; every mismatch traced to the skill, the workbook or the session |
| Commit hygiene | 15% | As-produced model, recalculation and fixes in separate, descriptive commits; any rerun documented |

---

## Tips

- **Don't fix the model before you commit it.** The as-produced commit is the only record of what your skill did unaided. Fix in later commits, and say what you fixed.
- **A clean audit is not a correct valuation.** Read the bridge from enterprise value to value per share line by line yourself.
- **Put the model's value per share next to `share_price` early.** If the two are not even in the same unit, nothing else in the table matters yet.
- **Commit incrementally.** Model, log, audit, verification — one commit each.
