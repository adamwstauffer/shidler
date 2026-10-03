---
template: reference
purpose: "Quick reference for students populating and interpreting non-US-GAAP financials (VAS, IFRS, and others) in the Performance Ratios workbook"
audience: student
courses: [BUS-629]
status: reference (read as needed during Stages 2 to 5)
related:
  - ../../../../../../templates/spec-template.md
  - ../../../../../../templates/spreadsheets/performance-ratios-template.xlsx
---

# Accounting Standards Quick Reference: VAS, IFRS, US GAAP

**When to use this:** your company does **not** report under US GAAP. This page tells you what to check, where to record it, and when a difference is large enough to change how you read a ratio.

You are not expected to memorize it. You are expected to (1) know when a difference is material to your ratio interpretation, (2) note it in your workbook and your Stage 4 spec, and (3) reflect on it in your Stage 5 analysis when the numbers look strange.

The three frameworks you will meet most:

- **VAS:** Vietnamese Accounting Standards (Ministry of Finance circulars, especially Circular 200/2014/TT-BTC).
- **IFRS:** International Financial Reporting Standards.
- **US GAAP:** U.S. Generally Accepted Accounting Principles (FASB Codification).

---

## The one rule: report as filed, disclose the difference

**Populate the workbook with the numbers as reported. Do not restate the financial statements.** The Balance Sheet, Income Statement, and Cash Flow Statement tabs (`BAL_`, `INC_`, `CASH_`) keep the as-reported figures. Cross-standard differences are *noted* in the Cover & Instructions tab (the sheet named `Cover` in the template), which is what the Stage 3 brief grades under source documentation. Any adjusted metric is computed separately, in Stage 5, and shown beside the as-reported one.

This is a disclosure exercise. It shows you understand the differences; it does not ask you to convert the company to US GAAP.

---

## When to consult this page

| Stage | What you are doing | What to look up here |
|---|---|---|
| **Stage 2** (memo) | Picking your company; noting its reporting standard | The snapshot table below, to set expectations |
| **Stage 3** (workbook) | Populating from the annual report | Step 1 and Step 2; any line item that surprises you (zero lease liability, a goodwill amortization expense) |
| **Stage 4** (spec) | Naming inputs and ratio formulas | Note any cross-standard caveat in the spec's Scope and Data Inputs sections |
| **Stage 5** (final analysis) | Interpreting ratios | Flag any ratio shaped by the standard rather than the economics; compute an adjusted metric where it matters |

---

## Step 1: Identify the reporting standard

Open the company's annual report or audited financial statements. Look for a note titled "Basis of Preparation" or "Summary of Significant Accounting Policies" (usually Note 1 or Note 2). Record these in the Cover & Instructions tab:

| Field | Example |
|---|---|
| Reporting standard | VAS, IFRS, CAS, Ind AS |
| Whether the standard is IFRS-converged | Yes / partly / no |
| Reporting currency (and functional currency, if disclosed) | VND, USD |
| Fiscal year end | 31 December |
| Source | Annual report URL and page |

**If your company publishes statements under more than one standard** (some large listed companies publish a local-standard set for the exchange and an IFRS set for international investors), **use the IFRS statements** for the ratio analysis. IFRS is the language your international peers report in, and IFRS 16 puts leases on the balance sheet, which is closer to the economics. Note the choice on the Cover tab, for example: *"Reporting standard for this analysis: IFRS (consolidated statements as published in the {YYYY} annual report). VAS statements also available; not used because VAS lease and goodwill accounting would distort leverage and EBIT for cross-border peer comparison."*

---

## Step 2: Check the high-impact areas

For each area, decide whether the difference applies to your company. If it does, note it on the Cover tab with the footnote it comes from. If it does not, or you cannot quantify it from the disclosures, write "N/A: not material" or "N/A: insufficient disclosure."

For each area that applies, record four things:

1. **Applies?** Yes / No / Cannot determine
2. **Direction of impact:** overstates or understates the line item against a US GAAP basis
3. **Magnitude:** the quantified amount if the disclosures permit, otherwise "not quantifiable from public filings"
4. **Source:** footnote number and page in the annual report

### The snapshot

| # | Area | VAS | IFRS | US GAAP | Ratios most affected |
|---|---|---|---|---|---|
| 1 | **Operating leases on balance sheet** | Mostly off balance sheet (legacy) | IFRS 16: on balance sheet | ASC 842: on balance sheet | D/E, leverage, asset turnover, ROA, EBITDA-based |
| 2 | **Inventory costing (LIFO)** | Not permitted (FIFO / weighted average) | Not permitted | **Permitted** | Gross margin, inventory turnover, current ratio |
| 3 | **Revenue recognition** | Legacy, less prescriptive | IFRS 15 (five-step) | ASC 606 (five-step, converged with IFRS 15) | Revenue, DSO, deferred revenue |
| 4 | **PP&E useful lives** | Tax-driven (Circular 45 framework) | Management estimate | Management estimate | Depreciation, EBIT, ROA, asset turnover |
| 5 | **Goodwill** | **Amortized** | Impairment only | Impairment only | EBIT, net income, ROA |
| 6 | **R&D / development costs** | Mostly expensed | Development phase **may be capitalized** | Mostly expensed (some software exceptions) | Intangibles, R&D expense, EBIT, ROA |
| 7 | **Impairment reversals** | n/a | Permitted (except goodwill) | Not permitted | Operating income |
| 8 | **Credit-loss model** | Incurred loss (legacy) | IFRS 9 expected credit loss | ASC 326 CECL | Provisions, net income (financial firms) |
| 9 | **Functional currency** | Usually VND | Management determines | Management determines | CTA in OCI and equity |

**Rule of thumb:** leases and inventory are the most common sources of cross-standard ratio noise. Goodwill needs an acquisition history; credit-loss models matter mostly for banks, insurers, and REITs, which the Stage 2 brief excludes.

---

## 1. Operating leases

**What the standards say.** VAS expenses operating leases straight-line: no lease asset, no lease liability (unless a finance lease meets strict criteria). IFRS 16 (effective 2019) puts all leases over 12 months on the balance sheet as a right-of-use (ROU) asset and a lease liability; the income statement shows depreciation plus interest. US GAAP ASC 842 also puts operating leases on the balance sheet, but the income statement keeps a single straight-line lease expense.

**What it does to ratios.** A lease-heavy VAS company (retail, airlines, restaurants, telecoms) looks less levered than an IFRS or US GAAP peer because the lease liability is invisible.

| Ratio | VAS against IFRS 16 / ASC 842 |
|---|---|
| Debt-to-equity | Understated under VAS |
| Total assets | Understated under VAS (no ROU asset) |
| Asset turnover, ROA | Overstated under VAS (smaller denominator) |
| EBITDA | IFRS 16 moves lease cost below EBITDA (depreciation and interest), which lifts EBITDA; under VAS the full lease cost stays in operating expenses. Direct comparison misleads. |
| EBITDA / interest | Lower under IFRS (lease interest added); under VAS neither side carries the lease economics |

**What to do.**

- **Stage 3 workbook:** populate as reported; note the lease treatment on the Cover tab.
- **Stage 4 spec:** under Data Inputs, note the standard and where the lease commitments are disclosed.
- **Stage 5 analysis:** if the company is lease-heavy, compute one adjusted metric (for example, D/E with operating-lease commitments capitalized at a multiple of annual rent) and show it beside the as-reported figure. Any multiple you use, such as 7× annual rent, is illustrative: state the multiple and cite where it comes from.

---

## 2. Inventory costing: the LIFO question

VAS and IFRS prohibit LIFO; US GAAP permits it. This matters only if you compare your company *to* a US GAAP peer that uses LIFO. In a rising-cost environment, LIFO raises COGS (lower gross margin and EBIT), understates inventory (higher inventory turnover, lower current ratio), and lowers net income, ROA, and ROE.

**What to do.** If a US peer uses LIFO, find the "LIFO reserve" in its 10-K inventory footnote and restate it to FIFO: `Inventory_FIFO = Inventory_LIFO + LIFO_reserve`; `COGS_FIFO = COGS_LIFO − ΔLIFO_reserve`. With no LIFO companies in your peer set, ignore this section.

---

## 3. Revenue recognition

VAS follows legacy principles based on the transfer of risks and rewards (close to the old IAS 18), with multi-element arrangements and variable consideration less prescriptively addressed. IFRS 15 and ASC 606 (converged, effective 2018) use the five-step model: identify the contract, identify performance obligations, determine the price, allocate it, recognize revenue as obligations are satisfied.

Differences are usually small for manufacturing and retail. They can be significant for telecoms (handset and service bundles), software and SaaS, licensing, real estate, and long-term construction or engineering contracts, where timing shifts revenue growth, receivables and DSO, and deferred revenue.

**What to do.** For those sectors, read the revenue-policy footnote, note any policy that differs from the five-step model in your Stage 4 spec, and expect to discuss it in your Stage 5 analysis.

---

## 4. PP&E useful lives and depreciation

Under VAS, useful lives follow a tax framework set by Ministry of Finance circular (Circular 45/2013/TT-BTC), and many companies align book depreciation to it; check the depreciation-policy note for the lives your company uses. Under IFRS and US GAAP, useful lives are management estimates reviewed annually. Depreciation patterns under VAS can therefore differ materially from a peer's.

| Ratio | Effect of shorter useful lives |
|---|---|
| Depreciation expense | Higher |
| EBIT, net income, ROA, ROE | Lower |
| Net PP&E | Lower |
| Asset turnover | Higher |
| EBITDA | Unchanged (depreciation is added back) |

**What to do.** If depreciation looks unusually high or low against peers, read the useful-lives disclosure. Where depreciation is the swing factor in an EBIT-based ratio, prefer the EBITDA-based version for peer comparison.

---

## 5. Goodwill: amortized or impaired?

VAS amortizes goodwill from business combinations over a set period (check the goodwill note for the period your company uses). IFRS 3 and US GAAP ASC 350 do not amortize goodwill for public companies; they test it for impairment at least annually. JGAAP (Japan) also amortizes goodwill.

For an acquisitive company reporting under VAS, amortization lowers EBIT, net income, ROA, and ROE against an IFRS peer, and goodwill on the balance sheet falls over time instead of staying flat. EBITDA is unaffected.

**What to do.** If goodwill is material, find the annual amortization in the goodwill schedule and note it in your spec. In Stage 5, consider showing **EBIT + goodwill amortization** as a comparability adjustment against IFRS or US GAAP peers.

---

## 6. R&D and development costs

VAS generally expenses R&D. IFRS (IAS 38) expenses research but **capitalizes development costs** that meet six criteria (technical feasibility, intent to complete, ability to use or sell, probable future benefits, adequate resources, reliable measurement). US GAAP (ASC 730) expenses R&D, with specific capitalization rules for internal-use software (ASC 350-40) and software for sale (ASC 985-20).

Capitalizing development costs lowers R&D expense and raises EBIT in the year capitalized (then amortization lowers later years), and raises intangible assets. It matters most for R&D-heavy companies (tech, pharma) reporting under IFRS; for most industrial and consumer companies it is immaterial.

**What to do.** For a tech or pharma pick, read the R&D footnote. If the company capitalizes development costs, note the balance and annual amortization on the Cover tab and add a side-by-side adjustment in Stage 5.

---

## 7. Impairment reversals

IFRS allows a prior impairment loss to be reversed (except on goodwill); US GAAP does not. If the income statement includes an impairment-reversal gain, note it: it inflates operating income against a US GAAP basis.

---

## 8. Credit losses on financial assets

VAS uses a legacy incurred-loss model. IFRS 9 (effective 2018) uses expected credit loss; US GAAP ASC 326 (CECL, effective 2020 for public companies) recognizes lifetime expected losses from day one. These move provisions and net income most for banks, insurers, and lenders, which the Stage 2 brief excludes. If your company has a large trade-receivables or consumer-credit book, expected-loss provisioning may run higher than under VAS; note it if material.

---

## 9. Foreign currency translation

VAS companies generally report in VND. Under IFRS (IAS 21) and US GAAP (ASC 830) the company determines its functional currency from the economics of its operations. For a company with mostly USD revenue or debt reporting in VND, translation can create a cumulative translation adjustment (CTA) in equity: it moves comprehensive income and book value, not net income.

**What to do.** Note functional and presentation currency on the Cover tab. If translation moves equity by more than a few percent a year, flag it in Stage 5.

---

## Common situations by framework

| Your company reports under... | What to expect |
|---|---|
| **IFRS** (or SFRS(I), K-IFRS, BR GAAP) | Generally close to US GAAP. Check leases (IFRS 16 single model), R&D capitalization, and impairment reversals. |
| **VAS (Vietnam)** | Significant gaps: no IFRS 16 (leases off balance sheet), no IFRS 9 (legacy credit-loss and historical-cost financial instruments), no IFRS 15 (legacy revenue recognition), goodwill amortized, depreciation on a tax framework. Fair value measurement is not systematic. |
| **CAS (China)** | Substantially converged with IFRS, but watch business combinations under common control, conservative fair value application, and government-grant presentation. Companies listed in both Shanghai/Shenzhen and Hong Kong may publish two sets of statements. |
| **Ind AS (India)** | Converged with IFRS with carve-outs. Regulatory overlays apply to banks. |
| **JGAAP (Japan)** | Goodwill is amortized, which depresses post-acquisition earnings against IFRS and US GAAP peers. R&D is expensed. Many large Japanese listed companies report under full IFRS instead; check which. |

---

## Step 3: Flag affected ratios

On the Ratios tab, any ratio materially affected by a cross-standard difference gets a note. The simplest way: add a cell comment pointing to the Cover tab note (for example, "EBITDA inflated by IFRS 16 lease treatment; see Cover note").

---

## Quick decision tree: "I see a weird number"

```
Is the ratio dramatically different from peers?
├── No → the standard is probably not the driver
└── Yes
    ├── Leverage or asset intensity (D/E, asset turnover, ROA)?
    │   └── Check operating-lease accounting (Section 1). VAS is the top suspect.
    ├── Gross margin or inventory turnover?
    │   └── Check inventory costing (Section 2). LIFO at a US peer is the top suspect.
    ├── EBIT-based (EBIT margin, EBIT/interest, ROE)?
    │   ├── Goodwill on the balance sheet? → Section 5
    │   ├── Tech or pharma? → Section 6
    │   ├── Impairment reversal in the P&L? → Section 7
    │   └── Otherwise → depreciation policy (Section 4)
    └── Revenue or DSO?
        └── Multi-element, SaaS, or long-term contracts? → Section 3
```

When in doubt, **EBITDA-based ratios are the most robust cross-standard comparison**: they sidestep depreciation, amortization, and most of the operating-lease treatment. They are not free of distortion (IFRS 16 still lifts EBITDA), but they are the cleanest first pass.

---

## What a strong submission does

You are graded on the **quality of your disclosure**, not on a full conversion. A strong Stage 3 submission for a non-US company:

- names the reporting standard, currency, fiscal year end, and source on the Cover tab;
- notes each high-impact area that applies (and writes "N/A" for those that do not);
- flags the affected ratios;
- cites specific footnotes in the annual report.

In Stage 5, the strong move is recognizing where the standard, not the business, is driving a ratio, and showing one adjusted comparison beside the as-reported figure. A weak submission treats VAS, IFRS, or CAS line items as if they were US GAAP without comment.

---

## Further reading

- **VAS:** the Ministry of Finance publishes the VAS standards and Circulars 200/2014 (chart of accounts) and 45/2013 (fixed-asset depreciation), mostly in Vietnamese. The large audit firms publish English summaries.
- **IFRS:** [ifrs.org](https://www.ifrs.org); Deloitte's IAS Plus carries free summaries.
- **US GAAP:** [FASB Codification](https://asc.fasb.org) (free basic access).
- **Comparisons:** PwC, KPMG, and EY each publish free "IFRS vs. US GAAP" comparison guides.

This is a practical, ratio-shaped reference. The summaries are simplified: exceptions, transition rules, and industry overlays are skipped. If you are relying on it for an accounting judgment that changes the substance of your analysis, rather than flagging a peer-comparison caveat, read the actual standard.
