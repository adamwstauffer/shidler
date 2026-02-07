# BUS-314 Accounting Ratios Project — Claude Code Context

## Project Overview

This is a **five-stage academic project** for BUS-314 where students analyze a publicly traded company using accounting and performance ratios. Students choose their own company, pull data from SEC filings, and build an Excel model computing 25+ financial ratios.

## Directory Structure

- `stage[1-5]-*.md` — Assignment instructions for each stage
- `company-selection.md` — Guide for choosing a public company
- `template-memo.md` — Memo template for Stages 1 and 5
- `template-spec.md` — Technical specification template for Stage 2
- `extra-credit.md` — Extra credit options including Claude Skills, Claude Code, and Claude Cowork
- `_templates/excel/` — Excel template files and guide
- `archive/` — Student working files (analysis, deliverables, prompts, specs)

## Ratio Categories

The project covers six categories of accounting ratios:

1. **Performance** — MVA, Market-to-Book, EVA
2. **Profitability** — ROA, ROC, ROE (start-of-year and average-based)
3. **Efficiency** — Asset Turnover, Receivables Turnover, Inventory Turnover, Profit Margin, Operating Profit Margin
4. **Leverage** — Debt Ratios, Times Interest Earned, Cash Coverage, Debt Burden, Leverage Ratio
5. **Liquidity** — Current Ratio, Quick Ratio, Cash Ratio, NWC-to-Assets
6. **Du Pont System** — ROA and ROE decomposition

## Named Range Conventions

When working with this project, use these naming patterns:

- **Balance Sheet:** `BAL_[item]_[year]` (e.g., `BAL_assets_total_2024`)
- **Income Statement:** `INC_[item]` (e.g., `INC_sales`, `INC_ebit`, `INC_net`)
- **Cash Flow:** `CASH_[item]` (e.g., `CASH_operating`)
- **Market/Analyst:** `share_price`, `shares_outstanding`, `cost_capital`, `tax_rate`
- **Derived (start of year):** `startYear_[item]`
- **Derived (current year):** `currentYear_[item]`
- **Derived (averages):** `avg_[item]`
- **Ratios:** `RATIO_[name]` (e.g., `RATIO_asset_turnover`)

## Key Formulas (Pseudocode)

### Derived Inputs
- `market_capitalization` = `share_price` * `shares_outstanding`
- `currentYear_after_tax_operating_income` = `INC_net` + (1 - `tax_rate`) * `INC_interest_expense`
- `currentYear_daily_sales_average` = `INC_sales` / 365
- `avg_equity` = AVERAGE(`startYear_equity`, `currentYear_equity`)

### Performance
- MVA = `market_capitalization` - `currentYear_equity`
- Market-to-Book = `market_capitalization` / `currentYear_equity`
- EVA = `currentYear_after_tax_operating_income` - (`cost_capital` * `startYear_total_capitalization`)

### Profitability
- ROA = `currentYear_after_tax_operating_income` / `startYear_total_assets`
- ROC = `currentYear_after_tax_operating_income` / `startYear_total_capitalization`
- ROE = `INC_net` / `startYear_equity`

### Efficiency
- Asset Turnover = `INC_sales` / `startYear_total_assets`
- Inventory Turnover = `INC_cost_goods_sold` / `startYear_inventory`
- Profit Margin = `INC_net` / `INC_sales`
- Operating Profit Margin = `currentYear_after_tax_operating_income` / `INC_sales`

### Leverage
- Long-term Debt Ratio = `currentYear_debt_long_term` / (`currentYear_debt_long_term` + `currentYear_equity`)
- Times Interest Earned = `INC_ebit` / `INC_interest_expense`
- Leverage Ratio = `currentYear_assets_total` / `currentYear_equity`

### Liquidity
- Current Ratio = `currentYear_assets_current` / `currentYear_liabilities_current`
- Quick Ratio = (`currentYear_cash_marketable_securities` + `BAL_receivables_current`) / `currentYear_liabilities_current`

### Du Pont
- Du Pont ROA = `RATIO_asset_turnover` * `RATIO_operating_profit_margin`
- Du Pont ROE = `RATIO_leverage` * `RATIO_asset_turnover` * `RATIO_operating_profit_margin` * `RATIO_debt_burden`

## Reference Spreadsheet

The master class spreadsheet with all ratio formulas and a worked example is at:
`BUS-314/_spreadsheets/BUS-314 Accounting & Performance Ratios - MASTER.xlsx`

## How to Help Students

When assisting with this project:

1. **Stage 1 (Memo):** Help frame the company choice and explain why ratio analysis matters. Keep it executive-friendly.
2. **Stage 2 (Spec):** Help structure inputs, named ranges, and calculation flow. Use pseudocode, not cell references.
3. **Stage 3 (Excel):** Help build or debug the spreadsheet. Validate Du Pont decompositions match direct calculations.
4. **Stage 4 (Prompt):** Help write a structured prompt that could regenerate the spreadsheet. Include all financial data values.
5. **Stage 5 (Analysis):** Help interpret ratios and formulate actionable recommendations for the CFO.

## Important Notes

- AI tools are **optional, not required** for any stage of this project.
- Students must document AI usage per course guidelines (`docs/ai-usage-guidelines.md`).
- Financial data should come from real SEC filings or reputable financial data sources.
- Avoid banks, insurance companies, and REITs — their financial statements don't align with these ratios.
