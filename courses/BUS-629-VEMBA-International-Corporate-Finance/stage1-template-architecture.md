# Stage 1: Template Architecture

**Weight:** 20% of project score

---

## Overview

Build a complete accounting ratios spreadsheet template from the ground up — no skeleton, no starter file. The template should be empty of company data but fully structured and ready to receive any company's financials.

## Why this comes first

Designing the container forces you to think about what data you need, how it flows between financial statements, and how ratios connect — before any numbers distract you. This is architectural thinking. You can't write a credible spec (Stage 4) for something you haven't built yourself.

---

## Deliverable

A blank `.xlsx` workbook saved to `models/templates/` in your repository.

**Required components:**
- Financial statement tabs (Balance Sheet, Income Statement, Cash Flow Statement)
- Ratios tab with an input section and all six ratio categories
- Named ranges defined (empty cells, but named)
- Color coding system applied
- Notes tab documenting your layout decisions and named range conventions

---

## Ratio categories

Your template must accommodate all six categories:

| Category | Example Ratios |
|----------|---------------|
| **Performance** | MVA, Market-to-Book, EVA |
| **Profitability** | ROA, ROC, ROE (start-of-year and average-based) |
| **Efficiency** | Asset Turnover, Receivables Turnover, Avg Collection Period, Inventory Turnover, Days in Inventory, Profit Margin, Operating Profit Margin |
| **Leverage** | Long-term Debt Ratio, Debt-Equity Ratio, Total Debt Ratio, Times Interest Earned, Cash Coverage, Debt Burden, Leverage Ratio |
| **Liquidity** | NWC-to-Assets, Current Ratio, Quick Ratio, Cash Ratio |
| **Du Pont** | ROA decomposition (Margin x Turnover), ROE decomposition |

---

## Best practices

These are guidelines, not rigid rules. Use your judgment — but be able to justify your choices in your Notes tab.

### Layout
- One tab per financial statement
- Separate inputs from calculations from outputs
- Consistent flow direction (left-to-right or top-to-bottom); never circular references

### Color coding
| Color | Meaning |
|-------|---------|
| Yellow | Editable input cells (data you'll enter) |
| Blue | Assumptions (tax rate, cost of capital) |
| Green | Formula cells (computed values) |
| Gray | Output / summary cells |

### Named ranges
Use prefixed conventions so ranges are self-documenting:

| Prefix | Source | Examples |
|--------|--------|----------|
| `BAL_` | Balance Sheet | `BAL_assets_total_2025`, `BAL_equity_2024` |
| `INC_` | Income Statement | `INC_sales`, `INC_net`, `INC_ebit` |
| `CASH_` | Cash Flow Statement | `CASH_operating`, `CASH_investing` |
| `RATIO_` | Computed ratios | `RATIO_ROA`, `RATIO_current_ratio` |
| `startYear_` | Prior-year values | `startYear_equity`, `startYear_assets_total` |
| `avg_` | Average values | `avg_total_assets`, `avg_equity` |

### Formatting
- Consistent number formats (thousands separators, decimal places)
- Percentages displayed as percentages, not decimals
- Right-aligned numbers, left-aligned labels
- Freeze panes for row/column headers
- No hardcoded numbers in formula cells — every formula should be traceable

### Auditability
- Every formula references named ranges or clearly labeled cells
- The Notes tab documents any design decisions, naming conventions, or assumptions
- A reviewer should be able to understand your model without asking you questions

---

## Rubric (% of Stage 1 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Structure & Layout | 30% | Logical tab organization; clear separation of inputs, calculations, outputs |
| Named Ranges | 30% | Consistent naming convention; all key cells named; documented in Notes tab |
| Formatting & Professionalism | 20% | Color coding applied; number formats consistent; print-ready appearance |
| Completeness | 20% | All six ratio categories represented; all required inputs have designated cells |
