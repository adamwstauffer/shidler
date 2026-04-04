# Stage 4: Technical Specification — Spec-Driven Design

**Weight:** 20% of project score

---

## Overview

Write a formal technical specification that fully defines both the Excel ratio model and the accounting ratio analysis for your company. The spec must be precise and complete enough that an LLM — with no prior context — can take the spec as its sole input and produce a correct, comprehensive ratio analysis with strategic recommendations.

**This is the central artifact of the project.**

It is not a "prompt" in the casual sense. It is a technical specification — the same kind of document a finance director would hand to a new analyst, an offshore team, or an automation system. The fact that the executor happens to be an LLM is incidental; the spec should work for any competent executor.

## Why spec-driven design matters

In professional practice, the ability to specify analytical work precisely is more valuable than the ability to execute it. Execution scales (via teams, tools, AI); specification requires domain expertise that cannot be delegated. A spec that produces wrong output reveals a gap in your understanding — and that feedback loop is where the deepest learning happens.

## Connection to earlier stages

- **Stage 1** taught you *what* a ratio model needs — structure, tabs, named ranges, color coding, formula flow
- **Stage 2** taught you *why* this company and *what* to look for
- **Stage 3** taught you *how* the numbers behave and where errors hide
- **Stage 4** synthesizes all of this: "I understand this well enough to specify it unambiguously for someone who has never seen it before"

---

## Deliverable

Technical specification document (`.md`, 3–5 pages) saved to `docs/specs/`. Use [`docs/templates/spec-template.md`](docs/templates/spec-template.md) as your starting point.

---

## Required specification components

### Part A — Model Specification

Defines the Excel ratio model: structure, data, formulas, and validation. Part A must be detailed enough that the executor could reconstruct your Stage 1 template and Stage 3 populated model from this document alone.

**1. Scope & Objective** — Company name, fiscal period, reporting standard (GAAP/IFRS/VAS), reporting currency, analytical objective, intended audience.

**2. Model Architecture** — Specify the spreadsheet structure:
   - Tab layout (which tabs, what each contains, how data flows between them)
   - Color coding conventions and their meaning
   - Input/calculation/output separation
   - Formatting requirements (number formats, decimal places, header styles)

**3. Data Inputs** — Complete, explicit table of every financial data point required. Organized by source:
   - Balance Sheet items (current year and prior year)
   - Income Statement items
   - Cash Flow Statement items
   - Market/Analyst inputs (share price, shares outstanding, cost of capital, tax rate)
   - **All values stated numerically** — the executor does not look up, infer, or estimate any data

**4. Named Range Conventions** — Full map of named ranges to values:

| Named Range | Source | Value | Unit |
|-------------|--------|-------|------|
| `BAL_assets_total_2025` | Balance Sheet | 394,328 | USD millions |
| `INC_sales` | Income Statement | 285,610 | USD millions |
| ... | ... | ... | ... |

**5. Derived Inputs** — Computed intermediate values (averages, start-of-year figures, daily rates, after-tax operating income) with explicit formulas in named-range notation.

**6. Ratio Definitions & Formulas** — Every ratio, organized by category (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont), with:
   - Formula in named-range notation (e.g., `RATIO_ROA = INC_net / startYear_assets_total`)
   - Expected unit (%, x, days, currency)
   - Brief interpretation guide (what does "high" or "low" mean for this ratio?)

**7. Validation Rules** — Internal consistency checks the executor must verify:
   - Du Pont ROA ≈ Direct ROA
   - Du Pont ROE ≈ Direct ROE
   - Balance Sheet balance (both years)
   - Any company-specific checks

### Part B — Analysis Specification

Defines what to do with the computed ratios. This is what transforms raw numbers into insight.

**8. Analysis Requirements** — For each ratio category, specify:
   - What to interpret and why it matters for this company
   - Benchmarks or comparison targets (industry averages, competitor values, or general expectations — provide actual numbers where available)
   - Cross-category connections to examine (e.g., "Assess whether leverage is amplifying ROE sustainably by examining debt ratios alongside profitability trends")

**9. Du Pont Decomposition** — Specific instructions for ROE breakdown: which component is the primary driver? Is the balance sustainable?

**10. Strategic Recommendation Requirements** — Number of recommendations (3–5), evidence standard (each must cite specific ratio values), actionable specificity (who does what by when).

**11. Output Format Specification** — Exact structure of the deliverable:
   - Document format (executive memo)
   - Required sections and their order
   - Length targets per section
   - Tone and audience (e.g., "addressed to the Board of Directors; executive-level language; no unexplained jargon")
   - How to present ratio results (tables, narrative, or both)

---

## Quality test

A well-written spec is **self-contained**. If you hand Part A + Part B to an LLM with zero additional context, it should be able to:

1. Reconstruct the ratio model (or verify the provided ratios against the formulas)
2. Produce a substantially correct analysis with meaningful strategic recommendations

If it can't, the spec has gaps — and identifying those gaps is the learning.

---

## Rubric (% of Stage 4 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Model Specification — Data & Structure (Part A, items 1–5) | 25% | Every input value present; model architecture fully defined; no gaps the executor must fill |
| Model Specification — Ratios & Validation (Part A, items 6–7) | 25% | All 25+ ratios specified with correct formulas in named-range notation; validation rules complete |
| Analysis Specification (Part B, items 8–11) | 25% | Clear interpretive guidance; meaningful benchmarks; actionable recommendation criteria; output format fully defined |
| Spec Craft & Clarity | 25% | Unambiguous language; logical organization; a competent executor could follow this without asking questions |
