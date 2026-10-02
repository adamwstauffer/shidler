# Specs

Technical specifications that define analytical work precisely enough for any competent executor — human or AI — to produce correct output without additional context.

## What belongs here

- **Stage 4 technical specifications** — the central project artifact. Each spec fully defines:
  - **Part A (Model Specification):** Spreadsheet architecture, all financial data inputs, named range conventions, ratio formulas, and validation rules
  - **Part B (Analysis Specification):** Interpretation requirements, benchmarks, strategic recommendation criteria, and output format
- **Methodology documents** — formal descriptions of analytical approaches

## Naming convention

```
YYYY-MM-DD-{company-slug}-spec.md
```

**Examples:**
- `2026-06-18-vinamilk-spec.md`

Files already submitted under an older name (with your last name, or a `stageN` prefix) still count — nothing to rename.

## Template

Use [`../../../../../../docs/templates/spec-template.md`](../../../../../../docs/templates/spec-template.md) as your starting point.

## Quality test

A well-written spec is **self-contained**. If you hand it to an LLM (or a new analyst) with zero additional context, they should be able to produce a substantially correct ratio analysis. If they can't, the spec has gaps.
