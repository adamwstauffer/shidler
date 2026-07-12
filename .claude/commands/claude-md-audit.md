# `/claude-md-audit` — Audit CLAUDE.md + memory for drift

Run periodically (monthly, or right after a `courses/` restructure) — **not** on every change. Detects stale path citations, cross-file contradictions, duplicated facts, and bloat across CLAUDE.md and the memory store.

## What this command does

You audit the canonical instruction + memory surface (`CLAUDE.md`, `MEMORY.md`, and the memory fact files) and produce a findings report. You are **read-only by default** — you report and *offer* fixes; you don't rewrite without approval.

Follow the methodology in `.claude/skills/claude-md-audit/SKILL.md` end-to-end: run all four checks (stale refs → contradictions → dup/bloat → structural hygiene), group findings by severity with `file:line` + suggested fix, and route anything you don't fix this session into the report so it isn't lost.

## Why a ritual, not a per-change rule

A "check CLAUDE.md on every commit" instruction is the most-skipped kind of rule. Drift is better prevented by **single-sourcing** facts (one home + pointers) and caught by this **periodic** scan — especially after this repo's frequent `courses/` restructures.

## Output

A severity-grouped findings report, ending with:
`CLAUDE.md audit: <N> stale refs / <N> contradictions / <N> dup-or-bloat / <N> hygiene. <recommendation>.`
