# Microsoft Corporation Ratio Model – Technical Specification

**Created by:** Spear
**Updated by:** Spear
**Date Created:** April 24, 2026
**Date Updated:** April 24, 2026
**Version:** 1.0
**LLM Used:** Claude (Anthropic) — used to assist with spec drafting and model review

**Role:** Financial Analyst / FP&A Analyst
**Audience:** CFO or Director of FP&A

**Purpose:** Provide a professional, quantitative specification documenting the Excel ratio model's analytical structure for computing and interpreting 25+ accounting and performance ratios from Microsoft Corporation's FY2024 financial statements. This post-build spec captures what was built, what was learned, and how the model should be refined for Stage 4.

---

## 1. Problem Statement

Microsoft Corporation (MSFT) is a publicly traded global technology company operating across three segments: cloud infrastructure (Azure), productivity software (Microsoft 365), and gaming (Xbox). This specification outlines the analytical framework for computing 25+ accounting and performance ratios from the company's FY2024 financial statements (fiscal year ended June 30, 2024), with FY2023 (ended June 30, 2023) serving as the start-of-year reference.

The objective is to assess Microsoft's financial health, operational efficiency, capital structure, and value creation using a structured ratio model. All inputs are sourced from the Microsoft 10-K FY2024 filed with the SEC. Results will support a CFO-level briefing in Stage 4, providing evidence-based commentary and strategic recommendations on Microsoft's current financial position.

---

## 2. Inputs (Known Variables)

### Balance Sheet Items (Current Year and Prior Year)

| Variable | Description | Named Range | FY2024 | FY2023 |
|---|---|---|---:|---:|
| Cash & marketable securities | Liquid assets | `BAL_cash_marketable_securities_[year]` | 18,314 | 34,704 |
| Receivables | Accounts receivable | `BAL_receivables_[year]` | 43,482 | 48,688 |
| Inventories | Inventory balance | `BAL_inventories_[year]` | 2,579 | 2,500 |
| Total current assets | Sum of current assets | `BAL_assets_current_[year]` | 88,660 | 107,152 |
| Net tangible fixed assets | PP&E less accumulated depreciation | `BAL_fixed_assets_net_[year]` | 96,028 | 71,800 |
| Intangible assets (goodwill) | Acquired intangibles | `BAL_assets_intangible_[year]` | 119,021 | 67,524 |
| Total assets | All assets | `BAL_assets_total_[year]` | 507,596 | 457,996 |
| Total current liabilities | Short-term obligations | `BAL_liabilities_current_[year]` | 82,588 | 77,652 |
| Long-term debt | Non-current borrowings | `BAL_debt_long_term_[year]` | 42,688 | 41,990 |
| Total liabilities | All liabilities | `BAL_liabilities_total_[year]` | 152,348 | 145,524 |
| Shareholders' equity | Book value of equity | `BAL_equity_shareholders_[year]` | 355,248 | 312,472 |

### Income Statement Items

| Variable | Description | Named Range | FY2024 |
|---|---|---|---:|
| Net sales | Total revenue | `INC_sales` | 245,122 |
| Cost of goods sold | Direct costs | `INC_cost_goods_sold` | 74,114 |
| SG&A expenses | Operating expenses | `INC_sga` | 171,008 |
| Depreciation | Non-cash expense | `INC_depreciation` | 17,645 |
| EBIT | Operating income | `INC_ebit` | 124,222 |
| Other income | Non-operating income | `INC_other_income` | 3,269 |
| Interest expense | Cost of debt | `INC_interest_expense` | 2,935 |
| Taxes | Income tax expense | `INC_taxes` | 16,950 |
| Net income | Bottom line | `INC_net` | 43,517* |
| Dividends | Shareholder distributions | `INC_dividends` | 21,771 |

*The model's Ratios tab uses $43,517M as net income. The Cash Flow Statement records $107,606M as the net income starting line. This discrepancy must be reconciled against the 10-K source before Stage 4. See Section 7.*

### Cash Flow Statement Items

| Variable | Description | Named Range | FY2024 |
|---|---|---|---:|
| Cash from operations | Operating cash flow | `CASH_operating` | 132,760 |
| Capital expenditures | Investment in fixed assets | `CASH_capex` | (44,482) |
| Cash from investments | Total investing cash flow | `CASH_investing` | (55,609) |
| Cash from financing | Total financing cash flow | `CASH_financing` | (44,364) |
| Net change in cash | Period cash change | `CASH_net_change` | 32,787 |

### Market / Analyst Inputs

| Variable | Description | Named Range | Value |
|---|---|---|---|
| Share price | Fiscal year-end closing price | `share_price` | $446.36 |
| Shares outstanding | Total shares (millions) | `shares_outstanding` | 7,433M |
| Cost of capital | Estimated WACC | `cost_capital` | 8.8% |
| Tax rate | Effective rate (FY2024) | `tax_rate` | 16.1% |

---

## 3. Assumptions & Constraints

- All figures are reported in millions of U.S. dollars unless otherwise noted.
- Tax rate is set at 16.1%, reflecting Microsoft's approximate effective rate for FY2024; the statutory 21% federal rate is not used.
- Cost of capital is an analyst-supplied estimate of 8.8% WACC and is not derived within the model.
- Interest is treated on a simple annual basis; no compounding adjustments are applied.
- Start-of-year values use the FY2023 balance sheet as the beginning balance for all FY2024 ratio calculations. Average-based ratios use the mean of FY2023 and FY2024 ending balances.
- Total capitalization is defined as long-term debt plus shareholders' equity; current-portion debt is excluded.
- After-tax operating income (NOPAT approximation) is computed as `INC_net + (1 − tax_rate) × INC_interest_expense`, not from EBIT directly.
- Quick ratio numerator uses cash and receivables only; inventories and other current assets are excluded.
- Market capitalization is point-in-time (fiscal year-end price × shares outstanding); no diluted share count adjustment is applied.
- No off-balance-sheet items, capitalized operating leases, or contingent liabilities are incorporated.

---

## 4. Calculation Flow

### Step 1: Derived Inputs

1. `market_capitalization` = `share_price` × `shares_outstanding`
2. `currentYear_after_tax_operating_income` = `INC_net` + (1 − `tax_rate`) × `INC_interest_expense`
3. `currentYear_daily_sales_average` = `INC_sales` / 365
4. `currentYear_cost_goods_sold_daily` = `INC_cost_goods_sold` / 365
5. `currentYear_working_capital_net` = `BAL_assets_current_2024` − `BAL_liabilities_current_2024`
6. `currentYear_total_capitalization` = `BAL_debt_long_term_2024` + `BAL_equity_shareholders_2024`
7. `startYear_total_capitalization` = `BAL_debt_long_term_2023` + `BAL_equity_shareholders_2023`
8. `avg_equity` = AVERAGE(`BAL_equity_shareholders_2023`, `BAL_equity_shareholders_2024`)
9. `avg_total_assets` = AVERAGE(`BAL_assets_total_2023`, `BAL_assets_total_2024`)
10. `avg_total_capitalization` = AVERAGE(`startYear_total_capitalization`, `currentYear_total_capitalization`)

### Step 2: Performance Ratios

- MVA = `market_capitalization` − `BAL_equity_shareholders_2024`
- Market-to-Book = `market_capitalization` / `BAL_equity_shareholders_2024`
- EVA = `currentYear_after_tax_operating_income` − (`cost_capital` × `startYear_total_capitalization`)

### Step 3: Profitability Ratios

- ROA (start) = `currentYear_after_tax_operating_income` / `BAL_assets_total_2023`
- ROC (start) = `currentYear_after_tax_operating_income` / `startYear_total_capitalization`
- ROE (start) = `INC_net` / `BAL_equity_shareholders_2023`
- ROA (avg) = `currentYear_after_tax_operating_income` / `avg_total_assets`
- ROC (avg) = `currentYear_after_tax_operating_income` / `avg_total_capitalization`
- ROE (avg) = `INC_net` / `avg_equity`

### Step 4: Efficiency Ratios

- Asset Turnover = `INC_sales` / `BAL_assets_total_2023`
- Receivables Turnover = `INC_sales` / `BAL_receivables_2023`
- Average Collection Period = `BAL_receivables_2023` / `currentYear_daily_sales_average`
- Inventory Turnover = `INC_cost_goods_sold` / `BAL_inventories_2023`
- Days in Inventory = `BAL_inventories_2023` / `currentYear_cost_goods_sold_daily`
- Profit Margin = `INC_net` / `INC_sales`
- Operating Profit Margin = `currentYear_after_tax_operating_income` / `INC_sales`

### Step 5: Leverage Ratios

- Long-term Debt Ratio = `BAL_debt_long_term_2024` / (`BAL_debt_long_term_2024` + `BAL_equity_shareholders_2024`)
- Long-term Debt-Equity Ratio = `BAL_debt_long_term_2024` / `BAL_equity_shareholders_2024`
- Total Debt Ratio = `BAL_liabilities_total_2024` / `BAL_assets_total_2024`
- Times Interest Earned = `INC_ebit` / `INC_interest_expense`
- Cash Coverage Ratio = (`INC_ebit` + `INC_depreciation`) / `INC_interest_expense`
- Debt Burden = `INC_net` / `currentYear_after_tax_operating_income`
- Leverage Ratio = `BAL_assets_total_2024` / `BAL_equity_shareholders_2024`

### Step 6: Liquidity Ratios

- NWC-to-Assets = `currentYear_working_capital_net` / `BAL_assets_total_2024`
- Current Ratio = `BAL_assets_current_2024` / `BAL_liabilities_current_2024`
- Quick Ratio = (`BAL_cash_marketable_securities_2024` + `BAL_receivables_2024`) / `BAL_liabilities_current_2024`
- Cash Ratio = `BAL_cash_marketable_securities_2024` / `BAL_liabilities_current_2024`

### Step 7: Du Pont Decomposition

- `RATIO_asset_turnover` → from Step 4
- `RATIO_operating_profit_margin` → from Step 4
- `RATIO_leverage` → from Step 5
- `RATIO_debt_burden` → from Step 5
- Du Pont ROA = `RATIO_asset_turnover` × `RATIO_operating_profit_margin`
- Du Pont ROE = `RATIO_leverage` × `RATIO_asset_turnover` × `RATIO_operating_profit_margin` × `RATIO_debt_burden`

---

## 5. Outputs

| Output | Description | Format | Purpose |
|---|---|---|---|
| Ratio summary table | All 25+ ratios organized by category | Table | Core analytical output |
| Du Pont decomposition | ROA and ROE factor breakdown | Table | Identifies return drivers |
| Formula documentation | Named-range formula for each ratio | Dedicated column | Auditability and reproducibility |
| Color-coded input table | Blue = assumptions; Yellow = financial data; Light yellow = formula outputs | Color scheme | Visual audit trail |
| Executive interpretation | Key findings and recommendations | 1–2 paragraphs | Stage 4 memo input |

**Selected key outputs from the current model:**

- MVA: ~$3.317 trillion | Market-to-Book: 9.34× | EVA: $12,324M
- ROE (start): 13.9% | ROA (start): 9.5% | ROC (start): 12.3%
- Asset Turnover: 0.535× | Operating Margin: 50.7% | Profit Margin: 17.8%
- Current Ratio: 1.07× | Quick Ratio: 0.75× | TIE: 42.3×
- Total Debt Ratio: 30.0% | Leverage Ratio: 1.43×

---

## 7. Model Review — What Worked & What to Improve

**What worked well:**
The named range system is the model's strongest structural feature. Every input has a unique, descriptive name, and all ratio formulas are built exclusively from those ranges, making every output fully traceable without decoding cell references. The balance sheet ties correctly (TA − TL&E = 0), confirming data entry integrity. The Du Pont section cross-references `RATIO_` named outputs rather than re-entering raw figures, eliminating double-entry risk. The three-tier color-coding convention (blue for analyst assumptions, yellow for raw inputs, light yellow for formula outputs) provides a clear visual audit trail and should be preserved in Stage 4.

**What should be changed:**
Two issues require correction before Stage 4. First, the **cash coverage ratio** output of 0.507 matches the operating profit margin rather than a coverage multiple — given Microsoft's minimal debt load, the expected value should be in the 40–50× range, consistent with TIE of 42.3×. The formula denominator (`INC_interest_expense`) likely was not applied correctly and must be verified. Second, there is a **net income discrepancy**: the Ratios tab uses $43,517M, while the Cash Flow Statement records $107,606M as the net income starting line. This mismatch affects ROE, profit margin, debt burden, and EVA, and must be reconciled directly against the 10-K income statement.

The NOPAT approximation should also be improved. The current method (`INC_net + (1 − tax_rate) × INC_interest_expense`) conflates operating and non-operating income. A cleaner formulation is `INC_ebit × (1 − tax_rate)`, which isolates operating performance and is more consistent with standard EVA methodology.

**What would improve auditability:**
A dedicated **Inputs** tab, separate from the Ratios tab, would isolate raw data entry from computed outputs and reduce overwrite risk. A **Checks** section under each ratio category — confirming, for example, that Du Pont ROE ≈ directly computed ROE within rounding tolerance — would catch formula drift automatically. The placeholder `BAL_receivables_YEAR` in the quick ratio formula should be replaced with the explicit `BAL_receivables_2024` named range to eliminate ambiguity.

**Additional analysis worth including:**
Free cash flow (`CASH_operating` + `CASH_capex`) should be computed explicitly to contextualize capital intensity relative to reported earnings. EVA sensitivity to WACC (e.g., at 7.0%, 8.8%, and 10.0%) would stress-test the value creation conclusion. Multi-year trend data for ROE, margins, and leverage would meaningfully strengthen the Stage 4 narrative.

---

## 8. Limitations & Next Steps

This model is limited to a single-year cross-sectional analysis; no multi-year trend data or industry peer benchmarks are incorporated. Off-balance-sheet items — including operating lease obligations and contingent liabilities — are excluded. The WACC is an analyst estimate rather than a model-derived figure, making EVA sensitive to that assumption. Market capitalization is point-in-time and subject to price volatility around the fiscal year-end date.

These limitations frame the Stage 4 work directly. The AI prompt for Stage 4 should instruct the model to: (1) correct the cash coverage formula, (2) reconcile the net income figure against the 10-K, (3) restate NOPAT using the EBIT-based method, (4) compute free cash flow explicitly, and (5) interpret all ratio outputs in the context of Microsoft's competitive position in enterprise cloud and productivity software. The Model Review findings above serve as the explicit improvement directives for the refined Stage 4 build.

---

*Data source: Microsoft Corporation 10-K FY2024, SEC EDGAR. All figures in millions of USD unless noted.*
