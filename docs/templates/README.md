# Templates & Examples

Reusable templates for course materials, assignments, and professional portfolio materials. These provide consistent structure across all student work — the same way investment banks and consulting firms maintain firm-wide templates for models, memos, and pitch materials.

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

**Together they enforce clarity, consistency, and reproducibility — exactly what employers expect.**

---

## Templates Directory

### Assignment & Project Templates

- **[`memo-template.md`](./memo-template.md)** — Executive memo (Stage 1 / Stage 2 deliverables)
- **[`spec-template.md`](./spec-template.md)** — Technical specification (Stage 4 deliverables; originally authored for ratios analysis, adaptable to other model-driven projects)
- **[`case-brief-template.md`](./case-brief-template.md)** — Case analysis brief (BUS-313, BUS-620)
- **[`prompt-log-template.md`](./prompt-log-template.md)** — Running log of AI prompts and outputs

### Professional Portfolio

- **[`portfolio/`](./portfolio/)** — Bio and resume templates for student GitHub portfolios

---

## Frontmatter Schema

Every Markdown template in this directory carries a YAML frontmatter block so humans and LLMs can identify the template's purpose without reading the body.

```yaml
---
template: memo                    # one of: memo, spec, case-brief, prompt-log
purpose: "Short description of what the template is for"
audience: student                 # student | instructor | both
fields_required: [list, of, fields, the, student, must, fill, in]
naming_convention: "YYYY-MM-DD-{slug}.md"
courses: [BUS-314, BUS-629, FIN-321]   # optional — courses that use this template
notes: "Optional caveats or adaptation notes"
---
```

**Why frontmatter:** When a student (or an LLM in the BUS-629 Stage 4 spec-drafting workflow) is choosing which template to apply, they should not have to read the entire body to figure out what the template is for. The `purpose` and `fields_required` keys answer that question in one block.

---

## File Naming Conventions

A single naming convention applies across the repo. When in doubt, follow these:

| Artifact | Convention | Example |
|----------|------------|---------|
| Decision memo / project memo | `YYYY-MM-DD-{slug}.md` | `2026-04-03-bus629-accounting-ratios-project-design.md` |
| Technical spec | `YYYY-MM-DD-{slug}.md` | `2026-05-15-aapl-ratios-spec.md` |
| Stage assignment file | `stageN-{slug}.md` | `stage4-technical-specification.md` |
| Student spreadsheet deliverable | `YYYY-MM-DD-{company-slug}-financials.xlsx` | `2026-05-12-toyota-financials.xlsx` |
| Prompt log | `prompt-log.md` (one per project, in `deliverables/`) | `deliverables/prompt-log.md` |

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

---

## Archived Templates

The following are preserved in `_archive/templates/` for historical reference:

- `prompt-example-interest-rate-parity.md` — pre-current-spec example
- `risk-memo-template.md` — superseded by the unified `memo-template.md`
- `spec-example-interest-rate-parity.md` — pre-current-spec example
