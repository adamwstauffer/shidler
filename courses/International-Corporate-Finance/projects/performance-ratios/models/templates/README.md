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

- **Color coding — the house legend.** Tan fill `FDE9D9` with regular dark text = a hardcoded input,
  the cells you type into and may change. Blue text `0070C0` = a formula — calculated, never type over
  it. Olive text `4F6228` = a link to another tab. Yellow fill `FFFF00` = a key assumption, fitted or
  judgmental rather than observed. **Blue never means "type here."** A workbook that paints an input
  blue tells the reader the exact opposite of the truth, and the failure is silent: nothing in Excel
  objects, the number just quietly becomes a hardcode where a formula used to be.
- **Named ranges:** Use prefixed conventions — `BAL_`, `INC_`, `CASH_`, `RATIO_`, `startYear_`, `avg_`
- **Tab structure:** One tab per financial statement; separate inputs from calculations from outputs
- **Auditability:** Every formula traceable; no hardcoded numbers in formula cells
- **Notes tab:** Document your layout decisions and named range conventions
