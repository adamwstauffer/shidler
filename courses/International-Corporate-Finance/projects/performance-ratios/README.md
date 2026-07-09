# Performance Ratios Project

Shared curriculum for the accounting/performance-ratios project — company selection, Excel model building, specification writing, and LLM-assisted analysis. Currently taught as BUS 629 (Vietnam EMBA); see [`../../BUS-629-VEMBA/README.md`](../../BUS-629-VEMBA/README.md) for that offering's syllabus, campus info, and roster. The predecessor BUS-314 (undergrad) iteration of this project is archived at `_archive/bus314/accounting-ratios/`.

## Stages

| Stage | File | What it covers |
|---|---|---|
| 0 | [`stage0-repo-setup.md`](stage0-repo-setup.md) | GitHub repo creation, collaborator access |
| 1 | [`stage1-template-architecture.md`](stage1-template-architecture.md) | Named-range Excel template familiarization |
| 2 | [`stage2-company-selection-memo.md`](stage2-company-selection-memo.md) | Company selection memo |
| 3 | [`stage3-model-population-validation.md`](stage3-model-population-validation.md) | Populate and validate the financial model |
| 4 | [`stage4-technical-specification.md`](stage4-technical-specification.md) | Technical specification (post-build reflection) |
| 5 | [`stage5-llm-analysis-evaluation.md`](stage5-llm-analysis-evaluation.md) | Interpret ratios, critically evaluate LLM-generated analysis |

## Directory Contents

```
performance-ratios/
├── _tools/                        grading scripts (instructor-facing)
│   ├── build_roster.py             builds ignore/roster.md + .csv from graded STAGEN_GRADES.md files
│   ├── build_team_roster_vn.py     generates the BUS-629 VEMBA team roster workbook
│   ├── grade_one.py                grade a single student across stages
│   ├── grade_stage0.py … grade_stage5.py   per-stage grading scanners
│   ├── rescore_stage0_bio.py       one-off Stage 0 bio-policy rescore
│   ├── sweep_stage.py              batch sweep grading across a whole stage
│   ├── _grading_comments.py        shared comment-bank helper
│   └── _safe_zip.py                shared zip-extraction helper
├── analysis/
│   └── validation/                 self-audit and validation reports (Stage 3)
├── data/                           source financial data and provenance
├── deliverables/                   final, presentation-ready outputs (Stage 5)
├── demo-portfolio-repo/            worked example of a finished student portfolio repo
│   ├── analysis/ data/ deliverables/ docs/ models/   mirrors the structure below
│   ├── BIO.md, README.md, README_v2.md, RESUME.md
├── docs/
│   ├── decisions/                  project-design decisions (incl. the original project-design memo)
│   ├── plans/                      project plans and timelines
│   ├── specs/                      technical specifications (Stage 4 deliverables land here)
│   └── templates/                  stub pointing at the canonical repo-level templates, plus gaap-conversion-quickref.md
├── models/
│   ├── builds/                     populated, working models (Stage 3)
│   └── templates/                  blank model frameworks, incl. gaap-bridge-template.xlsx
├── Performance-Ratios-Project.pptx  project overview slide deck
└── stage0-repo-setup.md … stage5-llm-analysis-evaluation.md
```

Grading scripts here operate against `../../BUS-629-VEMBA/ignore/` (the gitignored student-submission tree for the active offering) — they are not VEMBA-specific themselves, since the same rubric logic applies to any offering of this shared project.
