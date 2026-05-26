# MASTER FINANCIAL MODEL ASSUMPTIONS — SINGLE SOURCE OF TRUTH FOR VALUATION INPUTS

## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** May 26, 2026
**Status:** Draft — Pending Review
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

## 5. OPEN QUESTIONS — TO REVISIT

These items were deferred and need a decision before the spec is treated as final rather than draft:

1. **Beta value vs. beta methodology.** The current spec treats beta as company-specific with a uniform methodology. The original ask (2026-05-23) was for "risk free rate, beta, market risk premiums to always be the same regardless of which company." Need to confirm whether the intent is genuinely a single beta (e.g., 1.0 or market-average) for pedagogical comparability, or whether the methodology-uniform approach as currently codified is the right call. The former simplifies grading; the latter is more institutionally defensible.

2. **Non-USD DCFs.** The spec instructs analysts to use a local sovereign 10Y yield and document the deviation. For BUS-629 (Vietnam EMBA), we should decide whether to pre-populate Vietnam government bond yields in the spec, or keep this purely as a per-model override.

3. **Update mechanism.** Rf is "refreshed monthly (first business day)." Need an actual workflow — a scheduled prompt, a slash command (`/refresh-rf`), or a recurring calendar reminder. Without a binding mechanism, the value will go stale and the spec's authority erodes.

4. **Hardening beyond CLAUDE.md.** Today's setup relies on CLAUDE.md being loaded and Claude actually reading the linked spec. Stronger options were sketched (custom `/load-assumptions` slash command, project-local wrapper skill, UserPromptSubmit hook, self-validation script). Decide whether the CLAUDE.md directive is sufficient or whether to escalate to step 2 (slash command) once we see drift in practice.

5. **Student-facing version.** The spec is currently written for instructor/Claude consumption. For BUS-629 Stage 2+ students, decide whether to publish a simplified student-facing version (one-page assumption sheet) that captures only the values they need without the full methodology and update-cadence machinery.

6. **Integration with existing course rubrics.** BUS-314, FIN-321, and BUS-629 rubrics do not currently cite this spec. Need to decide when and how to retrofit (next course refresh? immediate addendum?).

---

## 6. ALTERNATIVES CONSIDERED

- **Edit the plugin-cache skill files directly.** Rejected — `C:\Users\adamw\.claude\plugins\cache\...` is overwritten on plugin update. Not durable.
- **Hook-based injection** (UserPromptSubmit injects the spec contents whenever the prompt matches valuation keywords). Rejected for now as overkill — adds ~200 lines of context per matching prompt, brittle to keyword drift. Reserved as escalation step 4 if CLAUDE.md alone proves insufficient.
- **Self-validation Python script** that scans built `.xlsx` files for spec compliance. Useful for after-the-fact audit, not for prevention. Reserved as escalation step 5.
- **Store assumptions in a JSON/YAML data file** that skills load programmatically. More precise than a markdown spec but loses the methodology-and-narrative content that makes the spec useful for human analysts and students. Markdown wins for this audience.

---

## 7. STATUS

Draft. Pending decisions on §5 items 1–6. Spec file and CLAUDE.md plumbing are live in the repo as of 2026-05-26.
