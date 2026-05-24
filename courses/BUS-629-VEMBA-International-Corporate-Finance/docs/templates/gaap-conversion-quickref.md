---
template: reference
purpose: "Quick-reference checklist for students populating non-US-GAAP financials into the BUS-629 ratios workbook"
audience: student
courses: [BUS-629]
related: [docs/decisions/2026-05-24-accounting-standards-conversion-framework.md]
---

# Accounting Standards Quick-Reference

**When to use this:** You pulled financial data from a company that does **not** report under US GAAP. This one-pager tells you what to check, what to adjust, and what to disclose so your workbook and ratios are graded fairly.

---

## Step 1 — Identify the reporting standard

Open the company's annual report or audited financial statements. Look for a note titled "Basis of Preparation" or "Summary of Significant Accounting Policies" (usually Note 1 or Note 2). Record:

| Field | Where to enter it |
|---|---|
| Reporting standard (e.g., VAS, IFRS, CAS, Ind AS) | Cover & Instructions tab → "Reporting Standard" |
| Whether the standard is IFRS-converged | Cover & Instructions tab → "IFRS Convergence Status" |
| Reporting currency | Cover & Instructions tab → "Currency" |
| Fiscal year end | Cover & Instructions tab → "FYE" |

---

## Step 2 — Check the five high-impact areas

For each area below, check whether the difference applies to your company. If it does, note it in the GAAP Bridge tab. If it does not (or you cannot quantify it from the available disclosures), write "N/A — not material" or "N/A — insufficient disclosure" in the Adjustment column.

### 1. Inventory method

| Question | What to look for |
|---|---|
| Does the company use LIFO? | IFRS and VAS prohibit LIFO, so this only matters if you are comparing *to* a US GAAP company that uses LIFO. If your US-listed comps use LIFO, add their LIFO reserve (from their 10-K inventory footnote) to make them FIFO-comparable. |

### 2. Leases

| Question | What to look for |
|---|---|
| Does the company report under IFRS 16? | If yes, all leases are on the balance sheet as right-of-use assets and lease liabilities. EBITDA will be higher than a US GAAP operating-lease equivalent because lease depreciation is below the EBITDA line. Note this in the GAAP Bridge tab. |
| Does the company report under VAS? | VAS has no equivalent to IFRS 16 — operating leases are off-balance-sheet. If comparing to IFRS or US GAAP peers, note that the company's total assets and total liabilities are understated relative to peers that capitalize leases. |

### 3. R&D / development costs

| Question | What to look for |
|---|---|
| Are development costs capitalized on the balance sheet? | Under IFRS (IAS 38), qualifying development costs are capitalized as intangible assets. Under VAS, practice varies. Under US GAAP, nearly all R&D is expensed. If your company capitalizes development costs, note the balance and annual amortization in the GAAP Bridge tab. |

### 4. Impairment reversals

| Question | What to look for |
|---|---|
| Has the company reversed a prior impairment? | IFRS allows reversal of impairment losses (except for goodwill). US GAAP does not. If the P&L includes an impairment reversal gain, note it in the GAAP Bridge tab — it inflates operating income relative to US GAAP. |

### 5. Revenue recognition timing

| Question | What to look for |
|---|---|
| Does the company report under a pre-IFRS 15 standard? | VAS still follows legacy IAS 18 principles. Differences are usually small for manufacturing/retail but can be significant for software, licensing, or construction companies. Note any disclosed policy that differs from the five-step model. |

---

## Step 3 — Fill in the GAAP Bridge tab

Your workbook's GAAP Bridge tab has pre-labeled rows for each area above. For each row:

1. **Applies?** — Yes / No / Cannot determine
2. **Direction of impact** — Overstates or understates the line item vs. US GAAP basis
3. **Magnitude** — Quantified amount (if disclosures permit) or "Not quantifiable from public filings"
4. **Source** — Footnote number and page from the annual report

You do **not** need to restate the financial statements. The GAAP Bridge tab is a disclosure exercise — it shows you understand the differences. The financial-statement tabs (INC_, BAL_, CASH_) keep the as-reported numbers.

---

## Step 4 — Flag affected ratios

On the Ratios tab, any ratio materially affected by a cross-standard difference should have a note. The simplest approach: add a comment to the cell referencing the GAAP Bridge row (e.g., "See GAAP Bridge row 2 — EBITDA inflated by IFRS 16 lease treatment").

---

## Common situations by framework

| Your company reports under... | What to expect |
|---|---|
| **IFRS** (or SFRS(I), K-IFRS, BR GAAP) | Generally close to US GAAP. Check leases (IFRS 16 single-model), R&D capitalization, and impairment reversals. |
| **VAS (Vietnam)** | Significant gaps: no IFRS 16 (leases off-balance-sheet), no IFRS 9 (financial instruments at historical cost), no IFRS 15 (legacy revenue recognition). Depreciation schedules follow MoF circulars, not useful life estimates — depreciation may be zero for some asset classes. Fair value measurement is not systematic. |
| **CAS (China)** | Substantially converged with IFRS but watch for: business combinations under common control (pooling method), conservative fair value application, and government grant presentation. Dual-listed firms (A-share + H-share) may have two different sets of financials. |
| **Ind AS (India)** | Converged with IFRS with carve-outs on financial instruments and bargain purchases. RBI overlay on bank provisioning. XBRL taxonomy is India-specific. |
| **JGAAP (Japan)** | Goodwill is amortized (max 20 years) — artificially depresses post-acquisition earnings vs. IFRS/US GAAP peers. All R&D is expensed. ~270 Japanese listed companies now use full IFRS voluntarily. |

---

## What you are graded on

You are graded on the **quality of your disclosure**, not on performing a full conversion. A strong Stage 3 submission for a non-US company:

- Identifies the reporting standard in the Cover tab
- Completes the GAAP Bridge tab for all five areas (even if most are "N/A")
- Notes affected ratios
- Cites specific footnotes from the annual report

A weak submission ignores the standard entirely and treats VAS/IFRS/CAS line items as if they were US GAAP without comment.

---

## Further reading

The full decision memo with detailed conversion mechanics, adjustment formulas, and a survey of global accounting frameworks is at:

[`docs/decisions/2026-05-24-accounting-standards-conversion-framework.md`](../../../../docs/decisions/2026-05-24-accounting-standards-conversion-framework.md)

You do not need to read the full memo to complete your Stage 3 deliverable — this quick-reference covers what you need.
