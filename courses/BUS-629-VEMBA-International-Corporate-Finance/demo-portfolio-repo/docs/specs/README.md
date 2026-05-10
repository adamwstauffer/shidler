# `docs/specs/`

Stage 4 technical specifications. A spec is the "how" document — methodology, formulas, assumptions, data sources, and pseudocode that a competent analyst could use to reproduce your model.

## What belongs here

- Methodology write-ups for each financial model in `models/builds/`
- Formula derivations and assumption logs
- Pseudocode for any calculation that's non-obvious from the workbook
- Data dictionaries describing every named range or input cell

## Naming conventions

- `<model-name>-spec.md` — e.g., `fx-hedging-spec.md`, `dcf-spec.md`
- Cross-link from the matching model's README in `models/builds/`
