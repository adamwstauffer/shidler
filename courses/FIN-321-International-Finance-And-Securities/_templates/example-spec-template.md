<div style="border-top: 6px solid #024731; border-bottom: 1px solid #B2B2B2; padding: 12px 0; margin-bottom: 24px; font-family: 'Open Sans', Helvetica, Arial, sans-serif;">
  <div style="color: #024731; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; font-size: 0.85rem;">University of Hawaiʻi at Mānoa · Shidler College of Business</div>
  <div style="color: #000000; font-weight: 700; font-size: 1.25rem; margin-top: 4px;">FIN-321 International Finance &amp; Securities</div>
  <div style="color: #525252; font-weight: 400; font-size: 0.95rem;">FX Transaction Hedging Project — Technical Specification</div>
</div>

<!--
BRAND FORMATTING — applied per docs/_branding/design.json (v1.0.0)
  ┌─ Colors ─────────────────────────────────────────────────────────────┐
  │ Primary green ........... #024731  RGB 2,71,49    Pantone 3435 C     │
  │ Primary black ........... #000000  RGB 0,0,0      Process Black      │
  │ Silver (secondary) ...... #B2B2B2  RGB 178,178,178 Cool Gray 5 C     │
  │ White (secondary) ....... #FFFFFF                                    │
  │ Neutral-600 (muted) ..... #525252  (secondary text, captions)        │
  │ UH-green 700 (hover) .... #013D26  (link hover, pressed state)       │
  │ UH-green 50 (tint) ...... #E6F2EF  (callout backgrounds)             │
  │ Yellow (Excel only) ..... #FFFF00  (input highlight — not brand)     │
  ├─ Typography ─────────────────────────────────────────────────────────┤
  │ Headings (web)  .......... Open Sans Bold (H1/H2) / Semibold (H3/H4) │
  │ Headings (print)  ........ Avenir Bold                               │
  │ Body (web)  .............. Open Sans Regular                         │
  │ Body (print)  ............ Avenir Book                               │
  │ Fallback stack  .......... Helvetica, Arial, sans-serif              │
  │ Monospace  ............... Consolas / ui-monospace                   │
  │ Body minimum size  ....... 10 pt (11–12 pt preferred for print)      │
  │ Leading  ................. 3–5 pt greater than type size (print)     │
  │ Alignment  ............... Flush left, ragged right                  │
  ├─ Accessibility ──────────────────────────────────────────────────────┤
  │ • ADA-compliant contrast ratios for ALL text and UI elements         │
  │ • No red body type                                                   │
  │ • No layouts that are too dark for readability                       │
  │ • No custom palettes or gradients outside the official brand         │
  └──────────────────────────────────────────────────────────────────────┘
  Full brand standard: docs/_branding/design.json · Source: https://manoa.hawaii.edu/brand/
-->

# [COMPANY NAME] — FX Transaction Hedge Model · Technical Specification

> <span style="color:#024731; font-weight:700;">Post-build specification</span> documenting the Stage 2 Excel hedge model, validating it against the scenario data, and articulating the refinements required for a production-grade version. Drives the Stage 4 AI prompt and final analysis.

| Field | Value |
|------|------|
| **Created by** | [name] |
| **Updated by** | [name] |
| **Date Created** | [YYYY-MM-DD] |
| **Date Updated** | [YYYY-MM-DD] |
| **Version** | [0.0] |
| **LLM Used** (optional) | [LLM name and how it was used] |
| **Role** | Treasury Analyst / FP&A Analyst |
| **Audience** | CFO / Director of Treasury |
| **Companion Workbook** | `excel-template/FIN 321 - Chapter 8 Transaction Hedging_2026_Stauffer_template.xlsx` (or student build) |

---

## 1. Problem Statement

Briefly restate the exposure, timing, and objective in professional terms (3–5 sentences).

<details>
<summary><span style="color:#024731; font-weight:600;">Example phrasing (Receivable)</span></summary>

> [Company] expects a [FC amount] receivable denominated in [EUR/GBP/JPY] settling in [T] days. A [depreciation/appreciation] in [currency pair] over that horizon would reduce realized USD proceeds and compress [gross margin / earnings / cash-flow coverage]. This specification documents the analytical framework used to quantify and compare four strategies — **no hedge**, **forward hedge**, **money-market hedge**, and **option (put) hedge** — and to produce the sensitivity evidence that supports the Stage 4 hedging recommendation.
</details>

**Include:**
- Exposure type (receivable or payable) and functional currency
- Foreign-currency amount, quote convention (USD per FC), settlement date
- Objective (protect USD value, preserve upside, minimize premium cost, etc.)
- Decision context (corporate treasury, business unit, board-approved policy)

---

## 2. Inputs (Known Variables)

All inputs should be exposed as workbook **named ranges** so Calculation Flow (§4) reads the same whether implemented in Excel, Python, or an AI prompt. Dates, sources, and access timestamps are recorded in the Notes tab. Market inputs (spot, forward, rates, premia) are the only cells an analyst should adjust for scenario work.

> <span style="color:#024731;">**Naming-convention decoder.**</span> The Stage 3 assignment prescribes a **standardized set of names** (left column below). The existing Stauffer template uses **legacy names** (right column) — these should be retired in the production build in favor of the standardized names. Where both are in use, define the legacy name as an alias pointing to the same cell.

### 2.1 Core Inputs

| Standardized Name | Description | Unit | Legacy Name (template) | Example |
|-------------------|-------------|------|------------------------|--------:|
| `FC_AMT` | Foreign-currency notional (receivable or payable) | FC | `recievable` *(sic)* / `contract_notional_value_payable` | 10,000,000 GBP |
| `S0_in` | Spot exchange rate at inception | USD per FC | `current_spot_price_payable` *(payable only)* | 1.4600 |
| `F0_in` | Forward rate to settlement | USD per FC | `for_GBPUSD` / `forward_price_payable` | 1.4400 |
| `R_USD` | USD interest rate to settlement | Annual % | `rate_us_1y_payable` | 6.00% |
| `R_FC` | Foreign-currency interest rate to settlement | Annual % | `rate_uk_1y_payable` | 6.50% |
| `T_DAYS` | Days to settlement | Days | *(implicit = 365)* | 365 |
| `K_PUT` | Put option strike (receivables) | USD per FC | `x_put` | 1.4600 |
| `K_CALL` | Call option strike (payables) | USD per FC | `call_strike` | 1.8000 |
| `PREM_PUT` | Put premium, USD per 1 FC | USD | `put_price` | 0.015 |
| `PREM_CALL` | Call premium, USD per 1 FC | USD | `call_price` | 0.010 |

### 2.2 Derived / Intermediate Values

| Name | Description | Source |
|------|-------------|--------|
| `FV_PREM_PUT` | Future value of put premium at settlement | `−PREM_PUT × FC_AMT × (1 + R_USD × T_DAYS/360)` *(legacy: `fv_put_outlay`)* |
| `FV_PREM_CALL` | Future value of call premium at settlement | `−PREM_CALL × FC_AMT × (1 + R_USD × T_DAYS/360)` |
| `S_T_grid` | Sensitivity spot grid at settlement | Built from `S0_in` ± 5% in 1% steps *(legacy: `gbpusd_1y_scenario`, `future_spot_price_payable`)* |
| `USD_NO_HEDGE` | USD proceeds / outlay under no hedge | `S_T × FC_AMT` *(legacy: `hedge_no`)* |

> <span style="color:#024731;">**Tip:**</span> Keep labels short and standardized — these names become Excel named ranges *and* the AI prompt parameters in Stage 4. Typos carried forward from a student build (e.g., `recievable`) should be corrected at the start of Stage 3.

---

## 3. Assumptions & Constraints

State every convention used. Clarity here is what makes the model reproducible.

- **Quote convention:** All rates expressed as **USD per unit of foreign currency** (e.g., USD/GBP, USD/EUR). A higher quote means FC appreciation.
- **Horizon:** Single-maturity model; `T_DAYS = 365` unless otherwise noted. Templates assume a 1-year tenor.
- **Day-count basis:** Interest applied on a **simple-annual (ACT/360)** basis as `r × T_DAYS/360`. For the default 1-year case this collapses to `(1 + r)`; the day-count factor must be made explicit before any sub-annual tenor is introduced.
- **Parity:** Money-market hedge is assumed to replicate the forward hedge under covered interest-rate parity; any gap is a test of parity, not a model error.
- **Option premium:** Paid upfront in USD, quoted per 1 unit of FC (no contract multiplier). Premia are expressed as a **negative cash flow** at t₀ and carried forward at `R_USD` to put them on the same footing as the settlement-date USD proceeds.
- **Counterparty / credit risk:** Excluded. All derivatives assumed frictionless and creditworthy.
- **Transaction costs & bid-ask spreads:** Excluded from the base case. Flagged as a sensitivity candidate in §6.
- **Tax / accounting treatment:** Excluded. Model reports pre-tax cash outcomes only.
- **Scenario construction:** Future spot `S_T` is varied deterministically across a grid; no probability weights and no implied-volatility distribution are applied.

---

## 4. Calculation Flow

Described in named-range pseudocode so the logic is portable across Excel, Python, and AI prompts. Formulas are written for a **receivable** exposure; §4.4 shows the sign flips required for a payable.

### Step 1 — Derived inputs

1. `DF_USD` = `1 + R_USD × T_DAYS / 360`
2. `DF_FC` = `1 + R_FC × T_DAYS / 360`
3. `FV_PREM_PUT` = `−PREM_PUT × FC_AMT × DF_USD`
4. `FV_PREM_CALL` = `−PREM_CALL × FC_AMT × DF_USD`

### Step 2 — Forward hedge (certainty benchmark)

- `USD_FWD` = `FC_AMT × F0_in`
- Locked-in at t₀; invariant across the `S_T` grid.

### Step 3 — Money-market hedge (parity check)

1. Borrow `FC_AMT / DF_FC` foreign currency today *(the discounted PV of the receivable)*.
2. Convert to USD at the spot rate: `(FC_AMT / DF_FC) × S0_in`.
3. Invest the USD to maturity: `USD_MM` = `(FC_AMT / DF_FC) × S0_in × DF_USD`.
4. At maturity, the FC receivable repays the foreign borrowing exactly — so the USD deposit is the locked-in proceed.

> **Parity check:** `USD_MM ≈ USD_FWD` within rounding. A persistent gap indicates a violation of covered interest-rate parity in the quoted inputs.

### Step 4 — Option hedge (floor with upside)

Put-and-hold strategy on the receivable:

- Pay `PREM_PUT × FC_AMT` USD today for a put on FC with strike `K_PUT`.
- At settlement, for each `S_T` on the grid:
  - `USD_PUT(S_T)` = `S_T × FC_AMT` + `MAX(0, (K_PUT − S_T) × FC_AMT)` + `FV_PREM_PUT`
  - Equivalently: `MAX(S_T, K_PUT) × FC_AMT + FV_PREM_PUT`

### Step 5 — Sensitivity table (rows of the grid)

For each `S_T` in `S_T_grid`:

| Column | Output | Formula |
|--------|--------|---------|
| No hedge | `USD_NO_HEDGE(S_T)` | `S_T × FC_AMT` |
| Forward | `USD_FWD` | constant across rows |
| Money market | `USD_MM` | constant across rows |
| Option (put) | `USD_PUT(S_T)` | `MAX(S_T, K_PUT) × FC_AMT + FV_PREM_PUT` |
| Winner vs. no hedge | label | `ARGMAX(USD_NO_HEDGE, USD_FWD, USD_MM, USD_PUT)` |
| Best active hedge | label | `ARGMAX(USD_FWD, USD_MM, USD_PUT)` |

### Step 6 — Summary metrics

- `USD_FLOOR_PUT` = `MIN(USD_PUT) across S_T_grid` *(worst-case put outcome on the grid — legacy cell `F29`)*
- `USD_BASE` = outcomes evaluated at `S_T = S0_in` *(the "baseline" row)*
- `HEDGE_PROFIT_k` = `USD_k − USD_NO_HEDGE` for k ∈ {forward, money market, option}

### 4.4 Payable variant (sign flips)

For a payable of `FC_AMT` to be settled in FC at maturity, the model mirrors §4.2–§4.5 with three substitutions: (a) **buy** the forward instead of sell, (b) **borrow USD today, invest in FC** for the money-market leg, and (c) use a **call on FC** with strike `K_CALL` and premium `PREM_CALL`. The sensitivity winner is the strategy that **minimizes** USD outlay at each `S_T`, not the one that maximizes it.

---

## 5. Outputs

| Output | Description | Format | Purpose |
|--------|-------------|--------|---------|
| Input panel | All named-range inputs with units, sources, and access dates | Top of each tab | Single source of truth |
| Strategy summary | `USD_FWD`, `USD_MM`, `USD_FLOOR_PUT`, `USD_BASE` per strategy | Table above sensitivity grid | Executive at-a-glance |
| Sensitivity table | USD proceeds / outlay for each strategy across `S_T_grid` ± 5% | Table on each tab | Core analytical evidence |
| Hedge-profit columns | `USD_k − USD_NO_HEDGE` for each strategy per row | Sub-table | Isolates hedge value-add |
| Winner / best-hedge labels | `ARGMAX` / `ARGMIN` labels per row | Two label columns | Quick-read decision cue |
| Sensitivity chart | Line chart of USD outcome vs. `S_T` for all four strategies | Embedded chart | Visual comparison |
| Executive summary (Stage 4) | 1–2 paragraph narrative with explicit recommendation | Separate memo | Downstream deliverable |

### 5.1 Computed Base-Case Values

Record the base-case outcome at `S_T = S0_in` once the model is built. This block serves as a regression checkpoint for the refined Stage 4 version.

| Strategy | USD Proceeds (Receivable) | USD Outlay (Payable) | Hedge Profit vs. No Hedge |
|----------|--------------------------:|---------------------:|--------------------------:|
| No hedge | | | — |
| Forward | | | |
| Money market | | | |
| Option (put / call) | | | |

---

## 6. Model Review — What Worked & What to Improve

Reflect candidly on the Stage 2 model. This section is what makes a *post-build* spec more valuable than a pre-build plan.

### 6.1 What Worked

- **Four-strategy comparison on one canvas.** No hedge, forward, money market, and option are all priced against the same `S_T` grid, which makes the trade-off inspection immediate.
- **Winner / best-hedge labels per row.** Columns K and L in the template return the dominant strategy at each scenario — a good UX for a non-quant reader.
- **Put payoff vectorized across the grid.** Option column applies `MAX(0, (K − S_T) × FC_AMT)` for every scenario, so the put payoff curve can be read directly.
- **Baseline marker at `S_T = S0_in`.** The `<-- baseline` annotation anchors the scenario range in a recognizable reference point.

### 6.2 What to Improve

- **Named-range discipline is incomplete.** On the receivable tab, only a subset of inputs (`recievable`, `for_GBPUSD`, `x_put`, `put_price`, `fv_put_outlay`, `gbpusd_1y_scenario`, `hedge_no`) have names; spot, US rate, and UK rate are still referenced as `$F$7`, `$F$9`, `$F$10`. **Fix:** add `S0_in`, `R_USD`, `R_FC`, `T_DAYS` and replace every hard cell reference.
- **Typo in a named range.** `recievable` should be `receivable` (or the standardized `FC_AMT`). Migrate and delete the old name.
- **Inconsistent references inside the sensitivity grid.** On the receivable tab, `G33 = hedge_no + J33` uses implicit intersection, but `G34:G45 = $D34 + J34` uses direct relative references. **Fix:** use `$D33 + J33` in all rows so the formula is uniform and implicit-intersection-free.
- **Named-range implicit intersection is fragile.** `gbpusd_1y_scenario` and `future_spot_price_payable` resolve to single cells only because Excel applies implicit intersection against the current row. Replace with explicit `$C33` references, or convert the grid to a dynamic-array `LET`/`BYROW` formulation.
- **Strike-price defaulting is inconsistent.** Payable tab anchors `K_CALL = S0_in`; receivable tab leaves `K_PUT` blank. **Fix:** default both strikes to `S0_in` and expose an override.
- **Sensitivity step size is hard-coded and unequal across tabs.** Receivable tab increments spot by 0.01 (small); payable tab by 0.05 (large). **Fix:** drive the grid off a single `STEP_FRAC` input (e.g., 1%) so `S_T_grid = S0_in × (1 + n × STEP_FRAC)` for `n = −5…+5`, giving a consistent ±5% range on both tabs.
- **Option summary cell is a "floor," not a "baseline."** `F29 = MIN(G33:G45)` reports the worst-case put outcome. Add a second cell that reports the put outcome at `S_T = S0_in` so the strategy-summary block shows both a **baseline** and a **floor**.
- **Day-count is implicit.** The `(1 + r)` formulation assumes 1-year simple interest. **Fix:** introduce `T_DAYS` and a `BASIS` toggle (360 vs. 365) so the model is reusable at non-annual tenors.
- **No chart is included.** The sensitivity grid is tabular only. **Fix:** add a line chart (USD outcome vs. `S_T`, one series per strategy) on each tab.
- **Money-market walk on the payable tab is longer than it needs to be** (five steps F21:F25, with a partial round-trip through FC). The textbook form is a two-step: (i) `USD_borrow = FC_AMT × S0 / DF_FC` today, (ii) `USD_MM = USD_borrow × DF_USD` at maturity. **Fix:** collapse to the two-step form and keep the longer walk as a commented audit trail only.
- **Transaction-cost sensitivity absent.** Add a bid-ask / commission knob on the forward and a spread on the option premium; real treasury desks never see the mid.

### 6.3 Auditability Checklist

- [ ] Every input has a standardized named range from §2.1
- [ ] Every formula in §4 uses named ranges — no bare `$F$n` references
- [ ] Money-market hedge ties to forward hedge within 0.05% (parity check)
- [ ] Put payoff at `S_T = K_PUT` equals `K_PUT × FC_AMT + FV_PREM_PUT` (kink verification)
- [ ] Sensitivity grid is symmetric around `S_T = S0_in` and driven by `STEP_FRAC`
- [ ] Notes tab records spot / forward / rate sources with access dates
- [ ] Cell colors match the legend: <span style="background:#FFFF00;">yellow</span> inputs, <span style="color:#0000FF;">blue</span> assumptions, black formulas, <span style="color:#024731;">green</span> cross-tab links

---

## 7. Sensitivity Plan

- **Grid:** `S_T_grid` spans `S0_in × (1 ± 5%)` in 1% increments → 11 rows (including the baseline).
- **Strategies plotted:** no hedge, forward, money market, option (put for receivable / call for payable).
- **Primary chart:** line chart with `S_T` on the x-axis and USD proceeds (or outlay) on the y-axis. Forward and money-market series are horizontal by construction; no-hedge is a straight line through the origin; option is piecewise-linear with a kink at the strike.
- **Secondary table:** hedge profit vs. no hedge for each strategy, to make the visual intuition numeric.
- **What the chart should communicate:** the trade-off between **certainty** (forward / money-market, flat lines), **optionality** (put / call, kinked payoff), and **naked exposure** (no hedge, unbounded on both sides).

---

## 8. Limitations & Next Steps

**Limitations.** This specification does not incorporate:
- Partial / layered / dynamic hedging (treated as static, full-notional hedge at t₀)
- Credit, counterparty, and settlement risk
- Implied-volatility-based option pricing (premia are scenario inputs, not Black-Scholes outputs)
- Accounting treatment (ASC 815 / IFRS 9 hedge accounting designation)
- Multi-currency or multi-horizon portfolio effects

**Next steps — Stage 4 will:** (a) translate the sensitivity evidence into a structured CFO recommendation memo, (b) formalize the AI prompt using §4 as the instruction block and §6.2 as the improvement brief, and (c) implement at least one of the §6.2 improvements (default priority: standardized named ranges + chart).

---

## 9. Writing a Strong Specification

> <span style="color:#024731; font-weight:600;">The spec should read like a handoff document, not a lab notebook.</span>

- **Communicate like a professional:** clear, structured, no filler.
- **Think one stage ahead:** the spec feeds directly into the Stage 4 AI prompt and recommendation memo.
- **Be internally consistent:** variables, labels, and steps must align with the actual workbook.
- **Be reproducible:** another treasury analyst — or an AI — should be able to rebuild the model from this spec alone.
- **Be reflective:** §6 should show honest post-build assessment, not self-congratulation.
- **Be executive-relevant:** the CFO should understand *what was built* and *why it matters* for the hedging decision.

---

## 10. How This Sets Up Stage 4

| What's Written in Stage 3 | What It Enables in Stage 4 |
|---------------------------|----------------------------|
| Standardized named ranges with precise definitions | AI uses standardized variable names; no improvisation |
| Step-by-step calculation flow | AI generates correct, auditable hedge formulas |
| Model review and improvement notes (§6.2) | AI builds the *improved* version, not just a replica |
| Explicit output requirements + chart spec | AI produces the exact tables, chart, and memo sections needed |
| Base-case output values (§5.1) | Regression checkpoints for the refined model |

---

## Appendix A — Change Log

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | [YYYY-MM-DD] | [name] | Initial post-build draft |
|  |  |  |  |

---

## Appendix B — Brand & Formatting Standards

All FIN-321 deliverables — this spec, the companion workbook, the Stage 4 memo, and any derivative chart or slide — must conform to the **University of Hawaiʻi at Mānoa Brand Style Guide** as codified in [`docs/_branding/design.json`](../../../docs/_branding/design.json) (v1.0.0). The tokens below are a reader-friendly extract; the JSON file is the source of truth.

### B.1 Color Palette

**Primary colors — logos, headings, accents. Do not substitute.**

| Token | Hex | RGB | CMYK | Pantone | Usage |
|-------|-----|-----|------|---------|-------|
| <span style="display:inline-block; width:12px; height:12px; background:#024731; border:1px solid #000; vertical-align:middle;"></span> UH Green | `#024731` | 2, 71, 49 | 93, 24, 85, 68 | 3435 C | Logos, H1/H2, key UI accents, primary buttons |
| <span style="display:inline-block; width:12px; height:12px; background:#000000; border:1px solid #B2B2B2; vertical-align:middle;"></span> Black | `#000000` | 0, 0, 0 | 0, 0, 0, 100 | Process Black | Body text, borders, maximum-contrast UI |

**Secondary colors — borders, muted elements, backgrounds.**

| Token | Hex | RGB | Pantone | Usage |
|-------|-----|-----|---------|-------|
| <span style="display:inline-block; width:12px; height:12px; background:#B2B2B2; border:1px solid #000; vertical-align:middle;"></span> Silver | `#B2B2B2` | 178, 178, 178 | Cool Gray 5 C | Subtle borders, rules, disabled states |
| <span style="display:inline-block; width:12px; height:12px; background:#FFFFFF; border:1px solid #B2B2B2; vertical-align:middle;"></span> White | `#FFFFFF` | 255, 255, 255 | — | Page backgrounds, inverse text, cards |

**Extended light-mode tokens (for tables, callouts, footnotes).**

| Purpose | Token | Hex |
|---------|-------|----:|
| Secondary text / captions | Neutral-600 | `#525252` |
| Tertiary text | Neutral-500 | `#737373` |
| Hover / pressed state | UH Green 700 | `#013D26` |
| Link text | Light-mode link | `#024731` |
| Tint / callout fill | UH Green 50 | `#E6F2EF` |
| Table border (subtle) | Neutral-200 | `#E5E5E5` |

**Status colors (informational banners only — never for body text).**

| State | Text | Background | Solid |
|-------|-----:|-----------:|------:|
| Success / Info | `#024731` | `rgba(2, 71, 49, 0.08–0.12)` | `#024731` |
| Warning | `#737373` | `rgba(178, 178, 178, 0.20)` | `#B2B2B2` |
| Error | `#B43232` | `rgba(180, 50, 50, 0.12)` | `#8B2727` |

> <span style="color:#024731; font-weight:600;">Prohibited:</span> custom palettes, gradients, red body type, non-ADA contrast combinations, or layouts too dark for print legibility. If a color is not in this appendix or `design.json`, it is not brand.

### B.2 Typography

| Element | Web (screen) | Print | Fallback | Weight |
|---------|--------------|-------|----------|-------:|
| H1 / H2 | Open Sans Bold | Avenir Bold | Helvetica, Arial | 700 |
| H3 / H4 | Open Sans Semibold | Avenir Bold | Helvetica, Arial | 600 |
| Body | Open Sans Regular | Avenir Book | Helvetica, Arial | 400 |
| Caption / footnote | Open Sans Regular | Avenir Book | Helvetica, Arial | 400 |
| Monospace (formulas, named ranges, code) | `ui-monospace` | Consolas | monospace | 400 |

**Sizing & setting rules:**

- Body type minimum **10 pt**; use **11–12 pt** for any printed copy intended for faculty, committees, or older audiences.
- **Leading** (line-height): 3–5 pt greater than type size on printed copy.
- **Alignment:** flush left, ragged right for body copy. Never center or fully justify body text.
- **Headlines:** Avenir Bold in ALL CAPS for emphasis, or sentence case for restrained look. Pick one and stay consistent within a deliverable.

### B.3 Applying the Palette in the Workbook

Excel is not a brand canvas, but it must still respect the palette. Use the color coding below — these apply to cell text/fill and match the `bus314` sibling skill's conventions.

| Element | Color | Hex | Notes |
|---------|-------|----:|-------|
| Section headings & banners (Input / Sensitivity / Outputs) | UH Green | `#024731` | Bold, 12 pt |
| Input cells (editable by analyst) | <span style="background:#FFFF00;">Yellow fill</span> | `#FFFF00` | Standard-industry input color; flagged as **Excel-only** — not a brand color |
| Assumption cells (analyst scenario knobs) | <span style="color:#0000FF;">Blue text</span> | `#0000FF` | Standard-industry hardcode color |
| Formula cells | Black text | `#000000` | All calculations |
| Cross-tab links | <span style="color:#024731;">UH Green text</span> | `#024731` | Mirrors brand primary |
| External links (e.g., Bloomberg pulls) | <span style="color:#B43232;">Dark red text</span> | `#B43232` | Used sparingly; never for commentary |
| Table gridlines / separators | Silver | `#B2B2B2` | 0.5 pt |
| Header row fill | UH Green | `#024731` | White text |

**Workbook typography:** set the workbook default font to **Open Sans** (fall back to Arial where Open Sans is unavailable). Do not use Calibri.

### B.4 Charts (Sensitivity Line Chart — §7)

| Series | Line color | Style | Weight |
|--------|-----------:|-------|-------:|
| No hedge | `#000000` (Black) | Solid | 1.5 pt |
| Forward hedge | `#024731` (UH Green) | Solid | 2.0 pt |
| Money-market hedge | `#013D26` (UH Green 700) | Dashed | 1.5 pt |
| Option hedge | `#525252` (Neutral-600) | Dotted | 2.0 pt |

- **Gridlines:** Silver `#B2B2B2`, 0.5 pt, horizontal only.
- **Axis labels & title:** Open Sans Semibold, black, 10 pt minimum.
- **Legend:** top or right, Open Sans Regular, 10 pt.
- **No 3-D effects, no drop shadows, no gradient fills.**

### B.5 Accessibility & Prohibited Practices

Derived directly from `design.json → accessibility`:

- Every text / background combination must clear **ADA AA contrast** (4.5:1 for body, 3:1 for large text). Check UH Green on white (✓ 11.5:1) and UH Green on silver (✗ 2.1:1 — do not use).
- **Never** use red type for body or primary content. Dark red `#B43232` is permitted only for error-state banners and external-link markers in the workbook.
- **Never** layer body copy on dark backgrounds — dark-mode tokens are reserved for digital product UI, not print or PDF deliverables.
- **Never** introduce custom palettes, gradients, or alternative brand marks. If a need arises, escalate via the UH Mānoa Branding and Marketing Office (`branding@hawaii.edu`, `(808) 956-3598`).

### B.6 File & Deliverable Conventions

- **Spec file name:** `stage3-spec-LASTNAME.md` (Stage 3 assignment requirement).
- **Workbook file name:** keep the Stauffer template's convention — `FIN 321 - Chapter 8 Transaction Hedging_[YEAR]_LASTNAME.xlsx`.
- **PDF export of the spec:** embed fonts; render at Letter size; margins ≥ 0.75 inch; body 11–12 pt.
- **All files** must carry the UH Mānoa banner block (see top of this template) and the brand footer (below).

---

<div style="border-top: 1px solid #B2B2B2; padding-top: 8px; margin-top: 24px; font-family: 'Open Sans', Helvetica, Arial, sans-serif; font-size: 0.8rem; color: #525252;">
  Prepared per UH Mānoa brand standards (<code>docs/_branding/design.json</code> v1.0.0). Primary green <span style="display:inline-block; width:10px; height:10px; background:#024731; border:1px solid #000;"></span> <code>#024731</code> · Black <span style="display:inline-block; width:10px; height:10px; background:#000000; border:1px solid #B2B2B2;"></span> <code>#000000</code> · Silver <span style="display:inline-block; width:10px; height:10px; background:#B2B2B2; border:1px solid #000;"></span> <code>#B2B2B2</code> · Body type Open Sans Regular, 11–12 pt for printed copies · ADA-compliant contrast · Flush-left, ragged-right alignment · No red body type · No custom palettes or gradients.
</div>
