# Stage 2: Company Selection Memo

**Step-by-step on Kumu:** [Stage 2 walkthrough](https://adamwstauffer.github.io/ai-lms/performance-ratios-stage2.html)

**Weight:** 10% of project score
**Format:** Deliverable-only — no in-class presentation
**Deliverable:** Markdown memo (`.md`) committed to your portfolio repo

> ## ⚠ Do this first — required for grading
>
> **Add `adamwstauffer` as a Write collaborator on your portfolio repo before you submit.** This is the single most important Stage 2 setup step. Without it I cannot leave tracked feedback on your work. **Collaborator penalty:** from Stage 2 on, a stage loses 5 raw points if `adamwstauffer` is not a Write collaborator on your repository at its deadline; fixing it before a stage's deadline lifts the penalty retroactively.
>
> Steps: Repo → **Settings** → **Collaborators** → **Add people** → search `adamwstauffer` → choose **Write** → **Add to this repository**. 60 seconds. Full walkthrough is in [§ Grant instructor write access to your repo](#grant-instructor-write-access-to-your-repo-required) below.

> **Where this fits in the project.**
> **Input:** Stage 1 ratios template (you already have a copy in your repo).
> **Output (this stage):** A memo at `docs/decisions/YYYY-MM-DD-{company-slug}-selection-memo.md` selecting the company you'll analyze for the rest of the semester.
> **Used by:** Stage 3 (you populate the template with this company's financials) and Stage 5 (graded on how you incorporated the instructor's tracked feedback on this memo).

> **Submission alternative — Lamaku upload.** GitHub is the required submission path. If you hit a hard wall with Git setup or pushing your work, you may upload this memo directly to Lamaku as a fallback. Use the same filename convention (`YYYY-MM-DD-{company-slug}-selection-memo.md`). Using the Lamaku fallback does **not** reduce your Stage 2 grade. By Stage 5, the memo must also live in your repo at `docs/decisions/` — your Stage 5 polish rubric assumes the full project history is in the repo. **The Lamaku fallback does not waive the collaborator requirement above — add `adamwstauffer` either way.**

> **Unfamiliar terms?** "PR" (pull request — the mechanism GitHub uses to deliver tracked feedback documents), "YAML frontmatter," "10-K," and other recurring terms are defined in the [Project glossary in the BUS-629 README](README.md#project-glossary).

---

## Overview

Write an executive memo selecting and justifying the company you will analyze for the remainder of this project. This memo frames your project scope, identifies data sources, and previews your analytical approach. It is reviewed by the instructor for approval and to surface revisions you will carry into later stages.

With the Stage 1 template in hand, you know exactly what data points the model needs — your memo should be precise about which financials matter and why.

---

## Deliverable

A 400–600 word Markdown memo (`.md`) saved to `docs/decisions/` in your repository.

**Filename:** `YYYY-MM-DD-{company-slug}-selection-memo.md` — all **lowercase**, hyphen-separated.

No last name: the repository is already named for you. A memo already submitted under an older name that included your last name still counts; nothing to rename. A misplaced or misnamed file never blocks you and is still graded; it may cost a point under professionalism, and moving it to the path the brief names fixes that.

Example: `2026-05-21-vinamilk-selection-memo.md`

**Template:** the repo memo template, available three ways:

- In this repo: [`templates/memo-template.md`](../../../../templates/memo-template.md)
- Public GitHub link (for sharing with AI tools): [`https://github.com/adamwstauffer/shidler/blob/main/templates/memo-template.md`](https://github.com/adamwstauffer/shidler/blob/main/templates/memo-template.md)
- Raw URL (for direct LLM upload): [`https://raw.githubusercontent.com/adamwstauffer/shidler/main/templates/memo-template.md`](https://raw.githubusercontent.com/adamwstauffer/shidler/main/templates/memo-template.md)

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

> **Never done this before?** A step-by-step walkthrough of GitHub account setup, your first commit (GitHub Desktop recommended), and the Collaborators panel lives in [Kumu onboarding](https://adamwstauffer.github.io/ai-lms/onboarding.html). Read it if any of this is new to you.

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

## Pro tip — draft first, then use an LLM to review and iterate

Draft the memo yourself in the template first — your company, your reasons, your hypotheses. Then give an LLM the right context and ask it to review your draft; after the review, iterate on it together. **You draft first, the LLM reviews, then you collaborate — and you make every call.**

### Step 1 — Write your first draft (no LLM yet)

Copy the template, rename it per the convention above, and fill in all six required sections in your own words. Your first draft must contain:

- **Your company and why** — the selection and one sentence on why, leading the Executive Summary
- **Eligibility, checked** — publicly traded, non-financial, 2+ years of statements you have actually located
- **2–3 hypotheses in "I expect X because Y" form** — each with a direction and a reason
- **The ratio categories that matter for this industry, and why**
- **Your data plan** — the specific sources (SEC EDGAR, HOSE portal, the company's IR page), currency and accounting standard

Rough is fine. Commit it before you open the LLM — that commit is your evidence of the first draft.

### Step 2 — Ask an LLM to review it (not rewrite it)

The memo template lives in a public GitHub repo, and most LLMs can read public URLs directly. In Claude.ai, ChatGPT, or another capable model, paste your draft below this prompt:

```
I'm writing a Stage 2 company selection memo for my finance course. The memo
template is at:

https://raw.githubusercontent.com/adamwstauffer/shidler/main/templates/memo-template.md

Here is my draft. Review it against the template and these requirements:
all six sections present; YAML frontmatter intact; 400–600 words; hypotheses
in "I expect X because Y" form with a direction and a reason; specific data
sources; written for a managing director — concise, evidence-tight.

For each problem you find, quote the line, say what is wrong and why it
matters. Ask me questions where my reasoning is thin. Don't rewrite the memo
and don't write new sections for me.

[PASTE YOUR DRAFT HERE]
```

**No URL access?** Download the template from [`https://github.com/adamwstauffer/shidler/blob/main/templates/memo-template.md`](https://github.com/adamwstauffer/shidler/blob/main/templates/memo-template.md) (click the **Raw** button, then save the page as `memo-template.md`), upload it via the paperclip icon, and say "I have uploaded the memo template" instead of giving the URL.

### Step 3 — Iterate together; you decide

Work through the review one point at a time:

```
Let's go through your review one point at a time. For each, I'll tell you
whether I agree. Where I agree, help me think through how to fix it — ask me
questions or show me options, but I'll write the change. Where I disagree,
I'll explain why, and you tell me if my reasoning holds.
```

Revise the memo yourself and commit each meaningful round. Reject review points you disagree with — a reasoned "no" is judgment, not a gap.

### What the LLM can help with vs. what stays yours

| The LLM can help by | What stays yours |
|---|---|
| Checking your draft against the six required sections and the template structure | Choosing the company — that's your judgment, not the LLM's |
| Testing whether your hypotheses are falsifiable and directional | Verifying the company meets eligibility (publicly traded, non-financial, 2+ years of data) |
| Questioning whether your data sources will actually carry the numbers you need | Confirming those sources actually have the data before submitting |
| Flagging wordiness against a concise senior-analyst register | Every sentence in the memo — the LLM does not know your company as well as you should |

**Log the prompts.** The review and iteration sessions belong in your `prompt-log.md` (repository root). Stage 4 will grade your prompt log; start the habit at Stage 2.

---

## Connecting GitHub to an AI tool (optional, but powerful)

Most AI tools can now read directly from your GitHub repo. This lets you ask the LLM to read your Stage 1 template or review your memo draft without copy-pasting files. Brief setup notes per tool:

| Tool | How to connect to your repo |
|---|---|
| **Claude (web / desktop)** | Use the "**Projects**" feature (Pro tier) — create a project, paste your public repo's raw URLs into the project knowledge, and every conversation in that project sees them. For a one-off chat: paste a raw URL into the prompt. |
| **Claude Code (CLI)** | Run `claude` inside your repo folder — it reads every file in the directory automatically. See [Kumu AI lab](https://adamwstauffer.github.io/ai-lms/ailab.html). |
| **ChatGPT (web)** | Use the "**Connectors**" or the GitHub plugin (Plus tier) to authorize a specific repo. Then ChatGPT can browse your files. For a one-off: paste a raw URL. |
| **GitHub Copilot Chat** | Built into VS Code, GitHub.dev, and the GitHub web UI. Asks about your repo without setup once you're signed in. Free for students with the GitHub Student Developer Pack. |
| **Codex (OpenAI)** | Connect through ChatGPT Pro ($200/mo); not required for this course. |

For Stage 2, the simplest path is to **paste the raw template URL and your draft into Claude.ai or ChatGPT** (see Pro Tip above). You can ignore the table until you're ready for richer workflows.

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

**Collaborator penalty:** from Stage 2 on, a stage loses 5 raw points if `adamwstauffer` is not a Write collaborator on your repository at its deadline; fixing it before a stage's deadline lifts the penalty retroactively. Without Write access I cannot leave tracked feedback on your work, which means the Stage 5 *feedback-incorporation* rubric line has nothing to grade against.

---

## Tips

- **Lead with the conclusion.** The opening line of your Executive Summary should be your selection and one sentence on why.
- **Hypotheses must be falsifiable and directional.** "I expect X because Y" is a hypothesis. "I'll see what the ratios show" is not.
- **Cite specific data sources.** "SEC EDGAR" is good. "The internet" is not.
- **Use the memo template's frontmatter.** It encodes the fields the rubric expects — leave it intact when you customize.
- **Expect feedback and plan for it.** The instructor will leave tracked review suggestions directly on your work — the way a manager or auditor marks up a draft. Stage 5 grades how you incorporated that feedback — track it from the start (a `docs/decisions/YYYY-MM-DD-{company-slug}-feedback-response-memo.md` follow-up memo is a clean way to do this).
