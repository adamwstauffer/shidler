# [Spec Title] – Technical Specification

**Created by:** [name]
**Updated by:** [name]
**Date Created:** [date]
**Date Updated:** [date]
**Version:** [0.0]
**LLM Used:** [LLM] (optional — if an LLM was used)

**Role:** Financial Analyst / FP&A Analyst
**Audience:** CFO or Director of FP&A

**Purpose:** Provide a professional, quantitative specification outlining the analytical structure for computing and interpreting accounting and performance ratios from a public company's financial statements.

---

## 1. Problem Statement

Briefly restate the company, time period, and analytical objective in professional terms.

Example phrasing:
> [Company Name] is a publicly traded [industry] company. This specification outlines the analytical framework for computing 25+ accounting and performance ratios from the company's FY[year] financial statements, enabling management to assess financial health, operational efficiency, leverage, and value creation.

Include:
- Company name and industry
- Fiscal year(s) under review
- Objective (e.g., assess financial health, benchmark performance, identify areas for improvement)
- Decision context (CFO briefing, board presentation, investor relations)

---

## 2. Inputs (Known Variables)

Create a clean, professional input table. This will become the foundation for your spreadsheet and future AI prompts. Group by source.

### Balance Sheet Items (Current Year and Prior Year)

| Variable | Description | Named Range | Year | Example |
|----------|-------------|-------------|------|---------|
| Cash & marketable securities | Liquid assets | `BAL_cash_marketable_securities_[year]` | Both | 2,577 |
| Receivables | Accounts receivable | `BAL_receivables_[year]` | Both | 498 |
| Inventories | Inventory balance | `BAL_inventories_[year]` | Both | 8,992 |
| Total current assets | Sum of current assets | `BAL_assets_current_[year]` | Both | 12,902 |
| Net tangible fixed assets | PP&E less depreciation | `BAL_fixed_assets_net_[year]` | Current | 28,519 |
| Total assets | All assets | `BAL_assets_total_[year]` | Both | 42,779 |
| Total current liabilities | Short-term obligations | `BAL_liabilities_current_[year]` | Current | 14,487 |
| Long-term debt | Non-current borrowings | `BAL_debt_long_term_[year]` | Both | 11,338 |
| Total liabilities | All liabilities | `BAL_liabilities_total_[year]` | Current | 30,946 |
| Shareholders' equity | Book value of equity | `BAL_equity_shareholders_[year]` | Both | 11,833 |

### Income Statement Items

| Variable | Description | Named Range | Example |
|----------|-------------|-------------|---------|
| Net sales | Total revenue | `INC_sales` | 78,112 |
| Cost of goods sold | Direct costs | `INC_cost_goods_sold` | 54,864 |
| SG&A expenses | Operating expenses | `INC_sga` | 16,233 |
| Depreciation | Non-cash expense | `INC_depreciation` | 2,357 |
| EBIT | Operating income | `INC_ebit` | 4,658 |
| Other income | Non-operating income | `INC_other_income` | 21 |
| Interest expense | Cost of debt | `INC_interest_expense` | 477 |
| Taxes | Income tax expense | `INC_taxes` | 921 |
| Net income | Bottom line | `INC_net` | 3,281 |
| Dividends | Shareholder distributions | `INC_dividends` | 1,330 |

### Cash Flow Statement Items

| Variable | Description | Named Range | Example |
|----------|-------------|-------------|---------|
| Cash from operations | Operating cash flow | `CASH_operating` | 7,117 |
| Cash from investments | Investing cash flow | `CASH_investments` | -2,944 |

### Market / Analyst Inputs

| Variable | Description | Named Range | Example |
|----------|-------------|-------------|---------|
| Share price | Market price per share | `share_price` | 109.53 |
| Shares outstanding | Total shares (millions) | `shares_outstanding` | 500 |
| Cost of capital | WACC or required return | `cost_capital` | 7.6% |
| Tax rate | Statutory or effective rate | `tax_rate` | 21% |

> *Tip:* Keep labels short and standardized. These names will become Excel named ranges and AI prompt parameters.

---

## 3. Assumptions & Constraints

State all conventions used. Clarity here ensures reproducibility.

Example list:
- All figures reported in millions unless otherwise noted.
- Tax rate assumed at statutory 21% (or effective rate from financial statements).
- Cost of capital estimated at [X]% based on [method/assumption].
- Interest rates quoted on a simple annual basis.
- Depreciation figure taken from [Income Statement / Cash Flow Statement].
- Start-of-year values use prior fiscal year's Balance Sheet.
- No off-balance-sheet items or contingent liabilities included.

---

## 4. Calculation Flow

Describe the logic and sequencing of your analysis — as if briefing a junior analyst or AI model builder. Use named-range pseudocode.

### Step 1: Derived Inputs
1. Compute `market_capitalization` = `share_price` x `shares_outstanding`
2. Compute `currentYear_after_tax_operating_income` = `INC_net` + (1 - `tax_rate`) x `INC_interest_expense`
3. Compute daily figures: `currentYear_daily_sales_average` = `INC_sales` / 365
4. Compute averages: `avg_equity` = AVERAGE(`startYear_equity`, `currentYear_equity`)
5. Compute `currentYear_working_capital_net` = `currentYear_assets_current` - `currentYear_liabilities_current`

### Step 2: Performance Ratios
- MVA = `market_capitalization` - `currentYear_equity`
- Market-to-Book = `market_capitalization` / `currentYear_equity`
- EVA = `currentYear_after_tax_operating_income` - (`cost_capital` x `startYear_total_capitalization`)

### Step 3: Profitability Ratios
- ROA = `currentYear_after_tax_operating_income` / `startYear_total_assets`
- ROC = `currentYear_after_tax_operating_income` / `startYear_total_capitalization`
- ROE = `INC_net` / `startYear_equity`
- (Repeat with average denominators)

### Step 4: Efficiency Ratios
- Asset Turnover = `INC_sales` / `startYear_total_assets`
- Receivables Turnover, Inventory Turnover, margins, etc.

### Step 5: Leverage Ratios
- Long-term Debt Ratio, Debt-Equity, Total Debt Ratio
- Times Interest Earned, Cash Coverage, Debt Burden, Leverage Ratio

### Step 6: Liquidity Ratios
- NWC-to-Assets, Current Ratio, Quick Ratio, Cash Ratio

### Step 7: Du Pont Decomposition
- Du Pont ROA = Asset Turnover x Operating Profit Margin
- Du Pont ROE = Leverage x Asset Turnover x Operating Profit Margin x Debt Burden

---

## 5. Outputs

| Output | Description | Format | Purpose |
|--------|-------------|--------|---------|
| Ratio summary table | All 25+ ratios organized by category | Table | Core analytical output |
| Du Pont decomposition | ROA and ROE breakdown | Table | Identifies return drivers |
| Formula documentation | Named-range formula for each ratio | Column | Auditability |
| Executive summary | Key findings and recommendations | 1–2 paragraphs | Stage 5 input |

---

## 6. Limitations & Next Steps

Briefly note any analytical limits and outline your next step.

Example phrasing:
> This specification does not incorporate industry peer comparisons, multi-year trend analysis, or off-balance-sheet items. The next phase will involve constructing an Excel model implementing this logic to compute all ratios from the company's actual financial data.

---

## Writing a Strong Specification

**Your spec should:**
- **Communicate like a professional:** clear, structured, and jargon-free.
- **Think one stage ahead:** your spec should feed directly into your Excel build or AI prompt.
- **Be internally consistent:** variables, labels, and steps must align.
- **Be reproducible:** a new analyst should be able to implement your plan without your help.
- **Be executive-relevant:** the CFO should understand *what you're doing* and *why it matters*.

---

## How This Sets You Up for Later Stages

| Stage | What This Spec Enables |
|-------|------------------------|
| **Stage 3** | Each "Input" and "Output" becomes a spreadsheet cell or named range. |
| **Stage 4** | Your "Calculation Flow" becomes an AI prompt instruction block. |
| **Stage 5** | Your "Outputs" drive the interpretation and recommendation. |

> *Treat your specification as the bridge between business insight and technical execution — the CFO should be confident your plan is sound even before seeing the numbers.*
