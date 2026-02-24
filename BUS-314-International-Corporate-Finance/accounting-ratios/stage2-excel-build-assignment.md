# Stage 2 – Excel Model Build (6 Points)

**Goal:** Transform your Stage 1 memo into a **working Excel model** that computes all accounting and performance ratios from your company's real financial statements.

---

## Scenario

You are continuing in your role as the **Financial Analyst** supporting your CFO. Your Stage 1 memo framed the project — identifying the company, the six ratio categories, and the data sources. Now, in Stage 2, you bring it to life — building a functioning spreadsheet that computes and compares ratios across categories.

**Why build before writing the spec?** You learn the most by doing. Building the model first gives you hands-on experience with the data, the formulas, and the judgment calls involved. When you write your Stage 3 specification afterward, you'll be documenting what you *actually built* — not guessing at what you *might* build. This produces a more precise, reflective, and useful spec.

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

Use **named ranges** following the course convention (e.g., `startYear_equity`, `currentYear_assets_total`, `avg_total_assets`). See the class spreadsheet and `_templates/excel/README.md` for the full naming guide.

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

- **Start from the provided template** (see `_templates/excel/README.md`) or build from scratch using the class spreadsheet as a guide.
- **Keep formulas transparent.** Use readable named ranges. Annotate with brief comments where logic may not be obvious.
- **Check reasonableness.**
  - ROA (start-of-year) and ROA (average) should be close but not identical.
  - Du Pont ROA should match your directly computed ROA.
  - Du Pont ROE should approximate your directly computed ROE.
  - Current ratio < 1 means negative NWC — make sure that matches.
- **Document your work.** Add a "Notes" section or tab with assumptions, data sources, and any adjustments.

---

## Deliverable

- File name: `stage2-model-LASTNAME.xlsx`
- Tabs: Financial statements + Ratios tab + optional Notes sheet
- **Due Date:** TBD
- **Points:** 6

---

## Evaluation

| Criterion | Description | Points |
|-----------|-------------|-------:|
| Structure & Clarity | Logical layout, consistent formatting, labeled inputs | 2 |
| Accuracy | Correct ratio calculations and internal consistency | 2 |
| Named Ranges & Auditability | Named ranges used; formula logic documented | 1 |
| Professionalism | Clear presentation, color coding, business-ready | 1 |

---

## How This Leads to Next Stages

| Stage | What You'll Use |
|-------|-----------------|
| **Stage 3 – Technical Specification** | You'll document your model's structure, formulas, and lessons learned — writing a spec is easier after you've built the thing. |
| **Stage 4 – Final Analysis** | You'll interpret the ratios, write a structured AI prompt, and recommend actions to your CFO. |

> *By completing Stage 2, you gain the hands-on experience that makes your Stage 3 specification precise and reflective — exactly what financial analysts do when documenting models for their teams.*
