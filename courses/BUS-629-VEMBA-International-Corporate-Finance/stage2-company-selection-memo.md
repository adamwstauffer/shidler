# Stage 2: Company Selection Memo

**Weight:** 10% of project score (70% deliverable / 30% presentation)
**Deliverable:** Markdown memo (`.md`) + in-class presentation

---

## Overview

Write an executive memo selecting and justifying the company you will analyze for the remainder of this project. This memo frames your project scope, identifies data sources, and previews your analytical approach.

In class you will present a 3–5 minute summary of your selection. The memo and the presentation together count for the Stage 2 grade.

## Why this comes after Stage 1

With the template in hand, you know exactly what data points the model needs. Your memo should be precise — "I need prior-year total assets because the template's start-of-year ROA depends on it" — not abstract hand-waving.

---

## Deliverable

A 400–600 word Markdown memo (`.md`) saved to `docs/decisions/` in your repository.

**Filename:** `YYYY-MM-DD-{lastname}-{company-slug}-selection.md`
Example: `2026-05-21-nguyen-vinamilk-selection.md`

**Template:** [`../../docs/templates/memo-template.md`](../../docs/templates/memo-template.md) — copy, rename per the convention above, fill in the sections, keep the YAML frontmatter intact.

**Audience:** A CFO or VP of Finance.

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
4. **Preliminary Observations** — 2–3 initial hypotheses about what the ratio analysis might reveal. (e.g., "Given [Company]'s aggressive expansion into Indochina, I expect high leverage ratios but potentially declining efficiency metrics.")
5. **Ratio Categories Preview** — Brief note on which ratio categories are most relevant for this company's industry and why.
6. **Data Collection Plan** — Which financial statements are needed, what market/analyst assumptions must be sourced, any currency or accounting standard considerations.

---

## In-class presentation (30% of stage grade)

A 3–5 minute presentation summarizing your selection.

**Suggested structure:**
- Company + ticker + one-line "why this company" (30 seconds)
- Two or three preliminary hypotheses (1–2 minutes)
- Data sources and any standards/currency challenges (1 minute)
- Q&A (1–2 minutes)

You may use slides or present from your memo on screen. Slides are not required.

---

## Rubric (Stage 2 = 10% of project)

### Deliverable — 70% of stage grade

| Criterion | % of deliverable |
|-----------|-----------------:|
| Company Selection & Rationale | 25% |
| Analytical Framing & Hypotheses | 25% |
| Data Source Identification | 25% |
| Professionalism & Communication (writing) | 25% |

### Presentation — 30% of stage grade

| Criterion | % of presentation |
|-----------|------------------:|
| Clarity and structure | 30% |
| Hypothesis quality | 30% |
| Response to Q&A | 25% |
| Professionalism (timing, presence) | 15% |

---

## Tips

- **Lead with the conclusion.** The opening line of your Executive Summary should be your selection and one sentence on why.
- **Make hypotheses falsifiable.** "I expect to find X because Y" is a hypothesis. "I'll see what the ratios show" is not.
- **Cite specific data sources.** "SEC EDGAR" is good. "The internet" is not.
- **Use the memo template's frontmatter.** It encodes the fields the rubric expects — leave it intact when you customize.
