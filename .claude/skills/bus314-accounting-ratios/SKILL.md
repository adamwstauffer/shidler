# BUS-314 Accounting Ratios — Claude Skill

Use this skill when helping students with the BUS-314 accounting ratios project (company selection, Excel model building, specification writing, or final analysis). Activate when working in `BUS-314-International-Corporate-Finance/accounting-ratios/`.

---

## Named Range Conventions

- **Balance Sheet:** `BAL_[item]_[year]` (e.g., `BAL_assets_total_2024`)
- **Income Statement:** `INC_[item]` (e.g., `INC_sales`, `INC_ebit`, `INC_net`)
- **Cash Flow:** `CASH_[item]` (e.g., `CASH_operating`)
- **Market/Analyst:** `share_price`, `shares_outstanding`, `cost_capital`, `tax_rate`
- **Derived (start of year):** `startYear_[item]`
- **Derived (current year):** `currentYear_[item]`
- **Derived (averages):** `avg_[item]`
- **Ratios:** `RATIO_[name]` (e.g., `RATIO_asset_turnover`)

---

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

---

## Reference Spreadsheet

Master class spreadsheet with all ratio formulas and a worked example:
`BUS-314-International-Corporate-Finance/_spreadsheets/BUS-314 Accounting & Performance Ratios - MASTER.xlsx`

---

## How to Help Students

The project uses a **4-stage workflow**: Memo, Excel Build, Spec, Final Analysis.

1. **Stage 1 (Memo):** Help frame the company choice and explain why ratio analysis matters. Keep it executive-friendly.
2. **Stage 2 (Excel Build):** Help build or debug the spreadsheet. Validate Du Pont decompositions match direct calculations. Use named ranges consistently.
3. **Stage 3 (Spec):** Help document the model with post-build reflection. Use pseudocode, not cell references. Guide the "Model Review" section — what worked, what to improve.
4. **Stage 4 (Final Analysis):** Help interpret ratios and formulate actionable recommendations for the CFO. If the student is writing a structured AI prompt, help ensure it includes all financial data values and follows prompt engineering best practices.

## Important Notes

- AI tools are **optional, not required** for any stage of this project.
- Students must document AI usage per course guidelines (`docs/ai-usage-guidelines.md`).
- Financial data should come from real SEC filings or reputable financial data sources.
- Avoid banks, insurance companies, and REITs — their financial statements don't align with these ratios.
