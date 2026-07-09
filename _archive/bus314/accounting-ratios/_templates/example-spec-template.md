<div style="border-top: 6px solid #024731; border-bottom: 1px solid #B2B2B2; padding: 12px 0; margin-bottom: 24px; font-family: 'Open Sans', Helvetica, Arial, sans-serif;">
  <div style="color: #024731; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; font-size: 0.85rem;">University of Hawaiʻi at Mānoa · Shidler College of Business</div>
  <div style="color: #000000; font-weight: 700; font-size: 1.25rem; margin-top: 4px;">BUS-314 International Corporate Finance</div>
  <div style="color: #525252; font-weight: 400; font-size: 0.95rem;">Accounting &amp; Performance Ratios Project — Technical Specification</div>
</div>

<!--
BRAND FORMATTING — applied per docs/_branding/design.json
  Primary green ............ #024731  (headings, accents, banner)
  Black .................... #000000  (body text)
  Silver ................... #B2B2B2  (subtle borders, rules)
  Neutral-600 .............. #525252  (secondary text)
  Heading font ............. Open Sans Bold (web) / Avenir Bold (print)
  Body font ................ Open Sans Regular (web) / Avenir Book (print)
  Body minimum size ........ 10pt; 11-12pt preferred for printed copies
  Alignment ................ Flush left, ragged right
  Accessibility ............ ADA-compliant contrast; no red body type
-->

# [COMPANY NAME] ([TICKER]) — Accounting & Performance Ratio Model · Technical Specification

> <span style="color:#024731; font-weight:700;">Post-build specification</span> documenting the Stage 2 Excel model, validating it against the data, and articulating the refinements required for production use. Drives the Stage 4 AI prompt and final analysis.

| Field | Value |
|------|------|
| **Created by** | [name] |
| **Updated by** | [name] |
| **Date Created** | [YYYY-MM-DD] |
| **Date Updated** | [YYYY-MM-DD] |
| **Version** | [0.0] |
| **LLM Used** (optional) | [LLM name and how it was used] |
| **Role** | Financial Analyst / FP&A Analyst |
| **Audience** | CFO / Director of FP&A |
| **Companion Workbook** | `_scenarios/BUS314_[TICKER]_Scenario.xlsx` (or student build) |

---

## 1. Problem Statement

Briefly restate the company, time period, and analytical objective in professional terms (3–5 sentences).

<details>
<summary><span style="color:#024731; font-weight:600;">Example phrasing</span></summary>

> [Company] is a publicly traded [industry] company. This specification documents the analytical framework for computing the full suite of 25+ accounting and performance ratios from the company's FY[year] financial statements, with FY[year-1] as the prior-year comparator. The model supports [decision context — e.g., CFO briefing, board presentation, investor relations] and provides the input structure for the Stage 4 AI-assisted executive memo.
</details>

**Include:**
- Company name and industry
- Fiscal years under review (current and comparator)
- Analytical objective (e.g., assess financial health, benchmark performance, identify improvement areas)
- Decision context and downstream use

---

## 2. Inputs (Known Variables)

All inputs are sourced from the company's 10-K (SEC EDGAR) unless otherwise noted. Figures are in $millions except share price (USD) and shares outstanding (millions). Market and analyst inputs are the only cells an analyst should adjust for scenario work.

> <span style="color:#024731;">**Naming-convention decoder.**</span> Raw inputs use the year-suffixed form `BAL_[item]_[yr]`. The calculation flow in §4 refers to those same cells through two aliases: `startYear_[item]` ≡ `BAL_[item]_[prior]` and `currentYear_[item]` ≡ `BAL_[item]_[curr]`. Income-statement and cash-flow items (`INC_*`, `CASH_*`) have no year suffix — the model is single-year for those statements. Define both aliases as Excel named ranges pointing at the same cells so §2 and §4 stay readable.

### 2.1 Balance Sheet Items (Current and Prior Year)

| Variable | Description | Named Range | Year(s) | FY[curr] | FY[prior] |
|----------|-------------|-------------|---------|---------:|----------:|
| Cash & marketable securities | Liquid assets | `BAL_cash_marketable_securities_[yr]` | Both | | |
| Receivables | Accounts receivable | `BAL_receivables_[yr]` | Both | | |
| Inventories | Inventory balance | `BAL_inventories_[yr]` | Both | | |
| Total current assets | Sum of current assets | `BAL_assets_current_[yr]` | Current | | |
| Net tangible fixed assets | PP&E less accumulated depreciation | `BAL_fixed_assets_net_[yr]` | Current | | |
| Total assets | All assets | `BAL_assets_total_[yr]` | Both | | |
| Total current liabilities | Short-term obligations | `BAL_liabilities_current_[yr]` | Current | | |
| Accounts payable | Supplier balances (needed for DPO / cash-conversion-cycle extension — §6.2) | `BAL_accounts_payable_[yr]` | Both | | |
| Long-term debt | Non-current borrowings | `BAL_debt_long_term_[yr]` | Both | | |
| Total liabilities | All liabilities | `BAL_liabilities_total_[yr]` | Current | | |
| Shareholders' equity | Book value of equity | `BAL_equity_shareholders_[yr]` | Both | | |

### 2.2 Income Statement Items (Current Year)

| Variable | Description | Named Range | FY[curr] |
|----------|-------------|-------------|---------:|
| Net sales | Total revenue | `INC_sales` | |
| Cost of goods sold | Direct costs | `INC_cost_goods_sold` | |
| SG&A expenses | Operating expenses | `INC_sga` | |
| Depreciation | Non-cash expense | `INC_depreciation` | |
| EBIT | Operating income | `INC_ebit` | |
| Other income | Non-operating income | `INC_other_income` | |
| Interest expense | Cost of debt | `INC_interest_expense` | |
| Taxes | Income tax expense | `INC_taxes` | |
| Net income | Bottom line | `INC_net` | |
| Dividends | Shareholder distributions | `INC_dividends` | |

### 2.3 Cash Flow Statement Items (Current Year)

| Variable | Description | Named Range | FY[curr] |
|----------|-------------|-------------|---------:|
| Cash from operations | Operating cash flow | `CASH_operating` | |
| Cash from investing | Investing cash flow | `CASH_investments` | |

### 2.4 Market / Analyst Inputs (Assumptions)

| Variable | Description | Named Range | Value |
|----------|-------------|-------------|------:|
| Share price | FY-end closing price | `share_price` | |
| Shares outstanding (M) | Diluted weighted avg | `shares_outstanding` | |
| Cost of capital | Estimated WACC | `cost_capital` | |
| Tax rate | Effective or statutory | `tax_rate` | |

> <span style="color:#024731;">**Tip:**</span> Keep labels short and standardized — these names become Excel named ranges *and* AI prompt parameters in Stage 4.

---

## 3. Assumptions & Constraints

State every convention used. Clarity here is what makes the model reproducible.

- All figures reported in $millions unless otherwise noted.
- Tax rate: [state whether statutory 21%, effective rate from financials, or blended — and why].
- Cost of capital: [state value and method — working WACC, CAPM refinement, class estimate].
- Interest quoted on a simple annual basis; no accrued-interest adjustment.
- Start-of-year balances come from the prior fiscal year's balance sheet.
- "Average" denominators use the arithmetic mean of start-of-year and current-year balances.
- Depreciation figure taken from [Income Statement / Cash Flow Statement]; any reconciliation noted.
- No off-balance-sheet items (unsecured guarantees, purchase commitments, contingent liabilities) included.
- [Industry-specific notes — e.g., for tech: "negative retained earnings reflect cumulative buybacks, not losses"; for retail: "inventory mix between finished goods and WIP not separated"].

---

## 4. Calculation Flow

Described in named-range pseudocode so the logic is portable to Excel, Python, or an AI prompt. All formulas assume the naming conventions in §2.

### Step 1 — Derived Inputs

1. `market_capitalization` = `share_price` × `shares_outstanding`
2. `currentYear_after_tax_operating_income` = `INC_net` + (1 − `tax_rate`) × `INC_interest_expense`
3. `currentYear_daily_sales_average` = `INC_sales` / 365
4. `currentYear_cost_goods_sold_daily` = `INC_cost_goods_sold` / 365
5. `currentYear_working_capital_net` = `currentYear_assets_current` − `currentYear_liabilities_current`
6. `startYear_total_capitalization` = `startYear_debt_long_term` + `startYear_equity`
7. `currentYear_total_capitalization` = `currentYear_debt_long_term` + `currentYear_equity`
8. `avg_equity` = AVERAGE(`startYear_equity`, `currentYear_equity`)
9. `avg_total_assets` = AVERAGE(`startYear_total_assets`, `currentYear_assets_total`)
10. `avg_total_capitalization` = AVERAGE(`startYear_total_capitalization`, `currentYear_total_capitalization`)

### Step 2 — Performance Ratios

- **MVA** = `market_capitalization` − `currentYear_equity`
- **Market-to-Book** = `market_capitalization` / `currentYear_equity`
- **EVA** = `currentYear_after_tax_operating_income` − (`cost_capital` × `startYear_total_capitalization`)

### Step 3 — Profitability Ratios (start-of-year and average denominators)

- **ROA** = `currentYear_after_tax_operating_income` / `startYear_total_assets`
- **ROC** = `currentYear_after_tax_operating_income` / `startYear_total_capitalization`
- **ROE** = `INC_net` / `startYear_equity`
- **ROA [avg]** = `currentYear_after_tax_operating_income` / `avg_total_assets`
- **ROC [avg]** = `currentYear_after_tax_operating_income` / `avg_total_capitalization`
- **ROE [avg]** = `INC_net` / `avg_equity`

### Step 4 — Efficiency Ratios

- **Asset Turnover** = `INC_sales` / `startYear_total_assets` → `RATIO_asset_turnover`
- **Receivables Turnover** = `INC_sales` / `startYear_receivables`
- **Avg Collection Period (days)** = `startYear_receivables` / `currentYear_daily_sales_average`
- **Inventory Turnover** = `INC_cost_goods_sold` / `startYear_inventory`
- **Days in Inventory** = `startYear_inventory` / `currentYear_cost_goods_sold_daily`
- **Profit Margin** = `INC_net` / `INC_sales`
- **Operating Profit Margin** = `currentYear_after_tax_operating_income` / `INC_sales` → `RATIO_operating_profit_margin`

### Step 5 — Leverage Ratios

- **Long-term Debt Ratio** = `currentYear_debt_long_term` / (`currentYear_debt_long_term` + `currentYear_equity`)
- **Debt-Equity Ratio** = `currentYear_debt_long_term` / `currentYear_equity`
- **Total Debt Ratio** = `currentYear_liabilities_total` / `currentYear_assets_total`
- **Times Interest Earned** = `INC_ebit` / `INC_interest_expense`
- **Cash Coverage Ratio** = (`INC_ebit` + `INC_depreciation`) / `INC_interest_expense`
- **Debt Burden** = `INC_net` / `currentYear_after_tax_operating_income` → `RATIO_debt_burden`
- **Leverage Ratio** = `currentYear_assets_total` / `currentYear_equity` → `RATIO_leverage`

### Step 6 — Liquidity Ratios

- **NWC to Assets** = `currentYear_working_capital_net` / `currentYear_assets_total`
- **Current Ratio** = `currentYear_assets_current` / `currentYear_liabilities_current`
- **Quick Ratio** = (`currentYear_cash_marketable_securities` + `currentYear_receivables`) / `currentYear_liabilities_current`
- **Cash Ratio** = `currentYear_cash_marketable_securities` / `currentYear_liabilities_current`

### Step 7 — Du Pont Decomposition

- **Du Pont ROA** = `RATIO_asset_turnover` × `RATIO_operating_profit_margin`
- **Du Pont ROE** = `RATIO_leverage` × `RATIO_asset_turnover` × `RATIO_operating_profit_margin` × `RATIO_debt_burden`

> <span style="color:#024731;">**Reasonableness checks:**</span> Du Pont ROA should tie to direct ROA within rounding. Du Pont ROE may diverge from direct ROE when leverage uses current-year equity while ROE uses start-of-year equity — flag any divergence greater than ~3 percentage points for review.

---

## 5. Outputs

| Output | Description | Format | Purpose |
|--------|-------------|--------|---------|
| Ratio summary table | All 25 ratios in category-grouped blocks with computed value + named-range formula | Table on `Ratios` tab | Core analytical output |
| Du Pont panel | ROA and ROE broken into turnover, margin, leverage, debt-burden components | Sub-table | Isolates return drivers |
| Formula-reference column | Named-range formula shown alongside every output cell | In-table column | Auditability / AI prompt fodder |
| Color-coded input map | <span style="background:#FFFF00;">Yellow</span> = raw data inputs, <span style="color:#0000FF;">Blue</span> = analyst assumptions, <span style="color:#024731;">Green</span> = computed formulas, Gray = derived/intermediate values | Cell formatting | Signals what can and cannot be changed |
| Executive summary (Stage 4) | 1–2 paragraph narrative tying ratios to CFO recommendations | Separate memo | Downstream deliverable |

### 5.1 Computed Output Values

Record each ratio's computed value here once the model is built — this block serves as a regression checkpoint for future versions.

| Category | Ratio | Value | Notes |
|----------|-------|------:|-------|
| Performance | MVA | | |
| Performance | Market-to-Book | | |
| Performance | EVA | | |
| Profitability | ROA (SOY) | | |
| Profitability | ROC (SOY) | | |
| Profitability | ROE (SOY) | | |
| Profitability | ROA (avg) | | |
| Profitability | ROC (avg) | | |
| Profitability | ROE (avg) | | |
| Efficiency | Asset Turnover | | |
| Efficiency | Receivables Turnover | | |
| Efficiency | Avg Collection Period | | |
| Efficiency | Inventory Turnover | | |
| Efficiency | Days in Inventory | | |
| Efficiency | Profit Margin | | |
| Efficiency | Operating Profit Margin | | |
| Leverage | Long-term Debt Ratio | | |
| Leverage | Debt-Equity Ratio | | |
| Leverage | Total Debt Ratio | | |
| Leverage | Times Interest Earned | | |
| Leverage | Cash Coverage Ratio | | |
| Leverage | Debt Burden | | |
| Leverage | Leverage Ratio | | |
| Liquidity | NWC to Assets | | |
| Liquidity | Current Ratio | | |
| Liquidity | Quick Ratio | | |
| Liquidity | Cash Ratio | | |
| Du Pont | Du Pont ROA | | |
| Du Pont | Du Pont ROE | | |

---

## 6. Model Review — What Worked & What to Improve

Reflect candidly on the Stage 2 model. This section is what makes a *post-build* spec more valuable than a pre-build plan.

### 6.1 What Worked

- [Named-range discipline — cross-reading between the Ratios tab and this spec should be one-to-one]
- [Du Pont ROA tie-out — turnover × margin vs. direct ROA within rounding]
- [Segregation of start-of-year / current-year / average blocks]
- [Other wins — formula readability, color coding, etc.]

### 6.2 What to Improve

- **Du Pont ROE denominator mismatch.** If leverage uses current-year equity while ROE uses start-of-year equity, the Du Pont product will diverge from direct ROE whenever equity changes materially year-over-year (common after buybacks or losses). Fix: add a parallel `RATIO_leverage_start` and a matching Du Pont ROE variant; show both.
- **Liquidity ratios need context.** Current ratio < 1 or negative NWC is not automatically a red flag — add a **cash conversion cycle** (DIO + DSO − DPO) so the liquidity block is interpretable rather than alarming. DPO requires `BAL_accounts_payable_[yr]` (now included in §2.1) plus `currentYear_cost_goods_sold_daily`.
- **Sensitivity panel missing.** EVA is highly sensitive to `cost_capital`, and profitability is sensitive to `tax_rate`. Add a two-variable data table (`cost_capital` × `tax_rate`) for the performance block.
- **Formula-documentation column should be live.** Today the "Named Range Formula" column is a static string. Use `=FORMULATEXT(<output_cell>)` so documentation stays synchronized if a formula is ever edited.
- **Peer / trend context is absent.** Ratios without a comparator are hard to act on. Add either (a) a second comparator column for a peer, or (b) a multi-year trend strip (FY-2 through FY-0).
- **Effective vs. statutory tax toggle.** Expose both rates as switchable assumptions for segment or multi-year analysis.
- [Other company-specific improvements identified during the build]

### 6.3 Auditability Checklist

- [ ] Every ratio has a named-range formula shown in an adjacent column
- [ ] Cell colors match the legend: yellow inputs, blue assumptions, green formulas, gray outputs
- [ ] Du Pont ROA ties to direct ROA within 0.1 percentage point
- [ ] No hardcoded numbers inside ratio formulas — only named ranges
- [ ] Notes tab documents data source, access date, and any manual adjustments

---

## 7. Limitations & Next Steps

**Limitations.** This specification does not incorporate:
- Peer benchmarking
- Multi-year trend analysis
- Off-balance-sheet items, contingent liabilities, or segment-level ratios
- FX-adjusted international revenue metrics
- Sensitivity analysis on `cost_capital`, `tax_rate`, or share price

**Next steps — Stage 4 will:** (a) translate the ratio outputs into a structured CFO recommendation memo, (b) formalize the AI prompt using this spec's Calculation Flow as the instruction block and §6.2 as the improvement brief, and (c) incorporate at least one of the improvements flagged in §6.2.

---

## 8. Writing a Strong Specification

> <span style="color:#024731; font-weight:600;">The spec should read like a handoff document, not a lab notebook.</span>

- **Communicate like a professional:** clear, structured, no filler.
- **Think one stage ahead:** the spec feeds directly into the Stage 4 AI prompt and final analysis.
- **Be internally consistent:** variables, labels, and steps must align with the actual model.
- **Be reproducible:** a new analyst should be able to rebuild the model from this spec without help.
- **Be reflective:** the Model Review section should show honest assessment, not self-congratulation.
- **Be executive-relevant:** the CFO should understand *what was built* and *why it matters*.

---

## 9. How This Sets Up Stage 4

| What's Written in Stage 3 | What It Enables in Stage 4 |
|---------------------------|----------------------------|
| Named ranges with precise definitions | AI uses standardized variable names; no improvisation |
| Step-by-step calculation flow | AI generates correct, auditable formulas |
| Model review and improvement notes | AI builds the *improved* version, not just a replica |
| Explicit output requirements | AI produces the exact tables and sections needed |
| Computed output values (§5.1) | Regression checkpoints for the refined model |

---

## Appendix A — Change Log

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | [YYYY-MM-DD] | [name] | Initial post-build draft |
|  |  |  |  |

---

<div style="border-top: 1px solid #B2B2B2; padding-top: 8px; margin-top: 24px; font-family: 'Open Sans', Helvetica, Arial, sans-serif; font-size: 0.8rem; color: #525252;">
  Prepared per UH Mānoa brand standards (<code>docs/_branding/design.json</code>). Primary green <span style="display:inline-block; width:10px; height:10px; background:#024731; border:1px solid #000;"></span> <code>#024731</code> · Body type Open Sans Regular, 11–12 pt for printed copies · ADA-compliant contrast · Flush-left, ragged-right alignment.
</div>
