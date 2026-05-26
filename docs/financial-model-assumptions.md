# Master Financial Model Assumptions

**Single source of truth for cross-company financial model inputs.**

This file holds the institutional "house view" — assumptions that should be **identical across every DCF, comps, LBO, merger model, and valuation exercise** built in this repo, regardless of which company is being analyzed. Company-specific inputs (revenue, margins, beta, capital structure) are derived per-company; the values in this file are not.

Any Claude skill, slash command, or human analyst building a financial model **must read this file first** and use these values unless the analysis has a documented reason to deviate (recorded in the deliverable's notes section).

---

## Accounting Basis (mandatory disclosure)

Every financial model must state the **accounting standard** under which the subject company reports. For comps sets with companies reporting under different standards, the model must identify unadjusted cross-standard items.

| Field | Required Value |
|---|---|
| Reporting standard | US GAAP, IFRS, VAS, CAS, JGAAP, Ind AS, or other (specify) |
| IFRS convergence status | Identical / Converged / Partially converged / Distinct |
| Conversion tier applied | Tier 1 (none) / Tier 2 (disclosure) / Tier 3 (quantitative bridge) |
| GAAP Bridge tab present? | Yes / No / N/A (US GAAP source) |

- **Tier 2 (disclosure-plus-footnote)** is the default for undergraduate work and BUS-629 Stage 3.
- **Tier 3 (quantitative bridge)** is expected for BUS-629 Stages 4–5 and any transaction-grade model.
- See [`docs/decisions/2026-05-24-accounting-standards-conversion-framework.md`](decisions/2026-05-24-accounting-standards-conversion-framework.md) for the full conversion hierarchy, adjustment mechanics, and framework survey.

> **Cell comments:** Every hardcoded cell affected by a cross-standard adjustment should cite the GAAP Bridge tab row and the source footnote from the annual report.

---

## Effective Dates

| Field | Value | Source | Last Updated |
|---|---|---|---|
| Risk-Free Rate (10Y UST) | **4.55%** | Federal Reserve H.15, 10Y constant maturity, daily | 2026-05-22 |
| Equity Risk Premium | **5.50%** | Damodaran implied ERP, US equities, monthly | 2026-05-01 |
| US Statutory Tax Rate | **21.0%** | IRC §11 (federal corporate) | 2017 (post-TCJA) |
| Blended US Effective Tax Rate (default) | **24.0%** | Fed + weighted-avg state, used when company effective rate unavailable | 2026-05-01 |

> **Update cadence:** Risk-free rate refreshed monthly (first business day). ERP refreshed quarterly. Tax rates only on tax law change.

### Refresh Mechanism

Update is **instructor-triggered, not automated**. Two trigger paths:

1. **Calendar-driven (primary).** First business day of each month, instructor runs the refresh — pull current 10Y UST yield from the Fed H.15 daily series and update the value, "Last Updated" date, and the Update Log entry. For non-USD currencies, refresh the table in §1.1 from the corresponding central-bank source.
2. **Session-driven (opportunistic).** When starting a valuation session, if the "Last Updated" date is more than one cadence period stale, refresh in-session before building the model. Do not build a model on stale Rf and hope to update later — the cell comments will then point to a date that doesn't match the value.

Every refresh adds one row to the Update Log (§6). Stale-but-undocumented values are worse than fresh-but-uncited ones because they break the audit trail. If you cannot determine the as-of date of a value in this file, treat the value as untrusted.

---

## 1. Cost of Capital Inputs

### 1.1 Risk-Free Rate

- **Value (USD):** 4.55%
- **Definition:** Daily 10-year U.S. Treasury constant-maturity yield, as of close on 2026-05-22.
- **Source URL:** https://www.federalreserve.gov/releases/h15/ (series DGS10)

**Non-USD risk-free rates** (use when valuing a company whose reporting and trading currency is not USD; document the currency on the model cover sheet):

| Currency | Instrument | Value | Source | Last Updated |
|---|---|---|---|---|
| **VND** | Vietnam 10Y Government Bond | **3.10%** | Bloomberg / Vietstock; used for BUS-629 Vietnamese-firm DCFs | 2026-05-22 |
| **EUR** | Germany 10Y Bund | **2.65%** | ECB; default Eurozone benchmark | 2026-05-22 |
| **GBP** | UK 10Y Gilt | **4.30%** | Bank of England | 2026-05-22 |
| **JPY** | Japan 10Y JGB | **1.45%** | BOJ | 2026-05-22 |
| **SGD** | Singapore 10Y SGS | **2.80%** | MAS | 2026-05-22 |
| **CNY** | China 10Y CGB | **2.20%** | PBOC; note state-influenced yield curve | 2026-05-22 |
| **INR** | India 10Y G-Sec | **6.85%** | RBI | 2026-05-22 |

For currencies not listed, use the local 10Y sovereign yield from the central bank or Bloomberg ticker, document the source, and add the new currency to this table during the next monthly refresh.

> **Country risk premium overlay:** For emerging markets, the local sovereign Rf already captures most country risk. For purely cross-border DCFs (e.g., a US-headquartered acquirer valuing a Vietnamese target), apply a country risk premium (CRP) on top of the US-USD discount rate instead of switching the Rf. Default CRPs follow Damodaran's country risk database; document the choice.

### 1.2 Equity Risk Premium

- **Value:** 5.50%
- **Definition:** Damodaran implied ERP for US equities, used as the market risk premium in CAPM.
- **Use this value in every Cost of Equity calculation** regardless of company.
- **Source:** Aswath Damodaran, NYU Stern, monthly implied ERP series.

### 1.3 Beta

**Default beta = 1.00 (market).** Every model in this repo uses β = 1.00 unless the analyst explicitly opts into a company-specific beta and documents the override in the model's notes section.

- **Why uniform:** Cross-model comparability across courses and research outputs requires that all CAPM-derived costs of equity differ only by Rf and ERP, both of which are also pegged in this spec. A student DCF on Apple and an instructor DCF on Toyota should produce comparable Ke values, and a per-company beta defeats that.
- **Documented override (opt-in):** For institutional research, transaction-grade models, or any work where an analyst wants company-specific beta, use the methodology hierarchy below. The override must be noted on the model's cover sheet or WACC sheet with a one-line justification.

**Override methodology (when opted in):**

- **Default source:** 5-year monthly raw beta vs. S&P 500 (or local index for non-US equities).
- **Acceptable proxies (in order):** Bloomberg → Yahoo Finance → Finbox → 24/7 Wall St → industry-average beta from comps if individual ticker unavailable.
- **If company is pre-IPO or has <2 years of trading history:** use unlevered industry beta + re-lever using target capital structure. Document the proxy.
- **Special case:** If a company has just been acquired, restructured, or has materially changed business mix, prefer fundamental beta (industry comp average) over raw historical beta.

### 1.4 Cost of Debt

- **Default approach:** Use yield-to-maturity on the company's longest-dated senior unsecured note, weighted by issuance.
- **If no traded debt:** Risk-free rate + credit spread by rating:

| Rating | Spread over Rf |
|---|---|
| AAA | 50 bp |
| AA | 75 bp |
| A | 100 bp |
| BBB | 175 bp |
| BB | 300 bp |
| B | 500 bp |
| CCC | 800 bp |

- **After-tax cost of debt** = Pre-tax cost × (1 − tax rate).

### 1.5 Tax Rate

- **Order of preference:**
  1. Company's most recent fiscal-year effective tax rate from 10-K (if stable; reject if affected by one-time items).
  2. 5-year average effective rate.
  3. Default blended US rate: **24.0%**.
- **Document the choice** in the WACC sheet cell comment.

### 1.6 WACC Mechanics

- **Capital structure weighting:** Always **market values** (market cap for equity, market value of debt — use book value as proxy if traded debt unavailable).
- **Net cash position:** When cash > debt, floor net debt at 0 in WACC weights. WACC will approximate cost of equity. Note this explicitly in the WACC sheet.
- **Don't blend short- and long-term debt** — use weighted-average maturity ≥ 1 year for cost of debt; treat short-term debt as part of net working capital.

---

## 2. DCF Mechanics

| Convention | Value | Rationale |
|---|---|---|
| Default projection period | **5 years** | Balances visibility horizon with terminal-value reliance |
| Discount timing | **Mid-year convention** (periods 0.5, 1.5, 2.5, 3.5, 4.5) | Cash flows assumed to occur ratably during the year |
| Terminal value method | **Gordon Growth (perpetuity)** | Default; use exit multiple as cross-check only |
| Terminal value timing | Discounted at final-year period (e.g., 4.5 for a 5-year forecast under mid-year) | |
| Default terminal growth (Base case) | **2.5%** | Approximate US long-term real GDP growth |
| Terminal growth (Bear) | **2.0%** | Conservative — below GDP |
| Terminal growth (Bull) | **3.0%** | Above-GDP, only justifiable for durable franchises |
| Hard ceiling on terminal g | **WACC − 50 bp** | Mathematical requirement (g < WACC); 50bp buffer for stability |
| Terminal value % of EV sanity check | 50–70% | If <40% terminal assumptions are too conservative; if >75% model is over-reliant on terminal |

### 2.1 Free Cash Flow Definition (Unlevered)

```
Unlevered FCF = EBIT × (1 − tax rate)
              + D&A (non-cash)
              − CapEx
              − Δ NWC
```

- **Stock-based compensation:** Treat as a real cash expense — do NOT add back to FCF. (If a company excludes SBC from non-GAAP FCF, **override** their definition.)
- **Leases:** Treat operating lease expense as an operating cost; treat finance lease debt as part of debt in capital structure.

### 2.2 Scenario Framework (Default)

Every DCF must include three scenarios with Bear / Base / Bull labels:

| Scenario | Revenue Growth Posture | Margin Posture | WACC Adjustment | Terminal g |
|---|---|---|---|---|
| **Bear** | Below-consensus / cycle-trough | Compression toward historical low | +100bp vs base | 2.0% |
| **Base** | Consensus / management guidance | Hold or modest expansion | CAPM-derived | 2.5% |
| **Bull** | Above-consensus / blue-sky | Continued expansion | −100bp vs base | 3.0% |

---

## 3. Comparable Companies Analysis

### 3.1 Multiples

| Multiple | Use for |
|---|---|
| EV/Revenue (NTM) | High-growth, pre-profit companies |
| EV/EBITDA (NTM) | Mature, capital-light businesses |
| EV/EBIT (NTM) | Capital-intensive (corrects for D&A differences) |
| P/E (NTM) | Financial services, REITs, stable earners |
| EV/(EBITDA − CapEx) | Capital-intensive infrastructure |

- **Always use NTM (next-12-months consensus)**, not LTM, unless trailing data is the only data available.
- **Statistics to report:** Median, mean, 25th and 75th percentiles. Median is the primary benchmark.

### 3.2 Outlier Handling

- Trim if z-score > 2.0 vs. the peer set.
- Document trimming in the comps tab notes.
- Never trim a peer just because it's inconvenient — only on statistical grounds.

---

## 4. LBO / Merger Model Conventions

| Convention | Value |
|---|---|
| Default hold period | 5 years |
| Default exit multiple method | Same as entry EBITDA multiple (assume no multiple expansion) |
| Sponsor return target | 20% IRR base case |
| Min cash balance assumption | $25M or 2% of revenue, whichever is higher |
| Mandatory amortization assumption | 1% of principal/year unless deal specifies |
| Excess cash sweep | 75% to debt paydown, 25% to balance sheet |
| Synergy phasing (merger models) | Year 1: 33%, Year 2: 67%, Year 3+: 100% |

---

## 5. Formatting & Presentation Standards

### 5.1 Color Coding (mandatory)

| Element | Font Color | Fill |
|---|---|---|
| Hardcoded input | Blue (`#0000FF`) | Light grey (`#F2F2F2`) |
| Formula / calculation | Black (`#000000`) | White |
| Sheet link / external reference | Green (`#008000`) | White |
| Section header | White, bold | Dark blue (`#1F4E79`) |
| Sub-header / column header | Black, bold | Light blue (`#D9E1F2`) |
| Key output (price, EV, IRR) | Black, bold | Medium blue (`#BDD7EE`) |

> **Resist the urge to add more colors.** Three blues, one grey, and white is the entire palette unless the user specifies otherwise. Course materials should also reference [`docs/_branding/design.json`](./_branding/design.json) for UH Mānoa institutional branding (UH Green `#024731` for headings on course materials).

### 5.2 Number Formats

| Type | Format |
|---|---|
| Currency (large) | `_($* #,##0.0_);_($* (#,##0.0);_($* "-"??_);_(@_)` |
| Currency (per-share) | `_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)` |
| Percentage | `0.0%;(0.0%);"-"` |
| Number | `#,##0.0;(#,##0.0);"-"` |
| Year header | Text (e.g., `"FY2027E"`) |
| Negative | Always parentheses, never minus sign |
| Zero | Display as `"-"` |

### 5.3 Required Documentation

- **Every blue (hardcoded) cell** must have a cell comment in the form:
  `Source: [System/Document], [Date], [Reference], [URL if applicable]`
- **Master assumption values** (Rf, ERP) should cite this file:
  `Source: docs/financial-model-assumptions.md §1.1 (2026-05-22 update)`

---

## 6. Update Log

| Date | Change | Reason |
|---|---|---|
| 2026-05-26 | Default beta set to 1.00 (override = company-specific, documented opt-in) | Resolution of 2026-05-26 memo §5 item 1: cross-model comparability requires uniform beta |
| 2026-05-26 | Added non-USD Rf table (VND, EUR, GBP, JPY, SGD, CNY, INR) + CRP guidance | Resolution of 2026-05-26 memo §5 item 2: BUS-629 needs Vietnam Rf in spec |
| 2026-05-26 | Added "Refresh Mechanism" subsection under Effective Dates | Resolution of 2026-05-26 memo §5 item 3: cadence needed an explicit trigger |
| 2026-05-24 | Add "Accounting Basis" mandatory disclosure section | Cross-standard comparability per 2026-05-24 conversion framework decision |
| 2026-05-23 | Initial version | Establish institutional house view for cross-model consistency |

---

## 7. How to Use This File (for Claude / analysts)

1. **At the start of any financial model build**, open this file and locate the relevant section.
2. **Before hardcoding Rf, ERP, or any value listed here**, check whether it appears in this file. If yes, use the value here and cite this file in the cell comment.
3. **If you need to deviate** (e.g., a foreign-currency DCF, a pre-revenue company), document the deviation explicitly in the model's notes/cover sheet.
4. **If a value here is stale** (older than its update cadence), update the value, bump the "Last Updated" date, and add an entry to the Update Log — don't quietly use a fresher value without updating the file.
