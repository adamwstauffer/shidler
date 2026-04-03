# Model Templates

Blank financial model frameworks — structured, formatted, and ready to receive data, but containing no company-specific values. In investment banking, these are the firm's reusable model skeletons (LBO templates, DCF frameworks, comp tables) that analysts populate for each new engagement.

## What belongs here

- **Stage 1 ratio templates** — your blank accounting ratios workbook built from scratch
- The template should be fully structured: tabs, headers, named ranges, color coding, formulas — but all data cells empty

## Naming convention

```
[lastname]-stage1-ratio-template.xlsx
```

**Examples:**
- `nguyen-stage1-ratio-template.xlsx`
- `tran-stage1-ratio-template.xlsx`

## Best practices

- **Color coding:** Yellow (inputs), Blue (assumptions), Green (formulas), Gray (outputs)
- **Named ranges:** Use prefixed conventions — `BAL_`, `INC_`, `CASH_`, `RATIO_`, `startYear_`, `avg_`
- **Tab structure:** One tab per financial statement; separate inputs from calculations from outputs
- **Auditability:** Every formula traceable; no hardcoded numbers in formula cells
- **Notes tab:** Document your layout decisions and named range conventions
