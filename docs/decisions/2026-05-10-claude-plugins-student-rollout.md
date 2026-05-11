# CLAUDE-FOR-FINANCIAL-SERVICES PLUGINS — STUDENT ROLLOUT & PROJECT IMPLICATIONS

## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** May 10, 2026
**Status:** Draft — Pending Review
**Scope:** All Shidler courses currently using the Spring 2026 portfolio workflow (BUS-313, BUS-314, FIN-321, BUS-620, BUS-629). Touches AI usage policy, project rubrics, and student onboarding.

---

## 1. SUMMARY

On 2026-05-10 the instructor installed the `claude-for-financial-services` Anthropic marketplace and enabled five plugins in the `shidler` repo: `financial-analysis`, `investment-banking`, `pitch-agent`, `gl-reconciler`, `market-researcher`. These plugins ship 30+ skills and 12 MCP connectors covering DCF/LBO/comps modeling, pitch-deck construction, deck QC, competitive-landscape analysis, datapack builds, CIM/teaser drafting, and GL reconciliation. They are directly applicable to BUS-314 (Accounting Ratios), FIN-321 (FX Hedging), BUS-313 (trade case studies), and the in-development BUS-629 (International Corporate Finance, Vietnam EMBA).

**The pedagogical opportunity is real but uneven across cohorts, and the access barriers are non-trivial.** This memo recommends a **demo-first, opt-in-pilot rollout** rather than a required deployment in AY 2026–27: (a) instructor uses the plugins to demonstrate industry workflows in class and to produce branded templates; (b) graduate-level cohorts (BUS-629 first, BUS-620 second) get a structured opt-in path with an install guide; (c) undergraduate cohorts (BUS-313, BUS-314, FIN-321) get exposure through instructor demos and one optional extra-credit module rather than a required tool. This preserves the existing "AI is optional, not required" policy from `CLAUDE.md`, addresses the Claude Pro cost barrier ($20/mo), and avoids the deep MCP-auth dependencies (FactSet, S&P Global, Moody's, PitchBook) that students cannot realistically access. The memo also catalogs which skills map to which project stage so the rubric can credit (or restrict) their use.

---

## 2. WHAT WAS INSTALLED

Five plugins from `claude-for-financial-services` were enabled at **project scope** in `<repo>/.claude/settings.json` (i.e., active only in `shidler/`, not globally). The marketplace registration lives at user scope in `~/.claude/settings.json`. Install process and scope mechanics are documented in `docs/guides/claude-code-plugins.md`.

| Plugin | Headline skills | Project-stage fit |
|---|---|---|
| `financial-analysis` | `3-statement-model`, `comps-analysis`, `dcf-model`, `lbo-model`, `audit-xls`, `clean-data-xls`, `competitive-analysis`, `ib-check-deck`, `deck-refresh` | BUS-314 Stage 2 build/audit; FIN-321 Stage 3 audit; BUS-629 modeling |
| `investment-banking` | `cim`, `teaser`, `merger-model`, `buyer-list`, `process-letter`, `one-pager`, `strip-profile`, `datapack-builder`, `deal-tracker`, `pitch-deck` | BUS-629 M&A simulations; BUS-313 industry briefings |
| `pitch-agent` | `pitch-deck`, `ib-check-deck`, `deck-refresh` + bundled financial-analysis skills | All courses' final-stage decks |
| `gl-reconciler` | `gl-recon`, `break-trace`, `audit-xls` | Niche — BUS-314 ratio reconciliation; BUS-629 fund-admin sidebar |
| `market-researcher` | `competitive-analysis`, `comps-analysis` + headless PPT author | BUS-313 country/trade analyses; BUS-629 sector decks |

`equity-research` is in the marketplace but **not yet installed**. The marketplace's `private-equity`, `wealth-management`, `fund-admin`, `operations`, `earnings-reviewer`, `meeting-prep-agent`, `model-builder`, `kyc-screener`, `valuation-reviewer`, `month-end-closer`, `statement-auditor`, `lseg`, and `sp-global` plugins are also available but out of scope for current courses.

### 2.1 MCP connectors (the auth wall)

The `financial-analysis` plugin ships authenticated MCP connectors for: Aiera, Chronograph, Daloopa, FactSet, Moody's, Morningstar, PitchBook, and S&P Global. Each requires a one-time `authenticate` call backed by **enterprise/paid credentials**. Students will not have these. This means student-side use of the plugins is limited to the skills that work against public/local data (most of `financial-analysis`, `investment-banking`, `pitch-agent`, `market-researcher` skills), not the live-data connectors. This is a real but bounded constraint — the modeling, drafting, and QC skills are usable on SEC filings, manually pasted data, or repo-stored exports.

---

## 3. PEDAGOGICAL OPPORTUNITY

### 3.1 Course-by-course fit

**BUS-314 — International Corporate Finance (Accounting Ratios, 4-stage, ~120 undergrads across 3 sections).**
- *Stage 2 (Excel build):* `financial-analysis:audit-xls` is a near-perfect match for the existing rubric — students would catch their own balance-sheet ties, formula errors, and named-range mistakes before submission. `bus314-accounting-ratios` skill already enforces the BAL_/INC_/CASH_/RATIO_ prefix convention; `audit-xls` is complementary.
- *Stage 4 (Final analysis):* `financial-analysis:ib-check-deck` could be used for self-QC on the recommendation memo.
- *Risk:* `3-statement-model` and `dcf-model` can build the model end-to-end, which would short-circuit the learning. Rubric must distinguish "student built, AI audited" from "AI built, student presented".
- *Note:* Ava Dodhi's custom Stage 2 (brand-guide variant per project memory) is unaffected — she's not building a ratios workbook.

**FIN-321 — International Finance & Securities (FX Hedging, 5-stage, ~80 undergrads).**
- *Stage 3 (Excel build):* `audit-xls` directly relevant. The 2026-Spring Stage 4 review (`docs/decisions/fin321/2026-05-02-fin321-stage4-submission-format-review.md`) already documented quality gaps in student Excel; plugin-assisted self-audit could lift the floor.
- *Stage 4 (Structured AI prompt):* `pitch-agent:ib-check-deck` for memo polish. The Stage 4 deliverable already grades on "structured prompt with verification" — students could use the plugins themselves as a meta-exercise in evaluating AI workflows.
- *Pedagogical tension:* The course explicitly teaches students to *write* the structured prompt. Using a plugin that *bundles* the workflow risks teaching the wrapper rather than the underlying skill. Counter-argument: industry exposure is itself a learning objective.

**BUS-313 — Economic & Financial Environment of Global Business (Trade case studies, ~80 undergrads).**
- *Group project:* `market-researcher:competitive-analysis` and `investment-banking:strip-profile` are well-matched to industry/country briefings.
- *Lowest stakes for plugin rollout* — students aren't building models, so the "AI built it for me" failure mode is muted. Best place to pilot if undergrad exposure is desired.

**BUS-629 — International Corporate Finance (Vietnam EMBA, in development).**
- *Highest fit and lowest barrier.* EMBA students are working professionals who may already have Claude Pro/Max via employer. The course outline (currently `courses/BUS-629-International-Corporate-Finance/`) covers FX, capital structure, and cross-border M&A — directly aligned with `investment-banking:cim`, `merger-model`, `buyer-list`. Recommend this be the **primary pilot cohort**.

**BUS-620 — Micro & Macro Economics (MBA).**
- Limited direct fit. `market-researcher` skills could support sector-policy analyses. Lower priority.

**BUS-122B — Intro Entrepreneurship/Sustainable Ag (community college).**
- No fit. Skip.

### 3.2 What the plugins actually accelerate

The skills that benefit students *without* gutting the learning are the ones that act on student-produced artifacts:

- **`audit-xls`** — verifies a student-built model. Doesn't build it.
- **`ib-check-deck`** — QCs a student-built deck against IB standards. Doesn't draft it.
- **`clean-data-xls`** — cleans messy data before analysis. Routine task.
- **`competitive-analysis`** (as a framework, not a generator) — provides structure for student-written analysis.

The skills that *replace* the student's work are the ones to constrain or disallow on graded deliverables:

- **`3-statement-model`** — fills out the IS/BS/CF template that students are supposed to build.
- **`dcf-model`** — builds the full DCF; in BUS-314 Stage 2 / FIN-321 Stage 3 this is the assignment.
- **`lbo-model`**, **`merger-model`** — same caveat for transactional courses.
- **`pitch-deck`**, **`cim`**, **`teaser`** — drafts the deliverable.

This is the **constructive/generative split**: constructive AI use (audit, polish, structure) should be encouraged; generative AI use (build the thing the rubric grades on) should be disclosed and either prohibited or carry a separate "process" deduction.

---

## 4. RECOMMENDED ROLLOUT

### 4.1 Tiered approach for AY 2026–27

**Tier 1 — Instructor demonstration (all courses, immediate).**
Use the plugins in class to demonstrate industry workflows: a 10-minute live `dcf-model` build during a BUS-314 lecture, an `ib-check-deck` review of a sample pitch deck for FIN-321, a `competitive-analysis` walkthrough for BUS-313. No student install required. Reinforces "this is what AI-assisted finance work looks like in practice" without forcing access or grading on it.

**Tier 2 — Optional opt-in (BUS-629 primary; BUS-313 secondary).**
Provide a student install guide (see §5 below) and one optional extra-credit module per course that uses a constructive plugin skill (e.g., "Run `audit-xls` on your Stage 2 model; submit the audit summary as a 1-page reflection — +0.5 to Stage 2 score, capped at the original ceiling"). EMBA cohort gets this first because of likely employer-paid Claude access.

**Tier 3 — Required (NOT recommended for AY 2026–27).**
Requiring plugin use would impose a $20/mo Claude Pro cost on undergrads, a non-trivial install/troubleshoot load on the instructor, and an equity gap between students with home machines and those reliant on lab computers. Revisit for AY 2027–28 once cost and access norms stabilize.

### 4.2 Why phase rather than launch broadly

- **Cost barrier.** Claude Pro is $20/mo. Even Free-tier Claude Code is rate-limited and won't run the heavy modeling skills reliably.
- **Install friction.** The marketplace add-via-HTTPS fix (`docs/guides/claude-code-plugins.md`) is non-obvious; per-machine trust prompts add friction in a classroom setting.
- **MCP auth gap.** Half the value of `financial-analysis` is in the live-data connectors students can't access. Setting expectations matters.
- **Rubric debt.** Current rubrics don't yet distinguish constructive from generative AI use; building that distinction into a syllabus takes one course-cycle of iteration.
- **Existing AI policy.** `CLAUDE.md` already states "AI use is optional, not required". A required plugin rollout would contradict that policy and the AI policy in each course `README.md`.

---

## 5. IMPLEMENTATION CHECKLIST

### 5.1 Instructor-side (now)

- [x] Marketplace and plugins installed in `shidler/` repo (`2026-05-10`).
- [x] Install guide written: `docs/guides/claude-code-plugins.md`.
- [ ] Resolve `1 error during load` reported by `/reload-plugins` — run `/doctor`, likely an MCP auth-not-yet-configured warning; safe to ignore for instructor use until a connector is needed.
- [ ] Install `equity-research@claude-for-financial-services --scope project` if it will be used (currently missing from `enabledPlugins`).
- [ ] Pilot one skill per course in a Spring 2026 demo session before AY 2026–27 launch:
  - BUS-314: `audit-xls` on a sample Stage 2 workbook.
  - FIN-321: `ib-check-deck` on a sample Stage 4 memo.
  - BUS-313: `competitive-analysis` for an industry brief.
  - BUS-629: `cim` or `merger-model` walkthrough.

### 5.2 Student-side (for Tier-2 opt-in cohorts, by start of AY 2026–27)

- [ ] Write `docs/guides/student-claude-code-onboarding.md` covering:
  - Claude Code install (Mac/Windows/Linux).
  - Claude Pro signup and the free-tier limits.
  - The HTTPS marketplace-add fix (precaution against the SSH error we hit).
  - Repo clone → `/plugin marketplace add ...` → `/plugin install ... --scope project` flow.
  - What to do if the per-machine trust prompt appears.
  - Which skills are *constructive* (encouraged) vs *generative* (must be disclosed in `prompt-log.md`).
- [ ] Update each course `README.md` AI policy section to add a "Plugin Use" subsection clarifying:
  - Plugins are optional and not required for any deliverable.
  - Any plugin-generated content must be logged in `deliverables/prompt-log.md` with the plugin name and the skill invoked.
  - Generative plugin use on graded deliverables (e.g., `dcf-model` for a Stage 2 build) incurs the same disclosure requirement as any AI generation; the rubric will weight student-authored work more heavily.
- [ ] Add to BUS-629 syllabus (in development) from day one rather than retrofitting.

### 5.3 Rubric adjustments (defer to next syllabus cycle)

- BUS-314 Stage 2 rubric: add "AI-audit credit" (+0.25) for students who run `audit-xls` and submit the output, conditional on the underlying model being student-built per named-range conventions.
- FIN-321 Stage 4 rubric: continue 2026-05-02 reforms; no plugin-specific changes in AY 2026–27.
- BUS-313 group project: optional "competitive landscape using plugin" extension module worth +1 point on the country brief.

---

## 6. RISKS & TRADE-OFFS

| Risk | Likelihood | Mitigation |
|---|---|---|
| Plugin generates the deliverable; student turns in unmodified output | High if generative skills are not constrained | Constructive/generative split in §3.2; rubric weighting in §5.3; prompt-log disclosure requirement |
| Equity gap between students with Claude Pro and without | High | Keep Tier 3 (required) off the table; Tier 2 modules carry small extra-credit value only |
| Instructor support load (install issues, plugin errors) scales with student count | Medium | Install guide + standard troubleshooting from `docs/guides/claude-code-plugins.md`; deflect to office hours |
| MCP-auth failures confuse students (e.g., `dcf-model` works but `factset` connector doesn't) | Medium | Documentation calls out which skills are local-data vs. require enterprise connectors |
| Plugin behavior changes mid-semester (Anthropic updates marketplace) | Low–Medium | Pin a known-good commit of the marketplace repo if drift becomes disruptive; for AY 2026–27, expect instability |
| Privacy/PII: students inadvertently feed graded artifacts to a cloud model | Low (artifacts are course assignments, not personal data) | Reinforce repo's existing `ignore/` and `ignore-term/` discipline; no student grades or PII in plugin prompts |
| Plugin overlap with existing skills (`bus314-accounting-ratios`, `brand-guidelines`, `xlsx`) creates ambiguity about which to use | Medium | Course CLAUDE.md should document precedence: course-specific skills first, plugin skills second |

---

## 7. DECISION

**Recommendation:** Adopt the phased rollout in §4.1.

- **Approve now:** Instructor-side Tier 1 (demos) for Spring 2026 remainder.
- **Plan for AY 2026–27 fall:** Tier 2 opt-in pilot in BUS-629 (Vietnam EMBA) and BUS-313 with the install guide, AI-policy updates, and extra-credit modules from §5.
- **Defer:** Tier 3 (required) until AY 2027–28 at earliest. Re-evaluate after one cycle of Tier 2 data.

**Open questions:**
1. Should the student install guide be public (in `docs/guides/`) or course-restricted (Lamaku-only)? Public is the default for the rest of the repo; if any plugin or workflow involves licensed data, restrict it.
2. Does the instructor want to install `equity-research` for FIN-321 use, or is the current 5-plugin set sufficient?
3. For BUS-629, does the syllabus need a Stage-0 "tools setup" assignment to ensure students arrive with working Claude Code + plugins?

---

## 8. APPENDIX — REFERENCES

- Install guide and scope mechanics: `docs/guides/claude-code-plugins.md`
- Repo `.claude/settings.json` (project-scope enablement, as of 2026-05-10)
- User `~/.claude/settings.json` (marketplace registration)
- Marketplace source: https://github.com/anthropics/financial-services
- Existing AI policy: `CLAUDE.md` § "Writing and AI Conventions"; per-course `README.md` AI-policy sections
- Related decision: `docs/decisions/fin321/2026-05-02-fin321-stage4-submission-format-review.md` (informs the constructive/generative split)
- BUS-314 ratios skill (course-specific): `.claude/skills/bus314-accounting-ratios/SKILL.md`
