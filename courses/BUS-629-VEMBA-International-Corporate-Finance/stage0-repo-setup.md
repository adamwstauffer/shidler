# Stage 0: Repository Setup & Infrastructure

**Weight:** 5% of project score

---

## Overview

Set up a professional-grade GitHub repository for your accounting ratios project. The directory structure is modeled on how analytical teams at investment banks, Big 4 firms, and corporate finance departments organize their work. You'll learn Git fundamentals, Markdown documentation, and professional file management — skills that underpin every subsequent stage.

## Why this matters

Every stage of this project depends on having a well-organized workspace. In professional finance, analysts who can't find files, version documents, or maintain a clean project structure waste enormous time. This stage removes the tooling barrier before any graded analytical work begins.

---

## Deliverable

A GitHub repository with the structure below. The course repository ([`courses/BUS-629-VEMBA-International-Corporate-Finance/`](../)) serves as a **living example** — study its READMEs, then replicate the structure in your own repo.

### Required directory structure

```
[your-github-username]/
├── README.md                  # Project charter: your name, company (TBD), timeline
├── docs/
│   ├── memos/                 # Executive memos (Stage 2, decision docs)
│   │   └── README.md
│   ├── specs/                 # Technical specifications (Stage 4)
│   │   └── README.md
│   ├── plans/                 # Project plans, timelines, status
│   │   └── README.md
│   └── templates/             # Reusable templates
│       ├── README.md
│       ├── memo-template.md   # Copy from course repo
│       └── spec-template.md   # Copy from course repo
├── models/
│   ├── templates/             # Stage 1: blank ratio template
│   │   └── README.md
│   └── builds/                # Stage 3: populated model
│       └── README.md
├── data/                      # Source financial data
│   └── README.md
├── analysis/
│   └── validation/            # Stage 3: self-audit reports
│       └── README.md
└── deliverables/              # Stage 5: final outputs
    └── README.md
```

---

## What you'll learn

### 1. README.md files

Each directory gets a README explaining:
- What belongs in this directory
- Naming conventions for files
- Any relevant context or instructions

A README is the "front door" to any directory. If someone new opened your repo, they should be able to navigate it from READMEs alone. Your top-level `README.md` serves as a **project charter** — your name, the project scope, and a status tracker you'll update as you complete each stage.

### 2. Markdown fundamentals

Through writing READMEs, you'll practice:
- **Headings** (`#`, `##`, `###`)
- **Lists** (bulleted and numbered)
- **Tables** (for structured data)
- **Links** (to other files in the repo)
- **Code blocks** (for naming conventions and examples)

These are the same formatting tools you'll use for memos (Stage 2), validation reports (Stage 3), specs (Stage 4), and final analysis (Stage 5).

### 3. Git basics

At minimum, you should be comfortable with:
- **Clone** — copy the repo to your local machine
- **Add & Commit** — save changes with descriptive messages
- **Push** — upload commits to GitHub
- **Pull** — sync changes from GitHub

Commit messages should be descriptive. Not "update" or "fix" — instead: "Add Stage 1 ratio template with named ranges" or "Complete Du Pont validation in Stage 3 audit."

### 4. Separation of concerns

Notice how the structure separates:
- **Raw data** (`data/`) from **analysis** (`analysis/`)
- **Blank templates** (`models/templates/`) from **populated models** (`models/builds/`)
- **Working documents** (`docs/`) from **final deliverables** (`deliverables/`)

This mirrors how professional teams prevent errors and maintain auditability. A model reviewer should be able to trace any number back to its source.

---

## Professional context

| Directory | IB / Professional Analogue |
|-----------|---------------------------|
| `docs/memos/` | Deal memos, investment committee briefs |
| `docs/specs/` | Model specification documents, methodology papers |
| `docs/plans/` | Project plans, pitch timelines |
| `docs/templates/` | Firm-wide memo and spec formats |
| `models/templates/` | Blank model frameworks (LBO template, DCF skeleton) |
| `models/builds/` | Working models with live data |
| `data/` | Data room, source documents |
| `analysis/validation/` | Working papers, model review documentation |
| `deliverables/` | Client-ready pitchbooks, final reports |

---

## What to submit

A link to your GitHub repository. The repository must contain:
- [ ] Full directory structure as shown above
- [ ] `README.md` files in every directory
- [ ] Top-level `README.md` with your name and project scope
- [ ] Templates copied from the course repo (`memo-template.md`, `spec-template.md`)
- [ ] At least 3 meaningful commits with descriptive messages

---

## Rubric (% of Stage 0 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Directory Structure | 30% | All required directories present; logical organization; no orphan files |
| README Quality | 30% | Every directory has a README; READMEs explain purpose and conventions; top-level README serves as project charter |
| Markdown & Formatting | 20% | Correct use of headings, lists, tables, links; consistent formatting |
| Git Fundamentals | 20% | Meaningful commits; descriptive commit messages; clean history |

---

## Tips

- **Start by studying the course repo.** Every directory in [`courses/BUS-629-VEMBA-International-Corporate-Finance/`](../) has a README you can reference.
- **Don't overthink the READMEs.** 5–10 lines per directory README is sufficient. Clarity over length.
- **Commit early and often.** Don't build the entire structure and commit once. Commit after creating each major section.
- **Your README.md will evolve.** Update your top-level README as you complete each stage — it becomes a living status tracker for your project.
