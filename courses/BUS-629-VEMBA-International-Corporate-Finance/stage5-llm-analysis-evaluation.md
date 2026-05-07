# Stage 5: LLM Analysis, Executive Evaluation, and Repo Polish

**Weight:** 25% of project score (70% deliverable / 30% presentation)
**Deliverable:** Polished GitHub repo URL submitted via Lamaku

---

## Overview

The capstone. Three things happen at this stage:

1. **Execute your Stage 4 spec with an LLM** to produce the full ratio analysis you deferred from Stage 3.
2. **Critically evaluate, correct, and annotate** the AI-generated output — and write a spec retrospective on what you'd change.
3. **Polish your repository** so it stands as a professional artifact you'd link from your LinkedIn.

Stage 5's deliverable is the repo URL itself — its final state *is* the work product.

## Why this is the capstone

The future of finance work is not "do the analysis" or "make the AI do the analysis." It's **specify the work, evaluate the output, and take responsibility for the final product**. This stage tests judgment — and closes the spec-driven design feedback loop. Where the LLM output diverges from your Stage 3 numbers or your domain knowledge, either the spec had a gap or one of your earlier stages had an error. Either way, you learn.

The repo polish component recognizes a separate truth: a portfolio artifact a recruiter can find is worth more than a perfect analysis stuck in a personal Dropbox.

---

## Deliverables (all in your repo)

| File | Location | Purpose |
|------|----------|---------|
| Raw LLM output | `deliverables/YYYY-MM-DD-{company-slug}-llm-raw.md` | Unedited LLM response from feeding the spec |
| Evaluated final analysis | `deliverables/YYYY-MM-DD-{company-slug}-final-analysis.md` | Your edited, annotated, corrected version |
| Spec retrospective | Section inside the final analysis OR `deliverables/YYYY-MM-DD-{company-slug}-spec-retrospective.md` | What you'd change about your Stage 4 spec |
| Updated prompt log | `deliverables/prompt-log.md` | Logs the Stage 5 LLM session(s) |

---

## How to execute

1. Open the LLM of your choice (Claude, ChatGPT, Gemini, or any capable model).
2. Paste your Stage 4 specification as the input — **nothing else**. No extra context, no "please also consider..." additions. The spec must stand alone. (This is the spec quality test from Stage 4 — now in production.)
3. Save the complete, unedited response as your raw LLM output.
4. Compare the LLM's analysis against your own Stage 3 model and your domain knowledge.
5. Write your evaluated final analysis with corrections, annotations, and your own executive voice.

---

## Required sections in the evaluated final analysis

1. **Company & Data Summary** — Verified company context, assumptions, accounting standard notes.
2. **Ratio Results & Interpretation** — All six categories (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont) with your corrections and additions to the LLM output where needed.
3. **Du Pont Analysis** — ROE decomposition with your commentary on whether the LLM's interpretation is sound.
4. **Strategic Recommendations** — 3–5 actionable recommendations, each with data support (cite specific ratio values) and your assessment: did the LLM get this right? What nuance did it miss?
5. **LLM Evaluation & Annotations** — What the LLM executed correctly. Where it deviated, hallucinated, or oversimplified. Errors caused by spec gaps vs. LLM limitations.
6. **Spec Retrospective (300–500 words)** — Where the deepest learning happens:
   - What would you change in your Stage 4 spec to produce better output?
   - Which spec sections were sufficient? Which were ambiguous?
   - If you re-ran with revisions, what would improve?
   - Rate your spec's effectiveness (1–5) with justification.
7. **Executive Justification** — Final investment or strategic thesis **in your own voice** — not the LLM's. The "so what?" that only a human with judgment can provide.

---

## Repo polish checklist

By Stage 5, your repo should look like a professional portfolio artifact. Before submitting:

- [ ] Top-level `README.md` updated with project status section listing all five stages and their commit hashes
- [ ] Every directory has a `README.md` explaining what's inside
- [ ] All filenames follow `YYYY-MM-DD-{slug}` convention
- [ ] No orphan files, dead links, or `_temp/` directories
- [ ] Commit history is clean (descriptive messages; no `wip` or `asdf` commits)
- [ ] Repo is **public** and accessible without login
- [ ] Repository description (top-right of GitHub repo page) summarizes the project in one line

---

## In-class presentation (30% of stage grade)

A 7–10 minute final presentation. This is your "investment thesis pitch" moment.

**Suggested structure:**
- Company + headline finding (the one thing you want the audience to remember) (1 minute)
- Top 2 ratio findings, with Du Pont context (3 minutes)
- Your top strategic recommendation, with evidence (2 minutes)
- Spec retrospective: what you'd change next time (2 minutes)
- Q&A (2–3 minutes)

---

## Rubric (Stage 5 = 25% of project)

### Deliverable — 70% of stage grade

| Criterion | % of deliverable | What distinguishes strong work |
|-----------|-----------------:|--------------------------------|
| Analytical correctness (ratios, Du Pont, interpretation) | 30% | Numbers tie to source; interpretations are defensible; LLM errors caught and corrected |
| LLM evaluation + spec retrospective | 25% | Specific, actionable critique of both the AI output and your own spec |
| Strategic recommendations + executive voice | 20% | Each rec backed by ratio evidence; recommendations are actionable; voice is yours, not the LLM's |
| Repo polish (structure, READMEs, naming, commits) | 25% | Repo presents as a professional artifact; no rough edges |

### Presentation — 30% of stage grade

| Criterion | % of presentation |
|-----------|------------------:|
| Headline + thesis clarity | 30% |
| Evidence quality (ratio citations, Du Pont) | 25% |
| Self-critique (spec retrospective) | 20% |
| Response to Q&A | 15% |
| Professionalism (timing, presence) | 10% |

---

## Tips

- **The LLM output is a draft, not a deliverable.** Treat it like a junior analyst's first pass: review every claim, every number, every recommendation. Your annotations are where the grade is earned.
- **Diverge with evidence.** If your Stage 3 numbers and the LLM's interpretation disagree, you have to pick a side and defend it. Don't paper over the disagreement.
- **Let the retrospective be honest.** "My spec was perfect" earns fewer points than "My Part B section 9 was vague — I told the LLM to 'recommend strategic actions' without specifying evidence standards, so it gave generic recommendations." Specificity is the rubric.
- **Polish the repo last.** Don't let it become an evening-before scramble. Allocate a dedicated commit pass for READMEs, naming, and repo description before the presentation.
