# Templates & Examples

Reusable templates for course materials, assignments, and professional portfolio materials. They give all student work the same structure.

## What is a "spec"?

In the OpenAI video [Introducing Specs](https://openai.com/index/introducing-specs/), a spec (short for specification) is a structured document that clearly defines:

- the goal of a task
- the steps required
- the expected inputs/outputs
- the evaluation criteria

It acts as a contract between humans and AI systems, ensuring consistency, reproducibility, and clarity in how work is done.

### Specs vs. Prompts

**Prompts:** Instructions given to an AI in natural language. They are flexible, conversational, and immediate. Example: "Explain Interest Rate Parity with an example."

**Specs:** Formalized blueprints that outline how to approach a problem systematically. They provide context, requirements, and evaluation rules.

**How they complement each other:**

- A spec defines the scope and structure of a task.
- A prompt executes a part of that task inside the spec.

In practice:

- The spec ensures that multiple people (or agents) would approach the problem the same way.
- The prompts are the tactical instructions used at each stage.

### Using Specs + Prompts in Economics

**In teaching:** Specs define structured student projects (e.g., analyzing tariffs, calculating FX hedges). Prompts help students generate analysis, visuals, or summaries.

**In research:** Specs define methodology (e.g., data sources, models, reproducibility requirements). Prompts handle execution (e.g., regression code, lit review summaries).

**In policy/consulting:** Specs provide consistent evaluation frameworks (e.g., for assessing monetary policy). Prompts generate scenario narratives and what-if analyses.

**Together they make the work clear, consistent, and reproducible.**

---

## Templates Directory

### Assignment & Project Templates

- **[`stage-brief-template.md`](./stage-brief-template.md)** — **The stage brief.** Every stage brief in every course uses its frontmatter block and its ten sections, in order. Carries the enumerated ban list (course codes, weeks, dates, weights, LMS names, delivery mode) that keeps a brief semester-invariant, and a register table mapping conversational phrasing to its instructional replacement. Authored 2026-08-02
- **[`memo-template.md`](./memo-template.md)** — Executive memo (Stage 1 / Stage 2 deliverables)
- **[`spec-template.md`](./spec-template.md)** — Technical specification (Stage 4 deliverables; originally authored for ratios analysis, adaptable to other model-driven projects)
- **[`case-brief-template.md`](./case-brief-template.md)** — Case analysis brief (BUS-313, BUS-620)
- **[`prompt-log-template.md`](./prompt-log-template.md)** — Running log of AI prompts and outputs
- **[`spec-retrospective-template.md`](./spec-retrospective-template.md)** — Retrospective on a spec after an AI build: what the spec got right and what it missed
- **[`spreadsheets/performance-ratios-template.xlsx`](./spreadsheets/performance-ratios-template.xlsx)** — Ratios workbook template for the Performance Ratios project

### Professional Portfolio

- **[`portfolio/`](./portfolio/)** — Bio and resume templates for student GitHub portfolios
- **[`portfolio/firstname-lastname/`](./portfolio/firstname-lastname/)** — The one sample student repository: how a finished `firstname-lastname` repo is laid out

---

## Frontmatter Schema

Every Markdown template in this directory carries a YAML frontmatter block so humans and LLMs can identify the template's purpose without reading the body.

```yaml
---
template: memo                    # one of: memo, spec, case-brief, prompt-log, stage-brief
purpose: "Short description of what the template is for"
audience: student                 # student | instructor | both
fields_required: [list, of, fields, the, student, must, fill, in]
naming_convention: "YYYY-MM-DD-{slug}.md"
courses: [BUS-314, BUS-629, FIN-321]   # optional — courses that use this template
notes: "Optional caveats or adaptation notes"
---
```

**Why frontmatter:** When a student (or an LLM in the BUS-629 Stage 4 spec-drafting workflow) is choosing which template to apply, they should not have to read the entire body to figure out what the template is for. The `purpose` and `fields_required` keys answer that question in one block.

### Instantiated stage briefs

A stage brief written *from* `stage-brief-template.md` carries a different block — the template's own frontmatter describes the template; an instantiated brief describes the assignment:

```yaml
---
template: stage-brief
project: perfect-competition-marginal-costs   # directory slug
stage: 1                                      # INTEGER, numbered per case from 1
title: "Repo + Brief"
capability: marginal-analysis                 # the capabilities/<capability>/ folder; omit if none
deliverables:                                 # the canonical path declaration
  - path: docs/briefs/YYYY-MM-DD-perfect-competition-brief.md
    format: markdown
    ai_boundary: human-first                  # per artifact: human-first | ai-first-verified | not-permitted
prerequisites: [1, 2]                         # prior stages whose deliverables must exist; [] for the first
points: 3                                     # must equal the rubric total
estimated_time: "60-80 min"
---
```

The `deliverables` block is the **canonical declaration** of the artifact paths. Downstream consumers — the Kumu stage page and the Kumu site's gate checks — hold literal mirrors of it, each citing the brief it mirrors, and the match is verified at PR rather than resolved at runtime. Changing a path here means changing those mirrors in the same pull request.

---

## File Naming Conventions

A single naming convention applies across the repo. When in doubt, follow these:

| Artifact | Convention | Example |
|----------|------------|---------|
| Decision memo / project memo | `YYYY-MM-DD-{slug}.md` | `2026-05-15-company-selection-memo.md` |
| Technical spec | `YYYY-MM-DD-{slug}.md` | `2026-05-15-aapl-ratios-spec.md` |
| Stage assignment file | `stageN-{slug}.md` | `stage4-technical-specification.md` |
| Student dated document | `YYYY-MM-DD-{slug}-{type}.md` — `{type}` one of `brief` · `spec` · `memo` · `analysis` · `log`; no last name (the repo is named for the student); older names already submitted still count | `2026-05-21-vinamilk-selection-memo.md` |
| Student spreadsheet deliverable | `YYYY-MM-DD-{company-slug}-financials.xlsx` | `2026-05-12-toyota-financials.xlsx` |
| Prompt log | `prompt-log.md` (one per repository, at the root; an older `deliverables/prompt-log.md` still counts) | `prompt-log.md` |

**Slug rules:** lowercase, hyphen-separated, no spaces or underscores. Keep slugs short but descriptive (3–6 words).

**Date rules:** ISO format (`YYYY-MM-DD`) so files sort chronologically. Use the date the document was first authored, not the date it was last edited.

---

## How to Use These Templates

1. **Copy the appropriate template** to your course or project directory
2. **Rename** following the naming convention above
3. **Customize for your needs** — Add course-specific context, requirements, and examples
4. **Keep the frontmatter** — Update fields like `courses` if you adapt the template, but leave the schema intact so tooling continues to work
5. **Maintain consistency** — Use the same template structure across all projects and courses

## Quick Reference

| Need | Template |
|------|----------|
| Write a project memo | [`memo-template.md`](./memo-template.md) |
| Create a project spec | [`spec-template.md`](./spec-template.md) |
| Analyze a case study | [`case-brief-template.md`](./case-brief-template.md) |
| Draft a professional bio | [`portfolio/bio-template.md`](./portfolio/bio-template.md) |
| Update your resume | [`portfolio/resume-template.md`](./portfolio/resume-template.md) |
| Log AI prompts | [`prompt-log-template.md`](./prompt-log-template.md) |
| Look back on a spec | [`spec-retrospective-template.md`](./spec-retrospective-template.md) |
| See a finished student repo | [`portfolio/firstname-lastname/`](./portfolio/firstname-lastname/) |

