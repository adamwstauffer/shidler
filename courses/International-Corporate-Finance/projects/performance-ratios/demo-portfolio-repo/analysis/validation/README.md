# `analysis/validation/`

Stage 3 validation reports. One report per model build in `models/builds/`.

## What a validation report covers

1. **Footing check** — do balance sheet, income statement, and cash flow tie out?
2. **Formula audit** — pick 3–5 non-trivial cells and trace their derivation by hand
3. **Stress test** — what happens at ±2σ inputs? Any `#DIV/0!`, `#REF!`, or implausible outputs?
4. **Assumption log** — list every assumption that materially drives the result, with rationale
5. **Known limitations** — what the model *doesn't* cover

## Naming conventions

- `<company>-<model>-validation-<YYYY-MM-DD>.md` — match the matching build's filename
- Cross-link from the build's row in `models/builds/README.md` if you maintain a build index
