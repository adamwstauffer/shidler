# Stage 3: Populated Financials

**Weight:** 20% of project score
**Format:** Upload-only — no presentation component
**Deliverable:** Populated `.xlsx` with company financials

> **Where this fits in the project.**
> **Input:** Stage 1 ratios template + Stage 2 company selection memo (you now know which company).
> **Output (this stage):** A populated workbook at `models/builds/YYYY-MM-DD-{lastname}-{company-slug}-financials.xlsx` with Income Statement, Balance Sheet, and Cash Flow for the selected company.
> **Used by:** Stage 4 (the data values populate the spec's "Data Inputs" section) and Stage 5 (the LLM analysis runs against these numbers; you'll manually verify ≥5 ratios from them).

> **Submission alternative — Lamaku upload.** GitHub is the required submission path. If you hit a hard wall pushing the workbook to your repo (file size, auth issues, etc.), you may upload it directly to Lamaku as a fallback. Use the same filename convention (`YYYY-MM-DD-{lastname}-{company-slug}-financials.xlsx`). Using the Lamaku fallback does **not** reduce your Stage 3 grade. By Stage 5, the workbook must also live in your GitHub repo (`models/builds/`) — the Stage 5 polish rubric assumes the full project history is in the repo.

> **Heads up — instructor write access.** If you haven't yet granted the instructor Write access on your repo (Stage 2 submission checklist item), do it now. Stage 5 grades how you incorporated the instructor's PR feedback on your Stage 2 memo, and PRs can't happen without write access.

> **Unfamiliar terms?** "Named ranges," "10-K," "commit," and other recurring terms are defined in the [Project glossary in the BUS-629 README](README.md#project-glossary).

---

## Overview

Populate the provided ratios template with real financial data for the company you selected at Stage 2. Income Statement, Balance Sheet, and Cash Flow only — full ratio interpretation and analysis come at Stage 5.

The Ratios tab will auto-populate from the pre-filled formulas as soon as the financial-statement tabs are filled. Your job at this stage is to verify the numbers tie to the source 10-K (or VAS / IFRS equivalent), not to interpret what they mean.

## Why this stage is financials-only

Splitting "get the data in" from "interpret what it says" produces two cleaner stages and forces a discipline you'll need in any analyst seat: be sure the numbers are right *before* you start telling stories about them. It also keeps Stage 5 substantive — the full analysis there is driven by your Stage 4 spec, not pre-baked.

---

## Deliverable

A populated workbook saved to `models/builds/` in your repository.

**Filename:** `YYYY-MM-DD-{lastname}-{company-slug}-financials.xlsx` — all **lowercase**, hyphen-separated.
Example: `2026-06-04-nguyen-vinamilk-financials.xlsx`

---

## Workbook requirements

- All financial statement data entered from 10-K / annual report / audited financials
  - Income Statement: current year + prior year
  - Balance Sheet: current year + prior year (prior year populates `startYear_*` named ranges)
  - Cash Flow: current year + prior year
- Market/analyst assumptions sourced and entered (share price as of fiscal year-end, shares outstanding, cost of capital, tax rate)
- For non-U.S. companies: reporting currency and any IFRS / VAS adjustments noted in the Cover & Instructions tab
- Ratios tab auto-populates — do not modify formulas, only verify they compute

---

## Self-check before submission

| Check | What to verify | If it fails |
|-------|---------------|---|
| **Balance Sheet balances** | Assets = Liabilities + Equity (both years) | A small discrepancy is usually a sign or rounding error in one line item. Larger gaps usually mean a missing line (intangibles, deferred tax, etc.). |
| **No `#REF!` or `#DIV/0!` cells** | Every formula resolves to a number | A `#DIV/0!` on a ratio means a denominator cell is empty. A `#REF!` means a named range is missing — check the Legend tab. |
| **Prior-year cells populated** | `startYear_*` named ranges have values, otherwise start-of-year ratios will fail | Most common Stage 3 mistake. Without prior-year totals, ROA, asset turnover, and inventory turnover all fail silently. |
| **Sign sanity** | No negative values where impossible (e.g., negative inventory) | A negative number here usually means you entered the value from a different statement section (e.g., a contra account). |
| **Source documentation** | Cover & Instructions tab notes the reporting standard, currency, fiscal year end, and source 10-K URL | If you used a non-US filing (VAS annual report, IFRS 20-F), note that here. |
| **Ratios tab is not blank** | Open the Ratios tab and confirm all rows show numbers (or `#DIV/0!` which the prior row catches) | If the entire tab is empty, you either skipped a financial-statement tab or you typed values into the wrong cells (the formulas reference *named ranges*, not cell addresses). |

This is a self-check, not a deliverable — your Stage 3 grade is on the workbook itself. The deeper validation work happens at Stage 5 when the spec-driven analysis is produced and evaluated.

---

## What to submit

Just commit the populated workbook to your repo. Stage 3 is graded by inspection of the file in `models/builds/`.

- [ ] `models/builds/YYYY-MM-DD-{lastname}-{company-slug}-financials.xlsx`
- [ ] Cover & Instructions tab updated with source URL, reporting standard, currency, fiscal year end
- [ ] Commit message describes what was populated (e.g., "Populate Vinamilk FY2024 + FY2023 financials")

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — fixing data ties, completing populated cells, cleaning `#REF!` errors, expanding the Cover tab — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (% of Stage 3 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Data accuracy (ties to source 10-K) | 40% | Spot-checks from Cover tab match audited financials line-for-line |
| Completeness (both years populated) | 25% | All `INC_*`, `BAL_*`, `CASH_*`, `startYear_*` cells filled |
| Source documentation | 20% | Cover tab cites source, standard, currency, FYE; non-US adjustments noted |
| Auto-computed ratios resolve cleanly | 15% | No `#REF!`, `#DIV/0!`, or `#NAME?` errors anywhere on Ratios tab |

---

## Tips

- **Tie out, don't transcribe.** Open the source 10-K and the template side-by-side. Cross-check totals (e.g., Total Assets, Total Revenue) before trusting line-item entries.
- **Currency and units matter.** Companies report in millions, billions, thousands, or units depending on the country. The Cover tab has a unit field — fill it in and stay consistent across tabs.
- **Don't interpret yet.** If a ratio looks weird, write it in your notes and bring it up in Stage 4's HIL iteration pass (a strange Stage 3 ratio is often a *spec gap* the LLM will inherit at Stage 5 — exactly the kind of thing the HIL iteration is meant to catch). Don't try to "fix" the data to make ratios behave.
- **Commit incrementally.** Don't populate the entire workbook and commit once. Commit after each statement (one for IS, one for BS, one for CF). Your Stage 4 spec retrospective will benefit from a clean history.

---

## Pro tip — use an LLM as a workbook assistant

Data entry is not the part of this stage that builds the skill. Use an LLM to handle the routine pieces so you can spend your time on the parts that matter (sourcing, tie-out, sanity-checking).

**Three high-value uses:**

| Task | What to ask the LLM |
|---|---|
| **Cover & Instructions tab draft** | Upload your populated template. Prompt: *"Read the Cover & Instructions tab. Fill in the company-context fields (source URL, reporting standard, currency, FYE) based on the company name and the financial-statement tabs. Return the cell values I should type into each labeled field. Do not modify formulas."* |
| **Formula sanity check** | Prompt: *"Read my populated template. Spot-check three computed ratios against the underlying named ranges. For each, show me the formula, the input values, and the expected result. Flag any rows where the input cells look wrong (sign errors, missing prior-year data, typos)."* |
| **Workbook formatting cleanup** | Prompt: *"My workbook has inconsistent formatting (some currency cells show no symbol, some percentages are formatted as decimals). Without changing any values, suggest exact Excel format strings I should apply to each named-range category (`BAL_*`, `INC_*`, `CASH_*`, `RATIO_*`) for consistency."* |

**What the LLM should NOT do at Stage 3:** Populate the actual financial statement values for you. That data must come from the source 10-K / annual report — that's the discipline this stage is teaching. Use the LLM for housekeeping, not for the numbers themselves.

**Log the prompts.** Add a row to `deliverables/prompt-log.md` for each meaningful session. Stage 4 grades the prompt log; building the habit at Stage 3 is free practice.

If you want richer LLM-with-Excel workflows, Claude.ai and ChatGPT both accept `.xlsx` uploads via the paperclip icon and can read the actual cell contents — not just describe them.
