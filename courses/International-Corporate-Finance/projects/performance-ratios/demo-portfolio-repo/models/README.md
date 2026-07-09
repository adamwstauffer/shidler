# `models/`

All Excel work for the course. The split between `templates/` and `builds/` matters — keep them separate.

## Subdirectories

| Folder | Purpose | Course stage |
|--------|---------|--------------|
| [`templates/`](templates/) | Blank model frameworks (skeletons with named ranges, no data) | Stage 1 |
| [`builds/`](builds/) | Populated, working models with real data | Stage 3 |

## Why the split

A *template* is a reusable framework — tabs, named ranges, formulas wired up but no inputs. A *build* takes that template and fills it with one company's (or one scenario's) data. Keeping them separate lets you reuse the template across multiple builds without forking history.

## Naming conventions

- Templates: `<model-name>-template.xlsx` — e.g., `dcf-template.xlsx`
- Builds: `<company>-<model>-<YYYY-MM-DD>.xlsx` — e.g., `vingroup-dcf-2026-05-09.xlsx`
