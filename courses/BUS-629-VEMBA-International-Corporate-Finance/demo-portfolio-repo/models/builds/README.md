# `models/builds/`

Populated, working models (Stage 3). Each build is a copy of a template from `models/templates/` with real input data filled in.

## What belongs here

- Working `.xlsx` files with a specific company's financials, scenarios, or assumptions
- One workbook per company-model pair
- Cross-link from the matching spec in `docs/specs/`

## Naming conventions

- `<company>-<model>-<YYYY-MM-DD>.xlsx` — e.g., `vingroup-dcf-2026-05-09.xlsx`, `vinamilk-ratios-2026-05-09.xlsx`
- Keep the date in the filename so you can tell a build apart from later refreshes

## Validation

Every build should have a corresponding validation report in `analysis/validation/` — at minimum, a check that totals foot, formulas don't break under stress inputs, and assumptions are logged.
