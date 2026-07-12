---
name: breakpoint
description: Emit a structured "pickup prompt" before a context break so work survives compaction or a new session. Auto-activates when running `/breakpoint`, when the user says "pickup prompt", "breakpoint", "hand off", "checkpoint this", or is about to run `/compact` or `/clear` mid-task. Reads git, open/merged PRs, branch/worktree state, the task list, and in-flight decision memos + grading passes, then writes a copy-paste-ready resume block to the conversation AND persists it to a dated file. CLAUDE.md prose alone gets skipped under load — this makes the handoff mechanical.
tools: Bash, Read, Write, Glob, Grep
---

# `/breakpoint` — Session pickup prompt

A breakpoint captures **everything a fresh session needs to resume without re-reading the whole transcript**, in one structured block. The output is the deliverable: it goes into the conversation **and is persisted to a dated file** so it survives `/compact` or seeds the next session even if the conversation context is lost entirely.

Direction is *forward and lateral*: what's done, what's in flight, what's blocked, where to pick up.

This repo is course materials, not shipping software — so "work in flight" means an active grading pass, a `docs/decisions/` memo mid-draft, or a course restructure, not a CI pipeline. The inputs below are retargeted accordingly.

## When to break

Strong signals to checkpoint (the skill should fire on any of these):

- The user says "pickup prompt", "breakpoint", "hand off", "checkpoint", or is about to `/compact` / `/clear`.
- **A grading pass is mid-flight** — `STAGE{N}_GRADES.md` partially written, some students scored and some not.
- **End of a phase** — a course restructure or a multi-file `git mv` just landed, before starting the next.
- **Before a risky operation** — a `git mv` restructure of `courses/`, an archive move, a force-push, a worktree teardown.
- Context is getting long and a compaction is likely.

When in doubt, ask; don't force it.

## Inputs (gather in this order; skip a line silently if the command errors or returns nothing)

1. **Current branch + worktree state.** `git branch --show-current`, `git status --short`, `git worktree list`. Note which branch each worktree holds. **Count worktrees and flag concurrent-session hazards** — more than a couple usually means another session shares the repo; a worktree nested inside `.claude/` is the nested-creation gotcha.
2. **Uncommitted / unpushed work — scope to THIS session's branch, not all local branches.**
   - Dirty tree: `git status --short`.
   - Unpushed commits on the current branch: `git rev-list --count @{u}..HEAD` (or `git log @{u}..HEAD --oneline`); if there's no upstream, the branch itself is unpushed.
   - **Do NOT use `git log --branches --not --remotes`** — it sweeps *every* local branch (including other sessions' work) and produces a misleading pile of "unpushed commits" that isn't yours.
   - Unpushed work is the highest-loss-risk state — surface it first, but only the work that's actually *yours*.
   - **Untracked stray files** (`git status --short` `??` lines) — this repo routinely has untracked `.claude/worktrees/` and draft memos; note which are intentional scratch vs. work that needs committing, so the next session doesn't blind-`git add`.
3. **Open PRs + their state.** If `gh` is available: `gh pr list --state open --author "@me" --json number,title,headRefName,baseRefName,isDraft` and, for each relevant PR, `gh pr checks <n>`. Capture stack relationships (base → head) explicitly.
4. **Recently merged PRs** (last ~24h or this session): `gh pr list --state merged --limit 10 --json number,title,mergedAt` — so the next session doesn't re-do landed work.
5. **Task list state.** Read the current task list (in-progress / pending / completed). If empty but work is clearly mid-flight, reconstruct from the transcript.
6. **In-flight decision memos + plans.** `Glob docs/decisions/*.md` (most recent first); flag any with `status: proposed` that this session is executing or that await ratification. Quote the memo's open question, don't paraphrase.
7. **Active grading passes.** If a grading task is live: which offering, which stage, which `STAGE{N}_GRADES.md`, how many students scored vs. remaining, whether the post-deadline sweep has run (`feedback_regrade_policy` — a stage locks once its sweep runs). **Never copy score numbers into the pickup block** (`feedback_score_privacy` — scores live only in the internal grades file and instructor email).
8. **Standing constraints.** Grading/house rules governing the current work (relevant `feedback_*` memories, a locked decision memo). Quote the constraint.

## Output — the pickup prompt

Emit the block below **to the conversation** (so it's in context before `/compact`) **and write the same block to a file** (see "Persist & archive"). Keep it terse — roughly one screen. Omit a section entirely if genuinely empty (don't pad with "N/A").

```markdown
## 🔖 Pickup Prompt — <YYYY-MM-DD HH:MM> — <one-line what-we're-doing>

**Resume entry point:** <the single first action the next session should take>

### Branch / worktree state
- On `<branch>` (worktree `<path>` if not primary). Tree: <clean | N files dirty>.
- Unpushed local commits: <none | sha + subject list>.
- Untracked strays: <list, flag intentional-scratch vs. needs-commit>.
- Worktrees live: <list, or "none">.  ⚠️ <concurrent-session caveat if relevant>

### Open PRs (stack order)
- #<n> `<title>` — base `<base>` ← head `<head>` — checks: <pass/fail/running>
- (note stacked relationships explicitly; merge order bottom-up)

### Merged this session
- #<n> `<title>`  (so we don't redo it)

### In-flight docs / grading
- Decision memo `<slug>` — status: <proposed>, open question: <quote>.
- Grading: <offering> Stage <N> — <M scored / K remaining>, sweep <run | not run>.  (no scores here)

### Task status
- ✅ <done>
- 🔄 <in progress — and exactly where it stopped>
- ⏳ <pending / blocked — on what>

### Standing constraints (do not violate)
- <quoted house rule / locked memo / scope boundary>
```

Close with one terminal line: `Breakpoint captured + persisted to <path> (<M> superseded archived) — <N> open PRs, <N> unpushed commits, resume at: <entry point>. Run /compact next.`

## Edge cases & constraints

- **Unpushed commits are the priority signal.** If the scoped check from input #2 shows unpushed commits, lead with them and recommend pushing before `/compact` — local-only commits are the thing most easily lost across a session boundary. Use the scoped check, never the all-branches sweep.
- **Score privacy is absolute.** A pickup block may name a grading pass in progress but must **never** embed a score number, a curved result, or a floor calculation (`feedback_score_privacy`). Those live only in the internal `STAGE{N}_GRADES.md` and instructor email.
- **Concurrent sessions.** If `git worktree list` shows multiple worktrees or `git status` looks unexpectedly dirty, flag it and name which branch each worktree holds.
- **Don't mutate state.** This skill is read-only except for the file write below and updating the task list to match reality. Never commit, push, or switch branches as part of a breakpoint.
- **Verify, don't trust handoff prose.** When resuming *from* a prior pickup prompt, re-check branch/PR state at HEAD before acting — the world may have moved.

## Persist & archive

**1. Persist the new breakpoint.** Write the same block emitted to the conversation to:

```
docs/breakpoints/<YYYY-MM-DD-HHMM>-<slug>.md
```

Use a `HHMM` timestamp (not just the date) so multiple breakpoints in a day sort and never collide. `<slug>` names the workstream (e.g. `fin321-stage3-grading`), not the session. Use the Write tool. The `docs/breakpoints/` folder is **gitignored** (only its `README.md` is tracked) — persisting is local housekeeping on a public repo, not a commit, and keeps any score-adjacent context off the tracked tree.

**2. Archive superseded breakpoints.** Sweep `docs/breakpoints/*.md` and move any **superseded** file into `docs/breakpoints/archive/` (create the dir if absent; preserve the filename). A breakpoint is superseded when EITHER a newer breakpoint shares its `<slug>` stem, OR every PR/task its "Resume entry point" tracks is now merged/closed (verify with `gh pr view`, don't assume from prose). **Do NOT archive another active session's live breakpoint** — when unsure, leave it and say so.

```bash
mkdir -p docs/breakpoints/archive
mv docs/breakpoints/<superseded>.md docs/breakpoints/archive/
```

**3. Report what moved.** State in the terminal line how many were archived so an over-eager sweep is visible.

## See also

- `/decision-memo` — capture a ratified decision (forward, canonical).
- Memory: `feedback_score_privacy`, `feedback_regrade_policy`, `feedback_emails_gitignored`.
