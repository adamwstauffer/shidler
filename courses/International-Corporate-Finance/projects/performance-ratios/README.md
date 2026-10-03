# Performance Ratios Project

Shared curriculum for the accounting/performance-ratios project: company selection, Excel model building, specification writing, and LLM-assisted analysis. Currently taught as BUS 629 (Vietnam EMBA); see [`../../BUS-629-VEMBA/README.md`](../../BUS-629-VEMBA/README.md) for that offering's syllabus and campus info. The predecessor BUS-314 (undergrad) iteration of this project is archived at `_archive/bus314/accounting-ratios/`.

## Stages

The stage names below are the briefs' own titles; every other page uses them.

| Stage | Brief | Name | Step-by-step on Kumu |
|---|---|---|---|
| 0 | [`stage0-repo-setup.md`](stage0-repo-setup.md) | Personal Portfolio Repository | [Stage 0](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage0.html) |
| 1 | [`stage1-template-architecture.md`](stage1-template-architecture.md) | Provided Ratios Template | [Stage 1](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage1.html) |
| 2 | [`stage2-company-selection-memo.md`](stage2-company-selection-memo.md) | Company Selection Memo | [Stage 2](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage2.html) |
| 3 | [`stage3-model-population-validation.md`](stage3-model-population-validation.md) | Populated Financials | [Stage 3](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage3.html) |
| 4 | [`stage4-technical-specification.md`](stage4-technical-specification.md) | Technical Specification | [Stage 4](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage4.html) |
| 5 | [`stage5-llm-analysis-evaluation.md`](stage5-llm-analysis-evaluation.md) | LLM Analysis, Executive Evaluation, and Repo Polish | [Stage 5](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage5.html) |

## Where files go

Dated documents are named `YYYY-MM-DD-{company-slug}-{type}.md` with no last name: briefs in `docs/briefs/`, memos in `docs/decisions/`, analyses in `analysis/`, the spec at `capabilities/performance-ratios/spec.md`, the prompt log at the repository root. This project also keeps a `models/` folder (`models/templates/` for the provided template, `models/builds/` for your populated workbook) because it ships a workbook; nothing goes in `deliverables/`. A misplaced or misnamed file never blocks you and is still graded; it may cost a point under professionalism, and moving it to the path the brief names fixes that.

The worked sample of a finished portfolio repository is [`templates/portfolio/firstname-lastname/`](../../../../templates/portfolio/firstname-lastname/).

## Directory contents

```
performance-ratios/
├── analysis/validation/     self-audit and validation reports (Stage 3)
├── capabilities/
│   └── performance-ratios/  what the Stage 4 spec holds and how it is tested
├── data/                    source financial data and provenance
├── docs/
│   ├── decisions/           project decisions
│   ├── plans/               project plans and timelines
│   └── templates/           stub pointing at the repo-level templates, plus gaap-conversion-quickref.md
├── models/
│   ├── builds/              populated, working models (Stage 3)
│   └── templates/           blank model frameworks
└── stage0-repo-setup.md … stage5-llm-analysis-evaluation.md
```
