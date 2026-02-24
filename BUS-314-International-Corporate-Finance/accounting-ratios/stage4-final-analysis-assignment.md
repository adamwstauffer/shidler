# Stage 4 – Final Analysis, Prompt Engineering & Recommendation (10 Points)

**Due:** TBD

## Goal

Deliver a polished, executive-ready memo summarizing your accounting ratio analysis and providing strategic recommendations. As part of this deliverable, you will also write a **structured AI prompt** that could regenerate your spreadsheet model — demonstrating your ability to convert domain knowledge into machine-readable instructions.

This stage combines quantitative rigor, interpretation, communication, and AI fluency — exactly what senior finance leaders expect from modern analysts.

**Hint:** Have your LLM generate a draft based on your Stage 2 spreadsheet output, then refine it with your own analysis and judgment. If you don't have AI access, write the analysis directly from your spreadsheet results and submit the prompt as a standalone document.

---

## Deliverable Requirements (2–4 page `.md` file uploaded to GitHub)

Must include:

---

### A. Company & Data Summary

Brief restatement:
- Company name, industry, and fiscal year analyzed
- Data sources used (10-K, Yahoo Finance, etc.)
- Any key assumptions (tax rate, cost of capital)

---

### B. Ratio Results Summary

Present your key findings organized by category:

| Category | Key Ratios to Highlight | What to Discuss |
|----------|------------------------|-----------------|
| **Performance** | MVA, Market-to-Book, EVA | Is the company creating or destroying value? |
| **Profitability** | ROA, ROC, ROE | How effectively does the company generate returns? |
| **Efficiency** | Asset Turnover, Inventory Days, Collection Period | How well does the company manage its assets? |
| **Leverage** | Debt Ratio, Times Interest Earned, Debt Burden | How much financial risk is the company taking? |
| **Liquidity** | Current Ratio, Quick Ratio, Cash Ratio | Can the company meet short-term obligations? |
| **Du Pont** | ROE decomposition | What drives returns — margin, turnover, or leverage? |

Focus on **insight rather than computation** — the CFO already has the numbers.

---

### C. Interpretation & Key Findings

For each ratio category, provide:
- What the ratio values **mean** in context
- Whether the values suggest **strength** or **concern**
- How they **compare** to general benchmarks or industry norms (if available)

Highlight the most important 3–5 findings that would matter to a CFO.

---

### D. Du Pont Analysis Discussion

Decompose ROE into its components and explain:
- Is profitability (margin) the main driver?
- Is asset efficiency (turnover) strong or weak?
- Is leverage amplifying returns — and is that sustainable?

---

### E. Strategic Recommendations

Provide 2–4 actionable recommendations based on your analysis. Examples:
- "Improve inventory management to reduce Days in Inventory from X to Y"
- "Current leverage ratio of X suggests capacity for additional debt financing"
- "Low quick ratio of X warrants building a larger cash buffer"
- "Strong EVA of $X confirms value creation — consider communicating this to investors"

Support each recommendation with data from your model.

---

### F. Structured AI Prompt (Required Component)

Write a **1–2 page structured prompt** (as a separate section or appendix) that could instruct an AI to generate your complete accounting ratios spreadsheet. Your prompt must include:

1. **Company-Specific Financial Data** — All Balance Sheet items (current and prior year), Income Statement items, Cash Flow items, market data (share price, shares outstanding), and analyst assumptions (cost of capital, tax rate). All values must be explicitly stated — AI does not infer missing data.

2. **Named Range Conventions** — Use standardized names matching your Stage 3 spec (e.g., `BAL_cash_marketable_securities_2024`, `INC_sales`, `CASH_operating`).

3. **Spreadsheet Requirements** — Instruct the AI to produce:
   - Financial statement data tabs with named ranges
   - Color coding: **Yellow** = Inputs, **Blue** = Assumptions, **Green** = Formulas, **Gray** = Outputs
   - All six ratio categories with formulas in named-range notation
   - Du Pont decomposition
   - Verification checks (Du Pont vs. direct calculations, Balance Sheet balance)

4. **Hierarchical Structure** — Use clear section headers (e.g., `# GOAL`, `# COMPANY FINANCIAL DATA`, `# RATIO FORMULAS`, `# VERIFICATION`).

---

### G. Executive Justification

Use management-level reasoning:
- Financial health assessment
- Operational efficiency opportunities
- Capital structure observations
- Liquidity position
- Value creation track record
- Accounting and reporting implications

---

## Prompt Engineering Best Practices

### 1. Avoid Vague Prompts

Example of a bad prompt:
> "Make me an accounting ratios spreadsheet."

Example of a good prompt:
> "Create an Excel workbook computing 25+ accounting ratios for [Company] using FY2024 10-K data. Use named ranges matching the convention BAL_[item]_[year] for Balance Sheet items..."

### 2. Provide All Variable Values

AI does not infer values. Include every financial statement line item explicitly.

### 3. Use Named Ranges Consistently

Never allow the AI to invent its own naming system. Define names in your prompt.

### 4. Specify Formatting Explicitly

Color codes, sections, layout — be explicit.

### 5. Include Context Files from GitHub

This is the most efficient way to use AI for models.

**Options for providing context:**
1. **Best:** GitHub links to your spec and template files
2. **Medium:** Upload `.md` or `.xlsx` files directly
3. **Least:** Copy/paste text manually

---

## Note on AI Access

If you do not have access to an AI tool capable of generating Excel files, you may:
1. Submit your structured prompt (Section F) as written.
2. Submit your Stage 2 model as the primary spreadsheet artifact with a brief note explaining that you would use the prompt to regenerate it.

The prompt itself is the primary deliverable — it demonstrates your ability to convert domain knowledge into machine-readable instructions.

---

## Evaluation

| Criterion | Description | Points |
|-----------|-------------|-------:|
| Ratio Interpretation | Demonstrates understanding of what ratios reveal | 2 |
| Strategic Recommendations | Actionable, data-supported recommendations | 2 |
| Du Pont Analysis | Meaningful decomposition and discussion | 1 |
| Structured AI Prompt | Clear, complete, reproducible prompt with all financial data | 2 |
| Professionalism & Communication | Executive-ready, well-structured deliverable | 1 |
| AI-Generated Output OR Manual Analysis | Working spreadsheet from prompt, or equivalent manual work | 2 |

---

## Career Relevance

This project builds skills used in:

### Financial Planning & Analysis (FP&A)
- Ratio trend analysis for management reporting
- Performance benchmarking across business units
- Budget variance analysis and forecasting

### Corporate Finance & Treasury
- Capital structure optimization
- Liquidity management and working capital analysis
- Investor relations and equity story development

### Accounting & Audit
- Financial statement analysis for audit risk assessment
- Ratio-based analytical procedures
- Internal controls evaluation

### Investment Banking & Equity Research
- Comparable company analysis (comps)
- Credit analysis and debt capacity assessment
- Valuation multiples and market-to-book analysis

### Data, Analytics & AI Roles
- Spec-to-model-to-prompt automation pipeline
- GitHub collaboration and version control
- AI-assisted financial modeling and reporting

---

## Why This Matters

This multi-stage journey reflects workflows used at Big 4 accounting firms, corporate FP&A teams, investment banks, and consulting firms. You are demonstrating analytical reasoning, automation fluency, model governance, financial decision leadership, and technical communication.

**This is a portfolio-ready artifact for internships, jobs, and graduate programs.**
