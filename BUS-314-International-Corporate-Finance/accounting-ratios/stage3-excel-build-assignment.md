# Stage 3 – Excel Model Build (4 Points)

**Goal:** Transform your Stage 2 technical specification into a **working Excel model** that computes all accounting and performance ratios from your company's real financial statements.

---

## Scenario

You are continuing in your role as the **Financial Analyst** supporting your CFO. Your Stage 1 memo framed the project. Your Stage 2 specification outlined the analytical plan. Now, in Stage 3, you bring it to life — turning your plan into a functioning spreadsheet that computes and compares ratios across categories.

---

## Include in Your Model

### 1. Financial Statement Data Tabs

Create organized input tabs for your company's data:

- **Balance Sheet** – Current year and prior year, with all line items needed for ratio calculations.
- **Income Statement** – Revenue through net income, including EBIT, depreciation, interest, and taxes.
- **Cash Flow Statement** – Operating, investing, and financing cash flows.

Use **yellow highlighting** for all editable input cells. Label every line item clearly.

### 2. Ratios Tab — Inputs Section

Pull all raw data into a single **Inputs** section on your Ratios tab:

- **Market / Analyst Inputs:** Share price, shares outstanding, cost of capital, tax rate, market capitalization.
- **Start-of-Year Items:** Equity, inventories, receivables, total assets, total capitalization (all from prior-year Balance Sheet).
- **Current-Year Items:** After-tax operating income, daily sales, book equity, cash, current assets/liabilities, long-term debt, NWC, total assets, total capitalization, total liabilities.
- **Mixed-Year Items:** Average equity, average total assets, average total capitalization, long-term debt + equity.

Use **named ranges** matching your Stage 2 spec (e.g., `startYear_equity`, `currentYear_assets_total`, `avg_total_assets`).

### 3. Ratios Tab — Ratio Calculations

Compute all ratios organized by category. Each ratio should show:
- The ratio name
- The computed output value
- The formula in named-range notation (e.g., `INC_net / startYear_equity`)

**Categories:**

| Category | Ratios |
|----------|--------|
| **Performance** | Market Value Added (MVA), Market-to-Book, Economic Value Added (EVA) |
| **Profitability** | ROA, ROC, ROE (start-of-year); ROA, ROC, ROE (average-based) |
| **Efficiency** | Asset Turnover, Receivables Turnover, Avg Collection Period, Inventory Turnover, Days in Inventory, Profit Margin, Operating Profit Margin |
| **Leverage** | Long-term Debt Ratio, Debt-Equity Ratio, Total Debt Ratio, Times Interest Earned, Cash Coverage, Debt Burden, Leverage Ratio |
| **Liquidity** | NWC-to-Assets, Current Ratio, Quick Ratio, Cash Ratio |
| **Du Pont** | ROA decomposition, ROE decomposition |

### 4. Outputs Section

A clean summary section showing:
- All ratio values in a formatted table
- Color coding: **Yellow** = Inputs, **Blue** = Assumptions, **Green** = Formulas, **Gray** = Outputs
- Named range column documenting each formula for auditability

### 5. Optional Enhancements

- Comparison to industry averages or a competitor
- Trend analysis (2+ years of data)
- Charts or visualizations (bar chart of ratio categories, Du Pont waterfall)
- A "Notes" sheet documenting assumptions and data sources

---

## Instructions & Hints

- **Start from the provided template** (see `_templates/excel/README.md`) or build from scratch following your Stage 2 spec.
- **Follow your Stage 2 spec closely.** Every variable and step in your plan should appear in your spreadsheet.
- **Keep formulas transparent.** Use readable named ranges. Annotate with brief comments where logic may not be obvious.
- **Check reasonableness.**
  - ROA (start-of-year) and ROA (average) should be close but not identical.
  - Du Pont ROA should match your directly computed ROA.
  - Du Pont ROE should approximate your directly computed ROE.
  - Current ratio < 1 means negative NWC — make sure that matches.
- **Document your work.** Add a "Notes" section or tab with assumptions, data sources, and any adjustments.

---

## Deliverable

- File name: `stage3-model-LASTNAME.xlsx`
- Tabs: Financial statements + Ratios tab + optional Notes sheet
- **Due Date:** TBD
- **Points:** 4

---

## Evaluation

| Criterion | Description | Points |
|-----------|-------------|-------:|
| Structure & Clarity | Logical layout, consistent formatting, labeled inputs | 1 |
| Accuracy | Correct ratio calculations and internal consistency | 1 |
| Named Ranges & Auditability | Named ranges used; formula logic documented | 1 |
| Professionalism | Clear presentation, color coding, business-ready | 1 |

---

## How This Leads to Next Stages

| Stage | What You'll Use |
|-------|-----------------|
| **Stage 4 – Prompt Engineering** | You'll use your model logic to design a prompt that generates this spreadsheet automatically. |
| **Stage 5 – Final Analysis** | You'll interpret the ratios and recommend actions to your CFO. |

> *By completing Stage 3, you bridge the gap between your written specification and a functioning analytical tool — exactly what financial analysts do before presenting to senior management.*
