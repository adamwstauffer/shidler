# Breakpoints — session pickup prompts

This folder holds **session pickup prompts** written by `/breakpoint` (see
`.claude/skills/breakpoint/SKILL.md`). Each file is a structured "resume from here" block
capturing branch/PR state, in-flight decision memos, active grading passes, and the next
action — so work survives a `/compact` or a new session.

## Why the folder is gitignored

Everything here **except this README is gitignored** (see `.gitignore`). Pickup prompts are
transient working state, and on a public repo they can brush up against grading context.
Keeping them local — never committed — is deliberate:

- They reference in-progress grading passes; per `feedback_score_privacy`, score numbers must
  never land on the tracked (public) tree. `/breakpoint` already omits scores, and gitignoring
  the folder is the belt-and-suspenders backstop.
- They go stale fast; there's no value in versioning them.

## Convention

- Filename: `<YYYY-MM-DD-HHMM>-<slug>.md` (HHMM so multiple/day sort and never collide).
- `<slug>` names the workstream (e.g. `fin321-stage3-grading`), not the session.
- Superseded breakpoints move to `archive/` in the same pass (also gitignored).

Run `/breakpoint` before `/compact`, at the end of a phase, or before a risky restructure.
