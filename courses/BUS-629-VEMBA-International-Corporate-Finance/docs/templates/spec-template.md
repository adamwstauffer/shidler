# [Specification Title]

**Author:** [Your Name]
**Date:** [YYYY-MM-DD]
**Version:** [1.0]
**Company:** [Company Name, Ticker, Exchange]

---

## 1. Scope & Objective

> What this specification defines. Company name, fiscal period, reporting standard (GAAP/IFRS/VAS), reporting currency, and the analytical objective. Who is the intended audience for the output?

---

## Part A — Model Specification

### 2. Model Architecture

> Define the spreadsheet structure: tab layout, what each tab contains, how data flows between tabs. Specify color coding conventions, input/calculation/output separation, and formatting requirements.

### 3. Data Inputs

> Complete table of every financial data point required, organized by source. All values stated explicitly — the executor does not look up, infer, or estimate any data.

| Named Range | Source | Value | Unit |
|-------------|--------|-------|------|
| `BAL_assets_total_2025` | Balance Sheet | | |
| `INC_sales` | Income Statement | | |
| `CASH_operating` | Cash Flow | | |
| `share_price` | Market Data | | |

### 4. Derived Inputs

> Computed intermediate values (averages, start-of-year figures, daily rates, after-tax operating income) with explicit formulas in named-range notation.

### 5. Ratio Definitions & Formulas

> Every ratio organized by category. For each ratio: formula in named-range notation, expected unit, and brief interpretation guide.

**Performance**
| Ratio | Formula | Unit |
|-------|---------|------|
| MVA | | Currency |
| Market-to-Book | | x |
| EVA | | Currency |

**Profitability**
| Ratio | Formula | Unit |
|-------|---------|------|
| ROA | | % |
| ROC | | % |
| ROE | | % |

**Efficiency**
| Ratio | Formula | Unit |
|-------|---------|------|
| Asset Turnover | | x |
| Receivables Turnover | | x |
| Inventory Turnover | | x |

**Leverage**
| Ratio | Formula | Unit |
|-------|---------|------|
| Debt Ratio | | % |
| Times Interest Earned | | x |
| Debt Burden | | x |

**Liquidity**
| Ratio | Formula | Unit |
|-------|---------|------|
| Current Ratio | | x |
| Quick Ratio | | x |
| Cash Ratio | | x |

**Du Pont**
| Ratio | Formula | Unit |
|-------|---------|------|
| ROA Decomposition | | % |
| ROE Decomposition | | % |

### 6. Validation Rules

> Internal consistency checks the executor must verify (Du Pont vs. direct calculations, Balance Sheet balance, etc.)

---

## Part B — Analysis Specification

### 7. Analysis Requirements

> For each ratio category: what to interpret, benchmarks or comparison targets, and cross-category connections to examine.

### 8. Du Pont Decomposition

> Specific instructions for ROE breakdown analysis. Which component is the primary driver? Is the balance sustainable?

### 9. Strategic Recommendations

> Requirements for recommendations: how many (3–5), evidence standard, actionable specificity.

### 10. Output Format

> Exact structure of the deliverable: sections, order, length targets, tone, audience, how to present ratio results.

---

## References

> Data sources, annual reports, and materials used to populate this specification.
