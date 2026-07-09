# Accounting Ratios — Claude Skill

Use this skill when helping students with the Performance Ratios project (company selection, Excel model building, specification writing, or final analysis). Activate when working in `courses/International-Corporate-Finance/projects/performance-ratios/`. This project is currently taught as BUS 629 (Vietnam EMBA); the original BUS-314 (undergrad) iteration is archived at `_archive/bus314/accounting-ratios/`.

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

Master class spreadsheet with all ratio formulas and a worked example. The BUS-314 copy is archived (superseded by `docs/spreadsheets/Corporate Finance Master Spreadsheets.xlsx`, which is now the current reference — see `docs/decisions/2026-07-08-generic-course-directory-naming.md` item 5):
`docs/spreadsheets/Corporate Finance Master Spreadsheets.xlsx`

---

## How to Help Students

The current (BUS 629) iteration uses a **6-stage workflow** (Stage 0 through Stage 5) — see `stage0-repo-setup.md` … `stage5-llm-analysis-evaluation.md` in `courses/International-Corporate-Finance/projects/performance-ratios/` for the exact deliverables and rubric per stage. In broad strokes:

1. **Repo setup:** GitHub repo + collaborator access.
2. **Template architecture:** Familiarize with the named-range Excel template (see conventions below).
3. **Company selection memo:** Help frame the company choice and explain why ratio analysis matters. Keep it executive-friendly.
4. **Model population + validation:** Help build or debug the spreadsheet. Validate Du Pont decompositions match direct calculations. Use named ranges consistently.
5. **Technical specification:** Help document the model with post-build reflection. Use pseudocode, not cell references.
6. **LLM analysis evaluation:** Help interpret ratios and formulate actionable recommendations, and critically evaluate LLM-generated analysis against the model's actual numbers.

The archived BUS-314 iteration used a simpler 4-stage workflow (Memo, Excel Build, Spec, Final Analysis) — if helping with that legacy material, follow its own stage docs in `_archive/bus314/accounting-ratios/` rather than the mapping above.

## Important Notes

- AI tools are **optional, not required** for any stage of this project.
- Students must document AI usage per course guidelines (`docs/ai-usage-guidelines.md`).
- Financial data should come from real SEC filings or reputable financial data sources.
- Avoid banks, insurance companies, and REITs — their financial statements don't align with these ratios.
