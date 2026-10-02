# Prompt Log

The AI sessions that **mattered** — the ones that changed a deliverable. Routine questions don't
belong here.

| Date | Goal | Exact Prompt | Tool | Output Location | Notes |
|------|------|--------------|------|-----------------|-------|
| 2026-10-02 | Scope the engagement | "Read docs/briefs/2026-10-02-lunch-plate-volume.md. What's ambiguous, and what data would I need to answer it? Don't answer the question yet." | Claude Code | `docs/briefs/` | Flagged that "cost" mixed fixed and variable; I split them in the brief. |
| 2026-10-04 | Build the model | "Build capabilities/marginal-analysis/model.xlsx from spec.md. Inputs on their own sheet, every calculated cell a formula." | Claude Code | `capabilities/marginal-analysis/model.xlsx` | First draft hardcoded MR; I asked for it to reference the price input. |
| 2026-10-06 | Stress-test the answer | "Argue against stopping at 160 plates. What would have to be true for 180 to be better?" | Claude | `docs/decisions/` | Price would need to exceed $15.50/plate; added as a trigger in the decision memo. |
