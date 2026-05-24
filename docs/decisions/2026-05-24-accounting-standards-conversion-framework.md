# ACCOUNTING STANDARDS CONVERSION FRAMEWORK — IFRS / SFRS / US GAAP & INTERNATIONAL METHODS

## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** May 24, 2026
**Status:** Draft — Pending Review
**Scope:** Cross-cutting — applies to BUS-314 (Accounting Ratios), FIN-321 (FX Hedging), BUS-629 (International Corporate Finance), and any future valuation or financial-modeling work in the Shidler portfolio.

---

## 1. SUMMARY

When students analyze non-US companies — or when instructor-built models compare firms across jurisdictions — the financial statements they encounter may be prepared under IFRS, SFRS, Chinese GAAP, Japanese GAAP, Indian Accounting Standards, or one of dozens of other national frameworks. Ratios, multiples, and valuation outputs are only meaningful if the underlying financials are on a comparable basis, and currently none of our project rubrics or model templates address how to handle cross-standard inputs.

This memo proposes a **conversion-aware modeling standard**: a documented hierarchy of adjustment methods, a mapping of the most impactful IFRS-to-US-GAAP differences (and vice versa), a survey of major international accounting regimes, and practical guidance for when full conversion is warranted versus when disclosure-plus-footnote is sufficient. The goal is not to turn undergrads into GAAP conversion specialists but to ensure that when a student pulls IFRS financials into a US-GAAP-denominated comps set, the rubric and the model both acknowledge the gap.

---

## 2. WHY THIS MATTERS NOW

Three forces converge:

1. **BUS-629 (Vietnam EMBA).** Students are analyzing Vietnamese firms that report under Vietnamese Accounting Standards (VAS), which are partially converged with IFRS but retain significant local departures. The BUS-629 M&A and valuation exercises will break if students treat VAS line items as US-GAAP equivalents.

2. **BUS-314 Accounting Ratios.** The 25+ ratio workbook assumes a US-GAAP input structure (BAL_, INC_, CASH_ named ranges). When students choose a non-US company — which the project brief permits — the mapping from IFRS line items to those named ranges is non-trivial (e.g., IFRS "other comprehensive income" classification, lease treatment, revenue recognition timing).

3. **Financial-analysis plugins.** The `comps-analysis`, `dcf-model`, and `3-statement-model` skills pull data that may be IFRS-sourced. Without a conversion policy, plugin outputs mix standards silently.

---

## 3. THE MAJOR ACCOUNTING FRAMEWORKS

### 3.1 US GAAP (ASC / FASB)

- **Jurisdiction:** United States (SEC registrants required; private companies may use GAAP or elect alternatives).
- **Standard-setter:** Financial Accounting Standards Board (FASB); codified in the Accounting Standards Codification (ASC).
- **Philosophy:** Rules-based. Detailed, prescriptive guidance with bright-line thresholds (e.g., ASC 842 lease classification tests, ASC 606 five-step revenue model). Extensive industry-specific guidance.
- **Strengths:** Consistency and comparability within the US market; reduced preparer judgment; deep precedent library.
- **Weaknesses:** Complexity and volume (~90,000 pages of codification); bright-line rules invite structuring to hit thresholds; limited flexibility for emerging transaction types.

### 3.2 IFRS (IASB)

- **Jurisdiction:** Required or permitted in 140+ countries including the EU, UK, Canada, Australia, Brazil, South Korea, and most of Africa and the Middle East.
- **Standard-setter:** International Accounting Standards Board (IASB); standards are IAS (legacy) and IFRS (current).
- **Philosophy:** Principles-based. Emphasizes substance over form; fewer bright-line tests; more reliance on professional judgment and "faithful representation."
- **Strengths:** Global comparability across jurisdictions; adaptable to novel transactions; shorter standards (relatively).
- **Weaknesses:** Judgment-dependent outcomes vary across preparers and auditors; less guidance for edge cases; IFRS-for-SMEs is a separate, simplified framework that doesn't map 1:1 to full IFRS.

### 3.3 SFRS (Singapore)

- **Jurisdiction:** Singapore (all companies incorporated or listed in Singapore).
- **Standard-setter:** Accounting Standards Council (ASC-SG); standards designated SFRS(I) for IFRS-identical standards.
- **Convergence status:** **Fully converged with IFRS** since January 1, 2018 (SFRS(I) framework). Pre-2018 Singapore FRS had minor local carve-outs; post-2018, SFRS(I) is word-for-word identical to IFRS with the same effective dates.
- **Practical implication:** For modeling purposes, SFRS(I) statements can be treated as IFRS statements. No conversion adjustments are required — the mapping is 1:1. Legacy SFRS (pre-2018) financials may have minor divergences in property revaluation treatment and government grant accounting, but these are rare in current filings.

### 3.4 Chinese Accounting Standards (CAS / ASBE)

- **Jurisdiction:** People's Republic of China (all listed companies since 2007; state-owned enterprises earlier).
- **Standard-setter:** Ministry of Finance (MoF); standards are Accounting Standards for Business Enterprises (ASBE).
- **Convergence status:** **Substantially converged with IFRS** in principle since the 2006 overhaul, but with critical local departures:
  - **Government grants:** CAS 16 allows recognition as deferred income or offset against asset cost — IFRS (IAS 20) permits both, but the default presentation differs.
  - **Business combinations under common control:** CAS uses predecessor/pooling-of-interests method; IFRS has no explicit standard (practice varies); US GAAP uses carryover basis.
  - **Fair value measurement:** CAS 39 mirrors IFRS 13 in structure but application is more conservative in practice; Chinese preparers and auditors tend to use cost or cost-less-impairment where IFRS firms would elect fair value.
  - **Related-party transactions:** Broader disclosure requirements reflecting SOE ownership structures.
  - **Revenue recognition:** CAS 14 (revised 2017) is aligned with IFRS 15, but enforcement rigor and interpretive guidance lag.
- **Key risk for models:** Dual-listed Chinese firms (A-shares + H-shares) may report under CAS domestically and IFRS for Hong Kong listing — the two sets of financials will differ, sometimes materially, for the same company and period.

### 3.5 Japanese GAAP (JGAAP)

- **Jurisdiction:** Japan (domestic-only listed companies; international-listed may use IFRS or US GAAP).
- **Standard-setter:** Accounting Standards Board of Japan (ASBJ).
- **Convergence status:** **Partially converged** — Japan adopted a "convergence rather than adoption" approach. Key remaining differences:
  - **Goodwill:** JGAAP amortizes goodwill over its useful life (max 20 years); IFRS impairment-only (IAS 36); US GAAP impairment-only (ASC 350, post-2017).
  - **Development costs:** JGAAP expenses all R&D; IFRS capitalizes development costs meeting IAS 38 criteria; US GAAP expenses (with ASC 985 exception for software).
  - **Comprehensive income:** JGAAP historically lacked a comprehensive income statement; now permits it but does not require recycling of OCI items in the same sequence as IFRS.
  - **Retirement benefits:** Significant differences in discount-rate methodology, corridor approach (phasing out), and plan-asset recognition.
- **Adoption trend:** Japan introduced "Japan's Modified International Standards" (JMIS) in 2015 as a bridge — essentially IFRS with goodwill amortization and OCI recycling preserved. Uptake has been limited. As of 2025, ~270 Japanese listed companies voluntarily apply full IFRS (representing ~50% of market cap on TSE Prime).

### 3.6 Indian Accounting Standards (Ind AS)

- **Jurisdiction:** India (all listed companies and companies above INR 250 crore net worth since 2016–2017).
- **Standard-setter:** Ministry of Corporate Affairs (MCA) with input from ICAI; standards are Ind AS, numbered to parallel IFRS (e.g., Ind AS 115 = IFRS 15).
- **Convergence status:** **Converged with IFRS with carve-outs**:
  - **Ind AS 17/116 (Leases):** Fully aligned with IFRS 16 since April 2019.
  - **Ind AS 109 (Financial Instruments):** Includes a carve-out allowing reclassification of debt instruments from amortized cost to FVTPL without the "business model change" test required by IFRS 9 — a concession to Indian banking sector lobbying.
  - **Ind AS 103 (Business Combinations):** Includes a carve-out for bargain purchases — negative goodwill is recognized in OCI rather than immediately in P&L as IFRS 3 requires.
  - **Regulatory overlay:** The Reserve Bank of India (RBI) imposes additional provisioning requirements on banks that override Ind AS 109 expected-credit-loss model in some cases.
- **Practical note:** India has not adopted IFRS directly; Ind AS is a distinct framework. XBRL filings with the MCA use an India-specific taxonomy, so automated data pulls (FactSet, S&P Capital IQ) may map Ind AS fields to IFRS equivalents with footnoted adjustments.

### 3.7 Other Notable Frameworks

| Framework | Jurisdiction | IFRS Alignment | Key Divergence |
|---|---|---|---|
| **Korean IFRS (K-IFRS)** | South Korea | Fully adopted (2011) | None — identical to IFRS. Treat as IFRS for modeling. |
| **Brazilian GAAP (BR GAAP / CPC)** | Brazil | Fully converged (2010) | Inflation-adjustment legacy (hyperinflation accounting was standard pre-Real Plan); monetary correction items may appear in older comparatives. |
| **Vietnamese Accounting Standards (VAS)** | Vietnam | Partially converged | Significant gaps: no IFRS 9 (financial instruments), no IFRS 15 (revenue), no IFRS 16 (leases). Historical cost dominant. Roadmap to full IFRS adoption by 2025 has slipped — MoF now targets 2028 for listed companies. |
| **UK GAAP (FRS 102)** | United Kingdom | Partially converged | Simplified single standard for non-listed companies; close to IFRS-for-SMEs but with UK-specific exemptions. Listed UK companies use full IFRS. |
| **Saudi GAAP → IFRS** | Saudi Arabia | Fully adopted (2017) | Pre-2017 Saudi GAAP was a distinct framework with zakat-accounting requirements; post-2017, IFRS with SOCPA interpretive guidance on zakat overlay. |
| **OHADA** | 17 Francophone African countries | Low convergence | SYSCOHADA (2017 revision) is structurally different — balance-sheet-centric, no comprehensive income statement, unique chart of accounts. Requires full reconstruction for IFRS/US GAAP comparability. |

---

## 4. KEY CONVERSION DIFFERENCES: IFRS ↔ US GAAP

The following table catalogs the adjustments most likely to materially affect ratios, multiples, and valuations in our course projects. Items are ranked by typical dollar-magnitude impact on large-cap companies.

### 4.1 High-Impact Differences

| Area | IFRS Treatment | US GAAP Treatment | Conversion Adjustment | Impact on Ratios |
|---|---|---|---|---|
| **Leases (IFRS 16 vs. ASC 842)** | Single model: all leases are finance leases on the balance sheet. Straight-line depreciation + front-loaded interest on the liability. | Dual model: finance leases (front-loaded expense) and operating leases (straight-line single lease expense). Both on balance sheet post-ASC 842, but P&L treatment differs. | Reclassify US GAAP operating lease expense from a single line item into depreciation + interest components (or vice versa). Adjust EBITDA: under IFRS, lease depreciation is excluded from EBITDA, inflating it; under US GAAP operating-lease model, the full lease payment hits above EBITDA. | **EBITDA:** IFRS-reported EBITDA is higher by the amount of the operating-lease depreciation component. **Debt/EBITDA, EV/EBITDA:** materially affected for asset-heavy companies (airlines, retail, logistics). |
| **Revenue Recognition (IFRS 15 vs. ASC 606)** | Largely converged — both use a five-step model. Key difference: IFRS allows the "cost-to-cost" method for performance obligations satisfied over time with fewer prescriptive constraints; licensing guidance is less granular. | More prescriptive guidance on licensing (functional vs. symbolic IP), principal-vs-agent, bill-and-hold, and consignment. Industry-specific legacy guidance largely superseded but interpretive letters persist. | Usually minimal adjustment required. Where differences arise, they are in the timing of revenue recognition for IP licenses and multi-element arrangements — check footnote disclosures for method elected. | **Revenue growth rates, gross margins** for software/media/pharma companies with significant licensing revenue. |
| **Inventory (IAS 2 vs. ASC 330)** | LIFO is prohibited. Cost is measured at lower of cost and net realizable value (NRV). Reversal of inventory write-downs is permitted. | LIFO is permitted and widely used (especially in manufacturing, oil & gas, retail). Lower of cost or market (LCM) with ceiling/floor test. Write-down reversals are prohibited. | **LIFO → FIFO conversion:** Add the LIFO reserve (disclosed in US GAAP footnotes) back to inventory and retained earnings; adjust COGS by the change in LIFO reserve. **Write-down reversal:** Remove any IFRS write-down reversals from COGS and inventory when converting to US GAAP basis. | **Gross margin, inventory turnover, current ratio, ROA.** LIFO firms in inflationary environments report lower inventory, lower earnings, and lower taxes — conversion to FIFO increases all three. |
| **Development Costs (IAS 38 vs. ASC 730)** | Capitalize development costs if six criteria are met (technical feasibility, intent to complete, ability to use/sell, probable future economic benefits, adequate resources, reliable cost measurement). | Expense all R&D as incurred, except for software development costs under ASC 985-20 (after technological feasibility) and internal-use software under ASC 350-40. | **IFRS → US GAAP:** Expense capitalized development costs; reverse the intangible asset; add back amortization. **US GAAP → IFRS:** Identify costs meeting IAS 38 criteria; capitalize and amortize. Requires footnote detail or management estimates. | **R&D expense, operating income, total assets, ROA, asset turnover.** Capitalization inflates assets and earnings in early periods, then reverses as amortization catches up. |
| **Impairment (IAS 36 vs. ASC 350/360)** | Single-step test: compare carrying amount to recoverable amount (higher of fair value less costs of disposal and value in use). **Reversal of impairment losses is permitted** (except for goodwill). | Two-step test for long-lived assets (ASC 360): Step 1 recoverability test (undiscounted cash flows), then Step 2 fair value measurement if Step 1 fails. **No reversal of impairment losses.** Goodwill: qualitative screen then quantitative test (ASC 350). | **IFRS → US GAAP:** Remove any impairment reversals from the P&L and adjust asset balances. **US GAAP → IFRS:** Potentially recognize reversals if conditions are met — but this is a judgment call and rarely done in mechanical conversion. | **Asset values, depreciation/amortization, operating income.** Impairment reversals under IFRS can swing earnings materially in recovery years. |
| **Goodwill** | Not amortized (annual impairment test per IAS 36). **IASB tentatively decided in 2024 to reintroduce amortization** — exposure draft expected; not yet effective. | Not amortized (annual impairment test per ASC 350). Private companies may elect the accounting alternative to amortize over ≤10 years. | Currently no conversion adjustment needed for public companies. If IASB reintroduces amortization (expected effective date ~2027–2028), IFRS-reporting acquirers will have lower earnings and declining goodwill balances relative to US GAAP peers — a significant comps distortion. | **EPS, ROA, ROE, P/E** post-acquisition. |
| **Financial Instruments (IFRS 9 vs. ASC 326 / ASC 815)** | Three classification categories based on business model and cash-flow characteristics: amortized cost, FVOCI, FVTPL. Expected credit loss (ECL) model for impairment. Hedge accounting under IFRS 9 is more flexible than IAS 39 (which some entities still use for macro hedging). | Classification: HTM (amortized cost), AFS (FVOCI equivalent), trading (FVTPL). Current expected credit loss (CECL) model under ASC 326 — similar in concept to ECL but with implementation differences (lifetime expected loss from day one vs. IFRS's 12-month/lifetime staging). | Reclassification adjustments for instruments that fall into different categories under each framework. CECL vs. ECL differences primarily affect banks and financial institutions — CECL front-loads more provision. | **Provision expense, net income, CET1 (banks), allowance ratios.** CECL adoption caused US banks to increase loan-loss provisions 30-50% on day one. |
| **Pension / Post-employment (IAS 19 vs. ASC 715)** | Remeasurement gains/losses go directly to OCI and are **never recycled** to P&L. Past-service costs are recognized immediately in P&L. | Corridor approach was eliminated in 2018 — now similar to IFRS. But US GAAP permits delayed recognition of prior-service costs via amortization from AOCI. Net periodic pension cost has a specific multi-component structure. | Adjust for differences in amortization of prior-service costs and the treatment of the net pension asset/liability discount rate (IFRS uses high-quality corporate bond rate; US GAAP same in concept but precedent library differs). | **Operating income, OCI, leverage ratios** for companies with large defined-benefit plans (legacy industrials, airlines, utilities). |

### 4.2 Medium-Impact Differences

| Area | Key Difference | When It Matters |
|---|---|---|
| **Investment Property (IAS 40 ** vs. no equivalent) | IFRS permits fair-value model with gains/losses in P&L; US GAAP uses cost model. | REITs, property companies. IFRS-reporting REITs show volatile earnings from revaluation. |
| **Biological Assets (IAS 41)** | IFRS requires fair value less costs to sell; US GAAP has no equivalent standard — cost model typical. | Agriculture, forestry, wine/spirits. Relevant for BUS-122B (sustainable agriculture). |
| **Provisions / Contingent Liabilities (IAS 37 vs. ASC 450)** | IFRS recognizes at "more likely than not" (>50%); US GAAP at "probable" (interpreted as ~75-80%). IFRS discounts long-term provisions; US GAAP generally does not. | Litigation-heavy industries, environmental remediation, warranty-intensive companies. |
| **Extraordinary Items** | IFRS prohibits the concept; US GAAP eliminated it in 2015 (ASU 2015-01). | No longer a conversion issue for current filings; matters for historical comparatives pre-2015. |
| **Borrowing Costs (IAS 23 vs. ASC 835)** | Both require capitalization — converged. Minor differences in scope (IFRS is broader in what qualifies as a "qualifying asset"). | Large construction/infrastructure projects. |
| **Segment Reporting (IFRS 8 vs. ASC 280)** | Both use the management approach — largely converged after ASU 2023-07 increased US GAAP disclosure requirements. | Analysts decomposing conglomerate valuations. |

---

## 5. CONVERSION METHODOLOGY HIERARCHY

For student projects and instructor models, apply the following hierarchy when encountering non-US-GAAP financials:

### Tier 1 — No Conversion Needed

**When:** The source framework is identical to IFRS (SFRS(I), K-IFRS, BR GAAP post-2010, Saudi IFRS post-2017) and the target basis is also IFRS.

**Action:** Use as-is. Note the jurisdiction and framework in the model's assumptions tab.

### Tier 2 — Disclosure-Plus-Footnote (Default for Student Projects)

**When:** The source is IFRS (or IFRS-converged) and the comps set is US GAAP, or vice versa. The analysis is a screening-level exercise (comps table, ratio analysis, preliminary valuation) rather than a transaction-grade model.

**Action:**
1. Identify the top 3–5 differences most material to the specific company (use the §4.1 table as a checklist).
2. Quantify the impact where data is available (e.g., LIFO reserve is disclosed; lease commitments are disclosed).
3. Add a "Basis of Preparation" note in the model's assumptions tab listing the source standard, the target standard, which adjustments were made, and which were identified but not adjusted (with a stated reason — usually "insufficient disclosure to quantify").
4. Flag the affected ratios/multiples with an asterisk and a footnote.

**Rubric implication:** Students are graded on the completeness and accuracy of the disclosure, not on performing full conversion.

### Tier 3 — Quantitative Adjustment (Advanced / Instructor Models)

**When:** The analysis supports a transaction (merger model, DCF for a cross-border acquisition target) or the difference is large enough to change the investment conclusion.

**Action:**
1. Pull the specific line items from footnotes (LIFO reserve, capitalized development costs, lease schedules, pension actuarial assumptions).
2. Construct a conversion bridge on a dedicated worksheet ("GAAP Bridge" or "IFRS Adj" tab).
3. Adjust the primary financial statements and recompute ratios/multiples on the converted basis.
4. Present both "as-reported" and "adjusted" columns for transparency.

**When to require this of students:** Only in BUS-629 (EMBA, working professionals) and only when the project rubric explicitly calls for it. Not appropriate for BUS-314 or FIN-321 undergrad projects absent extra-credit framing.

### Tier 4 — Full Restatement (Out of Scope)

**When:** A company is performing a first-time adoption of a new framework (e.g., IFRS 1 first-time adoption, or a Chinese company dual-listing and preparing IFRS reconciliation).

**Action:** This is audit-firm territory. Document that it exists as a concept; do not attempt in student work.

---

## 6. IMPLICATIONS FOR COURSE PROJECTS

### 6.1 BUS-314 — Accounting Ratios

- **Current state:** Named-range conventions (BAL_, INC_, CASH_, RATIO_) assume US GAAP structure. The `bus314-accounting-ratios` skill enforces this.
- **Change:** Add a "Basis of Preparation" row to the ASSUMPTIONS section of the master workbook template. When a student selects a non-US company, require Tier 2 disclosure. Update the Stage 2 rubric to include a checklist item: "If non-US GAAP source, are material differences identified and footnoted?"
- **No change to named ranges.** The BAL_/INC_/CASH_ structure is general enough to accommodate IFRS-to-GAAP mapped inputs — the line-item names are economic, not standard-specific (e.g., BAL_TotalAssets, INC_Revenue).

### 6.2 FIN-321 — FX Hedging

- **Current state:** FX hedging project may involve non-US companies as hedging counterparties or underlying exposures.
- **Change:** Stage 2 (Specification) should require students to identify the accounting framework of any non-US entity in the case and note whether hedge accounting treatment differs (IFRS 9 hedge accounting is more permissive than ASC 815).
- **Impact:** Primarily conceptual — the FX model itself is currency-focused, not accounting-standard-sensitive.

### 6.3 BUS-629 — International Corporate Finance (Vietnam EMBA)

- **Current state:** In development. Students will analyze Vietnamese, ASEAN, and potentially Chinese firms.
- **Change:** Build the conversion framework into the course from day one:
  - Stage 1 (Memo): Require identification of the target company's accounting framework and its convergence status with IFRS.
  - Stage 2 (Excel Build): Require a GAAP Bridge tab for any company not reporting under US GAAP or full IFRS.
  - Stage 3 (Spec): Include a section on "Key Accounting Differences and Adjustments Made."
  - This is the only course where Tier 3 (quantitative adjustment) should be the default expectation.
- **VAS-specific guidance:** Vietnamese Accounting Standards are the most divergent framework students will encounter. Key VAS gaps to document in the course materials:
  - No equivalent to IFRS 9 (financial instruments are at historical cost with ad hoc impairment).
  - No equivalent to IFRS 15 (revenue recognized per legacy IAS 18 principles with Vietnamese interpretive guidance).
  - No equivalent to IFRS 16 (operating leases are off-balance-sheet).
  - Fair value measurement is not systematically codified — appraisals follow Ministry of Finance circulars.

### 6.4 Plugin Interaction

- `financial-analysis:comps-analysis` and `financial-analysis:dcf-model` should be instructed (via `CLAUDE.md` directive or prompt context) to check and disclose the accounting standard of each company in the comps set.
- `financial-analysis:audit-xls` should flag when a workbook mixes IFRS and US GAAP line items without a noted reconciliation.
- **Action item:** Add a clause to the Financial Model Assumptions spec (`docs/financial-model-assumptions.md`) requiring that all models state the accounting basis and, for mixed-basis comps, identify unadjusted cross-standard items.

---

## 7. PRACTICAL CONVERSION QUICK-REFERENCE

For the five most common adjustments students will encounter, here is the mechanical procedure:

### 7.1 LIFO → FIFO Conversion (US GAAP → IFRS Basis)

```
Adjusted Inventory    = Reported Inventory + LIFO Reserve
Adjusted COGS         = Reported COGS − Δ LIFO Reserve
Adjusted Retained Earnings = Reported RE + LIFO Reserve × (1 − Tax Rate)
Adjusted Deferred Tax Liability += LIFO Reserve × Tax Rate
```

Source for LIFO reserve: US GAAP companies disclose this in the inventory footnote (ASC 330-10-50).

### 7.2 Capitalize R&D (US GAAP → IFRS Basis)

```
Identify qualifying development costs (post-feasibility, per IAS 38 criteria)
Adjusted Intangible Assets += Capitalized Development Cost (net of amortization)
Adjusted R&D Expense       −= Current-year capitalizable amount
Adjusted Amortization      += Amortization of previously capitalized costs
Adjusted Net Income        += Capitalization − Amortization (net of tax)
```

Requires management estimates or footnote detail on development-phase spending.

### 7.3 Lease Reclassification (IFRS → US GAAP Operating Lease Presentation)

```
Adjusted EBITDA = Reported EBITDA − ROU Depreciation included in IFRS EBITDA
                  (i.e., add back the full lease payment and deduct it as a single
                   operating expense line to match US GAAP operating-lease treatment)

Alternatively: leave EBITDA as-is and note that IFRS EBITDA includes lease depreciation
               while US GAAP operating-lease EBITDA does not — then use "EBITDA post-IFRS 16"
               consistently for all IFRS names in the comps set.
```

The cleanest practice for comps: pick one basis (pre-IFRS 16 or post-) and adjust all companies to it. FactSet and Capital IQ provide both.

### 7.4 Remove Impairment Reversals (IFRS → US GAAP Basis)

```
Adjusted Operating Income = Reported OI − Impairment Reversal Gain
Adjusted Asset Balance     = Reported Balance − Cumulative Reversals (net of re-depreciation)
```

Source: IAS 36 disclosures in IFRS footnotes quantify reversals by asset class.

### 7.5 Pension Remeasurement Recycling

```
No adjustment needed for the primary financial statements (both standards now
recognize actuarial gains/losses in OCI). Difference is in the amortization of
prior-service costs from AOCI:

US GAAP: amortizes prior-service cost from AOCI over remaining service period → hits P&L
IFRS:    recognizes prior-service cost immediately in P&L in the period of plan amendment

Check footnotes for prior-service cost amounts when comparing companies with
recent plan amendments.
```

---

## 8. SURVEY OF GLOBAL CONVERGENCE STATUS (2026)

The global landscape is moving toward IFRS, but the convergence is uneven and the timeline is long.

| Status | Count | Notable Jurisdictions |
|---|---|---|
| **IFRS required for all listed companies** | ~120 | EU (27), UK, Canada, Australia, South Korea, Brazil, South Africa, Saudi Arabia, Turkey, Russia (suspended post-2022), most of Africa/Middle East/LATAM |
| **IFRS required for some, permitted for others** | ~15 | Japan (voluntary), India (Ind AS — converged, not identical), Switzerland (SMI-listed required; others may use Swiss GAAP) |
| **National GAAP with IFRS convergence roadmap** | ~10 | Vietnam (VAS → IFRS target 2028), Thailand (TFRS — nearly identical), Indonesia (SAK → IFRS-converged) |
| **National GAAP — distinct framework** | ~10 | United States (US GAAP), China (CAS — substantially converged but distinct), Japan (JGAAP — for domestic filers), Uzbekistan, several Central Asian states |
| **Dual/multiple frameworks** | ~5 | China (CAS domestic + IFRS for H-shares), Japan (JGAAP or IFRS or JMIS or US GAAP), Switzerland (Swiss GAAP or IFRS) |

**Trend:** The long-term trajectory is toward IFRS as the global default, with the US as the most significant holdout. The SEC's 2024–2025 consideration of allowing IFRS for domestic filers has stalled; no near-term US GAAP/IFRS convergence is expected. The practical reality for the next decade is a two-standard world (US GAAP + IFRS) with a shrinking tail of local standards.

---

## 9. DECISION

### 9.1 Recommended Actions

1. **Adopt the conversion hierarchy (§5) as the standard for all Shidler financial models.** Tier 2 (disclosure-plus-footnote) is the default for undergrad work; Tier 3 (quantitative adjustment) is the default for BUS-629 (EMBA). Document this in `docs/financial-model-assumptions.md`.

2. **Update the BUS-314 master workbook template** to include a "Basis of Preparation" assumption row and a "GAAP Bridge" placeholder tab (hidden by default, shown when a non-US company is selected).

3. **Build VAS-to-IFRS conversion guidance into BUS-629 course materials** as a standalone reference document before AY 2026–27 launch. This is the highest-urgency item given the Vietnam EMBA cohort.

4. **Add accounting-standard metadata to the `comps-analysis` and `dcf-model` plugin prompts** via `CLAUDE.md` directive (already the binding override mechanism per existing `CLAUDE.md` policy). Each company in a comps table should show its reporting standard; mixed-basis sets should flag the unadjusted items.

5. **Do not require Tier 3 conversion for BUS-314 or FIN-321.** The learning objective is ratio analysis and FX hedging, not GAAP conversion. Tier 2 disclosure is sufficient and pedagogically appropriate.

### 9.2 Deferred

- Full GAAP bridge Excel template with pre-built formulas for the §7 adjustments. Build this as a `_templates/excel/` skeleton when BUS-629 course development reaches the modeling stage.
- IASB goodwill amortization standard: monitor the exposure draft timeline. If adopted with a ~2027–2028 effective date, update this memo and the comps methodology before the standard goes live.
- SEC IFRS-for-domestic-filers consideration: no action needed unless the SEC revives the rulemaking.

### 9.3 Open Questions

1. Should the GAAP Bridge tab in the BUS-314 workbook be a separate worksheet or a section within the existing ASSUMPTIONS tab?
2. For BUS-629, should the VAS conversion reference be a standalone document or integrated into each project's stage assignment?
3. Should the `bus314-accounting-ratios` skill be updated to prompt students about accounting basis when they enter a non-US ticker?

---

## 10. APPENDIX — REFERENCES

- IFRS Foundation, *IFRS Accounting Standards* (2026 Blue Book)
- FASB Accounting Standards Codification, accessed via FASB.org
- Deloitte, *iGAAP — IFRS Compared to US GAAP* (2025 edition)
- PwC, *IFRS and US GAAP: Similarities and Differences* (2025 edition)
- Vietnam Ministry of Finance, Circular 200/2014/TT-BTC (VAS chart of accounts and reporting framework)
- IASB Post-Implementation Review of IFRS 3 / Goodwill Amortization Discussion Paper (2024)
- Financial Model Assumptions (SSOT): `docs/financial-model-assumptions.md`
- BUS-314 Ratios Skill: `.claude/skills/bus314-accounting-ratios/SKILL.md`
- BUS-629 Course Directory: `courses/BUS-629-International-Corporate-Finance/`
- Repo decision memos: `docs/decisions/`
