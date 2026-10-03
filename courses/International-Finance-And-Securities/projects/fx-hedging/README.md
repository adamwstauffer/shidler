# FIN-321 FX Hedging Project — six-stage (Design → Build → Validate)

**Status: live (promoted 2026-07-10).** This is the current FIN-321 fx-hedging curriculum. The
prior four-stage version is archived at `_archive/fin321/stage-docs-v1/`, and the FIN-321
offering README's weight table matches these stages.

## Micro/Macro parity (2026-09-24)

BUS 620 Micro & Macro Economics is the guidepost for this project's conventions.
Three things changed to match it:

- **Stage 0 belongs to the course, not the project.** [`stage0-repo-setup.md`](stage0-repo-setup.md)
  now prescribes the course-independent portfolio repo standard (`capabilities/`, `docs/briefs/`,
  `docs/decisions/`, `data/`, `analysis/figures/`, `AGENTS.md`, `CLAUDE.md`, `prompt-log.md`),
  taught on [github-stage0.html](https://adamwstauffer.github.io/ai-lms/github-stage0.html). The
  old project-shaped skeleton (`docs/specs/`, `docs/plans/`, `docs/templates/`, `models/templates/`,
  `models/builds/`) is superseded.
- **Every brief carries `stage-brief` frontmatter** — the `deliverables` block is the path the
  course site's stage pages and `gates.js` mirror, as in BUS 620.
- **The reference skeleton** is the repo-wide worked sample,
  [`templates/portfolio/firstname-lastname/`](../../../../templates/portfolio/firstname-lastname/).

- **Stages 2–4 commit into the capability folder (2026-09-24).** The spec is
  `capabilities/fx-hedging/spec.md` and the workbook `capabilities/fx-hedging/model.xlsx`, beside the
  capability's `README.md` — as BUS 620 does with `capabilities/marginal-analysis/`. The old
  `docs/specs/` and `models/builds/` paths are superseded; Summer 2026 repositories keep them and are
  read against [`../../FIN-321/summer-2026/`](../../FIN-321/summer-2026/).

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

## Stages & weights

Every weight is a **percentage** — nothing is a hardcoded point total. Stage weights are % of
the project; each stage's rubric criteria (in the stage doc) are % of that stage. The project's
own share of the semester course grade is variable and set in the offering README / gradebook,
so changing it never requires touching these weights. **No extra credit.** The weight table below is
the single source of truth.

| Stage | Deliverable | Weight | Suggested week (6-wk term) |
| ----- | ----------- | -----: | ---- |
| 0 | Portfolio repository (course-level; the portfolio repo standard) | 8% | 2 (paired with stage 2) |
| 1 | Executive brief | 17% | 1 |
| 2 | Model specification | 21% | 2 |
| 3 | AI-assisted build + audit note | 17% | 3 |
| 4 | Market data + population | 12% | 4 |
| 5 | Validate & decision memo (capstone) | 25% | 5–6 |
| **Total** | | **100%** | |

Weeks are indicative for a 6-week summer term; the offering README sets actual dates. In a
15-week term the same stages spread roughly biweekly. **These stage docs are term-agnostic by
design — do not add dates to them.**

## The stage-gating chain

Each stage's output is the next stage's named input:

```
repo (0) → memo (1) → spec (2) → workbook + audit (3) → live-data populate (4) → LLM validation + recommendation (5)
```

## Conventions (shared with BUS 629)

- **Filenames:** dated documents are `YYYY-MM-DD-{scenario}-{slug}-{type}.md`, `{type}` one of
  `brief` · `spec` · `memo` · `analysis` · `log` — no last name (the repository is already named for
  you). Briefs go in `docs/briefs/`, decision memos in `docs/decisions/`, analyses in `analysis/`,
  the market-data memo beside the data in `data/` (scenario slugs: `solar-importer`,
  `pharma-exporter`, `tech-services`, `aerospace`). The spec and workbook keep their fixed paths
  in `capabilities/fx-hedging/`. Files already submitted under the older
  `YYYY-MM-DD-{lastname}-…` names still count — never renamed, never deducted (2026-10-02).
- **Named-range contract:** `FC_AMT`, `S0_in`, `F0_in`, `R_USD`, `R_FC`, `K_PUT`, `K_CALL`,
  `PREM_PUT`, `PREM_CALL`, `T_DAYS` — the shared vocabulary of spec, workbook, grader, and
  LLM prompts.
- **Color convention:** Yellow = inputs · Blue = assumptions · Green = formulas · Gray = outputs.
- **Prompt log:** a running `prompt-log.md` at the repo root, updated at every stage that uses
  an AI tool. Student drafts first, AI reviews, then the two iterate together.
- **Template policy:** no workbook is provided; you build yours from your own Stage 2 specification.

## Stage files

| File | Stage |
| ---- | ----- |
| `stage0-repo-setup.md` | 0 — Portfolio repository (course-level; companion page `github-stage0.html`) |
| `stage1-executive-brief.md` | 1 — Executive brief |
| `stage2-model-spec.md` | 2 — Model specification |
| `stage3-ai-build-audit.md` | 3 — AI-assisted build + audit |
| `stage4-market-data-population.md` | 4 — Market data + population |
| `stage5-validate-decision-memo.md` | 5 — Validate & decision memo |

Shared project files: `scenarios.md`, `_templates/template-decision-memo.md`,
`_templates/template-spec.md`. Grading checks every calculated
cell for a formula referencing named ranges; a hardcoded constant scores zero for that element.

## Career framing (carried from v1, applies to the whole arc)

This project mirrors the analyst-to-automation workflow used in corporate treasury, IB, FP&A,
audit, and AI-adjacent finance roles: exposure framing → model design → AI-assisted build →
data operations → validation and executive recommendation, all version-controlled. The finished
repo is a portfolio artifact for internships, jobs, and graduate programs.
