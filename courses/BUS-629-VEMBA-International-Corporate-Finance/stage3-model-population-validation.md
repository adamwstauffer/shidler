# Stage 3: Model Population & Validation

**Weight:** 25% of project score

---

## Overview

Populate your Stage 1 template with real financial data for your chosen company. Compute all ratios. Self-audit the model for internal consistency. This is the most heavily weighted analytical stage because it produces the quantitative foundation for everything that follows.

## Why a dedicated stage

In BUS-314 (undergrad), building and populating happen simultaneously. Separating them forces deliberate validation — a skill that distinguishes senior analysts from juniors. The self-audit checklist mirrors what a Big 4 review process looks like. This stage also builds the deep model familiarity required for writing a credible spec in Stage 4.

---

## Deliverables

1. **Completed workbook** (`.xlsx`) saved to `models/builds/`
2. **Validation report** (`.md`, 200–300 words) saved to `analysis/validation/`

---

## Workbook requirements

- All financial statement data entered from 10-K / annual report / audited financials
- All 25+ ratios computed with working formulas
- Named ranges populated and functional
- Market/analyst assumptions sourced and documented (share price, shares outstanding, cost of capital, tax rate)
- For non-U.S. companies: reporting currency and any IFRS/VAS adjustments noted in the Notes tab

---

## Self-audit checklist

Your validation report must address **each** of the following checks. For each, state the result and explain any discrepancies.

| Check | What to verify |
|-------|---------------|
| **Balance Sheet balances** | Assets = Liabilities + Equity (both years) |
| **Du Pont ROA consistency** | Du Pont ROA (Margin x Turnover) ≈ Direct ROA |
| **Du Pont ROE consistency** | Du Pont ROE ≈ Direct ROE |
| **Sign checks** | No negative ratios where impossible (e.g., negative current ratio) |
| **Reasonableness** | Ratios fall within plausible industry ranges |
| **Named range audit** | Spot-check 5 named ranges to confirm they point to correct cells |
| **Formula audit** | Spot-check 5 formulas to confirm they reference correct inputs |
| **Start-of-year vs. average** | Compare start-of-year and average-based profitability ratios; explain any divergence |

---

## Rubric (% of Stage 3 score)

| Criterion | % |
|-----------|---|
| Data Accuracy | 25% |
| Formula Correctness | 25% |
| Internal Consistency (Du Pont checks) | 25% |
| Validation Report & Self-Audit | 25% |
