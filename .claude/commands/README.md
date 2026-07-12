# Slash Commands

Repo-tailored slash commands for this course-materials repo. Cherry-picked and retargeted from
the `LiosAg/farm-management-assistant-v2` workflow layer — see
`docs/decisions/2026-07-12-claude-workflow-commands-cherry-pick.md` for the rationale and the
per-command tweaks.

Commands with real procedure delegate to a paired skill in `.claude/skills/<name>/`; the command
file is the thin entry point (what it does, args, output).

| Command | Purpose | Skill | Model |
|---|---|---|---|
| `/breakpoint` | Session pickup prompt before a context break — captures branch/PR/grading state, persists to `docs/breakpoints/` | `breakpoint` | session |
| `/suggest-optimal` | One-shot verify-then-pushback review of a converged proposal; returns THE optimal call | — | Fable → Opus |
| `/grill-me` | Sequential one-question-at-a-time convergence before a memo/restructure/rubric; Auto-Pushback + Repo Convergence Check | `grill-me` | Fable |
| `/decision-memo` | Author a `docs/decisions/` memo to house standard (grep-prior-first, house format, pause for ratification) | — | Fable |
| `/claude-md-audit` | Periodic drift scan of CLAUDE.md + the memory store (stale refs, contradictions, bloat) | `claude-md-audit` | session |
| `/memory-hygiene` | Validate + organize the Claude auto-memory store (`validate_memory.py`) | `memory-hygiene` | session |
| `/design-critique` | Brand-anchored critique of UH Mānoa-branded materials against `docs/_branding/design.json` | `design-critique` | session |

## Model routing

`/suggest-optimal`, `/grill-me`, and `/decision-memo` are **Fable-pinned** (via each command's
`model:` frontmatter) because they are judgment-dense and their output is canonical or
hard-to-reverse. `/suggest-optimal` falls back to Opus (`/model claude-opus-4-8`) if Fable is
unavailable. The rest run on the session model — they're mechanical. This mirrors the source
repo's §10 Model Routing convention; the pins are optional and can be removed if undesired.
