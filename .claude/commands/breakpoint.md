# `/breakpoint` — Emit a session pickup prompt

Run at a context break — before `/compact` or `/clear`, when a grading pass is mid-flight, at the end of a phase, or before a risky `git mv` restructure — to capture everything a fresh session needs to resume.

## What this command does

You produce **one structured pickup prompt** and emit it to the conversation so it survives compaction. You do not change git state. You speak directly — this is a status artifact, not a narrative.

Follow the methodology in `.claude/skills/breakpoint/SKILL.md` end-to-end: gather the inputs in the order specified (branch/worktree state, unpushed commits, open + merged PRs, task list, in-flight decision memos, active grading passes, standing constraints), render the pickup-prompt block exactly, and respect every edge case (unpushed commits lead, stacked PRs rendered bottom-up, concurrent-session caveats flagged, **score numbers never included**, read-only).

## Argument

`[<note>]` — Optional one-line hint about what you're working on, used in the prompt header. If omitted, infer it from the session.

## Output

1. The full `## 🔖 Pickup Prompt` block (to the conversation).
2. The same block persisted to `docs/breakpoints/<YYYY-MM-DD-HHMM>-<slug>.md` (gitignored working state), superseded breakpoints archived in the same pass.
3. One terminal line: `Breakpoint captured + persisted to <path> — <N> open PRs, <N> unpushed commits, resume at: <entry point>. Run /compact next.`
