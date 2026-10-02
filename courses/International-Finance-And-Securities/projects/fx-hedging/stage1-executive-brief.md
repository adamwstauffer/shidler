---
template: stage-brief
project: fx-hedging
stage: 1
title: "Executive Brief"
capability: fx-hedging
deliverables:
  - path: "docs/briefs/YYYY-MM-DD-{scenario}-hedge-brief.md"
    format: markdown
prerequisites: [0]
weight: "17% of project"
# ai_boundary per deliverable: pending instructor ruling (2026-09-24 Micro/Macro parity pass)
---

# Stage 1 – Executive Brief (17% of project)

> The brief's content matches the prior four-stage version (where it was the memo) (archived at
> `../../../../_archive/fin321/stage-docs-v1/stage1-memo-assignment.md`); this stage is typically
> already in flight when the term opens. This version adds the rubric table (grading transparency)
> and the canonical save location/filename.

## Goal

Using `_templates/template-decision-memo.md`, write a **400–600 word executive brief to your CFO**
explaining your firm's **FX receivable exposure** and why hedging is worth considering.

## Instructions

**Scenario:** Your firm expects to receive a foreign-currency payment (see your assigned
scenario in `scenarios.md`) on a specific future date. Exchange-rate volatility could affect
how much your company ultimately receives in USD.

**Include:**

1. **What the exposure is** — currency, amount, timing.
2. **Why it's risky** — what could go wrong for USD proceeds.
3. **Three hedge families** — forward, money market, options — with quick pros/cons for each.
4. **Next steps** — what you'll build in Stages 2–5:
   - *Model Specification (Stage 2):* design the workbook — inputs, named ranges, calculation
     flow — before building.
   - *AI-Assisted Build (Stage 3):* generate the workbook from your spec and audit the output.
   - *Market Data (Stage 4):* load live market data and confirm the model holds up.
   - *Validate & Decision Memo (Stage 5):* validate against an independent LLM run and
     deliver the hedge recommendation in a decision memo.

**Tone:** executive-friendly and clear. The CFO has 90 seconds.

**This is the project's engagement brief** (Kumu's deliverable-templates page) — one document,
not two. Alongside the four items above it carries the engagement brief's own sections and
frontmatter (`type: brief`, a one-line `hypothesis`):

- **What I am assuming** — the assumptions taken as given, and which you would test with more time.
- **Hypothesis** — "I expect X because Y," in real quantities: a prediction about what the model
  will show, not a recommendation (that waits for Stage 5).
- **How I would know I was wrong** — the observation that would falsify the hypothesis.

It goes in `docs/briefs/`, at the path below — briefs ask, memos answer, and the decision memo in
`docs/decisions/` comes at Stage 5. (Before 2026-10-02 the brief lived in `docs/decisions/`; one
already committed there still counts.)

## Where this project's files go

Stage 0 stood up your portfolio repo to the course-independent standard, and this project adds no
folders to it. Every stage from here commits into a folder you already have — the spec and the
workbook into the capability folder, `capabilities/fx-hedging/`, the way BUS 620 keeps
`capabilities/marginal-analysis/`.

```
firstname-lastname/
  capabilities/
    fx-hedging/        README.md, spec.md (Stage 2), model.xlsx (Stages 3–4)
  docs/
    briefs/            the executive brief (Stage 1)
    decisions/         the decision memo (Stage 5)
  data/                market data, with source and timestamp
  analysis/            the build audit, and the validation work
```

| Stage | Deliverable | Where it goes |
|---|---|---|
| 1 | Executive brief (hedge framing) | `docs/briefs/YYYY-MM-DD-{scenario}-hedge-brief.md` |
| 2 | Model specification | `capabilities/fx-hedging/spec.md` · `capabilities/fx-hedging/README.md` |
| 3 | Built workbook + build audit | `capabilities/fx-hedging/model.xlsx` · `analysis/YYYY-MM-DD-{scenario}-build-audit-analysis.md` |
| 4 | Market-data memo | `data/YYYY-MM-DD-{scenario}-market-data-memo.md` |
| 5 | Validation + decision memo | `analysis/YYYY-MM-DD-{scenario}-validation-analysis.md` · `docs/decisions/YYYY-MM-DD-{scenario}-hedge-decision-memo.md` |

This section moved here from Stage 0 (course site 2026-08-20; this brief 2026-09-24), because
Stage 0 is now the course-level workspace. **Superseded 2026-09-24 (Adam):** it used to add two
project folders, `docs/specs/` and `models/builds/`; the spec and workbook now go in
`capabilities/fx-hedging/` instead. Summer 2026 repositories keep the old folders.

## Deliverable

- File: `docs/briefs/YYYY-MM-DD-{scenario}-hedge-brief.md`
- 400–600 words, from the decision-memo template, YAML frontmatter intact.
- Committed and pushed.
- Already submitted under the older name (`docs/decisions/YYYY-MM-DD-{lastname}-{scenario-slug}-hedge-framing.md`)? It still counts, exactly as if it carried the new name — nothing to move or rename.

## Evaluation

| Criterion | Description | Weight |
| --------- | ----------- | -----: |
| Exposure framing | Currency, amount, timing, and business consequence stated precisely | 25% |
| Hedge families & trade-offs | All three families, with honest pros/cons, not boilerplate | 25% |
| Next steps | Correctly frames the Stage 2–5 arc as a plan the CFO can approve | 25% |
| Professionalism | Executive tone, 400–600 words, template used, correct location and filename, committed | 25% |

---

## How this leads to Stage 2

Every variable you name in this brief — the receivable amount, the timing, the rates that matter —
becomes a **named input** in your Stage 2 specification. If the brief is vague about the exposure,
the spec will be vague about the model. Write the brief like the model depends on it, because it
does.
