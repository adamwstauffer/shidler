# AGENTS.md

Conventions for any AI agent (Claude Code, Codex, Copilot, ...) working in this repo.
This file is canonical; `CLAUDE.md` only points here.

## Who I am and what this repo is

I'm an MBA student. This repo is my professional portfolio: each engagement starts with a brief in
`docs/briefs/`, ends with a decision in `docs/decisions/`, and is built from a capability in
`capabilities/`.

## How to work with me

- **I'm the reviewer, you're the doer.** Draft, compute, and propose; I decide what ships.
- **Ask before guessing.** If the brief is ambiguous, say so and stop — don't invent scope.
- **Never invent facts.** No made-up numbers, sources, or experience. Missing data gets a
  `<placeholder>` and a note, not a plausible-looking value.
- **Every number has a source.** Inputs live in `data/` with provenance in `data/README.md`.

## Excel rules

- Every calculated cell is a formula. Only raw inputs may be typed values.
- Inputs are black text on a tan fill on their own sheet; formulas are blue text on light gray. Blue always means calculated, never "type here."
- Recalculate and confirm zero `#REF!` / `#DIV/0!` / `#VALUE!` before saying a model is done.

## Writing rules

- Lead with the answer. A decision memo's first paragraph is the recommendation.
- Write for a manager or senior reviewer: plain language, numbers with units, no jargon dumps.

## Logging

When a session changes a deliverable, add a row to `prompt-log.md`: date, goal, the prompt that
mattered, tool, where the output went, and what I changed afterward.

## Never commit

Anything listed in `.gitignore`: credentials, `.env` files, scratch exports, and anything with
someone else's personal information.
