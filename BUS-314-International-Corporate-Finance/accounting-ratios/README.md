# BUS-314 Multi-Stage Project – Accounting & Performance Ratios

Author: Adam Stauffer
Last Updated: 2026-02-24

## Project Overview

In this four-stage project you will select a **publicly traded company**, pull data from its most recent financial statements (Balance Sheet, Income Statement, and Cash Flow Statement), and build a comprehensive **accounting ratios model** in Excel. Along the way you will write a professional memo, construct a working spreadsheet, draft a technical specification documenting your model, and deliver a final analysis with strategic recommendations and a structured AI prompt.

Each stage builds on the last — your memo frames the problem, your Excel build implements the model, your spec documents and reflects on what you built, and your final analysis interprets the results for management.

## Deliverable Timeline

| Stage | Deliverable | Points |
|-------|------------|--------|
| 1 | Executive Memo | 4 |
| 2 | Excel Model Build | 6 |
| 3 | Technical Specification | 4 |
| 4 | Final Analysis, Prompt Engineering & Recommendation | 10 |
| EC | Extra Credit | up to 3 |
| | **Total** | **24 + 3 EC** |

## Ratio Categories Covered

Your model will compute ratios across six categories taught in class:

1. **Performance** – MVA, Market-to-Book, EVA
2. **Profitability** – ROA, ROC, ROE (start-of-year and average-based)
3. **Efficiency** – Asset Turnover, Receivables Turnover, Inventory Turnover, Profit Margin
4. **Leverage** – Debt Ratios, Times Interest Earned, Cash Coverage, Debt Burden
5. **Liquidity** – Current Ratio, Quick Ratio, Cash Ratio, NWC-to-Assets
6. **Du Pont System** – ROA and ROE decomposition

## Project Structure

```
BUS-314/accounting-ratios/
├── README.md                          ← you are here
├── stage1-memo-assignment.md          ← Stage 1 instructions
├── stage2-excel-build-assignment.md   ← Stage 2 instructions
├── stage3-spec-assignment.md          ← Stage 3 instructions
├── stage4-final-analysis-assignment.md ← Stage 4 instructions
├── extra-credit.md                    ← Extra credit options
├── company-selection.md               ← How to choose your company
├── _scenarios/                        ← Company scenario spreadsheets
├── _templates/
│   └── excel/
│       └── README.md                  ← Excel template guide
└── archive/
    ├── analysis/                      ← Your working files
    ├── deliverables/                  ← Final outputs
    ├── prompts/                       ← AI prompt iterations
    └── specs/                         ← Technical specs
```

## Getting Started

1. You will be assigned one of the company scenarios in `_scenarios/`.
2. Work through the stages in order — each one feeds the next.
3. Use `../_templates/template-decision-memo.md` and `../_templates/template-spec.md` as starting points.
4. Use the accounting ratio spreadsheet provided in class and available in Lamaku as your Excel template.
5. Commit all Markdown deliverables (`.md`) to your GitHub repository.
6. Store your working files in the `archive/` subdirectories.

## AI Tools (Optional, Not Required)

AI tools like Claude, ChatGPT, or Copilot can accelerate your work — especially in Stage 4. However, **AI is not required for any stage.** Students without AI access can complete every deliverable using standard resources (SEC filings, Excel, class notes). If you use AI, document it per the course AI Usage Guidelines.

## Committing Your Work

All Markdown deliverables (`.md` files) should be committed to your GitHub repository. Recommended locations:

| Deliverable | Where to Save |
|-------------|---------------|
| Stage 1 memo | `docs/decisions/` |
| Stage 2 Excel model | `docs/templates/excel/` |
| Stage 3 spec | Root of your project directory or `docs/` |
| Stage 4 final analysis | Root of your project directory or `docs/` |

**Workflow:**
1. Create your `.md` file using the appropriate template.
2. Save it in the recommended directory within your repository.
3. Stage, commit, and push: `git add <file>` → `git commit -m "Stage X deliverable"` → `git push`.
4. Verify your file is visible on GitHub.

## Key Resources

- **Financial Statements:** SEC EDGAR, Yahoo Finance, Macrotrends, company investor relations pages
- **Class Spreadsheet:** `BUS-314/_spreadsheets/BUS-314 Accounting & Performance Ratios - MASTER.xlsx`
- **Scenario Workbooks:** `_scenarios/BUS314_[TICKER]_Scenario.xlsx`
- **Course AI Guidelines:** `docs/ai-usage-guidelines.md`
