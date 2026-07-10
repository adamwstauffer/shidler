# FX Hedging Project v2 — canonical six-stage redesign (DRAFT)

**Status: Kumu-improved draft (2026-07-09), pending Adam's review.** Nothing in this folder is
live. On approval, these docs replace the four `stage*-assignment.md` files one level up, and
the FIN-321 offering README's points table is updated to match. Design rationale and options
analysis: `ai-lms/docs/plans/2026-07-09-fin321-fx-hedging-restructure-memo.md`.

## What changed vs. v1 (Build → Document → Analyze)

The v2 arc is **Design → Build → Validate**, aligned with the proven BUS 629 performance-ratios
flow. Three structural moves:

1. **Spec before build.** Students design the workbook (named ranges, tabs, formula plan)
   *before* any Excel exists. The build then tests their own design.
2. **AI generates, students audit.** Stage 3 makes AI-assisted generation explicit and graded —
   the deliverable includes an audit note proving the student inspected and corrected the output.
3. **Data after structure.** Live market data lands at stage 4 and doubles as a robustness test:
   a model that breaks when fresh prices are loaded had the wrong structure.

Excel understanding is proven at four checkpoints no AI can do *for* the student:
design (2), audit (3), populate + cross-check (4), hand-verification (5).

## Stages & points (24 + 2 EC — project weight in the course unchanged at 25%)

| Stage | Deliverable | Points | Suggested week (6-wk term) |
| ----- | ----------- | -----: | ---- |
| 0 | Portfolio repository (canonical skeleton) | 2 | 2 (paired with stage 2) |
| 1 | Executive memo | 4 | 1 |
| 2 | Model specification | 5 | 2 |
| 3 | AI-assisted build + audit note | 4 | 3 |
| 4 | Market data + population | 3 | 4 |
| 5 | LLM analysis & validation (capstone) | 6 (+2 EC) | 5–6 |
| **Total** | | **24 (+2 EC)** | |

Weeks are indicative for a 6-week summer term; the offering README sets actual dates. In a
15-week term the same stages spread roughly biweekly. **These stage docs are term-agnostic by
design — do not add dates to them.**

## The stage-gating chain

Each stage's output is the next stage's named input:

```
repo (0) → memo (1) → spec (2) → workbook + audit (3) → live-data populate (4) → LLM validation + recommendation (5)
```

## Conventions (shared with BUS 629)

- **Filenames:** `YYYY-MM-DD-{lastname}-{scenario-slug}-{kind}.{ext}`
  (scenario slugs: `solar-importer`, `pharma-exporter`, `tech-services`, `aerospace`).
- **Named-range contract:** `FC_AMT`, `S0_in`, `F0_in`, `R_USD`, `R_FC`, `K_PUT`, `K_CALL`,
  `PREM_PUT`, `PREM_CALL`, `T_DAYS` — the shared vocabulary of spec, workbook, grader, and
  LLM prompts.
- **Color convention:** Yellow = inputs · Blue = assumptions · Green = formulas · Gray = outputs.
- **Prompt log:** a running `prompt-log.md` at the repo root, updated at every stage that uses
  an AI tool. LLM-as-drafter, student-as-editor.
- **Template policy:** the instructor workbook is **withheld** during the build and used as the
  grading key. (Open question for Adam — release it after stage 3 as a diff-against-yours
  exercise? See memo §6.)

## Files in this draft set

| File | Stage |
| ---- | ----- |
| `stage0-repo-setup.md` | 0 — Portfolio repository |
| `stage1-executive-memo.md` | 1 — Executive memo (content unchanged from v1; rubric table added) |
| `stage2-model-spec.md` | 2 — Model specification |
| `stage3-ai-build-audit.md` | 3 — AI-assisted build + audit |
| `stage4-market-data-population.md` | 4 — Market data + population |
| `stage5-llm-analysis-validation.md` | 5 — LLM analysis & validation |

Unchanged and reused from v1: `../scenarios.md`, `../_templates/template-decision-memo.md`,
`../_templates/template-spec.md`. Grading scripts (`../_tools/`) need an update pass on
approval — the new logic is the formula-presence audit (outputs must be formulas referencing
named ranges; hardcoded constants score zero for that cell).

## Career framing (carried from v1, applies to the whole arc)

This project mirrors the analyst-to-automation workflow used in corporate treasury, IB, FP&A,
audit, and AI-adjacent finance roles: exposure framing → model design → AI-assisted build →
data operations → validation and executive recommendation, all version-controlled. The finished
repo is a portfolio artifact for internships, jobs, and graduate programs.
