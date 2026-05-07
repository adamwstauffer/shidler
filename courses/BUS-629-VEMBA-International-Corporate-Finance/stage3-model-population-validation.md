# Stage 3: Populated Financials

**Weight:** 20% of project score
**Format:** Upload-only — no presentation component
**Deliverable:** Populated `.xlsx` with company financials

---

## Overview

Populate the provided ratios template with real financial data for the company you selected at Stage 2. Income Statement, Balance Sheet, and Cash Flow only — full ratio interpretation and analysis come at Stage 5.

The Ratios tab will auto-populate from the pre-filled formulas as soon as the financial-statement tabs are filled. Your job at this stage is to verify the numbers tie to the source 10-K (or VAS / IFRS equivalent), not to interpret what they mean.

## Why this stage is financials-only

Splitting "get the data in" from "interpret what it says" produces two cleaner stages and forces a discipline you'll need in any analyst seat: be sure the numbers are right *before* you start telling stories about them. It also keeps Stage 5 substantive — the full analysis there is driven by your Stage 4 spec, not pre-baked.

---

## Deliverable

A populated workbook saved to `models/builds/` in your repository.

**Filename:** `YYYY-MM-DD-{company-slug}-financials.xlsx`
Example: `2026-06-04-vinamilk-financials.xlsx`

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

| Check | What to verify |
|-------|---------------|
| **Balance Sheet balances** | Assets = Liabilities + Equity (both years) |
| **No `#REF!` or `#DIV/0!` cells** | Every formula resolves to a number |
| **Prior-year cells populated** | `startYear_*` named ranges have values, otherwise start-of-year ratios will fail |
| **Sign sanity** | No negative values where impossible (e.g., negative inventory) |
| **Source documentation** | Cover & Instructions tab notes the reporting standard, currency, fiscal year end, and source 10-K URL |

This is a self-check, not a deliverable — your Stage 3 grade is on the workbook itself. The deeper validation work happens at Stage 5 when the spec-driven analysis is produced and evaluated.

---

## What to submit

Just commit the populated workbook to your repo. Stage 3 is graded by inspection of the file in `models/builds/`.

- [ ] `models/builds/YYYY-MM-DD-{company-slug}-financials.xlsx`
- [ ] Cover & Instructions tab updated with source URL, reporting standard, currency, fiscal year end
- [ ] Commit message describes what was populated (e.g., "Populate Vinamilk FY2024 + FY2023 financials")

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
- **Don't interpret yet.** If a ratio looks weird, write it in your notes and bring it up in Stage 4 — but don't try to "fix" the data to make ratios behave.
- **Commit incrementally.** Don't populate the entire workbook and commit once. Commit after each statement (one for IS, one for BS, one for CF). Your Stage 4 spec retrospective will benefit from a clean history.
