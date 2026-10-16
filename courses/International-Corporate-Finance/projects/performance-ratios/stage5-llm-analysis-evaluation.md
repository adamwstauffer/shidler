---
template: stage-brief
project: performance-ratios
stage: 5
title: "LLM Ratio Analysis & Executive Evaluation"
capability: performance-ratios
deliverables:
  - path: "analysis/YYYY-MM-DD-{company-slug}-llm-raw-log.md"
    format: markdown
  - path: "analysis/YYYY-MM-DD-{company-slug}-verification-analysis.md"
    format: markdown
  - path: "analysis/YYYY-MM-DD-{company-slug}-analysis.md"
    format: markdown
  - path: "analysis/YYYY-MM-DD-{company-slug}-spec-retrospective-analysis.md"
    format: markdown
  - path: "prompt-log.md"
    format: markdown
prerequisites: [2, 3, 4]
---

# Stage 5: LLM Ratio Analysis & Executive Evaluation

**Step-by-step on Kumu:** [Stage 5 walkthrough](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage5.html)

**Collaborator penalty:** from Stage 2 on, a stage loses 5 raw points if `adamwstauffer` is not a Write collaborator on your repository at its deadline; fixing it before a stage's deadline lifts the penalty retroactively.

**Format:** Deliverable-only — no in-class presentation
**Deliverable:** Five artifacts committed to your portfolio repo (table below)

> **Where this fits in the project.**
> **Input:** Stage 4 spec (executed by an LLM with no other context) + Stage 3 financials (for manual verification) + the instructor's PR feedback on your Stage 2 memo (for feedback incorporation).
> **Output (this stage):** Five artifacts in your repo (raw LLM output, final analysis, manual verification table, spec retrospective, updated prompt log).
> **Used by:** Stage 7 (the manual verification table returns, in the same shape, to audit your DCF) and Stage 8 (the valuation memo builds on this analysis, and the repo polish pass covers every file you commit here).

> **GitHub only from here on.** The Lamaku fallback available at Stages 2–4 does **not** apply at Stage 5 or after: the artifacts are committed to your repo. If you used Lamaku for any earlier stage, push those artifacts to the repo now — Stages 6–8 read them there, and the Stage 8 repo polish assumes the full project history lives in the repo.

> **Unfamiliar terms?** "PR," "commit history," "named range," "spec," and other recurring terms are defined in the [Project glossary in the BUS-629 README](README.md#project-glossary).

---

## Overview

The ratio analysis closes here. Two things happen at this stage:

1. **Execute your Stage 4 spec with an LLM** to produce the full ratio analysis you deferred from Stage 3.
2. **Verify, evaluate, correct, and annotate** the AI-generated output — including a manual recomputation of at least five ratios — and write a structured spec retrospective on what you'd change.

The repo polish pass now closes the whole project, in Stage 8, after the valuation arc (Stages 6–8) has added its files.

## Why this stage matters

The future of finance work is not "do the analysis" or "make the AI do the analysis." It's **specify the work, evaluate the output, and take responsibility for the final product**. This stage tests judgment — and closes the spec-driven design feedback loop. Where the LLM output diverges from your Stage 3 numbers or your domain knowledge, either the spec had a gap or one of your earlier stages had an error. Either way, you learn.

---

## Deliverables (all in your repo)

All filenames are **lowercase**, hyphen-separated, dated `YYYY-MM-DD`, and named as the table gives them: `YYYY-MM-DD-{company-slug}-{type}`, no last name (the repository is already named for you), `{type}` ending in `memo`, `analysis` or `log`. Memos go in `docs/decisions/`, analyses and the raw run log in `analysis/`, the prompt log at the repository root. Nothing new goes in `deliverables/`. Files committed before 2026-10-02 under older names or paths (in `deliverables/`, under names with your last name, or `analysis/validation/…-stage5-verification.md`) still count as they are; nothing to move or rename. A misplaced or misnamed file never blocks you and is still graded; it may cost a point under professionalism, and moving it to the path the brief names fixes that.

| # | File | Location | Purpose |
|--:|------|----------|---------|
| 1 | Raw LLM output | `analysis/YYYY-MM-DD-{company-slug}-llm-raw-log.md` | Unedited LLM response from feeding the spec |
| 2 | **Manual ratio verification table** | `analysis/YYYY-MM-DD-{company-slug}-verification-analysis.md` | Recompute ≥5 ratios by hand from Stage 3 financials and compare to the LLM's values |
| 3 | Evaluated final analysis | `analysis/YYYY-MM-DD-{company-slug}-analysis.md` | Your edited, annotated, corrected version of the LLM output |
| 4 | **Spec retrospective** | `analysis/YYYY-MM-DD-{company-slug}-spec-retrospective-analysis.md` | Structured self-evaluation of your Stage 4 spec, using the repo template |
| 5 | Updated prompt log | `prompt-log.md` (repository root) | Logs the Stage 5 LLM session(s) |
| 6 | (Optional) Stage 2 feedback response | `docs/decisions/YYYY-MM-DD-{company-slug}-feedback-response-memo.md` | If the instructor's Stage 2 feedback resulted in scope or framing changes, document them here. Otherwise, show feedback incorporation in commits to the original Stage 2 memo. |

**Suggested production order:** 1 → 2 → 3 → 4 → 5 (plus #6 if you're shipping a standalone feedback-response memo). Producing the raw LLM output first and the verification table second forces you to confront discrepancies *before* you start writing the final analysis — which is the discipline this stage is teaching.

---

## How to execute

1. Open the LLM of your choice (Claude, ChatGPT, Gemini, or any capable model).
2. Paste your Stage 4 specification as the input — **nothing else**. No extra context, no "please also consider..." additions. The spec must stand alone. (This is the spec quality test from Stage 4 — now in production.)
3. Save the complete, unedited response as your raw LLM output.
4. Compare the LLM's analysis against your own Stage 3 model and your domain knowledge.
5. Recompute at least five ratios manually from your Stage 3 financials. Record them in the verification table (see below).
6. Write your evaluated final analysis with corrections, annotations, and your own executive voice.
7. Fill out the spec retrospective template (see below).

---

## Manual ratio verification table

Verifying the LLM's numbers against your own arithmetic is the cleanest way to catch hallucinated values, named-range mismatches, and silent unit errors. This artifact is graded.

**Three sources of ratio values exist in this project — be clear which two you're comparing.**

| Source | Where it comes from | What it represents |
|---|---|---|
| **Template's auto-computed** | Your Stage 3 workbook's Ratios tab | Excel formulas pre-built into the template, computed from your data tabs |
| **LLM's stated** | Your Stage 5 raw LLM output | Numbers the LLM produced by reading your Stage 4 spec |
| **Your manual** | The verification table you're building now | Recomputed by hand from the Stage 3 financial data |

The verification table compares **manual vs. LLM**. The template's auto-computed values are a useful sanity check on both, but they're not the column being graded.

Create `analysis/YYYY-MM-DD-{company-slug}-verification-analysis.md` with at least five rows. Pick ratios from across categories (don't recompute five liquidity ratios — show coverage). Strong work picks ratios the LLM is most likely to get wrong (anything involving averages, start-of-year values, or unit conversions).

| Ratio | Formula (named-range notation) | Manual value (show arithmetic) | LLM's value | Match? | One-line note |
|---|---|---|---|---|---|
| ROA (average assets) | `currentYear_after_tax_operating_income` / ((`BAL_assets_total_curr` + `BAL_assets_total_prior`) / 2) | 12,500 / ((100,000 + 96,000) / 2) = 12.76% | 12.76% | ✓ | LLM used the averaging convention of the template's ROA [avg] row |
| Current Ratio | `BAL_assets_current_curr` / `BAL_liabilities_current_curr` | 45,000 / 30,000 = 1.50 | 1.50 | ✓ | — |
| Average collection period | `BAL_receivables_prior` / (`INC_sales` / 365) | 8,000 / (80,000 / 365) = 36.5 days | 36.0 days | ✗ | LLM used a 360-day year without disclosing it |
| Inventory Turnover | `INC_cost_goods_sold` / `BAL_inventories_prior` | 60,000 / 13,000 = 4.62× | 4.00× | ✗ | LLM used year-end inventory (`BAL_inventories_curr`, 15,000), not the start-of-year balance the template uses |
| Long-term debt-to-equity | `BAL_debt_long_term_curr` / `BAL_equity_shareholders_curr` | 35,000 / 50,000 = 0.70 | 0.70 | ✓ | — |

The figures above are illustrative, not from any company. The names are the template's own: see the Ratios tab, and Formulas → Name Manager, for the full list. Balance-sheet names end in `_curr` (current year-end) or `_prior` (prior year-end); income-statement and cash-flow names carry no year suffix because they hold the current year only.

Discrepancies are not failures — they are the most informative rows in the table. A discrepancy with a one-line note explaining its cause earns full credit; a missing or unflagged discrepancy does not.

---

## Spec retrospective — use the template

The structured retrospective lives at [`../../templates/spec-retrospective-template.md`](../../../../templates/spec-retrospective-template.md). Copy it, rename per the convention `YYYY-MM-DD-{company-slug}-spec-retrospective-analysis.md`, and place it in `analysis/`.

The template requires:

1. **Section-by-section verdict** on your Stage 4 spec (Clear / Vague / Missing) with the symptom in your Stage 5 output that justifies each verdict.
2. **Top three gaps with evidence** — each gap tied to where it surfaced in the LLM output, what your spec caused, and the exact spec language you would add.
3. **Three revisions** you would make if you re-ran, each tied to a numbered gap.
4. **Effectiveness rating (1–5)** with anchored justification.
5. **Forward link** — one sentence on what changes in how you approach the next spec.
6. **Retrospective process feedback** (≤150 words) — a structural suggestion for the template itself, graded for thoughtfulness.

Vague rows ("Part A.4 was OK") do not earn the verdict. Specificity ("Part A.4 listed `BAL_assets_total` without its `_curr` / `_prior` suffix; the LLM pulled the prior year-end instead of the current one in the ROA computation") does.

---

## Required sections in the evaluated final analysis

1. **Company & Data Summary** — Verified company context, assumptions, accounting standard notes.
2. **Ratio Results & Interpretation** — All six categories (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont) with your corrections and additions to the LLM output where needed.
3. **Du Pont Analysis** — ROE decomposition with your commentary on whether the LLM's interpretation is sound.
4. **Strategic Recommendations** — 3–5 actionable recommendations, each with data support (cite specific ratio values) and your assessment: did the LLM get this right? What nuance did it miss?
5. **LLM Evaluation & Annotations** — What the LLM executed correctly. Where it deviated, hallucinated, or oversimplified. Errors caused by spec gaps vs. LLM limitations.
6. **Executive Justification** — Final investment or strategic thesis **in your own voice** — not the LLM's. The "so what?" that only a human with judgment can provide.

The spec retrospective lives in its own file (per the template) rather than as a section here — but the final analysis should link to it.

---

## Stage 2 feedback incorporation

**Weight:** 5% of the Stage 5 grade.

> **Step-by-step guide:** The full rubric-shaped walkthrough — how to read a PR, the three response patterns (accept / modify / reject), and a worked example — lives at [Kumu onboarding](https://adamwstauffer.github.io/ai-lms/onboarding.html). Read it the week before Stage 5 is due, not the night before.

The instructor reviewed your Stage 2 memo and returned PR-style suggestions on your repo. Stage 5 grades how you incorporated that feedback. Two acceptable forms (either counts):

- **Revised memo committed alongside your final analysis** — your `docs/decisions/YYYY-MM-DD-{company-slug}-selection-memo.md` shows commits that respond to the instructor's PR comments, OR you ship a follow-up memo at `docs/decisions/YYYY-MM-DD-{company-slug}-feedback-response-memo.md` describing what changed.
- **Commits demonstrably responding to feedback** — commit messages reference specific PR comments (e.g., "Tighten hypothesis 2 per instructor PR comment #3"), or the diffs show the requested changes were made.

If you received feedback and ignored it without comment, this rubric line scores zero. If you received feedback and disagreed with it, that is fine — but the disagreement must be visible (a comment on the PR, or a note in a follow-up memo explaining why you kept the original approach). Silence reads as oversight, not judgment.

This is not a hard gate; it is a rubric line. A strong project that genuinely had little feedback to incorporate (the instructor's PR comments were minor) can still earn most of this 5% by demonstrating awareness — a one-line note in the final analysis acknowledging the PR review and what stuck.

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — expanding the verification table, tightening the final-analysis edits, completing the spec retrospective — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (% of Stage 5 score)

| Criterion | % of Stage 5 | What distinguishes strong work |
|-----------|-------------:|--------------------------------|
| Analytical correctness (ratios, Du Pont, interpretation) | 30% | Numbers tie to source; interpretations are defensible; LLM errors caught and corrected |
| Manual verification artifact | 15% | ≥5 ratios recomputed by hand from Stage 3 financials; discrepancies with the LLM's values flagged and explained |
| LLM evaluation + spec retrospective (template-backed) | 25% | Specific, actionable critique of both the AI output and your own spec; retrospective uses the template structure with evidence-tied verdicts |
| Strategic recommendations + executive voice | 25% | Each rec backed by ratio evidence; recommendations are actionable; voice is yours, not the LLM's |
| Stage 2 feedback incorporation | 5% | Visible response to the instructor's PR comments — revised memo, follow-up memo, or commit history that references the feedback |

Repo polish is graded at Stage 8.

---

## Tips

- **The LLM output is a draft, not a deliverable.** Treat it like a junior analyst's first pass: review every claim, every number, every recommendation. Your annotations are where the grade is earned.
- **Verify before you interpret.** The manual verification table is your discipline check — don't skip it and don't dash it off. The most impressive rows are the ones where you caught the LLM in a unit error or an averaging shortcut.
- **Diverge with evidence.** If your Stage 3 numbers and the LLM's interpretation disagree, you have to pick a side and defend it. Don't paper over the disagreement.
- **Let the retrospective be honest.** "My spec was perfect" earns fewer points than "My Part B section 9 was vague — I told the LLM to 'recommend strategic actions' without specifying evidence standards, so it gave generic recommendations." Specificity is the rubric.
- **If you tried a Claude Skill or plugin** (see Stage 4 sidebar and [Kumu AI lab](https://adamwstauffer.github.io/ai-lms/ailab.html)), include a one-line note in your final analysis or prompt log on what you learned. Ungraded; portfolio-shaped.

---

## Beyond this assignment — how Claude for Financial Services would change this analysis in the real world

**Not part of the rubric. Not required. But if you take this same workflow into a corporate-finance, equity-research, or investment-banking job after graduation, the gap between what you just did and what's possible with industry-grade AI tooling is large — and worth understanding now.**

The analysis you just produced is the *educational* version of the workflow: you build a model from a single 10-K, draft a spec, feed it to a general-purpose LLM, and write the strategic recommendation yourself. That builds the disciplines (spec craft, verification, executive judgment) the course is grading.

In an institutional setting — corporate FP&A, sell-side research, buy-side analyst desk, M&A advisory — the same analysis is built on a different stack. Anthropic's **Claude for Financial Services** marketplace bundles plugins that automate or accelerate every layer of this work. Here is how the same Stage 5 analysis would look with that stack:

| Step you did in this assignment | Real-world workflow with Claude for Financial Services |
|---|---|
| **Manually source 10-K from EDGAR; populate the workbook by typing** | `financial-analysis:3-statement-model` reads SEC filings via the SEC connector and populates a 3-statement template automatically. |
| **Manually recompute five ratios by hand to verify the LLM** | `financial-analysis:audit-xls` audits the full workbook against the named-range convention, flags formula errors, and produces a verification report. |
| **Compare your company in isolation, with no peer set** | `financial-analysis:comps-analysis` pulls a peer set from FactSet / S&P Capital IQ (live-data connectors), computes operating metrics and trading multiples, and benchmarks your company's ratios against the peer median and quartiles — the standard institutional view. |
| **Write generic strategic recommendations** | `equity-research:initiate` or `equity-research:thesis` drafts an institutional-quality investment thesis with catalysts, risks, and a target-price range — anchored to the comps and a DCF rather than to a single-company read. |
| **Hand-type the LLM evaluation section** | `financial-analysis:debug-model` and `pitch-agent:ib-check-deck` run a structural audit of the analysis itself — checking number consistency across sections, narrative-data alignment, and IB-standard language. |
| **Present the analysis by hand** | `pitch-agent:pitch-deck` and `financial-analysis:competitive-analysis` produce a branded deck of the same analysis automatically; the repo becomes the working file, the deck becomes the client-facing deliverable. |

### What this means for you

- **Where you may meet this stack.** In a corporate-finance, equity-research, banking, FP&A, consulting or PE role, or when you decide whether to roll these tools out to your own team, the question is how you direct your analysts and your AI vendors, not only how you use the tools yourself. Knowing what is possible matters more than memorizing any one product.
- **The judgment skills this course teaches still matter — they matter *more*.** The plugins automate the *building*. The institutional value-add becomes the *judgment*: which peer set is the right one? Which ratio anomaly is a real signal vs. an accounting artifact? Which strategic recommendation does the buyer actually need? Those questions don't have a plugin.
- **The Claude for Financial Services plugins assume enterprise data subscriptions you don't have as a student.** FactSet, S&P Global, Moody's, PitchBook — those live-data connectors require paid access. The plugins that work on local data (`audit-xls`, `ib-check-deck`, `competitive-analysis` against public filings, `3-statement-model` from SEC filings) you can try as a student.

### If you want to try one before you leave the course

The lightest-weight experiment: install `financial-analysis:audit-xls` and run it against your Stage 3 workbook (the same workbook you've been working in all semester). Full walkthrough prompts are in [Kumu AI lab](https://adamwstauffer.github.io/ai-lms/ailab.html). Plan ~30 minutes including the Claude Code install.

That one experiment shows you the gap between what a general-purpose LLM does well and what purpose-built finance tooling does. It is also a head start: Stage 7 runs `audit-xls` on the DCF you build in Stage 6.

**Optional.** Adding a `docs/decisions/YYYY-MM-DD-{company-slug}-ai-tooling-memo.md` memo (100–300 words: what you tried, what it did well, what it got wrong, whether you'd use it on a real engagement) records what you learned from it.
