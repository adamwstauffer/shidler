# International Corporate Finance

Corporate finance fundamentals — financing and investment decisions, securities, and financial statement analysis — taught through a hands-on performance-ratios project.

## Offerings

| Shidler Code | Population | Status | Details |
|---|---|---|---|
| BUS 629 | Masters — VEMBA | Active | [`BUS-629-VEMBA/README.md`](BUS-629-VEMBA/README.md) |
| BUS 314 | Undergrad | Inactive — superseded by BUS 629's project design | [`BUS-314/README.md`](BUS-314/README.md) |

## Shared Curriculum

[`projects/performance-ratios/`](projects/performance-ratios/) — the current project design (spec-driven, 6-stage: repo setup through LLM analysis evaluation). This is what BUS 629 teaches today; if an undergraduate offering resumes, it would use this same shared project rather than reviving the archived BUS-314 design.

## Directory Contents

```
International-Corporate-Finance/
├── BUS-314/                                 offering: syllabus (inactive)
│   └── README.md                            points to _archive/bus314/ for historical project materials
├── BUS-629-VEMBA/                          offering: syllabus, roster, ignore/ (gitignored)
│   ├── BUS-629 Danh sách Nhóm.xlsx          cohort roster
│   └── README.md                            syllabus: course code, campus locations, textbook
├── projects/
│   └── performance-ratios/                  shared curriculum — see its own README for full contents
│       ├── _tools/                          grading scripts (grade_stage0–5.py, sweep_stage.py, roster builders)
│       ├── analysis/                        self-audit and validation reports
│       ├── data/                            source financial data and provenance
│       ├── deliverables/                    final, presentation-ready outputs
│       ├── demo-portfolio-repo/             worked example of a finished student portfolio repo
│       ├── docs/                            decisions/, plans/, specs/, templates/
│       ├── models/                          builds/ (populated models), templates/ (blank frameworks)
│       ├── Performance-Ratios-Project.pptx  project overview slide deck
│       └── stage0-repo-setup.md … stage5-llm-analysis-evaluation.md
└── README.md                                you are here
```

See `_archive/bus314/` for the archived BUS-314 project materials (its own README documents that directory's contents).
