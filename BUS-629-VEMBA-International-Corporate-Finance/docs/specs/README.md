# Specs

Technical specifications that define analytical work precisely enough for any competent executor — human or AI — to produce correct output without additional context.

## What belongs here

- **Stage 4 technical specifications** — the central project artifact. Each spec fully defines:
  - **Part A (Model Specification):** Spreadsheet architecture, all financial data inputs, named range conventions, ratio formulas, and validation rules
  - **Part B (Analysis Specification):** Interpretation requirements, benchmarks, strategic recommendation criteria, and output format
- **Methodology documents** — formal descriptions of analytical approaches

## Naming convention

```
[lastname]-stage4-spec.md
```

**Examples:**
- `nguyen-stage4-spec.md`
- `tran-stage4-vinamilk-spec.md`

## Template

Use [`../templates/spec-template.md`](../templates/spec-template.md) as your starting point.

## Quality test

A well-written spec is **self-contained**. If you hand it to an LLM (or a new analyst) with zero additional context, they should be able to produce a substantially correct ratio analysis. If they can't, the spec has gaps.
