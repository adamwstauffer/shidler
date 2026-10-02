---
name: formula-check
description: Audit an Excel workbook in this repo for hardcoded numbers in cells that should be formulas. Use before calling any model.xlsx done.
---

# formula-check

1. Open the workbook named by the user (default: every `capabilities/*/model.xlsx`).
2. Treat the `Inputs` sheet and any sheet named `Data` as raw inputs — literals are allowed there.
3. On every other sheet, list each cell that holds a typed number instead of a formula.
4. Report as a table: sheet · cell · value · suggested formula. Do not edit the file.
