# BUS 629: International Corporate Finance

**Vietnam Executive MBA Program** | University of Hawai'i at Manoa, Shidler College of Business

## Course Overview

This course explores international corporate finance topics and applications relevant to global business contexts. The primary project is a **spec-driven accounting ratios analysis** where students build financial models, write technical specifications, and critically evaluate LLM-generated analysis.

## Instructor

**Adam W. Stauffer** | [adamstau@hawaii.edu](mailto:adamstau@hawaii.edu)

For more information about the instructor, see [BIO.md](../BIO.md).

## Project: Accounting Ratios Analysis

A 6-stage project adapted from BUS-314 for MBA-level rigor. Students build ratio templates from scratch, select their own companies (including non-U.S. and ASEAN-listed firms), and use spec-driven design to delegate analysis to an LLM — then critically evaluate the output.

| Stage | Deliverable | Weight |
|-------|------------|--------|
| 0 | Repository Setup & Infrastructure | 5% |
| 1 | Template Architecture | 20% |
| 2 | Company Selection Memo | 10% |
| 3 | Model Population & Validation | 25% |
| 4 | Technical Specification | 20% |
| 5 | LLM Analysis & Executive Evaluation | 20% |

See [project design memo](docs/memos/2026-04-03-bus629-accounting-ratios-project-design.md) for full details.

## Repository Structure

This repository serves as a **living example** of the directory structure students should replicate in their own repos. Each directory contains a `README.md` explaining its purpose and conventions.

```
BUS-629-VEMBA-International-Corporate-Finance/
├── README.md                  ← You are here
├── docs/
│   ├── memos/                 # Executive memos and decision documents
│   ├── specs/                 # Technical specifications
│   ├── plans/                 # Project plans and timelines
│   └── templates/             # Reusable templates (memo, spec)
├── models/
│   ├── templates/             # Blank model frameworks (Stage 1)
│   └── builds/                # Populated, working models (Stage 3)
├── data/                      # Source financial data and provenance
├── analysis/
│   └── validation/            # Self-audit and validation reports (Stage 3)
└── deliverables/              # Final, presentation-ready outputs (Stage 5)
```

## Key Links

| Resource | Location |
|----------|----------|
| Project Design Memo | [`docs/memos/2026-04-03-bus629-accounting-ratios-project-design.md`](docs/memos/2026-04-03-bus629-accounting-ratios-project-design.md) |
| Memo Template | [`docs/templates/memo-template.md`](docs/templates/memo-template.md) |
| Spec Template | [`docs/templates/spec-template.md`](docs/templates/spec-template.md) |
| Brand Guidelines | [`../docs/_branding/design.json`](../docs/_branding/design.json) |

---

*Course materials are under active development.*
