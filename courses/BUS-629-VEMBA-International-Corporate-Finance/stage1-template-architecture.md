# Stage 1: Provided Ratios Template

**Weight:** 20% of project score
**Format:** Upload-only — no presentation component
**Deliverable:** `performance-ratios-template.xlsx` uploaded to your repo

---

## Overview

Use the provided Excel ratios template — built by your instructor — as the foundation for the rest of the project. Download it, study its structure, and upload your own copy to your portfolio repo.

You will not modify the template at this stage. The point of Stage 1 is to make sure every student is working from the same architecture and named-range conventions before any company data lands in the model.

## Why we provide the template

In undergraduate sections (BUS-314), students design their own templates from scratch — that's a useful exercise for first-time modelers. At the EMBA level, the learning happens further down the pipeline: in *populating* a model under real reporting standards (Stage 3), in *specifying* analytical work precisely enough that an LLM can execute it (Stage 4), and in *evaluating* AI-generated analysis against your own judgment (Stage 5). Standardizing the template at Stage 1 protects the time we'll need for those higher-leverage activities.

---

## The provided template

**File:** [`../../docs/templates/spreadsheets/performance-ratios-template.xlsx`](../../docs/templates/spreadsheets/performance-ratios-template.xlsx)

**Tabs included:**

| Tab | Contents |
|-----|----------|
| **Cover & Instructions** | Project overview, how to use the template, named-range key |
| **Legend** | Color-coding key (yellow = inputs, blue = assumptions, green = formulas, gray = outputs) |
| **Income Statement** | Skeleton with line items and named-range placeholders (`INC_*`) |
| **Balance Sheet** | Skeleton with current and prior year columns (`BAL_*`, `startYear_*`) |
| **Cash Flow** | Skeleton for operating, investing, financing activities (`CASH_*`) |
| **Ratios** | All six categories with formulas pre-filled in named-range notation (`RATIO_*`) — auto-populates once Stage 3 financials are entered |

The Ratios tab is **fully formulaic** — no hardcoded numbers. When you populate the financial statements at Stage 3, ratios compute automatically.

---

## Deliverable

Upload your own copy of `performance-ratios-template.xlsx` to:

```
[your-repo]/models/templates/performance-ratios-template.xlsx
```

You should also create the following directory skeleton in your repo (if you haven't already):

```
your-repo/
├── README.md            # Bio (from Stage 0)
├── RESUME.md            # Resume (from Stage 0)
├── BIO.md               # Optional (from Stage 0)
├── docs/
│   ├── decisions/       # Memos and decision documents (Stage 2)
│   │   └── README.md
│   ├── specs/           # Technical specifications (Stage 4)
│   │   └── README.md
│   └── plans/           # Optional project plans
├── models/
│   ├── templates/       # ← Place performance-ratios-template.xlsx here
│   └── builds/          # Populated model lands here at Stage 3
├── data/                # Source financial data (Stage 3)
├── analysis/
│   └── validation/      # Self-audit reports
└── deliverables/        # Final outputs (Stage 5)
```

Each directory should have a short `README.md` explaining what belongs there. The course repo (`courses/BUS-629-VEMBA-International-Corporate-Finance/`) is a living example — copy and adapt its READMEs.

---

## What to submit

Submit nothing separately — just commit the template and the directory structure to your repo. Stage 1 is graded by inspection of the repo URL you submitted at Stage 0.

The repo must contain:

- [ ] `models/templates/performance-ratios-template.xlsx` (unmodified copy of the provided template)
- [ ] Directory skeleton above with a `README.md` in each directory
- [ ] At least 2 new commits since Stage 0 with descriptive messages

---

## Rubric (% of Stage 1 score)

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Template uploaded correctly | 30% | File is unmodified, in the right directory, with the correct filename |
| Directory structure | 40% | All required directories present; README.md in each; logical organization |
| README quality | 20% | READMEs explain purpose and conventions; not just placeholders |
| Commit hygiene | 10% | Meaningful commit messages; clean history |

---

## Tips

- **Open the template before uploading.** Click through every tab. Read the Cover & Instructions tab. Skim the Ratios tab — note how every formula is in named-range notation. You'll need this familiarity at Stages 3 and 4.
- **Don't modify the template at this stage.** If you spot something you'd want to change, write it down — it'll be useful for your Stage 4 spec.
- **Use the templates README as your reference.** [`../../docs/templates/README.md`](../../docs/templates/README.md) documents the file naming convention (`YYYY-MM-DD-{slug}.md`) you'll use for memos and specs in later stages.
