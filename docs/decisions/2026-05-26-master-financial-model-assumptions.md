# MASTER FINANCIAL MODEL ASSUMPTIONS — SINGLE SOURCE OF TRUTH FOR VALUATION INPUTS

## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** May 26, 2026
**Status:** Approved — §5 items resolved 2026-05-26
**Scope:** Cross-cutting — applies to every DCF, comps, LBO, merger model, 3-statement build, and valuation exercise produced in this repo. Affects FIN-321, BUS-314, BUS-629, and any future course or research output that touches valuation.

---

## 1. SUMMARY

Across the course portfolio and research outputs in this repo, every valuation model independently re-derives the same handful of market inputs — risk-free rate, equity risk premium, default tax rate, terminal-growth conventions, color palette, and number formats. The result is silent drift: one DCF uses Rf = 4.25%, another uses 4.55%, a student model uses 4.0% because that was the textbook number, and outputs are no longer comparable across models built only weeks apart.

This memo establishes a **single source of truth** for cross-company financial-modeling assumptions, codified in [`docs/financial-model-assumptions.md`](../financial-model-assumptions.md). It also wires the repo's `CLAUDE.md` so that any Claude-assisted financial model build will read the spec before hardcoding any of the values it covers. Company-specific inputs (beta, revenue, margins, capital structure) continue to be derived per-company; only the **shared institutional inputs and methodology** are centralized.

---

## 2. WHY THIS MATTERS NOW

Three pressures converge:

1. **Pilot DCF on NVDA (2026-05-23).** While building a 5-year DCF on NVIDIA via the `financial-analysis:dcf-model` plugin skill, every input — Rf, ERP, beta methodology, tax rate, terminal growth, color palette — was re-derived from scratch with no shared reference. The output was good, but the next DCF in the repo would start from zero again.

2. **Plugin skill proliferation.** The repo now exposes `financial-analysis:*`, `investment-banking:*`, `equity-research:*`, `pitch-agent:*`, and `market-researcher:*` plugin skills. Each carries its own default conventions. Without a binding override, every plugin invocation is a fresh roll of the dice on Rf/ERP/format choices.

3. **Course portfolio consistency.** FIN-321 (FX Hedging), BUS-629 (International Corporate Finance), and the BUS-314 ratios workbook will eventually share a valuation backbone. If students see Rf = 4.55% in one course and Rf = 4.25% in another for the same valuation date, the rubric loses credibility.

The conversion-aware accounting framework decided on 2026-05-24 sits one layer below this — it tells us how to compare across IFRS/GAAP/VAS line items. This memo sits one layer above — it tells us what shared market and methodology inputs to use once the accounting basis is clean.

---

## 3. DECISION

Adopt [`docs/financial-model-assumptions.md`](../financial-model-assumptions.md) as the **binding institutional source of truth** for cross-company financial-model inputs. The file covers:

- **Cost of capital inputs** — risk-free rate, equity risk premium, beta methodology and proxy hierarchy, cost-of-debt credit spreads by rating, tax rate hierarchy (10-K → 5-yr avg → default 24% blended).
- **DCF mechanics** — 5-year default horizon, mid-year discounting, Gordon Growth terminal value, terminal-g ranges, FCF definition (with explicit treatment of SBC and leases), Bear/Base/Bull scenario framework.
- **Comps mechanics** — multiples by business type, NTM (not LTM) basis, outlier trimming rule (z-score > 2).
- **LBO/merger conventions** — hold period, exit multiple method, synergy phasing.
- **Formatting standards** — color palette (3 blues + grey + white), number formats, cell-comment citation format.
- **Update cadence** — Rf monthly, ERP quarterly, tax rates only on law change.
- **Accounting basis disclosure** — incorporated by reference to the 2026-05-24 accounting-standards memo.

Plumbing is via `CLAUDE.md`, which is loaded at the start of every Claude Code session in this repo. A new section ("Financial Model Assumptions — mandatory for valuation work") directs Claude to read the spec before executing any valuation skill. Because plugin-cache skills (`financial-analysis:*`, `investment-banking:*`, etc.) are not safely editable — they get overwritten on plugin update — the `CLAUDE.md` directive is the binding override layer.

---

## 4. WHAT WAS IMPLEMENTED TODAY

1. **Created `docs/financial-model-assumptions.md`** — the SSOT spec. Populated with values current as of 2026-05-22 (Rf = 4.55%, ERP = 5.50%, blended tax = 24.0%) and full methodology sections for cost of capital, DCF mechanics, comps, LBO/merger conventions, formatting, and update cadence.

2. **Updated `CLAUDE.md`** — added (a) a "Financial Model Assumptions (mandatory for valuation work)" section directing Claude to read the spec first; and (b) a row in the Key Reference Paths table pointing to the spec.

3. **Linter / follow-up edit** (intentional, not part of today's Claude run): an "Accounting Basis (mandatory disclosure)" section was added to the top of the spec file, requiring every model to state the reporting standard (US GAAP / IFRS / VAS / CAS / JGAAP / Ind AS) and the conversion tier applied, with a cross-reference to the 2026-05-24 accounting-standards conversion framework memo. This means the two policy layers (market inputs + accounting basis) are now wired together at the spec level.

---

## 5. RESOLUTIONS

All open items addressed on 2026-05-26. Decisions and the implementation locations are below.

### 5.1 Beta value vs. beta methodology — RESOLVED

**Decision:** **Default beta = 1.00** (market). Company-specific beta is a **documented opt-in override** with a one-line justification on the model's cover sheet.

**Rationale:** The original 2026-05-23 ask was unambiguous — "risk free rate, beta, market risk premiums to always be the same regardless of which company." Cross-model comparability requires uniform beta. The override path preserves analyst judgment for transaction-grade or research work where company-specific beta is justified, but the default behavior is consistent.

**Implemented at:** [`docs/financial-model-assumptions.md`](../financial-model-assumptions.md) §1.3, rewritten to lead with the β = 1.00 default and demote the per-company methodology to override territory.

### 5.2 Non-USD DCFs — RESOLVED

**Decision:** Pre-populate a non-USD risk-free rate table in §1.1 of the spec, anchored on currencies the repo's courses actually touch (VND for BUS-629) plus the obvious major-market peers (EUR, GBP, JPY, SGD, CNY, INR). Currencies not listed are filled in opportunistically during monthly refresh. Country risk premium (CRP) overlay guidance added for cross-border cases where the analyst wants to keep a USD discount rate.

**Implemented at:** [`docs/financial-model-assumptions.md`](../financial-model-assumptions.md) §1.1, with the 7-currency table and a CRP guidance paragraph.

### 5.3 Update mechanism — RESOLVED

**Decision:** Manual refresh, instructor-triggered, with two trigger paths:
1. **Calendar-driven (primary):** First business day of each month — instructor refreshes Rf from Fed H.15 daily series and the non-USD table from corresponding central-bank sources. Updates the value, the "Last Updated" date, and adds an Update Log row.
2. **Session-driven (opportunistic):** If at session start the "Last Updated" date is more than one cadence period stale, refresh in-session before building the model.

No scheduled-agent or cron infrastructure required. A `/refresh-market-rates` slash command can be scaffolded later if friction becomes apparent, but the manual approach is sufficient for now.

**Implemented at:** [`docs/financial-model-assumptions.md`](../financial-model-assumptions.md) Effective Dates section, new "Refresh Mechanism" subsection.

### 5.4 Hardening beyond CLAUDE.md — RESOLVED (deferred)

**Decision:** **Stay at the CLAUDE.md directive level until drift is observed in a built model.** If a future model is found hardcoding Rf ≠ spec value or β ≠ 1.00 without a documented override, escalate to a project-local wrapper skill (`.claude/skills/load-house-assumptions/`) or a UserPromptSubmit hook. Specifically:

- **Trigger to escalate:** Any model produced by Claude in this repo that uses an Rf, ERP, beta, or tax-rate default different from the spec, without a deviation note in the model's notes section.
- **Escalation step:** Project-local wrapper skill is the next move (lower friction than a hook, more durable than spec-reading dependency on CLAUDE.md).

This deferral is intentional: we have one data point (the NVDA DCF) where the spec was followed cleanly because the spec was created during the build. Real test is whether subsequent unrelated valuation work follows the spec on first attempt.

### 5.5 Student-facing version — RESOLVED

**Decision:** Create a one-page simplified version covering only the values students need (Rf, ERP, β, tax rate, terminal g, projection period, formatting basics) without the methodology, update-cadence, and override apparatus.

**Implemented at:** [`docs/financial-model-assumptions-student.md`](../financial-model-assumptions-student.md). Linked from the full spec via §7 and from course READMEs (see §5.6).

### 5.6 Integration with existing course rubrics — RESOLVED

**Decision:** Add a one-line reference (pointing to the student one-pager) to the READMEs of valuation-relevant courses. Do NOT modify the rubrics themselves — the spec is cross-cutting and rubric edits should be deferred to the next planned course refresh.

**Implemented at:**
- [`courses/BUS-629-VEMBA-International-Corporate-Finance/README.md`](../../courses/BUS-629-VEMBA-International-Corporate-Finance/README.md) — added two rows to the Key Links table (student one-pager + full spec).
- [`courses/FIN-321-International-Finance-And-Securities/README.md`](../../courses/FIN-321-International-Finance-And-Securities/README.md) — added a "Required Reference" paragraph to the AI + GitHub Course Project section.

**Excluded:** BUS-314 (ratios course; cost-of-capital spec is not load-bearing for the existing ratios project). Reassess when BUS-314 adds a valuation module.

---

## 6. ALTERNATIVES CONSIDERED

- **Edit the plugin-cache skill files directly.** Rejected — `C:\Users\adamw\.claude\plugins\cache\...` is overwritten on plugin update. Not durable.
- **Hook-based injection** (UserPromptSubmit injects the spec contents whenever the prompt matches valuation keywords). Rejected for now as overkill — adds ~200 lines of context per matching prompt, brittle to keyword drift. Reserved as escalation step 4 if CLAUDE.md alone proves insufficient.
- **Self-validation Python script** that scans built `.xlsx` files for spec compliance. Useful for after-the-fact audit, not for prevention. Reserved as escalation step 5.
- **Store assumptions in a JSON/YAML data file** that skills load programmatically. More precise than a markdown spec but loses the methodology-and-narrative content that makes the spec useful for human analysts and students. Markdown wins for this audience.

---

## 7. STATUS

Approved. All §5 items resolved on 2026-05-26. Spec file, student one-pager, CLAUDE.md plumbing, and course README references are live in the repo. Single deferred item is §5.4 (hardening beyond CLAUDE.md), which is intentionally on a "wait-for-evidence-of-drift" trigger rather than pre-emptively built.
