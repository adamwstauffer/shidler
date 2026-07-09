# `models/templates/`

Blank model frameworks (Stage 1). A template here has:

- Tab structure laid out
- Named ranges defined (e.g., `BAL_TotalAssets`, `INC_Revenue`)
- Formulas wired up against the named ranges
- **No company-specific input data**

Keep templates pristine. When you start working on a real company, copy the template into `models/builds/` and fill it there — don't overwrite the template.

## Naming conventions

- `<model-name>-template.xlsx` — e.g., `accounting-ratios-template.xlsx`, `fx-hedging-template.xlsx`
- One model per file. If you need multiple variants, use suffixes: `dcf-template-v2.xlsx`
