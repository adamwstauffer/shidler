---
title: "Cherry-Picking the farm-management-assistant .claude Workflow Layer"
date: 2026-07-12
status: accepted
owner: Adam W. Stauffer
scope: repo-wide
related:
  - 2026-05-10-claude-plugins-student-rollout.md
  - 2026-02-15-repo-hierarchy.md
---

# Cherry-Picking the farm-management-assistant `.claude` Workflow Layer

> **Drafted by Claude for Adam's review — nothing here is adopted.** Source reviewed:
> [`LiosAg/farm-management-assistant-v2/.claude`](https://github.com/LiosAg/farm-management-assistant-v2/tree/main/.claude)
> and its [`CLAUDE.md`](https://github.com/LiosAg/farm-management-assistant-v2/blob/main/CLAUDE.md),
> at HEAD on 2026-07-12. Adam flagged `/breakpoint`, `/suggest-optimal`, and `/grill-me` as the
> three he uses most.

## Executive Summary

The farm repo carries ~35 slash commands and ~30 skills; **our `.claude/commands/` and
`.claude/agents/` are empty placeholders** — we have skills but no command/workflow layer. Most of
the farm arsenal is software- and certlib-specific (SDD pipeline, Postgres SSOT MCP, Reg-cluster
PRDs) and irrelevant here. But a focused subset is domain-agnostic judgment tooling that ports
cleanly to a docs/Markdown/Excel repo. **Recommendation: port six commands in three tiers.** Tier 1
is the three Adam named — `/breakpoint`, `/suggest-optimal`, `/grill-me` — each retargeted off
Postgres/certlib onto *this* repo's ground truth (`recalc.py`, xlsx validation, path/link
resolution, `git`/`gh`). Tier 2 adds `/decision-memo` (our `docs/decisions/` convention already
matches theirs exactly) and `/claude-md-audit`. Tier 3 (memory-hygiene, design-critique) is
optional. Everything SDD/certlib/`/ship` is explicitly skipped. Net new footprint: ~6 thin command
files, two skill folders, one `docs/breakpoints/` convention, one CLAUDE.md paragraph.

## Background

- **What we have.** Eight skills (`brand-guidelines`, `accounting-ratios`, `docx`, `internal-comms`,
  `pdf`, `pptx`, `skill-creator`, `xlsx`), a mature `docs/decisions/` memo practice using
  `YYYY-MM-DD-<slug>.md`, and an active auto-memory store (`MEMORY.md` + ~12 fact files). No slash
  commands, no subagents.
- **What they have.** A command↔skill split (a thin `.claude/commands/<x>.md` that points to
  `.claude/skills/<x>/SKILL.md` for methodology), a numbered "Principles" set, a **§10 Model
  Routing** convention (Fable for architecture/decisions, Opus for execution, Sonnet/Haiku for
  test gen/fix), and weekly solo-founder rituals (`/monday`, `/retro`) driving toward a launch date.
- **The structural mismatch to respect.** Their repo is a shipping software monorepo with CI, PRs,
  worktrees, and a live database. Ours is course materials on a *semester* cadence, where "ground
  truth" is `recalc.py` returning 0, an Office file validating, and links resolving — not a schema
  query. Every port below is a *retarget*, not a copy.

## Decisions

### Tier 1 — the three Adam named (port first)

#### 1. `/breakpoint` — session pickup prompt

- **Fit: high.** It exists precisely because "CLAUDE.md prose alone gets skipped under load" — we
  just lived that through a `/compact` mid-grading-session. Mechanically captures branch/worktree
  state, unpushed commits, open + merged PRs, task list, and in-flight work into one resume block,
  emitted to the conversation **and** persisted to a dated file.
- **Port as:** a `breakpoint` skill + thin `/breakpoint` command (their split).
- **Tweaks:**
  - Persist to **`docs/breakpoints/<YYYY-MM-DD-HHMM>-<slug>.md`** (they use
    `docs/engineering-rituals/breakpoints/`; we have no such tree). Keep it **gitignored/untracked**
    — it is working state, and this is a public repo (cf. `feedback_emails_gitignored`).
  - **Active-work inputs:** we have no `docs/plans/`. Substitute *in-flight decision memos*
    (`docs/decisions/*` with `status: proposed`) and *open grading passes* (per-offering
    `*/ignore/` dirs, internal `STAGE{N}_GRADES.md`). Keep the git/PR inputs verbatim — grading
    does touch student repos and this repo's PRs.
  - **Strip:** SDD phase language, R-baseline/fresh-volume risk cases, certlib worktree hazards.
  - **Score-privacy guard (add):** the pickup block may name a grading pass in progress but must
    **never** embed score numbers (`feedback_score_privacy`).
- **Model:** leave on the session model — it's mechanical, not judgment-dense.

#### 2. `/suggest-optimal` — one-shot verify-then-pushback review

- **Fit: high, nearly model-agnostic.** Replaces the shorthand *"review, improve, push back, and
  give me the optimal."* Skeptical reviewer of an already-reasoned proposal: verify load-bearing
  claims → endorse what survives → numbered pushback → land ONE optimal → pause for ratification.
  The sibling of `/grill-me` (converge-then-decide vs. one-question-convergence).
- **Port as:** command-only (no separate skill needed; the methodology is short).
- **Tweaks:**
  - **Replace the ground-truth layer.** They verify claims against live Postgres via
    `mcp__ssot-schema-tools`. Ours: grep/read the actual file and cite `file:line`; run
    `scripts/.../recalc.py` (expect 0 errors); validate a changed `.xlsx` with openpyxl and confirm
    every calculated cell is a formula (`feedback_excel_formulas`); confirm referenced paths resolve
    and no links break. This *is* the CLAUDE.md "Goal-driven — verify what done looks like" rule,
    operationalized.
  - **Keep** the Fable pin with Opus fallback and the Verified → Endorse → Pushback → Optimal →
    Pause output contract.
  - **Strip:** SSOT/`db_ssot.json` cautions, certlib memory citations.

#### 3. `/grill-me` — sequential convergence interrogation

- **Fit: high for the *core loop*; the farm version is ~90% certlib and must be gutted.** The
  durable engine is: **one question at a time, always with a recommended answer, pause for the
  human** — used *before* brainstorming to converge decisions before they calcify in a memo or
  restructure. Plus the **Auto-Pushback Pass** (mandatory Pass 1 surfaced in an R-table, a
  threshold-triggered Pass 2, a hard 2-pass cap — human pushback is Pass 3).
- **Port as:** a `grill-me` skill + thin `/grill-me` command.
- **Keep:** core loop, Auto-Pushback Pass mechanic, crystallization triggers (a settled
  hard-to-reverse call → propose a `docs/decisions/` memo inline; a disambiguated term → glossary
  line), exit criteria (three "defer"s in a row → back off).
- **Replace the "Codebase Convergence Check"** — their 15-row certlib/OSP/SSOT anti-pattern table —
  with a lean **"Repo Convergence Check"**: before recommending a *new* course dir, project, stage,
  template, or spreadsheet, grep what already exists (`courses/`, `docs/templates/`,
  `docs/decisions/`, `_archive/`) and prefer extending it. This directly institutionalizes our own
  CLAUDE.md principles ("no speculative restructuring," "surgical changes"). Fold in our grading
  memories as guardrails (`feedback_no_double_deductions`, `feedback_grading_curves`,
  `feedback_score_privacy`).
- **Drop entirely:** SSOT MCP, the `mapping_strategy` taxonomy, OSP-form Layer 1/2 architecture, the
  effectiveness-log CSV, all Reg-cluster PRD references.
- **Model:** Fable-pinned (judgment-dense), matching the farm repo.

### Tier 2 — strong adjacent fits (port alongside, or next)

#### 4. `/decision-memo` — author a memo to house standard

- **Fit: near-perfect.** We *already* write `docs/decisions/YYYY-MM-DD-<slug>.md` in exactly their
  structure (Status/Context/Decision/Rationale/Alternatives-rejected/Consequences). The command adds
  discipline this very memo followed by hand: **grep prior decisions first** (amend vs. supersede),
  verify load-bearing claims, draft to the skeleton, set `status:`, and **pause for ratification**.
- **Tweaks:** point the "grep prior" step at `docs/decisions/` + `_archive/`; drop the
  certlib "Downstream Remap Candidates" section; keep Fable pin. Naming already matches
  (course-specific memos get the `-<course-code>-` infix per CLAUDE.md).

#### 5. `/claude-md-audit` — periodic drift scan

- **Fit: medium.** We have one big CLAUDE.md plus a MEMORY.md index — smaller surface than their
  CLAUDE.md *family*, but drift still bites (a memory naming a moved file; CLAUDE.md citing a path
  that got restructured — we restructure `courses/` often). Retarget the four checks (contradictions
  → stale refs → dup/bloat → hygiene) onto **CLAUDE.md + MEMORY.md + the memory fact files**, and
  verify path citations against the live tree. Read-only; reports and offers fixes.

### Tier 3 — optional / defer

- **`memory-hygiene`** (medium) — we have a live memory store; a validator that catches broken
  `MEMORY.md` index links and dangling `[[refs]]` is genuinely useful, but it ships a
  `validate_memory.py` that would need porting. Recommend only if memory grows past ~25 entries.
- **`/design-critique`** (medium) — reframe their brand-slop critic onto **UH Mānoa** tokens
  (`docs/_branding/design.json`) + the `brand-guidelines` skill; scores branded HTML/pptx/pdf
  output. Nice-to-have, not load-bearing.
- **`/retro` + `/monday`** (low) — solo-founder *weekly* launch cadence; Adam runs a *semester /
  per-stage-deadline* cadence. Only worth it reframed as a per-stage grading retro; defer.

### Explicitly skipped

The entire SDD suite (`sdd-*`), certlib commands (`certlib-*`), `derive-rules`,
`validate-derivation-rules`, `r-baseline`/`r-series-summarize`, `db-migration-playbook`,
`playwright-patterns`, `webapp-testing`, and `/ship` (gated PR merge + Codex triage — our grading
workflow *inspects* student repos, it doesn't merge into this one). All software/database-specific.

## Cross-cutting tweaks (apply to every ported command)

1. **Command↔skill split.** Thin `.claude/commands/<x>.md` (what + args + output) delegating to
   `.claude/skills/<x>/SKILL.md` (methodology), for commands with real procedure (`breakpoint`,
   `grill-me`). `suggest-optimal` and `decision-memo` can be command-only.
2. **Path retargets.** No `docs/plans/`, `docs/engineering-rituals/`, or `reports/`. Persistence →
   `docs/breakpoints/` (untracked). Effectiveness logs → dropped.
3. **Ground-truth swap.** Every `mcp__ssot-schema-tools` / `db_ssot.json` check → `recalc.py`,
   openpyxl xlsx validation, path/link resolution, `git`/`gh`.
4. **Memory citations.** Their `feedback_*` slugs → ours where analogous
   (`feedback_score_privacy`, `feedback_grading_curves`, `feedback_no_double_deductions`,
   `feedback_excel_formulas`), else dropped.
5. **Model routing (optional).** They pin judgment commands to Fable. Suggest the same for
   `/decision-memo`, `/grill-me`, `/suggest-optimal`; leave `/breakpoint` on the session model.
   Flag as optional — this session runs Opus 4.8 and Fable is available. If adopted, add a short
   **§ Model Routing** note to CLAUDE.md so the pins are documented, not mysterious.
6. **CLAUDE.md.** Add one "Slash Commands" paragraph next to "Skills Available" listing the ported
   set, so the command layer is discoverable.

## Alternatives considered

- **Port the whole `.claude` tree.** Rejected — ~80% is certlib/SDD/database noise that would rot
  unmaintained and violate "simplicity first / no speculative restructuring."
- **Do nothing; keep working ad-hoc.** Rejected — the exact failure `/breakpoint` and `/grill-me`
  prevent (handoff prose skipped under load; convergence work pushed onto the human) is one we hit
  regularly, including the compaction earlier this session.
- **Write equivalents from scratch.** Rejected — these are dogfooded, iteration-hardened
  methodologies; retargeting is cheaper and safer than reinventing.

## Consequences

- **New files:** `.claude/commands/{breakpoint,suggest-optimal,grill-me,decision-memo,claude-md-audit}.md`;
  `.claude/skills/{breakpoint,grill-me}/SKILL.md`; a `docs/breakpoints/` dir (gitignored); a CLAUDE.md
  addition (Slash Commands + optional Model Routing).
- **No change** to existing skills, courses, or grading toolchain.
- **Ratifying this memo unblocks:** building Tier 1 first (the three Adam named), getting them in
  front of real use, then deciding Tier 2/3 by whether Tier 1 earns its keep.

## Status

**Accepted** — Adam ratified "build all" on 2026-07-12; all three tiers built the same day.

## Update — built 2026-07-12

All seven commands shipped (Tiers 1–3), each retargeted per the tweaks above:

| Command | Files |
| --- | --- |
| `/breakpoint` | `.claude/commands/breakpoint.md` + `.claude/skills/breakpoint/SKILL.md` |
| `/suggest-optimal` | `.claude/commands/suggest-optimal.md` (Fable-pinned, Opus fallback) |
| `/grill-me` | `.claude/commands/grill-me.md` + `.claude/skills/grill-me/SKILL.md` (Fable-pinned) |
| `/decision-memo` | `.claude/commands/decision-memo.md` (Fable-pinned) |
| `/claude-md-audit` | `.claude/commands/claude-md-audit.md` + `.claude/skills/claude-md-audit/SKILL.md` |
| `/memory-hygiene` | `.claude/commands/memory-hygiene.md` + `.claude/skills/memory-hygiene/SKILL.md` + `validate_memory.py` |
| `/design-critique` | `.claude/commands/design-critique.md` + `.claude/skills/design-critique/SKILL.md` |

Supporting scaffolding: `docs/breakpoints/` convention (README tracked, contents gitignored),
`.claude/commands/README.md` index + model-routing note, and a CLAUDE.md "Slash Commands"
section. `validate_memory.py` verified against the live store (12 memories, 0 errors, 6 warnings —
all pre-existing memory-store drift the validator is designed to surface, left for a future
`/memory-hygiene` pass). Every path the commands cite was confirmed to resolve.
