# FIN-321 Multi-Stage Project – FX Exposure and Hedging Strategies

Author: Adam Stauffer
Last Updated: 2026-03-25

## Project Overview

This project guides students through the full analyst-to-automation workflow used in corporate treasury and financial risk management. Beginning with a business-level problem, students progressively translate FX exposure into a working model, a formal specification, and a final executive recommendation with integrated prompt engineering.

## Deliverables

| Stage | Deliverable | Points |
| ----- | --------------------------------- | -----: |
| 1 | Executive Memo | 4 |
| 2 | Excel Model Build | 6 |
| 3 | Technical Specification | 4 |
| 4 | Final Analysis, Prompt Engineering & Recommendation | 10 |
| **Total** | | **24** |

## Stage Sequence & Rationale

The project follows a **Build → Document → Analyze** workflow:

1. **Stage 1 – Executive Memo:** Define the business problem and frame the hedging decision for the CFO.
2. **Stage 2 – Excel Model Build:** Build a working prototype from the scenario. Experiential knowledge of what the model requires in practice informs every subsequent stage.
3. **Stage 3 – Technical Specification:** Document what was built and articulate an improved design. A spec written after building is more precise, more realistic, and more useful as an AI prompt input.
4. **Stage 4 – Final Analysis, Prompt Engineering & Recommendation:** Interpret model results, write a structured AI prompt, and deliver an executive-ready hedge recommendation.

## Assignment Files

| File | Description |
| --------------------------------- | ---------------------------------------- |
| `stage1-memo-assignment.md` | Stage 1 instructions and rubric |
| `stage2-excel-build-assignment.md`| Stage 2 instructions and rubric |
| `stage3-spec-assignment.md` | Stage 3 instructions and rubric |
| `stage4-final-analysis-assignment.md` | Stage 4 instructions and rubric |
| `scenarios.md` | Assigned firm scenarios |
| `../_templates/template-decision-memo.md` | Starter template for Stage 1 memo |
| `../_templates/template-spec.md` | Starter template for Stage 3 spec |

## Committing Your Work

All Markdown deliverables (`.md` files) should be committed to your GitHub repository. Recommended locations:

| Deliverable | Where to Save |
|-------------|---------------|
| Stage 1 memo | `docs/decisions/` |
| Stage 2 Excel model | `docs/templates/excel/` |
| Stage 3 spec | Root of your project directory or `docs/` |
| Stage 4 final analysis | Root of your project directory or `docs/` |

**Workflow:**
1. Create your `.md` file using the appropriate template.
2. Save it in the recommended directory within your repository.
3. Stage, commit, and push: `git add <file>` → `git commit -m "Stage X deliverable"` → `git push`.
4. Verify your file is visible on GitHub.

Version control is not just a submission mechanism — it is a core professional skill practiced throughout this project.
