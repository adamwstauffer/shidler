# Stage 5: LLM Analysis, Executive Evaluation, and Repo Polish

**Weight:** 25% of project score
**Format:** Deliverable-only — no in-class presentation
**Deliverable:** Polished GitHub repo URL submitted via Lamaku

> **Where this fits in the project.**
> **Input:** Stage 4 spec (executed by an LLM with no other context) + Stage 3 financials (for manual verification) + the instructor's PR feedback on your Stage 2 memo (for feedback incorporation).
> **Output (this stage):** Six artifacts in your repo (raw LLM output, final analysis, manual verification table, spec retrospective, updated prompt log, and the polished repo itself), plus the public repo URL submitted on Lamaku.
> **Used by:** You. The repo is your portfolio piece — share the URL on LinkedIn.

> **About the GitHub-vs-Lamaku question.** Stage 5's deliverable **is** the GitHub repo URL — the repo itself is the artifact. Lamaku is only used to submit the URL pointer (and your presentation slides, if any). The Lamaku fallback available at earlier stages (memo, workbook, spec uploaded directly) does **not** apply at Stage 5: by this point, all prior-stage artifacts must be consolidated into your public GitHub repo. The polish rubric assumes the full project history lives in the repo. If you used Lamaku for any earlier stage, push those artifacts to the repo before the Stage 5 deadline.

> **Unfamiliar terms?** "PR," "commit history," "named range," "spec," and other recurring terms are defined in the [Project glossary in the BUS-629 README](README.md#project-glossary).

---

## Overview

The capstone. Three things happen at this stage:

1. **Execute your Stage 4 spec with an LLM** to produce the full ratio analysis you deferred from Stage 3.
2. **Verify, evaluate, correct, and annotate** the AI-generated output — including a manual recomputation of at least five ratios — and write a structured spec retrospective on what you'd change.
3. **Polish your repository** so it stands as a professional artifact you'd link from your LinkedIn.

Stage 5's deliverable is the repo URL itself — its final state *is* the work product.

## Why this is the capstone

The future of finance work is not "do the analysis" or "make the AI do the analysis." It's **specify the work, evaluate the output, and take responsibility for the final product**. This stage tests judgment — and closes the spec-driven design feedback loop. Where the LLM output diverges from your Stage 3 numbers or your domain knowledge, either the spec had a gap or one of your earlier stages had an error. Either way, you learn.

The repo polish component recognizes a separate truth: a portfolio artifact a manager, audit reviewer, or future collaborator can find is worth more than a perfect analysis stuck in a personal Dropbox.

---

## Deliverables (all in your repo)

All filenames are **lowercase**, hyphen-separated, dated `YYYY-MM-DD`, and include your `{lastname}-{company-slug}` (matching the convention used at every other stage).

| # | File | Location | Purpose |
|--:|------|----------|---------|
| 1 | Raw LLM output | `deliverables/YYYY-MM-DD-{lastname}-{company-slug}-llm-raw.md` | Unedited LLM response from feeding the spec |
| 2 | **Manual ratio verification table** | `analysis/validation/YYYY-MM-DD-{lastname}-{company-slug}-stage5-verification.md` | Recompute ≥5 ratios by hand from Stage 3 financials and compare to the LLM's values |
| 3 | Evaluated final analysis | `deliverables/YYYY-MM-DD-{lastname}-{company-slug}-final-analysis.md` | Your edited, annotated, corrected version of the LLM output |
| 4 | **Spec retrospective** | `deliverables/YYYY-MM-DD-{lastname}-{company-slug}-spec-retrospective.md` | Structured self-evaluation of your Stage 4 spec, using the repo template |
| 5 | Updated prompt log | `deliverables/prompt-log.md` | Logs the Stage 5 LLM session(s) |
| 6 | (Optional) Stage 2 feedback response | `docs/decisions/YYYY-MM-DD-{lastname}-stage2-feedback-response.md` | If the instructor's Stage 2 feedback resulted in scope or framing changes, document them here. Otherwise, show feedback incorporation in commits to the original Stage 2 memo. |

**Suggested production order:** 1 → 2 → 3 → 4 → 5, then the repo polish pass (plus #6 if you're shipping a standalone feedback-response memo). Producing the raw LLM output first and the verification table second forces you to confront discrepancies *before* you start writing the final analysis — which is the discipline this stage is teaching.

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

Create `analysis/validation/YYYY-MM-DD-{lastname}-{company-slug}-stage5-verification.md` with at least five rows. Pick ratios from across categories (don't recompute five liquidity ratios — show coverage). Strong work picks ratios the LLM is most likely to get wrong (anything involving averages, start-of-year values, or unit conversions).

| Ratio | Formula (named-range notation) | Manual value (show arithmetic) | LLM's value | Match? | One-line note |
|---|---|---|---|---|---|
| ROA | `INC_net_income_2025` / ((`BAL_assets_total_2025` + `BAL_assets_total_2024`) / 2) | 12,500 / ((100,000 + 96,000) / 2) = 12.76% | 12.76% | ✓ | LLM used correct averaging convention |
| Current Ratio | `BAL_current_assets_2025` / `BAL_current_liabilities_2025` | 45,000 / 30,000 = 1.50 | 1.50 | ✓ | — |
| Days Sales Outstanding | (`BAL_receivables_2025` / `INC_revenue_2025`) × 365 | (8,000 / 80,000) × 365 = 36.5 days | 36.0 days | ✗ | LLM used 360-day convention without disclosing |
| Inventory Turnover | `INC_cogs_2025` / ((`BAL_inventory_2025` + `BAL_inventory_2024`) / 2) | 60,000 / ((15,000 + 13,000) / 2) = 4.29× | 4.62× | ✗ | LLM used end-of-year inventory only, not the two-year average |
| Debt-to-Equity | `BAL_debt_total_2025` / `BAL_equity_total_2025` | 35,000 / 50,000 = 0.70 | 0.70 | ✓ | — |

Discrepancies are not failures — they are the most informative rows in the table. A discrepancy with a one-line note explaining its cause earns full credit; a missing or unflagged discrepancy does not.

---

## Spec retrospective — use the template

The structured retrospective lives at [`../../docs/templates/spec-retrospective-template.md`](../../../../docs/templates/spec-retrospective-template.md). Copy it, rename per the convention `YYYY-MM-DD-{lastname}-{company-slug}-spec-retrospective.md`, and place it in `deliverables/`.

The template requires:

1. **Section-by-section verdict** on your Stage 4 spec (Clear / Vague / Missing) with the symptom in your Stage 5 output that justifies each verdict.
2. **Top three gaps with evidence** — each gap tied to where it surfaced in the LLM output, what your spec caused, and the exact spec language you would add.
3. **Three revisions** you would make if you re-ran, each tied to a numbered gap.
4. **Effectiveness rating (1–5)** with anchored justification.
5. **Forward link** — one sentence on what changes in how you approach the next spec.
6. **Retrospective process feedback** (≤150 words) — a structural suggestion for the template itself, graded for thoughtfulness.

Vague rows ("Part A.4 was OK") do not earn the verdict. Specificity ("Part A.4 listed `BAL_assets_total` without year suffix; LLM pulled FY2024 instead of FY2025 in the ROA computation") does.

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

**Weight:** 5% of the deliverable rubric.

> **Step-by-step guide:** The full rubric-shaped walkthrough — how to read a PR, the three response patterns (accept / modify / reject), and a worked example — lives at [`docs/guides/responding-to-pr-feedback.md`](../../../../docs/guides/responding-to-pr-feedback.md). Read it the week before Stage 5 is due, not the night before.

The instructor reviewed your Stage 2 memo and returned PR-style suggestions on your repo. Stage 5 grades how you incorporated that feedback. Two acceptable forms (either counts):

- **Revised memo committed alongside your final analysis** — your `docs/decisions/YYYY-MM-DD-{lastname}-{company-slug}-selection.md` shows commits that respond to the instructor's PR comments, OR you ship a follow-up memo at `docs/decisions/YYYY-MM-DD-{lastname}-stage2-feedback-response.md` describing what changed.
- **Commits demonstrably responding to feedback** — commit messages reference specific PR comments (e.g., "Tighten hypothesis 2 per instructor PR comment #3"), or the diffs show the requested changes were made.

If you received feedback and ignored it without comment, this rubric line scores zero. If you received feedback and disagreed with it, that is fine — but the disagreement must be visible (a comment on the PR, or a note in a follow-up memo explaining why you kept the original approach). Silence reads as oversight, not judgment.

This is not a hard gate; it is a rubric line. A strong project that genuinely had little feedback to incorporate (the instructor's PR comments were minor) can still earn most of this 5% by demonstrating awareness — a one-line note in the final analysis acknowledging the PR review and what stuck.

---

## Repo polish checklist

By Stage 5, your repo should look like a professional portfolio artifact. **Budget 2–3 hours** for this pass — most of the time is per-directory READMEs and the commit-history cleanup, not the README itself. Don't leave this for the night before.

### Target directory hierarchy

Use this as your reference. A polished Stage 5 repo should look like this (filenames will reflect your own name and company):

```
firstname-lastname/                         (your portfolio repo root)
├── README.md                               # Project overview, status, "what you'll find here"
├── RESUME.md                               # Your resume (from Stage 0)
├── BIO.md                                  # Optional longer bio (from Stage 0)
├── LICENSE                                 # MIT or Apache-2.0
├── .gitignore                              # Excludes .DS_Store, ~$*.xlsx, *.tmp, etc.
│
├── docs/
│   ├── README.md                           # Explains what's in docs/
│   ├── decisions/
│   │   ├── README.md
│   │   ├── 2026-05-21-{lastname}-{company}-selection.md       # Stage 2 memo
│   │   └── 2026-07-03-{lastname}-stage2-feedback-response.md  # (optional) Stage 5 follow-up
│   └── specs/
│       ├── README.md
│       └── 2026-06-18-{lastname}-{company}-spec.md            # Stage 4 spec
│
├── models/
│   ├── README.md
│   ├── templates/
│   │   └── performance-ratios-template.xlsx                   # Stage 1 (unmodified)
│   └── builds/
│       └── 2026-06-04-{lastname}-{company}-financials.xlsx    # Stage 3
│
├── analysis/
│   ├── README.md
│   └── validation/
│       ├── README.md
│       ├── 2026-06-19-{lastname}-{company}-stage4-iteration.md   # (optional) Stage 4 HIL note
│       └── 2026-07-03-{lastname}-{company}-stage5-verification.md  # Stage 5 verification table
│
└── deliverables/
    ├── README.md
    ├── prompt-log.md                                          # All AI sessions logged
    ├── 2026-07-02-{lastname}-{company}-llm-raw.md             # Stage 5 raw LLM output
    ├── 2026-07-03-{lastname}-{company}-final-analysis.md      # Stage 5 final analysis
    └── 2026-07-03-{lastname}-{company}-spec-retrospective.md  # Stage 5 retrospective
```

### Checklist

Before submitting:

- [ ] Top-level `README.md` updated with project status section listing all five stages and their commit hashes
- [ ] Top-of-README "what you'll find here" block — one paragraph orienting a manager, reviewer, or peer who just clicked the repo link
- [ ] **One-line repo description** set in the GitHub repo page header (the field at the top of the repo page, not in the README) — summarizes the project in one sentence
- [ ] **`LICENSE` file** at repo root (MIT or Apache-2.0 recommended — pick one, both signal "this is a portfolio piece you may reference")
- [ ] **`.gitignore`** excluding common scratch files (`.DS_Store`, `~$*.xlsx`, `*.tmp`, etc.) — keeps the repo clean
- [ ] Every directory has a `README.md` explaining what's inside
- [ ] All filenames follow `YYYY-MM-DD-{lastname}-{company}-{kind}.{ext}` convention
- [ ] No orphan files, dead links, or `_temp/` directories
- [ ] Commit history is clean (descriptive messages; no `wip` or `asdf` commits)
- [ ] Repo is **public** and accessible without login

### Pro tip — use an LLM to reorganize and clean up your repo

The polish pass is exactly the kind of routine reorganization an LLM is good at. Two approaches depending on which AI tool you're using:

**Option 1 — Claude Code (in your terminal):**

```
cd ~/path/to/your/firstname-lastname
claude
```

Then prompt:

```
Read every file in this repo. Compare the current structure against the Stage 5
target hierarchy in:
https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/International-Corporate-Finance/projects/performance-ratios/stage5-llm-analysis-evaluation.md

Identify:
1. Misnamed files (not following YYYY-MM-DD-{lastname}-{company}-{kind} convention)
2. Files in the wrong directory
3. Missing per-directory READMEs (every folder should have one)
4. Orphan or temp files that should be deleted

For each issue, propose the exact git mv command or git rm command to fix it.
Do NOT run any commands yourself. Print the list of commands so I can review
each one before executing.

After that list, draft per-directory README.md files for any directory missing one.
Use 4–6 sentences each: what's in the directory, naming conventions used, how it
relates to the project stages.
```

**Option 2 — Claude.ai or ChatGPT (web, no install):**

Compress your repo to a `.zip`, upload it to the LLM, and paste:

```
I have uploaded my portfolio repo as a zip. The Stage 5 target structure is
documented at:
https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/International-Corporate-Finance/projects/performance-ratios/stage5-llm-analysis-evaluation.md

Audit my repo against that target. Produce:
1. A table of every file currently in the repo, with columns: current path |
   correct path | action needed (rename / move / delete / keep)
2. Draft per-directory README.md text for every directory that needs one
3. A list of any missing artifacts (e.g., LICENSE, .gitignore) with suggested
   minimal content I can copy in

Be specific. Do not say "rename inconsistent files" — list the exact files.
```

**What the LLM should NOT do at Stage 5:** Generate the actual analysis content for you, or rewrite your final analysis to "improve" it. The polish pass is about file organization and presentation, not about the analytical substance — that substance is what the rubric is grading.

**Log the prompt** in `deliverables/prompt-log.md`. The repo-cleanup conversation is just as logged-worthy as the analytical ones.

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — expanding the verification table, tightening the final-analysis edits, completing the spec retrospective, finishing the repo polish — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (Stage 5 = 25% of project)

| Criterion | % of Stage 5 | What distinguishes strong work |
|-----------|-------------:|--------------------------------|
| Analytical correctness (ratios, Du Pont, interpretation) | 25% | Numbers tie to source; interpretations are defensible; LLM errors caught and corrected |
| Manual verification artifact | 10% | ≥5 ratios recomputed by hand from Stage 3 financials; discrepancies with the LLM's values flagged and explained |
| LLM evaluation + spec retrospective (template-backed) | 25% | Specific, actionable critique of both the AI output and your own spec; retrospective uses the template structure with evidence-tied verdicts |
| Strategic recommendations + executive voice | 20% | Each rec backed by ratio evidence; recommendations are actionable; voice is yours, not the LLM's |
| Stage 2 feedback incorporation | 5% | Visible response to the instructor's PR comments — revised memo, follow-up memo, or commit history that references the feedback |
| Repo polish (structure, READMEs, naming, commits, license, description) | 15% | Repo presents as a professional artifact; no rough edges; expanded polish checklist satisfied |

---

## Tips

- **The LLM output is a draft, not a deliverable.** Treat it like a junior analyst's first pass: review every claim, every number, every recommendation. Your annotations are where the grade is earned.
- **Verify before you interpret.** The manual verification table is your discipline check — don't skip it and don't dash it off. The most impressive rows are the ones where you caught the LLM in a unit error or an averaging shortcut.
- **Diverge with evidence.** If your Stage 3 numbers and the LLM's interpretation disagree, you have to pick a side and defend it. Don't paper over the disagreement.
- **Let the retrospective be honest.** "My spec was perfect" earns fewer points than "My Part B section 9 was vague — I told the LLM to 'recommend strategic actions' without specifying evidence standards, so it gave generic recommendations." Specificity is the rubric.
- **Polish the repo last — but not last-night.** Don't let it become an evening-before scramble. Allocate a dedicated commit pass for READMEs, naming, license, and repo description.
- **If you tried a Claude Skill or plugin** (see Stage 4 sidebar and [`docs/guides/student-ai-enhancements.md`](../../../../docs/guides/student-ai-enhancements.md)), include a one-line note in your final analysis or prompt log on what you learned. Ungraded; portfolio-shaped.

---

## Beyond this assignment — how Claude for Financial Services would change this analysis in the real world

**Not part of the rubric. Not required. But if you take this same workflow into a corporate-finance, equity-research, or investment-banking job after graduation, the gap between what you just did and what's possible with industry-grade AI tooling is large — and worth understanding now.**

The analysis you just produced is the *educational* version of the workflow: you build a model from a single 10-K, draft a spec, feed it to a general-purpose LLM, and write the strategic recommendation yourself. That builds the disciplines (spec craft, verification, executive judgment) the course is grading.

In an institutional setting — corporate FP&A, sell-side research, buy-side analyst desk, M&A advisory — the same analysis is built on a different stack. Anthropic's **Claude for Financial Services** marketplace bundles plugins that automate or accelerate every layer of this work. Here is how the same Stage 5 analysis would look with that stack:

| Step you did in this assignment | Real-world workflow with Claude for Financial Services |
|---|---|
| **Manually source 10-K from EDGAR; populate the workbook by typing** | `financial-analysis:3-statement-model` reads SEC filings via the SEC connector and populates a 3-statement template automatically. Time: ~5 minutes per company. |
| **Manually recompute five ratios by hand to verify the LLM** | `financial-analysis:audit-xls` audits the full workbook against the named-range convention, flags formula errors, and produces a verification report. Catches dozens of issues, not five. |
| **Compare your company in isolation, with no peer set** | `financial-analysis:comps-analysis` pulls a peer set from FactSet / S&P Capital IQ (live-data connectors), computes operating metrics and trading multiples, and benchmarks your company's ratios against the peer median and quartiles — the standard institutional view. |
| **Write generic strategic recommendations** | `equity-research:initiate` or `equity-research:thesis` drafts an institutional-quality investment thesis with catalysts, risks, and a target-price range — anchored to the comps and a DCF rather than to a single-company read. |
| **Hand-type the LLM evaluation section** | `financial-analysis:debug-model` and `pitch-agent:ib-check-deck` run a structural audit of the analysis itself — checking number consistency across sections, narrative-data alignment, and IB-standard language. |
| **Repo polish by hand** | `pitch-agent:pitch-deck` and `financial-analysis:competitive-analysis` produce a branded deck of the same analysis automatically; the repo becomes the working file, the deck becomes the client-facing deliverable. |

### What this means for you

- **You will use this stack in your career.** Whether you move into a corporate-finance, equity-research, investment-banking, FP&A, consulting, or PE role — or whether you **roll these tools out to your own team or employees** as a manager or executive — AI-assisted financial analysis is becoming standard. For EMBA students already in senior positions, the leverage from understanding what's possible is in *how you direct your analysts and your AI vendor relationships*, not just in how you personally use the tools. Knowing what's possible matters more than memorizing any individual product.
- **The judgment skills this course teaches still matter — they matter *more*.** The plugins automate the *building*. The institutional value-add becomes the *judgment*: which peer set is the right one? Which ratio anomaly is a real signal vs. an accounting artifact? Which strategic recommendation does the buyer actually need? Those questions don't have a plugin.
- **The Claude for Financial Services plugins assume enterprise data subscriptions you don't have as a student.** FactSet, S&P Global, Moody's, PitchBook — those live-data connectors require paid access. The plugins that work on local data (`audit-xls`, `ib-check-deck`, `competitive-analysis` against public filings, `3-statement-model` from SEC filings) you can try as a student.

### If you want to try one before you leave the course

The lightest-weight experiment: install `financial-analysis:audit-xls` and run it against your Stage 3 workbook (the same workbook you've been working in all semester). Full walkthrough prompts are in [`docs/guides/student-ai-enhancements.md`](../../../../docs/guides/student-ai-enhancements.md). Plan ~30 minutes including the Claude Code install.

That single experiment is worth more than reading another article on "AI in finance." You will see the gap between what general-purpose LLMs do well and what purpose-built finance tooling does — and you'll be ahead of every peer who only used ChatGPT.

**This is portfolio-shaping work, not coursework.** Adding a `docs/decisions/YYYY-MM-DD-{lastname}-ai-tooling-experiment.md` memo (100–300 words: what you tried, what it did well, what it got wrong, whether you'd use it on a real engagement) is a stronger LinkedIn-pitchable artifact than another polish pass on the rubric checklist.
