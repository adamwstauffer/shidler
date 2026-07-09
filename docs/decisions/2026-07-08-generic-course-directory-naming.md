---
title: "Generic Course Directory Naming — Subject-First Structure"
date: 2026-07-08
status: approved
owner: Adam W. Stauffer
scope: repo-wide
related:
  - 2026-02-15-repo-hierarchy.md
---

# Generic Course Directory Naming — Subject-First Structure

## Summary

`courses/` moves from course-code-first naming (`BUS-314-...`, `BUS-629-...`) to subject-first naming (`International-Corporate-Finance/`, etc.), with course codes documented in READMEs rather than folder names. Every subject directory shares one consistent shape:

```
courses/<Subject-Name>/
├── README.md                    subject hub — Shidler code(s), links to projects/ and offering folder(s)
├── projects/
│   └── <project-slug>/          shared curriculum: stage docs, analysis, deliverables, models, _templates/, _tools/
└── <CODE[-POPULATION]>/         one per offering: tailored README/syllabus, roster, ignore/ (student data)
```

`courses/` itself stays (not `subjects/`). BUS-314 is fully superseded by BUS-629's project design and gets archived, not kept as a live offering. Grading/template tooling belongs to the shared project, not the offering, since it operationalizes shared curriculum regardless of which cohort is being graded.

## Resolved (was open)

1. **Ratios pptx** → `Performance-Ratios-Project.pptx`.
2. **FIN-321 pptx** → renamed too, for consistency: `FIN321_AI_Hedging_Project.pptx` → `FX-Hedging-Project.pptx`.
3. **`ignore-term/` → `ignore/`** everywhere (FIN-321 was the only holdout).
4. **`BUS-620/ignore/in-progess/` → `projects/in-progress/`** — confirmed, all three case studies promote to tracked/public.
5. **Master Ratios Spreadsheet** — checked tab-for-tab: `docs/spreadsheets/Corporate Finance Master Spreadsheets.xlsx` contains every tab from the old BUS-314 master except `Personal taxes (class example)`, confirmed fine to lose. `docs/spreadsheets/Corporate Finance Master Spreadsheets.xlsx` is now the live Master Ratios Spreadsheet reference; the old BUS-314 copy moved with the rest of BUS-314 into `_archive/bus314/_spreadsheets/`.
6. **`courses/`** stays as the top-level name.
7. **BUS-629-VEMBA `docs/decisions/2026-05-16-bus629-pop-quiz-extension.md`** → deleted (not flattened/kept).
8. **`_tools/` (grading scripts)** for both BUS-314 and BUS-629 → not offering-specific, moves to `projects/performance-ratios/_tools/`. Same logic applied to FIN-321's `_tools/` and `_templates/` → `projects/fx-hedging/`.
9. **BUS-314's `accounting-ratios/`** (and `_templates/`, `_tools/`, `_spreadsheets/`) → superseded by `projects/performance-ratios/`, archived wholesale to `_archive/bus314/`. **Amended 2026-07-10:** a lightweight `BUS-314/README.md` offering folder is restored under `International-Corporate-Finance/`, matching the `BUS-629-VEMBA/` naming pattern for consistency — the *project content* stays archived, but the offering itself should be discoverable in the live `courses/` tree rather than only in `_archive/`. The README is marked inactive and points to `_archive/bus314/` for the full historical project.
10. **Consistency pattern applied repo-wide**, including to FIN-321 and BUS-313 which weren't explicitly detailed before — see hierarchy below. **This is my extrapolation of your consistency instruction, flagging it explicitly since it wasn't spelled out per-subject**: FIN-321 gets a `projects/fx-hedging/` + `FIN-321/` split; BUS-313 gets a `projects/github-portfolio-extra-credit/` + `BUS-313/` split (its only concrete project artifact is the GitHub-portfolio extra-credit assignment — the team case-study project referenced in the syllabus has no dedicated files on disk beyond what's already in `ignore/`, so there's nothing else to move into `projects/`).
11. **BUS-620 / BUS-620-DLEMBA** — `dlemba/` renamed to `BUS-620-DLEMBA/`; new `BUS-620/` folder added for the MBA-specific README, matching the `BUS-629-VEMBA/` naming pattern.

## Target Directory Hierarchy (final)

```
courses/
├── README.md                                           Shidler code → subject directory map
│
├── International-Corporate-Finance/
│   ├── README.md                                        subject hub
│   ├── projects/
│   │   └── performance-ratios/
│   │       ├── Performance-Ratios-Project.pptx
│   │       ├── stage0-repo-setup.md … stage5-llm-analysis-evaluation.md
│   │       ├── analysis/ data/ deliverables/ demo-portfolio-repo/ models/
│   │       ├── docs/                                     incl. docs/decisions/2026-04-03-bus629-accounting-ratios-project-design.md
│   │       └── _tools/                                    grade_stage2/3/4.py — paths updated
│   └── BUS-629-VEMBA/
│       ├── README.md                                     current BUS-629 README, moved as-is
│       └── BUS-629 Danh sách Nhóm.xlsx
│       (ignore/ stays here — student submissions/grading records)
│
├── International-Finance-And-Securities/
│   ├── README.md
│   ├── projects/
│   │   └── fx-hedging/
│   │       ├── FX-Hedging-Project.pptx                   renamed from FIN321_AI_Hedging_Project.pptx
│   │       ├── excel-template/
│   │       ├── README.md scenarios.md stage1…stage4 assignment docs
│   │       ├── _templates/
│   │       └── _tools/
│   └── FIN-321/
│       ├── README.md                                     current top-level README, moved as-is
│       └── ignore/                                        renamed from ignore-term/
│
├── International-Economics-And-Trade/                     renamed from BUS-313-...
│   ├── README.md
│   ├── projects/
│   │   └── github-portfolio-extra-credit/
│   │       ├── extra-credit-github-portfolio.md
│   │       └── BUS313_Extra_Credit_GitHub_Portfolio.pptx
│   └── BUS-313/
│       ├── README.md                                      heading stays "BUS 313: The Economic and Financial Environment of Global Business"
│       ├── _tools/
│       └── ignore/
│
├── Micro-And-Macro-Economics/
│   ├── README.md
│   ├── projects/
│   │   ├── individual-research/                           renamed from individual-project/
│   │   ├── team-research/                                  renamed from team-project/
│   │   └── in-progress/                                    promoted from ignore/in-progess/
│   ├── BUS-620/
│   │   └── README.md                                       moved from current top-level README.md
│   └── BUS-620-DLEMBA/
│       └── README.md                                        renamed from dlemba/README.md
│
└── Windward-Community-College/                              unchanged

_archive/
└── bus314/                                                  entire old BUS-314 dir (README, accounting-ratios/, _templates/, _tools/, ignore-term/, and _spreadsheets/ pending item 5)

docs/decisions/                                              flattened, bus313/bus314/bus629/fin321 subdirs removed (all 12 files already match YYYY-MM-DD-<code>-<slug>)

.claude/skills/
└── accounting-ratios/                                       renamed from bus314-accounting-ratios/
```

## Documentation Updates Required

- Root `README.md` — repo tree, Active Courses table, campus-locations table
- `CLAUDE.md` — Active Courses table (correct BUS 629's "GAAP conversion + DCF" description — no such project exists, see Investigation below), Key Reference Paths
- `.claude/skills/accounting-ratios/SKILL.md` — activation path → `courses/International-Corporate-Finance/projects/performance-ratios/`
- `docs/decisions/README.md` — document the flattened `YYYY-MM-DD-<code>-<slug>` convention
- New hub READMEs: `courses/README.md`, `courses/International-Corporate-Finance/README.md`, `courses/International-Finance-And-Securities/README.md`, `courses/International-Economics-And-Trade/README.md`, `courses/Micro-And-Macro-Economics/README.md`

## Investigation: where's the DCF project?

No `dcf/` folder or DCF stage docs exist anywhere in the repo. BUS-629's actual stage docs are the same ratios workflow as BUS-314. The GAAP-conversion methodology shows up as one supporting artifact inside the ratios project (`models/templates/gaap-bridge-template.xlsx`), not a separate project. `CLAUDE.md`'s "GAAP conversion + DCF (active)" description is aspirational text that never matched what's taught — corrected as part of this migration.

## Out of Scope

- BUS 122B / Windward Community College — unchanged.
- `docs/decisions/2026-02-15-repo-hierarchy.md` — left as historical record, not rewritten.
- `.claude/settings.local.json` — will have stale path strings in old permission entries; harmless, not worth a mass edit.

## Migration Mapping

| Old path | New path |
|---|---|
| `courses/BUS-629-VEMBA-.../{stage0-5*.md, analysis, data, deliverables, demo-portfolio-repo, docs, models, _tools}` | `courses/International-Corporate-Finance/projects/performance-ratios/` |
| `courses/BUS-629-.../BUS629_AI_Ratios_Project.pptx` | `.../projects/performance-ratios/Performance-Ratios-Project.pptx` |
| `courses/BUS-629-.../{README.md, roster, ignore}` | `courses/International-Corporate-Finance/BUS-629-VEMBA/` |
| `courses/BUS-629-.../docs/decisions/bus629/2026-05-16-...md` | deleted |
| `courses/BUS-314-International-Corporate-Finance/` | `_archive/bus314/` |
| `courses/FIN-321-.../project-fx-hedging/` + `_templates/` + `_tools/` | `courses/International-Finance-And-Securities/projects/fx-hedging/` |
| `courses/FIN-321-.../{README.md, ignore-term→ignore}` | `courses/International-Finance-And-Securities/FIN-321/` |
| `courses/BUS-313-.../{extra-credit-github-portfolio.md, BUS313_Extra_Credit_GitHub_Portfolio.pptx}` | `courses/International-Economics-And-Trade/projects/github-portfolio-extra-credit/` |
| `courses/BUS-313-.../{README.md, _tools, ignore}` | `courses/International-Economics-And-Trade/BUS-313/` |
| `courses/BUS-620-.../individual-project/` | `courses/Micro-And-Macro-Economics/projects/individual-research/` |
| `courses/BUS-620-.../team-project/` | `courses/Micro-And-Macro-Economics/projects/team-research/` |
| `courses/BUS-620-.../ignore/in-progess/` | `courses/Micro-And-Macro-Economics/projects/in-progress/` |
| `courses/BUS-620-.../README.md` | `courses/Micro-And-Macro-Economics/BUS-620/README.md` |
| `courses/BUS-620-DLEMBA-.../README.md` | `courses/Micro-And-Macro-Economics/BUS-620-DLEMBA/README.md` |
| `docs/decisions/{bus313,bus314,bus629,fin321}/*.md` | `docs/decisions/*.md` |
| `.claude/skills/bus314-accounting-ratios/` | `.claude/skills/accounting-ratios/` |

## Implementation Order

1. Flatten `docs/decisions/<code>/` subdirs.
2. Delete BUS-629 pop-quiz-extension decision doc.
3. `git mv` the four subject renames.
4. Carve `projects/performance-ratios/` + `BUS-629-VEMBA/` out of `International-Corporate-Finance/`.
5. Archive BUS-314 wholesale to `_archive/bus314/` (spreadsheet pending item 5 resolution).
6. Carve `projects/fx-hedging/` + `FIN-321/` out of `International-Finance-And-Securities/`.
7. Carve `projects/github-portfolio-extra-credit/` + `BUS-313/` out of `International-Economics-And-Trade/`.
8. Carve `projects/{individual-research,team-research,in-progress}/` + `BUS-620/` + `BUS-620-DLEMBA/` out of `Micro-And-Macro-Economics/`.
9. Rename pptx files; fix hardcoded paths in relocated grading scripts.
10. Rename/repoint the `accounting-ratios` skill.
11. Write new hub READMEs; update root `README.md`, `CLAUDE.md`, `docs/decisions/README.md`.
12. Repo-wide grep sweep for stale old-path strings; fix any dead links.
