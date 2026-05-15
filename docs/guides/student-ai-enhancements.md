---
title: "Student AI Enhancements — Above-and-Beyond Guide"
audience: students (all Shidler courses with portfolio repos)
status: optional / ungraded
last_updated: 2026-05-13
related:
  - ../decisions/2026-05-10-claude-plugins-student-rollout.md
  - claude-code-plugins.md
---

# Student AI Enhancements — Above-and-Beyond Guide

This guide is **optional and not graded**. It is for students who have finished the core stage requirements and want to extend their portfolio repo with two industry-relevant tools:

1. **Claude Skills** — small, reusable prompt-and-instruction bundles you author yourself. They let you encode your own workflow ("how I do a DCF", "how I draft a memo") so Claude follows it consistently next time.
2. **Claude for Financial Services plugins** — Anthropic's marketplace of professional finance skills (DCF modeling, pitch-deck QC, competitive-landscape analysis, etc.). Installing one is a way to see how production-grade prompt engineering is packaged.

Neither is required. Nothing about the rubric rewards you for shipping a skill or installing a plugin. The reward is what you learn by trying.

---

## Before you start — honest caveats

- **Claude Pro costs $20/month.** Claude Code's free tier is rate-limited and will not run the heavier plugin skills reliably. The plugins work best with a paid Claude account.
- **Some plugin connectors need enterprise data subscriptions.** The `financial-analysis` plugin ships connectors to FactSet, S&P Global, Moody's, PitchBook, etc. — all require paid credentials students don't have. The skills that work on **public SEC filings, your own Excel files, or repo-stored data** still work fine.
- **You can do all of this without ever installing Claude Code.** The walkthrough prompts below also work in Claude desktop ([claude.ai](https://claude.ai)) and ChatGPT. The CLI is more powerful for repo work; the web app is faster to try.
- **Do not paste your grade, your classmates' work, or any PII** into any AI tool, plugin or otherwise.

---

## Path A — Author your own Claude Skill

Why it matters: a Claude Skill is a tiny artifact (one folder, one Markdown file) that captures *your* opinionated way of doing a task. Once you have one, every future Claude session can use it. This is the same authoring pattern professional teams use; the file format is the same one Anthropic itself ships.

### Walkthrough prompt — paste into Claude desktop or ChatGPT

```
I'm a finance student at the University of Hawai`i at Mānoa. I have a portfolio
repo on GitHub with a few finance artifacts (a populated 3-statement workbook,
a memo, a technical spec). I want to author my first Claude Skill that captures
how I approach [PICK ONE: financial-ratio analysis / DCF valuation / memo drafting /
spec writing] so future sessions of Claude can reproduce my approach.

Walk me through, step by step:

1. What a Claude Skill is, what a SKILL.md file looks like, and what the
   YAML frontmatter must contain.
2. How to decide what belongs in a single skill versus what should be split.
3. How to draft the SKILL.md for my chosen topic, given what's already in my
   repo. Ask me three to five clarifying questions before drafting.
4. Where the skill file should live in my repo (folder structure, naming).
5. How to invoke the skill from a future Claude Code or Claude desktop session.
6. One realistic example of when the skill would have changed Claude's output
   versus a no-skill baseline.

Constraints:
- Keep the SKILL.md under 100 lines for v1.
- The skill must be usable by Claude with zero prior context about my repo —
  it should be self-contained.
- Tell me what NOT to include (anti-patterns).

After we draft v1, I will paste it back and you will critique it as if I
submitted it for code review.
```

### Where to read more

- Anthropic's own `superpowers:writing-skills` skill is the authoritative reference. If you have Claude Code, you can invoke it directly with `/superpowers:writing-skills`.
- The `skill-creator` skill (`/skill-creator:skill-creator` in Claude Code) generates skills interactively.
- Look at the skills already in this repo (`.claude/skills/bus314-accounting-ratios/SKILL.md`) for a working example of the format.

### Where to put your skill

Two options, both legitimate:

- **In your portfolio repo** at `.claude/skills/{your-skill-name}/SKILL.md`. This makes the skill visible to anyone who clones your repo (and to managers, peers, or reviewers who browse it).
- **In your user-level Claude config** at `~/.claude/skills/{your-skill-name}/SKILL.md`. This makes the skill available in every Claude Code session on your machine but invisible to others.

For portfolio purposes, putting it in the repo is the move.

---

## Path B — Install and try a Claude for Financial Services plugin

Why it matters: the `claude-for-financial-services` marketplace bundles 12+ plugins covering DCF, LBO, comps, M&A pitch decks, equity research initiation, GL reconciliation, and more. Installing one is a 5-minute exercise. Running a skill against your own Stage 3 workbook or Stage 4 spec is a 30-minute exercise that will teach you more about prompt engineering than reading an article ever will.

The instructor's full rationale for plugin use, including the constructive-vs-generative distinction (which uses are encouraged, which need disclosure), is in [`docs/decisions/2026-05-10-claude-plugins-student-rollout.md`](../decisions/2026-05-10-claude-plugins-student-rollout.md). Read that first if you plan to use a plugin on a graded deliverable.

The install mechanics (marketplace registration vs. project enablement, the SSH-vs-HTTPS gotcha) are in [`docs/guides/claude-code-plugins.md`](claude-code-plugins.md).

### Walkthrough prompt — paste into Claude Code (CLI)

Run `claude` in your portfolio repo first, then paste:

```
I want to try one Claude for Financial Services plugin against an artifact
already in my portfolio repo. I have Claude Code installed and I'm in my repo.

Walk me through:

1. Confirming Claude Code is set up correctly (which version, signed in, project
   scope working).
2. Adding the claude-for-financial-services marketplace using the HTTPS URL
   (not SSH — explain why this matters).
3. Choosing ONE plugin appropriate for what I have. My repo currently contains:
   [LIST YOUR ARTIFACTS — e.g., a populated Stage 3 workbook for {company},
   a Stage 4 LLM-drafted spec, a Stage 2 memo]. Recommend one plugin (e.g.,
   audit-xls, ib-check-deck, competitive-analysis) and explain why it fits.
4. Installing that plugin at project scope (not user scope) so my classmates'
   repos are unaffected.
5. Verifying the plugin loaded with no MCP-auth errors. Explain what an MCP
   connector is and which connectors will not work for me as a student
   (FactSet, S&P Global, Moody's, etc. — all enterprise-only).
6. Invoking ONE skill from the plugin against ONE of my artifacts. Walk me
   through the prompt I should use.
7. Reading the skill's output critically: which parts are useful, which parts
   are generic, which parts depend on data I don't have.

Then ask me to commit the output of that run to my repo with a clear commit
message explaining what tool I used and what I learned.

Constraints:
- Do not install more than one plugin. The goal is to learn the workflow,
  not to fill my repo with tooling.
- Do not run any skill that would generate the deliverable my course is
  grading me on (e.g., do not use dcf-model to build the DCF that's
  supposed to be my own work).
- Flag, before each step, anything that will cost money (Claude Pro tier)
  or require external accounts.
```

### Walkthrough prompt — paste into Claude desktop (no CLI needed)

If you have not installed Claude Code, you can still understand what the plugins do and read their skill definitions:

```
I'm a finance student exploring the claude-for-financial-services marketplace
without installing Claude Code yet. Walk me through:

1. What a Claude Code "plugin" is, what a "skill" inside a plugin is, and how
   they relate to a "SKILL.md" file I might author myself.
2. The plugins currently available in claude-for-financial-services
   (financial-analysis, investment-banking, pitch-agent, gl-reconciler,
   market-researcher, equity-research) and what each does in one sentence.
3. For my use case ([DESCRIBE: e.g., I am writing a memo recommending whether
   Vinamilk should refinance its USD debt]), which two or three skills would
   be most useful and why.
4. The trade-offs of using each skill versus drafting from scratch:
   - What the skill is likely to do well.
   - What it is likely to do badly (and why I should still review every line).
   - The signs that the output is leaning on data I don't have (e.g., live
     FactSet quotes I can't verify).

End by giving me one specific question I should ask myself before using any
of these skills on a graded deliverable.
```

### After you run a plugin

If you used a plugin on a graded deliverable, log it in your `deliverables/prompt-log.md`:

| Date | Tool | Skill invoked | What you asked it to do | What you kept | What you changed or rejected |
|---|---|---|---|---|---|

The repo's existing AI policy (see your course `README.md` and `CLAUDE.md`) requires you to disclose AI use. Plugin use is AI use.

---

## Path C — Just getting Claude Code set up (no plugins yet)

If Paths A and B feel like jumping ahead, this is the first step.

**For students who have never used a terminal:** see the dedicated step-by-step guide at [`claude-code-install-for-non-technical-users.md`](claude-code-install-for-non-technical-users.md). It walks through Windows and Mac install in ~30 minutes with no prior CLI experience assumed.

**For students who want to skip ahead with an AI walkthrough**, paste into Claude desktop or ChatGPT:

```
I'm a finance student on a [Windows / Mac / Linux] machine. I have a GitHub
account and a portfolio repo I want to clone locally. I have never used a
command line. Walk me through:

1. Installing Claude Code (link me to the official install page; explain what
   it is in one sentence).
2. Signing in to Claude Code from the terminal.
3. Cloning my portfolio repo to my computer (give me the exact `git clone`
   command if I tell you my repo URL).
4. Opening Claude Code in my repo folder (`cd` plus `claude`).
5. Asking Claude Code one simple question that proves the setup works (e.g.,
   "list the files in this repo and summarize what kind of project it is").

For each step, tell me:
- Exactly what to type.
- What I should see if it worked.
- The single most common error and how to fix it.

Stop after Step 5 and let me confirm it worked before suggesting anything else.
Do not try to teach me everything in one prompt.
```

---

## What to write up if you did this

This is the part that turns the exercise into a portfolio artifact:

- Add a `docs/decisions/YYYY-MM-DD-{lastname}-ai-tooling-experiment.md` memo (use the repo memo template) capturing:
  - What you tried (Path A, B, or C).
  - One concrete thing it changed about how you approach your finance work.
  - One thing the tool got wrong that your finance training caught.
  - Whether you would do it again.

A 400-word honest reflection on what an AI tool got wrong is more impressive on a portfolio than a 4,000-word claim that AI "transformed your workflow." Experienced managers and senior reviewers can tell the difference.

---

## A word on the rubric

Nothing in this guide moves your grade. The core stage rubrics — your spec, your model, your memo, your repo polish — are what your grade is built on. This guide exists because the gap between the floor of the rubric and what you could ship is wider than the rubric can grade. If you have the time and curiosity, close some of that gap.

If you finish a path here and want feedback, open an issue or pull request in your portfolio repo and tag the instructor — that's the channel for above-and-beyond work.
