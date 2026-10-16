---
name: performance-ratios
description: The named-range contract of the performance-ratios workbook — what every name means, which valuation inputs can be derived from it, and the identities any model built on it must satisfy. Use whenever an agent reads, extends or builds on the workbook (a DCF, a WACC sheet, a memo), and before trusting any number it produces from it.
---

# performance-ratios

The workbook is the single source of every historical input. An agent reads it **by name, never
by cell address** — cells move, names do not. This skill says what the names mean, what can be
derived from them, and what has to hold true for a downstream model to be trusted.

## 1. Read the workbook first

1. List every defined name and the cell it points to. Any name below that is missing, points to an
   empty cell or returns an error is a stop: report it, do not guess a value.
2. Read the Cover for the **currency and scale** of the statements (for example "VND million",
   "EUR thousand"). Every amount on the statement tabs carries that unit. The statement tabs'
   subtitles may still say `$millions` from the template — the Cover wins; fix the subtitle.
3. Read the four analyst assumptions on the Ratios tab and where each came from.

## 2. Naming convention

| Pattern | Meaning | Examples |
|---|---|---|
| `BAL_<item>_curr`, `BAL_<item>_prior` | Balance-sheet line, current or prior year-end | `BAL_debt_long_term_curr`, `BAL_equity_shareholders_prior` |
| `INC_<item>` | Income-statement line, current year only | `INC_sales`, `INC_ebit`, `INC_interest_expense` |
| `CASH_<item>` | Cash-flow subtotal, current year only | `CASH_operating`, `CASH_investments` |
| no prefix | Analyst assumption | `share_price`, `shares_outstanding`, `cost_capital`, `tax_rate` |
| `startYear_<item>` | Alias of a prior-year balance | `startYear_equity` ≡ `BAL_equity_shareholders_prior` |
| `currentYear_<item>` | Current-year balance or derived figure | `currentYear_after_tax_operating_income` |
| `avg_<item>` | Mean of start-of-year and current-year | `avg_equity`, `avg_total_capitalization` |
| `RATIO_<name>` | Ratio reused in the Du Pont decomposition | `RATIO_asset_turnover`, `RATIO_leverage` |

`yearCurrent` and `yearStart` hold the fiscal years; `market_capitalization` =
`share_price × shares_outstanding`.

**Units of the assumptions.** `share_price` is in the currency's base unit per share (not
millions). `shares_outstanding` is in millions. So `market_capitalization` comes out in
currency-millions — it only lines up with the statements when the statements are in millions too.
If the statements are in thousands or billions, convert in one labeled cell; never by editing
the inputs.

## 3. Derived inputs for a valuation

These are **not** all named in the template. When a model needs one, add it as a new named
formula on the Ratios tab (or on the model's own sheet) — never type the number.

| Derived input | Definition from the names | Note |
|---|---|---|
| Total debt | `BAL_debt_short_term_curr + BAL_debt_long_term_curr` | The template's "total capitalization" uses long-term debt only. Say which one you use. |
| Net debt | total debt − `BAL_cash_marketable_securities_curr` | Negative = net cash; it is *added* to enterprise value. |
| NOPAT (operating profit after tax) | `INC_ebit × (1 − tax_rate)` | Unlevered: no interest, no other income. |
| After-tax operating income (as named) | `currentYear_after_tax_operating_income` = `INC_net + (1 − tax_rate) × INC_interest_expense` | This **includes after-tax other income** (interest earned on cash, investment gains). Fine for return ratios; overstates the operating cash flow a DCF should discount. |
| Average capital | `avg_total_capitalization` | Long-term debt + equity, averaged. Return on capital uses `startYear_total_capitalization` or this — say which. |
| Capital expenditure | the Cash Flow Statement's capital-expenditures line | **Not named in the template.** Add `CASH_capex` before using it. Recorded as a negative (cash out). |
| Change in working capital | the Cash Flow Statement's total-change-in-working-capital line | **Not named.** Add `CASH_working_capital_change`. Positive = cash released. |
| Free cash flow (base year) | NOPAT + `INC_depreciation` + `CASH_capex` + `CASH_working_capital_change` | Signs as recorded on the cash-flow tab: capex already negative, a working-capital build already negative. |
| Effective tax rate | `INC_taxes / INC_taxable_income` | Compare with `tax_rate`; a large gap needs a sentence, not a silent pick. |

**What the workbook cannot supply.** It holds one year of income statement and cash flow and
two year-ends of balance sheet. A model that needs a growth history, a beta, a risk-free rate, a
market risk premium or a non-controlling-interest figure must take each from a cited source and
label it as an assumption — the workbook does not contain it, and the agent must not invent it.
If the company reports non-controlling interest inside equity, note that the template folds it
into shareholders' equity.

## 4. Identities any model built on the workbook must satisfy

Check each one and report it as pass / fail with the two numbers compared. A failure is a stop.

1. **Balance sheet balances**, both years: `BAL_assets_total_*` = `BAL_liabilities_total_*` + `BAL_equity_shareholders_*`.
2. **Du Pont ties**: the Ratios tab's Du Pont return on assets equals the direct one (the check
   column shows ✓).
3. **Base year ties to the statements**: the model's base-year revenue, EBIT and depreciation are
   references to `INC_sales`, `INC_ebit` and `INC_depreciation` — not retyped numbers.
4. **Operating income reconciles**: `currentYear_after_tax_operating_income` − NOPAT equals
   `(1 − tax_rate) × INC_other_income + (tax_rate × INC_taxable_income − INC_taxes)`. The second
   term is zero when reported tax equals `tax_rate × INC_taxable_income`. If it does not
   reconcile, a name is pointing at the wrong line.
5. **Cash from operations rebuilds**: `CASH_operating` = `INC_net + INC_depreciation` + total
   change in working capital. If it differs from the cash-flow statement the company filed, say
   by how much and why (the template's indirect method starts from net income; many filers start
   from profit before tax).
6. **Cost of capital is bracketed**: a weighted average cost of capital lies between the
   after-tax cost of debt and the cost of equity. If the model computes a WACC, `cost_capital`
   either links to it or the difference is explained.
7. **Terminal growth is below the discount rate**: g < WACC, in the same currency (a local-currency
   cash flow takes a local-currency discount rate and a local-currency g).
8. **The equity bridge ties**: enterprise value − net debt (− non-controlling interest, where
   reported) = equity value; equity value ÷ `shares_outstanding` = value per share, in the
   currency's base unit — the same unit as `share_price`.
9. **Sensitivity center is the model**: the center cell of every sensitivity table equals the
   model's own value per share.
10. **No hardcodes in calculation cells**: every number in a calculation cell traces to a name or
    to a labeled assumption cell.

## 5. Rules

- Never overwrite a yellow input or an assumption cell to make an identity pass. Fix the formula
  or the mapping, and say what you changed.
- Never rename or delete an existing name — other checks read them. Add new names; do not move
  cells under existing ones.
- Report first, edit on request.
