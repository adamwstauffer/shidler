---
title: "VAS ↔ IFRS ↔ US-GAAP — A Ratio-Interpretation Quick Reference"
audience: Students analyzing non-U.S.-listed companies (especially Vietnamese / ASEAN firms)
status: reference (read as needed during Stages 3, 4, 5)
last_updated: 2026-05-13
related:
  - github-mba-guide.md
  - ../templates/spec-template.md
---

# VAS ↔ IFRS ↔ US-GAAP — A Ratio Quick Reference

If you picked a non-U.S.-listed company for your project — which the syllabus encourages, particularly ASEAN-listed firms — you're going to run into places where the company's financials are not directly comparable to a U.S. peer's. This guide is a practical, ratio-shaped reference for the most common divergences across three reporting frameworks:

- **VAS** — Vietnamese Accounting Standards (Ministry of Finance Circulars, especially Circular 200/2014/TT-BTC).
- **IFRS** — International Financial Reporting Standards (used by most ASEAN listings outside Vietnam, and by large Vietnamese companies that publish a second set of statements).
- **US GAAP** — U.S. Generally Accepted Accounting Principles (FASB Codification).

You are **not** expected to memorize this. You are expected to (1) know when a difference is material to your ratio interpretation, (2) note it in your **Cover & Instructions** tab and your **Stage 4 spec**, and (3) reflect on it in your **Stage 5 final analysis** when the numbers look strange.

---

## When to consult this guide

| Stage | What you're doing | What to look up here |
|-------|-------------------|----------------------|
| **Stage 2** (memo) | Picking your company; noting reporting standard | Read the snapshot table below to set expectations |
| **Stage 3** (workbook) | Populating from the 10-K equivalent | Look up each line item that surprises you (a Vietnamese firm with zero lease liability, a goodwill amortization expense, etc.) |
| **Stage 4** (spec) | Naming derived inputs and ratio formulas | Note any cross-standard adjustments in the spec's Data Inputs section |
| **Stage 5** (final analysis) | Interpreting ratios | Flag any ratio whose value is materially shaped by the standard, not the underlying economics |

---

## The big-picture snapshot

The differences that matter for ratio analysis cluster in eight areas. Here is the short version. Each row has its own section below.

| # | Area | VAS | IFRS | US GAAP | Ratios most affected |
|---|------|-----|------|---------|---------------------|
| 1 | **Operating leases on balance sheet** | Mostly off-BS (legacy) | IFRS 16: on-BS | ASC 842: on-BS | D/E, leverage, asset turnover, ROA, EBITDA-based |
| 2 | **Inventory costing — LIFO** | Disallowed (FIFO / weighted-avg) | Disallowed | **Allowed** | Gross margin, inventory turnover, current ratio |
| 3 | **Revenue recognition** | Legacy, less prescriptive | IFRS 15 (5-step) | ASC 606 (5-step, converged with IFRS 15) | Revenue, DSO, deferred revenue |
| 4 | **PP&E useful lives** | Tax-driven (Circular 45 default) | Management estimate | Management estimate | Depreciation, EBIT, ROA, asset turnover |
| 5 | **Goodwill** | **Amortized** (10–20 yr) | Impairment-only | Impairment-only | EBIT, net income, ROA |
| 6 | **R&D costs** | Mostly expensed | Development phase **may be capitalized** | Mostly expensed (some software exceptions) | Intangibles, R&D expense, EBIT, ROA |
| 7 | **Credit-loss model** | Incurred loss (legacy) | IFRS 9 — Expected Credit Loss (ECL) | ASC 326 — CECL (since 2020) | Loan-loss provision, net income (banks/financial) |
| 8 | **Functional currency** | Often VND-mandated | Management determines | Management determines | CTA in OCI/equity, comprehensive income |

**Rule of thumb:** **leases and inventory** are by far the most common sources of cross-standard ratio noise for the company picks in this course. Most students will hit one or both. The rest are either rarer (goodwill — needs an M&A history) or restricted to specific sectors (credit-loss model — banks only, which Stage 2 excludes).

---

## If your company publishes statements under multiple standards

Many large Vietnamese listings (Vinamilk, FPT, Vingroup, Masan, Vietcombank's parent VCB) publish **both VAS statements (required for the HOSE/HNX filing) and IFRS statements (for international investors)**. If your company does this, **use the IFRS statements** for your ratio analysis. Two reasons:

1. **Comparability** — IFRS is the language your international peer set will be reporting in.
2. **Lease accounting** — IFRS 16 brings operating leases onto the balance sheet, which is far closer to the economics. A VAS-only set of statements will systematically understate leverage and asset intensity for any lease-heavy business.

Note the choice in your Cover & Instructions tab: *"Reporting standard for this analysis: IFRS (consolidated statements as published in the {YYYY} annual report). VAS statements also available; not used here because lease and goodwill accounting under VAS would distort leverage and EBIT for cross-border peer comparison."*

---

## 1. Operating leases on the balance sheet

### What the standards say

- **VAS** — operating leases are generally expensed straight-line. **No lease asset, no lease liability** on the balance sheet (unless the lease is a finance lease meeting strict criteria).
- **IFRS 16** (effective 2019) — *all* leases over 12 months are on-BS. Lessee recognizes a **right-of-use asset** and a **lease liability**. Income statement: depreciation on the ROU asset + interest on the liability (replaces the straight-line operating-lease expense).
- **US GAAP — ASC 842** (effective 2019 for public) — also brings operating leases on-BS. Same ROU asset; lease liability. But the income statement still shows a single straight-line lease expense (so the recharacterization is balance-sheet only, not P&L).

### What this means for ratios

A lease-heavy VAS-reporting company (retail, airlines, restaurants, telecoms) looks **much less levered** than a peer reporting under IFRS or US GAAP because the lease liability is invisible.

| Ratio | What happens under VAS vs. IFRS/ASC 842 |
|-------|------------------------------------------|
| **Debt-to-Equity** | Understated under VAS (lease liability hidden) |
| **Total Assets** | Understated under VAS (no ROU asset) |
| **Asset Turnover** (Revenue / Assets) | **Overstated** under VAS (smaller denominator) |
| **ROA** | **Overstated** under VAS (smaller denominator) |
| **EBITDA** | Under IFRS, lease expense is split into depreciation+interest, which lifts EBITDA. Under VAS, the full lease cost stays in operating expenses, depressing EBITDA. Direct comparison is misleading. |
| **EBITDA / Interest** | Under IFRS, interest is higher (lease-interest portion), so the coverage ratio is lower. Under VAS, neither side picks up the lease economics. |

### What to do

- **In your Stage 3 workbook** — populate the numbers as reported. Don't try to retroactively adjust.
- **In your Stage 4 spec** — under Data Inputs, note: *"Reporting standard: VAS. Operating-lease commitments disclosed in Note {N} but not capitalized on the balance sheet. Adjusted leverage metrics that capitalize operating leases (at e.g. 7× annual rent) are noted in the analysis section for peer comparability."*
- **In your Stage 5 analysis** — if your company is lease-heavy, **compute one adjusted metric** (e.g., adjusted D/E with operating leases capitalized at 7× annual rent) and show it alongside the as-reported metric. This is a strong-work signal — it tells the grader you understood the standard's effect on the ratio.

> **Why 7× annual rent?** A common analyst rule-of-thumb for capitalizing operating leases when full lease-disclosure data isn't available. S&P and Moody's used 8× pre-IFRS-16; 6–7× is the more common analyst convention. Cite whatever multiple you pick.

---

## 2. Inventory costing — the LIFO question

### What the standards say

- **VAS** — FIFO or weighted-average. **LIFO is not permitted.**
- **IFRS** — FIFO or weighted-average. **LIFO is not permitted.**
- **US GAAP** — FIFO, weighted-average, **or LIFO**. LIFO is uncommon but used (often for tax reasons since the LIFO conformity rule).

### What this means for ratios

In a **rising-cost environment** (most industries, most years), LIFO compared to FIFO:

- Inflates COGS → **lower gross margin, lower EBIT**
- Understates inventory (recent purchases are expensed first; older, cheaper inventory sits on the BS) → **higher inventory turnover, lower current ratio**
- Lowers net income → **lower ROE, lower ROA**

If you're picking a Vietnamese or ASEAN company and comparing it to a U.S. peer using LIFO, **the U.S. peer's ratios are not directly comparable** unless you adjust for the **LIFO reserve** (a footnote disclosure showing what inventory would be under FIFO).

### What to do

- If you're comparing your company to a U.S. peer that uses LIFO, **check the U.S. peer's 10-K for a "LIFO reserve" footnote**. The adjustment is: `Inventory_FIFO = Inventory_LIFO + LIFO_reserve`; `COGS_FIFO = COGS_LIFO - ΔLIFO_reserve`.
- For pure within-Vietnam or within-IFRS comparisons (no LIFO companies in your peer set), **no adjustment is needed** and you can ignore this section.
- Note the comparability issue in your spec if relevant; flag it in the Stage 5 analysis if it shifts a ratio interpretation.

---

## 3. Revenue recognition

### What the standards say

- **VAS** — accrual-based, generally based on transfer of risks and rewards. Multi-element arrangements and variable consideration are less prescriptively addressed. Practices can vary.
- **IFRS 15** and **US GAAP ASC 606** (largely converged, effective 2018) — five-step model: identify contract → identify performance obligations → determine transaction price → allocate price to obligations → recognize revenue when obligations are satisfied. **Same outcomes in most cases.**

### What this means for ratios

For most companies the divergence is small — revenue gets recognized in roughly the same period. But for **multi-element contracts** (telecoms with handset + service bundles; software-as-a-service; long-term construction or engineering contracts), VAS can produce different timing.

| Ratio | What can happen |
|-------|-----------------|
| **Revenue growth** | A telecom that allocates more of a bundled contract to handsets (Day-1 revenue) vs. service (recognized over the contract term) shifts the timing. |
| **Days Sales Outstanding (DSO)** | Different timing → different receivables → different DSO. |
| **Deferred revenue** | IFRS 15 / ASC 606 require explicit recognition of contract liabilities (deferred revenue) for unbilled performance obligations. VAS may book it differently. |

### What to do

- For most company picks (industrial, consumer goods, retail), revenue-recognition differences are immaterial.
- For **telecoms, software, long-term contractors, real estate**, read the revenue accounting policy footnote carefully. Note the methodology in your Stage 4 spec.
- If your company is a SaaS or long-term-contract business, expect a paragraph on this in your Stage 5 final analysis under "LLM Evaluation & Annotations."

---

## 4. PP&E useful lives and depreciation

### What the standards say

- **VAS** — useful lives are **prescribed by tax law** via Circular 45/2013/TT-BTC. Examples: buildings 25–50 years, manufacturing equipment 7–15 years, office equipment 3–10 years. Many Vietnamese companies align book depreciation to tax-mandated lives to avoid book/tax differences.
- **IFRS** and **US GAAP** — useful lives are **management estimates**, reviewed annually. Companies tend to use longer lives (especially for buildings — often 40–50 yr in IFRS/US GAAP filings).

### What this means for ratios

If your VAS-reporting company uses shorter prescribed lives than an international peer:

| Ratio | Effect under VAS shorter-life depreciation |
|-------|-------------------------------------------|
| **Depreciation expense** | Higher |
| **EBIT** | Lower |
| **Net income, ROA, ROE** | Lower |
| **Net PP&E** | Lower (faster accumulated depreciation) |
| **Asset turnover** | Higher (smaller denominator) |
| **EBITDA** | Unchanged — depreciation is added back |

EBITDA-based comparisons are the safest cross-standard metric here, which is one reason analysts default to EBITDA when comparing across jurisdictions.

### What to do

- If depreciation looks unusually high or low relative to peers, check the useful-lives disclosure in the notes (usually Note 11 or 12 in a VAS filing).
- In your Stage 5 analysis, if depreciation appears to be the swing factor for an EBIT-based ratio, prefer the EBITDA-based version of the same ratio for peer comparison.

---

## 5. Goodwill — amortized or impaired?

### What the standards say

- **VAS** — goodwill arising from business combinations is **amortized**, typically over **10 years** (max 20 years per VAS 11). Books a recurring amortization expense.
- **IFRS** (IFRS 3) — **no amortization.** Goodwill is tested for impairment annually (or more often if a triggering event occurs).
- **US GAAP** (ASC 350) — same as IFRS: **no amortization** for public companies (private companies have an election). Annual impairment test.

### What this means for ratios

For a Vietnamese company with significant M&A history (Vingroup, Masan, FPT, Vietjet):

| Ratio | Effect under VAS amortization vs. IFRS impairment-only |
|-------|------------------------------------------------------|
| **Amortization expense** | Present under VAS, absent under IFRS/US GAAP |
| **EBIT** | Lower under VAS |
| **Net income, ROA, ROE** | Lower under VAS |
| **EBITDA** | Unchanged (amortization added back) |
| **Goodwill on BS** | Falls over time under VAS; flat under IFRS/US GAAP unless impaired |

This is a real, recurring difference for acquisitive Vietnamese groups. A direct EBIT or net-income comparison between Vingroup (VAS, amortizing goodwill) and a multinational peer (IFRS, impairment-only) overstates the multinational's underlying earnings power.

### What to do

- If your company has material goodwill on the balance sheet, check Note {N} (goodwill schedule) for the annual amortization. If material, note it in your spec.
- In your Stage 5 analysis, consider showing **EBIT + goodwill amortization** as a comparability adjustment when benchmarking against IFRS/US GAAP peers.

---

## 6. R&D — expensed or capitalized?

### What the standards say

- **VAS** — research and development is generally **expensed** as incurred.
- **IFRS** (IAS 38) — research is expensed; **development costs are capitalized** if six criteria are met (technical feasibility, intent to complete, ability to use/sell, future economic benefits, adequate resources, reliably measurable). In practice, software and pharma firms capitalize significant amounts.
- **US GAAP** (ASC 730) — R&D is generally **expensed** as incurred. **Exception:** internal-use software (ASC 350-40) and software for sale (ASC 985-20) have specific capitalization rules.

### What this means for ratios

For a tech, pharma, or biotech pick:

| Ratio | Effect of IFRS capitalization vs. VAS/US-GAAP expensing |
|-------|--------------------------------------------------------|
| **R&D expense (P&L)** | Lower under IFRS (development portion is capitalized) |
| **EBIT, net income** | Higher under IFRS in the year of capitalization, lower in subsequent years (as the capitalized cost is amortized) |
| **Intangible assets** | Higher under IFRS |
| **ROA** | Mixed — numerator higher in year 1, denominator larger ongoing |

This matters most for **R&D-heavy companies under IFRS** (European pharma, some Asian tech). For typical Vietnamese industrials or consumer-goods companies, R&D is small relative to revenue and the divergence is immaterial.

### What to do

- For most picks, ignore this section.
- For a tech or pharma pick, check the R&D footnote for capitalization disclosure. If your company capitalizes development costs, your "R&D intensity" ratio is not directly comparable to a US peer expensing all R&D — add a side-by-side adjustment in Stage 5.

---

## 7. Credit losses on financial assets

### What the standards say

- **VAS** — incurred-loss model (legacy). Loss recognized when objective evidence exists that the asset is impaired.
- **IFRS 9** (effective 2018) — **Expected Credit Loss (ECL) model.** Recognize lifetime expected losses for all assets that have experienced significant credit deterioration; 12-month expected loss otherwise.
- **US GAAP — ASC 326 (CECL)** (effective 2020 for public) — **Current Expected Credit Loss.** Recognize lifetime expected losses from day one for all financial assets at amortized cost.

### What this means for ratios

**Banks, insurers, lessors, and consumer-finance companies** see large swings in loan-loss provision under ECL/CECL versus the legacy incurred-loss model. Net income, EPS, and capital ratios all move.

### What to do

- **The course's Stage 2 eligibility criteria exclude banks, insurance, and REITs** (these have materially different ratio structures), so most students won't hit this.
- If you picked a corporate with a significant **trade-receivables book** (industrial / retail with consumer-credit operations), the ECL model can push receivables-related provisioning higher than under VAS. Note it if material.

---

## 8. Foreign currency translation

### What the standards say

- **VAS** — companies report in **VND** unless an exception is granted. Foreign-currency transactions translated at the closing rate at each reporting date.
- **IFRS** (IAS 21) and **US GAAP** (ASC 830) — largely converged. The company determines its **functional currency** based on the economics of its operations (the currency that most influences sales prices, labor, materials). Translation method depends on functional vs. presentation currency.

### What this means for ratios

For a Vietnamese exporter or a company with significant USD-denominated debt or revenues, the **functional-currency designation matters**. If a Vietnamese company has predominantly USD revenues (e.g., a tech outsourcing firm) and reports in VND under VAS, FX-translation noise can create a CTA item in equity that wouldn't appear if functional currency were USD.

| Ratio | Effect |
|-------|--------|
| **Comprehensive income** | CTA flows through OCI; affects total comprehensive income but not net income |
| **Book value, equity-based ratios** | CTA accumulates in equity; can grow or shrink the equity base over time |

### What to do

- Note the functional currency and presentation currency in your Cover tab.
- If currency translation is moving equity by more than a few percent of total equity per year, flag it in the Stage 5 analysis. Otherwise, immaterial for ratio interpretation.

---

## Quick decision tree — "I see a weird number. What do I do?"

```
Is the ratio dramatically different from peers?
├── No → ignore; the standard is probably not the driver
└── Yes
    ├── Is it a leverage or asset-intensity ratio (D/E, asset turnover, ROA)?
    │   └── Yes → check operating-lease accounting (Section 1). Vietnamese VAS = top suspect.
    ├── Is it gross margin or inventory turnover?
    │   └── Yes → check inventory costing method (Section 2). LIFO at the US peer = top suspect.
    ├── Is it EBIT-based (EBIT margin, EBIT/interest, ROE)?
    │   ├── Goodwill on the BS? → Section 5 (amortization)
    │   ├── Tech/pharma? → Section 6 (R&D)
    │   └── Otherwise → check depreciation policy (Section 4)
    └── Is it revenue or DSO?
        └── Multi-element / SaaS / long-term contractor? → Section 3
```

When in doubt, **EBITDA-based ratios are the most robust cross-standard comparison** — they sidestep depreciation, amortization, and (mostly) operating-lease treatment. They are not free of distortion, but they are the cleanest first-pass.

---

## Worked example — Vinamilk (VAS, lease-light, consumer staples)

Vinamilk publishes both VAS and IFRS statements. For a hypothetical Stage 4 analysis:

- **Reporting standard chosen:** IFRS consolidated statements (used for peer comparability).
- **Inventory costing:** weighted-average. Comparable to any IFRS or U.S. peer not using LIFO.
- **Leases:** light — owns most production facilities and farms. The IFRS-16 ROU asset is a few percent of total assets. Direct comparison to a peer like Mengniu (IFRS) is clean.
- **Goodwill:** modest from regional dairy acquisitions; under IFRS, no amortization. EBIT comparison to Mengniu is clean.
- **R&D:** small; expensed. Not material.

**Result:** for Vinamilk, the standards-driven ratio distortion is minimal. Direct comparison to IFRS-reporting Asian dairy peers is straightforward. Note in Stage 4 spec: *"Standards-driven comparability adjustments: none required. Reporting under IFRS with FIFO/wavg inventory, no LIFO. Lease commitments immaterial. Goodwill non-amortizing."*

## Worked example — Vingroup (VAS, lease-heavy, conglomerate with goodwill)

Vingroup files under VAS. For a hypothetical Stage 4 analysis:

- **Reporting standard chosen:** VAS (the only standard the company publishes in full).
- **Leases:** material. Vincom Retail subsidiary leases significant retail space; operating-lease commitments disclosed in the notes but not capitalized on the BS.
- **Goodwill:** significant from Vinhomes, Vincom Retail, VinFast historical structures. Amortizing under VAS.
- **R&D (VinFast):** expensed as incurred.

**Result:** the reported leverage ratios understate the true balance-sheet leverage by a material amount. Reported EBIT is depressed by goodwill amortization that wouldn't appear under IFRS.

In Stage 5, students who picked Vingroup should compute:

- **Adjusted D/E**, capitalizing operating-lease commitments at 7× annual rent (note the multiple).
- **EBIT + goodwill amortization** as an alternative profitability measure for peer comparability.
- A one-paragraph note explaining that these adjustments are not corrections — they are comparability bridges to international peers reporting under IFRS.

This kind of work — recognizing where the standard, not the underlying economics, is driving the ratio — is the analytical judgment Stage 5 is testing.

---

## Further reading

If you want to go deeper than this guide:

- **VAS** — the Ministry of Finance publishes the 26 active VAS standards plus Circulars 200/2014 (chart of accounts) and 45/2013 (PP&E useful lives). Most are available in Vietnamese only; English summaries are produced by the Big Four firms (e.g., EY's "Doing business in Vietnam" series).
- **IFRS** — [ifrs.org](https://www.ifrs.org) (the standards are paywalled but the summaries on Deloitte's IASPlus are free).
- **US GAAP** — [FASB Codification](https://asc.fasb.org) (free academic access).
- **Comparison resources** — PwC, KPMG, and EY each publish annual "IFRS vs. US GAAP" guides (~100 pages, free PDFs). Deloitte's IASPlus has a "IFRS vs. VAS" comparison series.

For most ratio-interpretation needs in this course, **the guide you're reading right now is enough**. The Big Four PDFs are for the rare case where you need the citation.

---

## A word on what this guide is and is not

This is a **practical, ratio-shaped** reference. It is not a substitute for an accounting textbook, and the standards summaries above are deliberately simplified — exceptions, transition rules, and industry-specific overlays are skipped. If you find yourself relying on this guide to make an accounting judgment that affects the substance of your analysis (rather than just flagging a peer-comparison caveat), **read the actual standard** or ask the instructor.

The goal here is not to make you a cross-border accounting specialist. It is to give you the vocabulary and the awareness to **notice when a ratio is being driven by the standard, not the business**, and to make that noticing visible in your Stage 5 analysis. That is itself the analytical skill the course is grading.
