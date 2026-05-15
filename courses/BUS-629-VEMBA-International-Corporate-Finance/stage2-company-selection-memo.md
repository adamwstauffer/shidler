# Stage 2: Company Selection Memo

**Weight:** 10% of project score
**Format:** Deliverable-only — no in-class presentation
**Deliverable:** Markdown memo (`.md`) committed to your portfolio repo

> ## ⚠ Do this first — required for grading
>
> **Add `adamwstauffer` as a Write collaborator on your portfolio repo before you submit.** This is the single most important Stage 2 setup step. Without it I cannot leave tracked feedback on your work, and a **−5 point penalty applies to your Stage 2 raw score** (and every subsequent stage until it is fixed).
>
> Steps: Repo → **Settings** → **Collaborators** → **Add people** → search `adamwstauffer` → choose **Write** → **Add to this repository**. 60 seconds. Full walkthrough is in [§ Grant instructor write access to your repo](#grant-instructor-write-access-to-your-repo-required) below.

> **Where this fits in the project.**
> **Input:** Stage 1 ratios template (you already have a copy in your repo).
> **Output (this stage):** A memo at `docs/decisions/YYYY-MM-DD-{lastname}-{company-slug}-selection.md` selecting the company you'll analyze for the rest of the semester.
> **Used by:** Stage 3 (you populate the template with this company's financials) and Stage 5 (graded on how you incorporated the instructor's tracked feedback on this memo).

> **Submission alternative — Lamaku upload.** GitHub is the required submission path. If you hit a hard wall with Git setup or pushing your work, you may upload this memo directly to Lamaku as a fallback. Use the same filename convention (`YYYY-MM-DD-{lastname}-{company-slug}-selection.md`). Using the Lamaku fallback does **not** reduce your Stage 2 grade. By Stage 5, the memo must also live in your repo at `docs/decisions/` — your Stage 5 polish rubric assumes the full project history is in the repo. **The Lamaku fallback does not waive the collaborator requirement above — add `adamwstauffer` either way.**

> **Unfamiliar terms?** "PR" (pull request — the mechanism GitHub uses to deliver tracked feedback documents), "YAML frontmatter," "10-K," and other recurring terms are defined in the [Project glossary in the BUS-629 README](README.md#project-glossary).

---

## Overview

Write an executive memo selecting and justifying the company you will analyze for the remainder of this project. This memo frames your project scope, identifies data sources, and previews your analytical approach. It is reviewed by the instructor for approval and to surface revisions you will carry into later stages.

With the Stage 1 template in hand, you know exactly what data points the model needs — your memo should be precise about which financials matter and why.

---

## Deliverable

A 400–600 word Markdown memo (`.md`) saved to `docs/decisions/` in your repository.

**Filename:** `YYYY-MM-DD-{lastname}-{company-slug}-selection.md` — all **lowercase**, hyphen-separated.
Example: `2026-05-21-nguyen-vinamilk-selection.md`

**Template:** the repo memo template, available three ways:

- In this repo: [`docs/templates/memo-template.md`](../../docs/templates/memo-template.md)
- Public GitHub link (for sharing with AI tools): [`https://github.com/adamwstauffer/shidler/blob/main/docs/templates/memo-template.md`](https://github.com/adamwstauffer/shidler/blob/main/docs/templates/memo-template.md)
- Raw URL (for direct LLM upload): [`https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/memo-template.md`](https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/memo-template.md)

Copy, rename per the convention above, fill in the sections, keep the YAML frontmatter intact.

**Audience and tone.** Adam Stauffer reads your memo; write to him in the tone of a **senior analyst** writing to a managing director — concise, decision-oriented, evidence-tight. Expect feedback. Plan to revise either this memo directly or to carry the revisions forward into later stages — see Stage 5's "Stage 2 feedback incorporation" rubric line.

---

## Grant instructor write access to your repo (required)

**This is a required Stage 2 setup step. A −5 point penalty applies to your raw score if it isn't done by the submission deadline, and the penalty carries forward into every subsequent stage until it is fixed.**

The instructor delivers feedback as a tracked review document opened directly on your repo — the same idea as a manager handing back a marked-up draft memo, an auditor's review note on a working paper, or an analyst peer-review on a deal memo. You read the suggestions inline, accept or push back on each one, and the back-and-forth becomes the historical record graded by the Stage 5 *feedback-incorporation* rubric line. The mechanism GitHub uses for this is called a **Pull Request (PR)** — concrete, traceable, and either accepted or revised — but the workflow itself is the same one used in finance, accounting, audit, and consulting practices to mark up draft work.

**Steps (GitHub web UI, 60 seconds):**

1. Open your portfolio repo on GitHub.
2. Click **Settings** (top-right of repo nav).
3. In the left sidebar, click **Collaborators**.
4. Click **Add people**.
5. Search for **`adamwstauffer`** (the instructor's GitHub handle) and select that account.
6. Choose the **Write** role.
7. Click **Add to this repository**.

You can verify by reloading the Collaborators page — `adamwstauffer` should appear with the Write role.

**Choose Write.** Write is the right answer for this project — it lets me open feedback documents directly on your repo without waiting for merge approvals. If you have a specific reason for being more cautious (corporate policy concern about granting Write on a personal repo), Triage is an acceptable fallback that still lets me review and comment, just not propose direct edits. If you are unsure, pick Write.

**Why this is graded.** Stage 2 is the first stage with tracked feedback, and Stage 5 explicitly grades how you incorporated that feedback. If I cannot leave feedback on your work, Stage 5's incorporation rubric line is hard to satisfy and the project loses one of its core learning loops (revising work in response to a supervisor's review — a routine professional skill in every finance/accounting/audit/consulting setting).

> **Never done this before?** A step-by-step walkthrough of GitHub account setup, your first commit (GitHub Desktop recommended), and the Collaborators panel lives in [`docs/guides/github-mba-guide.md`](../../docs/guides/github-mba-guide.md). Read Sections 4–7 if any of this is new to you.

---

## Company eligibility

- Publicly traded on a major exchange (NYSE, NASDAQ, HOSE, HNX, SGX, SET, IDX, PSE, Bursa Malaysia, or other recognized exchange)
- Annual report or 10-K equivalent available with sufficient detail for ratio computation
- Non-financial company (banks, insurance, and REITs have materially different ratio structures)
- Minimum 2 years of comparable data (current year + prior year)

### Non-U.S. companies are encouraged

Especially firms listed on Vietnamese or ASEAN exchanges. If financial statements are in a language other than English, the ratio analysis and all deliverables must still be written in English. Note any IFRS vs. U.S. GAAP differences that affect ratio interpretation.

---

## Required sections

1. **Company Overview** — Name, ticker, exchange, industry, brief business description, market cap, reporting currency.
2. **Selection Rationale** — Why this company? Relevance to your industry, employer, career goals, or analytical interest. What makes it a compelling ratio analysis subject? (e.g., recent M&A, industry disruption, capital structure shift, cross-border operations).
3. **Data Availability & Sources** — Confirm access to 10-K / annual report / audited financials. Identify specific data sources (SEC EDGAR, company IR page, HOSE disclosure portal, Yahoo Finance, etc.). Note fiscal year end and reporting standards (U.S. GAAP, IFRS, VAS).
4. **Preliminary Observations** — 2–3 initial hypotheses about what the ratio analysis might reveal. Each hypothesis must state a **direction** and a **reason** in the form **"I expect X because Y"** (e.g., "I expect rising leverage ratios from FY2023 → FY2024 because Vinamilk financed its Indochina expansion with USD debt issued in early 2024"). Open-ended framings ("we'll see what the ratios show") do not earn full credit.
5. **Ratio Categories Preview** — Brief note on which ratio categories are most relevant for this company's industry and why.
6. **Data Collection Plan** — Which financial statements are needed, what market/analyst assumptions must be sourced, any currency or accounting standard considerations.

---

## Pro tip — use an LLM to help draft the memo

You are not expected to start from a blank page. The memo template is structured precisely so an LLM can fill it in if you give it the right context. **Use the LLM as a drafter; you are the editor.**

### Option 1 — Give the LLM the template's public URL (recommended)

The memo template lives in a public GitHub repo. Most LLMs can read public URLs directly.

In Claude.ai, ChatGPT, or another capable model, paste:

```
I'm drafting a Stage 2 company selection memo for my finance course. The memo
template is at:

https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/memo-template.md

Please read the template, then draft a memo for the company [YOUR COMPANY,
e.g., Vinamilk (VNM, HOSE)] that fills in every section. Use the YAML
frontmatter exactly as shown. Length: 400–600 words. Audience: a managing
director — concise, evidence-tight.

Before you draft, ask me three to five clarifying questions about the company
(industry, why I chose it, what hypotheses I have, what data sources I'll use).
```

### Option 2 — Upload the template as a file

Download the template from [`https://github.com/adamwstauffer/shidler/blob/main/docs/templates/memo-template.md`](https://github.com/adamwstauffer/shidler/blob/main/docs/templates/memo-template.md) (click the **Raw** button, then save the page as `memo-template.md`).

Open Claude.ai (or ChatGPT). Upload the file via the paperclip icon. Then prompt the same way as Option 1, but say "I have uploaded the memo template" instead of giving a URL.

### What the LLM should produce vs. what you must do

| LLM does well | You must do |
|---|---|
| Filling out all six required sections with on-template structure | Choose the company — that's your judgment, not the LLM's |
| Suggesting falsifiable hypotheses in "I expect X because Y" form | Verify that the company actually meets eligibility (publicly traded, non-financial, 2+ years of data) |
| Identifying likely data sources (SEC EDGAR, HOSE portal, IR pages) | Confirm those sources actually have the data you need before submitting |
| Drafting in concise senior-analyst voice | Edit for accuracy — the LLM does not know your company as well as you should |

**Log the prompt.** Anything more than a 2-line nudge belongs in your `deliverables/prompt-log.md`. Stage 4 will grade your prompt log; start the habit at Stage 2.

---

## Connecting GitHub to an AI tool (optional, but powerful)

Most AI tools can now read directly from your GitHub repo. This lets you ask the LLM to read your Stage 1 template, draft against it, or QC your memo without copy-pasting files. Brief setup notes per tool:

| Tool | How to connect to your repo |
|---|---|
| **Claude (web / desktop)** | Use the "**Projects**" feature (Pro tier) — create a project, paste your public repo's raw URLs into the project knowledge, and every conversation in that project sees them. For a one-off chat: paste a raw URL into the prompt. |
| **Claude Code (CLI)** | Run `claude` inside your repo folder — it reads every file in the directory automatically. See [`docs/guides/claude-code-install-for-non-technical-users.md`](../../docs/guides/claude-code-install-for-non-technical-users.md). |
| **ChatGPT (web)** | Use the "**Connectors**" or the GitHub plugin (Plus tier) to authorize a specific repo. Then ChatGPT can browse your files. For a one-off: paste a raw URL. |
| **GitHub Copilot Chat** | Built into VS Code, GitHub.dev, and the GitHub web UI. Asks about your repo without setup once you're signed in. Free for students with the GitHub Student Developer Pack. |
| **Codex (OpenAI)** | Connect through ChatGPT Pro ($200/mo); not required for this course. |

For Stage 2, the simplest path is to **paste the raw template URL into Claude.ai or ChatGPT** (see Pro Tip above). You can ignore the table until you're ready for richer workflows.

---

## Submission checklist

- [ ] **`adamwstauffer` added as a Write collaborator on the repo** — required; −5 raw points until fixed (see [§ Grant instructor write access](#grant-instructor-write-access-to-your-repo-required))
- [ ] Memo committed to `docs/decisions/` with the correct filename
- [ ] YAML frontmatter intact from the template
- [ ] All six required sections present
- [ ] Hypotheses written in "I expect X because Y" form
- [ ] (If using fallback) memo uploaded to Lamaku with the same filename convention

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — including addressing collaborator status, restructuring sections, tightening hypotheses — can move your score up. The full rubric applies, no cap on the bump. You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (Stage 2 = 10% of project)

| Criterion | % of Stage 2 |
|-----------|-------------:|
| Company Selection & Rationale | 25% |
| Analytical Framing & Hypotheses (falsifiable; directional) | 25% |
| Data Source Identification | 25% |
| Professionalism & Communication | 25% |

**Collaborator-status penalty: −5 raw points** if `adamwstauffer` is not a Write collaborator on your repo by the submission deadline. The penalty carries forward into every subsequent stage until fixed — and once fixed before a stage's deadline, it lifts retroactively. Without Write access I cannot leave tracked feedback on your work, which means the Stage 5 *feedback-incorporation* rubric line has nothing to grade against.

---

## Tips

- **Lead with the conclusion.** The opening line of your Executive Summary should be your selection and one sentence on why.
- **Hypotheses must be falsifiable and directional.** "I expect X because Y" is a hypothesis. "I'll see what the ratios show" is not.
- **Cite specific data sources.** "SEC EDGAR" is good. "The internet" is not.
- **Use the memo template's frontmatter.** It encodes the fields the rubric expects — leave it intact when you customize.
- **Expect feedback and plan for it.** The instructor will leave tracked review suggestions directly on your work — the way a manager or auditor marks up a draft. Stage 5 grades how you incorporated that feedback — track it from the start (a `docs/decisions/{date}-stage2-feedback-response.md` follow-up memo is a clean way to do this).
