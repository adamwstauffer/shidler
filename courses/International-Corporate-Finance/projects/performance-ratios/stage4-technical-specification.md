# Stage 4: LLM-Drafted Technical Specification

**Weight:** 20% of project score
**Format:** Deliverable-only — no in-class presentation
**Deliverable:** Technical specification (`.md`) drafted with an LLM, plus a prompt log entry and evidence of human-in-the-loop (HIL) iteration

> **Where this fits in the project.**
> **Input:** Stage 1 ratios template (the model architecture) + Stage 3 populated workbook (the data values) + project instructions.
> **Output (this stage):** A technical specification at `docs/specs/YYYY-MM-DD-{lastname}-{company-slug}-spec.md`, plus visible evidence of at least one HIL iteration (in your prompt log, or as a standalone iteration file in `analysis/validation/`).
> **Used by:** Stage 5 (you feed *only* this spec to an LLM to produce the full analysis — the spec must stand alone).

> **Submission alternative — Lamaku upload.** GitHub is the required submission path. If you cannot push the spec to your repo, you may upload the `.md` file (and your prompt-log entry, as a separate file if needed) directly to Lamaku as a fallback. Use the same filename convention (`YYYY-MM-DD-{lastname}-{company-slug}-spec.md`). Using the Lamaku fallback does **not** reduce your Stage 4 grade. By Stage 5, the spec must also live in `docs/specs/` in your GitHub repo — the Stage 5 polish rubric assumes the full project history is in the repo.

> **Heads up — instructor write access.** If you haven't yet granted the instructor Write access on your repo, do it now (Stage 2 submission checklist item). Stage 5 grades 5% on how you incorporated the instructor's PR feedback on your Stage 2 memo — that 5% is unearnable without write access.

> **Unfamiliar terms?** "HIL," "spec," "diff," "named-range notation," and other recurring terms are defined in the [Project glossary in the BUS-629 README](README.md#project-glossary).

---

## Overview

Use an LLM (Claude or another capable model) to draft a formal technical specification that fully defines both the Excel ratio model and the analytical work to be done on your selected company. The spec must be precise enough that an LLM with no prior context — given only the spec as input — can produce a correct, comprehensive ratio analysis with strategic recommendations.

You are not writing the spec from a blank page. You are using an LLM to **draft** it, conditioned on the project instructions and your Stage 1 template. Your job is to direct the drafting, evaluate the output, and ship a spec that *you* would sign your name to.

**This is the central artifact of the project.**

## Why spec-driven design + LLM drafting

Two pedagogical moves stack here:

1. **Spec-driven design.** The ability to specify analytical work precisely is more valuable than the ability to execute it. Execution scales (via teams, tools, AI); specification requires domain expertise that cannot be delegated.
2. **LLM as drafter, you as editor.** The future of finance work is not "write everything from scratch" or "let AI write everything." It's specify the work, evaluate the output, and take responsibility for the final product.

A spec that produces wrong output at Stage 5 reveals a gap in your spec — and that feedback loop is where the deepest learning happens.

---

## Deliverable

A technical specification (`.md`, 3–5 pages) saved to `docs/specs/` in your repository, plus a corresponding prompt log entry.

**Spec filename:** `YYYY-MM-DD-{lastname}-{company-slug}-spec.md`
Example: `2026-06-18-nguyen-vinamilk-spec.md`

**Spec template — available three ways:**

- In this repo: [`docs/templates/spec-template.md`](../../../../docs/templates/spec-template.md)
- Public GitHub link: [`https://github.com/adamwstauffer/shidler/blob/main/docs/templates/spec-template.md`](https://github.com/adamwstauffer/shidler/blob/main/docs/templates/spec-template.md)
- Raw URL (for direct LLM upload — paste this URL into Claude.ai or ChatGPT and ask it to read): [`https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/spec-template.md`](https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/spec-template.md)

Copy, rename per the convention above, fill in the sections, keep the YAML frontmatter intact.

**Prompt log:** Add a row to your `deliverables/prompt-log.md` for each meaningful prompt session used to draft the spec. Use [`../../docs/templates/prompt-log-template.md`](../../../../docs/templates/prompt-log-template.md) if you don't already have one.

---

## Two LLM workflows — pick one

> **Never used a command line?** Choose **Workflow A**. It works in any browser, requires no install, and lets you focus on the spec instead of the tooling. Workflow B is faster once you're set up but adds an install/troubleshooting step. For Claude Code setup as a follow-on (optional), see [`docs/guides/claude-code-install-for-non-technical-users.md`](../../../../docs/guides/claude-code-install-for-non-technical-users.md).

### Workflow A — Claude desktop / ChatGPT (file uploads + URLs)

Best if you don't yet have a CLI workflow. Works in any browser. **No install required.**

1. Open [Claude](https://claude.ai) (or ChatGPT, or another capable model).
2. Give the LLM these inputs (combine file uploads and URLs — whichever is easier per item):
   - **This Stage 4 brief** — easiest is to paste the raw URL: `https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/International-Corporate-Finance/projects/performance-ratios/stage4-technical-specification.md`
   - **Spec template (raw URL)** — `https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/spec-template.md`
   - **Your Stage 1 template** (`.xlsx`) — upload via the paperclip icon
   - **Your Stage 3 populated workbook** (`.xlsx`) — upload via the paperclip icon; this gives the LLM real numbers to populate the Data Inputs section
3. Prompt:

   ```
   Read the Stage 4 brief and spec template at the URLs above. Then, using the
   spec template's structure, draft a technical specification for [COMPANY]
   accounting ratios analysis.

   Requirements:
   - Populate every section (Part A items 1–7, Part B items 8–11)
   - Use named-range notation (BAL_*, INC_*, CASH_*, RATIO_*) throughout
   - Where data values appear in my uploaded Stage 3 workbook, include them
     numerically in the Data Inputs table
   - Keep the YAML frontmatter from the template intact

   Before drafting, list the three or four assumptions you'll need from me
   (e.g., reporting standard, fiscal year, intended audience for the analysis).
   ```

4. Iterate. Ask the LLM to expand sparse sections, tighten verbose ones, and verify formulas tie to your template's named ranges.
5. Copy the final output into `docs/specs/YYYY-MM-DD-{lastname}-{company-slug}-spec.md` in your repo.

> **Why give the LLM URLs instead of just uploading files?** Two reasons. (1) The raw URL points at the *current* version of the template — if the instructor updates the template mid-semester, your LLM session reads the latest version automatically. (2) URLs are easier to share with classmates and easier to reproduce later. Files in a chat session evaporate; URLs do not.

### Workflow B — Claude Code CLI (terminal)

Best if you already cloned your repo locally and want the LLM to read repo files directly.

1. Install [Claude Code](https://claude.ai/code) and `cd` into your portfolio repo.
2. Launch `claude`.
3. Prompt:
   ```
   Read these files:
   - https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/International-Corporate-Finance/projects/performance-ratios/stage4-technical-specification.md
   - https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/spec-template.md
   - models/templates/performance-ratios-template.xlsx (in this repo)
   - models/builds/<your Stage 3 file>.xlsx (in this repo)

   Draft a technical specification for {company} accounting ratios analysis,
   following the spec-template structure. Save it to
   docs/specs/<YYYY-MM-DD>-<lastname>-<company-slug>-spec.md.
   ```
4. Iterate inside Claude Code, asking it to refine specific sections.
5. Commit and push when done.

---

## Required spec components

### Part A — Model Specification

Defines the Excel ratio model: structure, data, formulas, and validation. Detailed enough that the executor could reconstruct your Stage 1 template and Stage 3 populated model from this document alone.

1. **Scope & Objective** — Company, fiscal period, reporting standard (GAAP/IFRS/VAS), reporting currency, analytical objective, intended audience.
2. **Model Architecture** — Tab layout, color coding, input/calculation/output separation, formatting requirements.
3. **Data Inputs** — Complete table of every financial data point required, with values stated numerically (sourced from your Stage 3 workbook).
4. **Named Range Conventions** — Full map of named ranges (`BAL_*`, `INC_*`, `CASH_*`, `RATIO_*`) to values.
5. **Derived Inputs** — Computed intermediate values (averages, start-of-year figures, after-tax operating income) with explicit formulas in named-range notation.
6. **Ratio Definitions & Formulas** — Every ratio organized by category (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont) with formula in named-range notation, expected unit, and brief interpretation guide.
7. **Validation Rules** — Internal consistency checks (Du Pont vs. direct, Balance Sheet balance, etc.).

### Part B — Analysis Specification

Defines what to do with the computed ratios.

8. **Analysis Requirements** — For each ratio category: what to interpret, benchmarks or comparison targets, cross-category connections to examine.
9. **Du Pont Decomposition** — Specific instructions for ROE breakdown analysis.
10. **Strategic Recommendation Requirements** — Number of recommendations (3–5), evidence standard, actionable specificity.
11. **Output Format** — Exact structure of the deliverable: sections, order, length targets, tone, audience.

---

## Quality test

A well-written spec is **self-contained**. If you hand Part A + Part B to an LLM with zero additional context (which is exactly what Stage 5 will do), it should be able to:

1. Reconstruct the ratio model — or verify the provided ratios against the formulas
2. Produce a substantially correct analysis with meaningful strategic recommendations

If it can't, the spec has gaps. Identifying those gaps is the learning.

---

## Human-in-the-loop (HIL) review requirement

A single-shot LLM dump with no visible iteration is below standard for this stage. You must submit **evidence of at least one HIL review pass** — a round of work in which you identified a gap in the LLM's draft and revised either the prompt or the spec to address it.

Acceptable evidence (pick one — all three count equally; presented easiest-first):

1. **Before/after note** *(easiest — recommended for most students).* A 150–250 word commentary inside your prompt log describing the most consequential gap you found in the LLM's first draft, why your spec caused it, and what you changed. **Best for:** every student. No new file needed; you write it into your existing prompt log.
2. **Round-2 prompt** *(natural if you iterate as you go).* A second prompt-log entry (or a clearly-labeled second block within the same entry) showing how you re-prompted the LLM after reviewing round-1 output. Must include the specific gap you identified in round 1. **Best for:** students who naturally re-prompt the LLM rather than hand-edit its output.
3. **Annotated diff** *(most thorough).* A short before/after comparison file at `analysis/validation/YYYY-MM-DD-{lastname}-{company-slug}-stage4-iteration.md` showing excerpts of one or more spec sections side-by-side, with a one-line note per change explaining what gap each revision addressed. **Best for:** students comfortable with side-by-side comparison tables, or whose spec saw substantial rework.

A useful HIL pass is **specific.** "I asked it to expand the section" does not earn this credit. "I noticed Part A.4 listed `BAL_assets_total` without the year suffix, so the Stage 5 LLM would not know which year to pull — I added the year-suffix convention to the Named Range Conventions section and re-ran" does.

**Natural place to catch weird Stage 3 ratios.** If a ratio looked odd when you populated Stage 3, the HIL iteration is the right place to surface it. A strange ratio is often a spec gap the Stage 5 LLM will inherit. Walking the LLM through the weird ratio in your HIL pass — and revising your spec so the issue is addressed — is high-value HIL work.

This requirement is part of the "Spec craft + prompt log quality" rubric criterion (see below). You do not get a separate score for it.

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — sharpening the spec, iterating against the LLM output for completeness, expanding the prompt log — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (Stage 4 = 20% of project)

| Criterion | % of Stage 4 | What distinguishes strong work |
|-----------|-------------:|--------------------------------|
| Model spec — Data & Structure (Part A, items 1–5) | 25% | Every input value present numerically; architecture fully defined |
| Model spec — Ratios & Validation (Part A, items 6–7) | 25% | All 25+ ratios specified with correct formulas in named-range notation |
| Analysis spec (Part B, items 8–11) | 25% | Clear interpretive guidance; meaningful benchmarks; actionable recommendation criteria |
| Spec craft + prompt log quality | 25% | Unambiguous spec language; **at least one visible HIL iteration** (before/after note, round-2 prompt, or annotated diff) in which the student identified a gap in the LLM's draft and revised either the prompt or the spec. A prompt log of a single one-shot dump does not earn this credit. |

---

## Tips

- **Spec the model, not just the analysis.** The most common failure mode is jumping to Part B before Part A is airtight. The LLM at Stage 5 needs both.
- **Cite numerically.** "Total assets" is not a spec. "`BAL_assets_total_2025` = 394,328 USD millions" is.
- **Iterate the prompt, not just the output.** If the LLM keeps producing weak Part A sections, your prompt is the problem — fix the prompt and re-run, rather than hand-editing the output.
- **Log meaningfully.** "Asked Claude to write the spec" is not a useful log entry. "Iterated three times on the Du Pont section because the first two drafts confused decomposition with attribution" is.

---

## If you're curious — Claude Skills and Claude-for-Financial-Services plugins

**Not graded. Optional. Finish the core spec first.**

Two above-and-beyond extensions for students with time and a Claude Pro account:

- **Author a Claude Skill** that reshapes your spec into the `SKILL.md` format Anthropic uses for production prompts.
- **Try one Claude-for-Financial-Services plugin** (e.g., `audit-xls`, `ib-check-deck`) against your Stage 3 workbook or this Stage 4 spec.

Full walkthrough prompts, the constructive-vs-generative-use policy, and a setup guide live in [`docs/guides/student-ai-enhancements.md`](../../../../docs/guides/student-ai-enhancements.md).
