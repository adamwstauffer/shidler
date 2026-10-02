---
title: "Responding to Instructor PR Feedback — A Stage-5 Checklist"
audience: Students with portfolio repos receiving instructor PR feedback
status: required reading before Stage 5 submission
last_updated: 2026-05-13
related:
  - github-mba-guide.md
  - claude-code-install-for-non-technical-users.md
---

# Responding to Instructor PR Feedback

A short, focused guide for the moment that matters most: the instructor opened a pull request on your portfolio repo and you need to respond to it before Stage 5. The Stage 5 rubric grades **5% of your project score** on how visibly you responded — silence is the failure mode this guide is designed to prevent.

If this is the first time you've encountered a pull request, read **Section 8 of [`github-mba-guide.md`](github-mba-guide.md#8-reading-and-responding-to-a-pull-request-pr) first** — it covers the mechanics (where to click, what each tab means). This guide is the rubric-shaped checklist that goes on top of those mechanics.

---

## What "5% for PR feedback" actually grades

The rubric line is:

> **Stage 2 feedback incorporation (5%)** — Visible response to the instructor's PR comments: revised memo, follow-up memo, or commit history that references the feedback.

Three things matter, in order:

1. **Visibility.** The grader has to be able to *find* your responses. A response that lives only in your head, or only in a Slack DM to a classmate, does not count.
2. **Specificity.** "I addressed the feedback" doesn't earn the points. *"PR comment #3 was held because the company's own 10-K uses this phrasing — see reply on that thread"* does.
3. **Coverage.** Every comment should have a response. Ignoring three comments costs more than rejecting them with reasoning.

You earn the full 5% by being **obvious**, not by being **right** about every comment.

---

## The 4-step workflow

Run this once, the week before Stage 5 is due.

### Step 1 — Open the PR and read every comment, top to bottom

1. Go to your repo on github.com → **Pull requests** tab → click the instructor's PR.
2. **Skim the Conversation tab** for the high-level summary the instructor may have left.
3. **Click "Files changed"** — this is where most inline comments live. Read each comment **in full** before you respond to any of them.

> **Why read all first?** Comments later in the file often clarify or recontextualize earlier ones. You'll respond more accurately if you've seen the whole picture.

### Step 2 — Respond to each comment with one of three patterns

For every comment (general, inline, or "Suggested change"), pick one of these three:

**A. Accept** — the suggestion is correct, apply it.

- For a "Suggested change" block: click **Commit suggestion**. Edit the auto-generated commit message to reference the comment number, e.g., *"Tighten hypothesis 2 per PR comment #3."*
- For a general comment that proposes a change: make the change in the file (via web UI or GitHub Desktop), then **reply on the comment thread**: *"Done in commit `a3f9c12`."*
- Click **Resolve conversation**.

**B. Modify** — the suggestion is in the right direction but you want a different version.

- Reply with your alternative phrasing: *"Going with `growth-stage` instead of `growing` here — same intent, but matches the company's own 10-K wording. Done in commit `a3f9c12`."*
- Make the edit, commit it, push.
- Click **Resolve conversation**.

**C. Reject** — you disagree with the suggestion and are keeping the original.

- Reply with **one or two sentences of reasoning**. Examples:
    - *"Holding the original framing. The 10-K calls this `expansion-stage`; the instructor's `mature-market` framing would imply the wrong life-cycle phase."*
    - *"Keeping the multi-sector scope. Narrowing to consumer staples would defeat the memo's sector-comparison purpose. Took the comment as a prompt to clarify scope in the opening paragraph instead — see commit `b4c2e8d`."*
- Click **Resolve conversation**.

> **A reject with a reason earns more credit than an accept with no commit reference.** The rubric grades visibility and reasoning, not deference.

### Step 3 — Merge the PR (after every comment has a response)

1. Return to **Conversation** tab.
2. Scroll to the bottom. Verify every comment thread shows **Resolved** (collapsed gray bars).
3. Click the green **Merge pull request** button.
4. Edit the merge commit message to summarize: *"Apply Stage 2 instructor feedback — tightened hypotheses 1–2, corrected source citation in para 4, held scope per reply."*
5. Click **Confirm merge**.

### Step 4 — Document the response in your Stage 5 deliverables

This is the step that earns the 5%.

In your **final analysis** (or your **prompt log**), write **one paragraph** pointing the grader at the evidence:

> *"Stage 2 PR feedback was reviewed on {date}. Commits `a3f9c12` and `b4c2e8d` apply the tightening suggested on hypotheses 1 and 2, and commit `f7d8e91` corrects the source citation flagged in PR comment #4. The scope question raised in comment #3 was held — my reply on that thread explains the choice. Full PR is at {URL}."*

That paragraph is sufficient. It does three jobs:

- **Locates the evidence** (specific commit hashes and PR comment numbers)
- **Shows coverage** (every comment is addressed, including the rejection)
- **Demonstrates judgment** (you took some, modified one, rejected one — with reasoning)

If the feedback resulted in a meaningful scope or framing change, you can also write a `docs/decisions/YYYY-MM-DD-{lastname}-stage2-feedback-response.md` memo with more detail. **Not required** — the in-PR comments plus the paragraph above are enough for full credit.

---

## Worked example — a realistic PR response

Say the instructor's PR has four comments:

| # | Comment | Your response | What you do |
|---|---|---|---|
| 1 | "Hypothesis 2 is too broad — consider tightening to a specific sector." | Accept | Edit the hypothesis. Commit: *"Tighten hypothesis 2 per PR comment #1."* Click **Resolve**. |
| 2 | "Suggestion: change `growing market` to `growth-stage market`." (suggested change block) | Modify | Click **Commit suggestion**, but edit the commit message to: *"Apply rephrase from PR comment #2 — kept `growth-stage` per 10-K language."* Click **Resolve**. |
| 3 | "Why exclude Vietnamese companies from the screen?" | Reject | Reply: *"Including them — the screen excluded them because of a data-availability issue I've since resolved. Updated the screen in commit `b4c2e8d`."* (This is a "reject the framing but address the underlying concern" response.) Click **Resolve**. |
| 4 | "Source citation in para 4 looks broken." | Accept | Fix the link. Commit: *"Fix broken citation in para 4 per PR comment #4."* Click **Resolve**. |

Then in your final analysis:

> *"The instructor's Stage 2 PR review was merged on {date}. Three suggestions were applied directly: hypothesis 2 was tightened (`commit a3f9c12`, PR comment #1), the `growth-stage market` rephrase was kept (`commit c5e1d4a`, PR comment #2), and the broken citation in paragraph 4 was fixed (`commit f7d8e91`, PR comment #4). Comment #3 (Vietnamese-company exclusion) was a flag I resolved differently — the original screen excluded them because of a data-availability issue, which is now fixed in `b4c2e8d`. Full PR thread: {URL}."*

This earns full 5%. Total time investment: ~30 minutes for the comment review + ~10 minutes for the paragraph.

---

## Common pitfalls

| Pitfall | Why it costs points | Fix |
|---|---|---|
| Merging the PR without responding to comments | The merge button doesn't *resolve* threads; grader sees unanswered comments | Resolve every thread before merging |
| Generic "thanks, addressed all" reply at the top of the Conversation tab | No commit references, no per-comment specificity | Reply on **each** comment thread individually, with commit hashes |
| Silently ignoring a comment you disagreed with | Reads as oversight, not judgment | Reply with one or two sentences of reasoning and resolve the thread |
| Forgetting to push your commits | The PR shows your replies but not the actual changes | After each commit, click **Push origin** in GitHub Desktop (or `git push` in CLI) |
| Burying the response in your repo without surfacing it in the final analysis | Grader has to hunt for evidence | Add the one-paragraph summary to your final analysis (Step 4 above) |
| Waiting until the night before Stage 5 to respond | Some responses (e.g., a contested scope question) take real thought | Schedule the PR review the week before |

---

## What if I never got a PR from the instructor?

Two possibilities:

1. **Instructor write access isn't set up.** Check Settings → Collaborators on your repo. If `adamwstauffer` is **Pending** or absent, no PRs can be opened. Fix this immediately — see [Section 7 of `github-mba-guide.md`](github-mba-guide.md#7-adding-a-collaborator-granting-the-instructor-write-access).
2. **Your Stage 2 memo had little to flag.** It happens. In that case, write a one-line acknowledgement in your final analysis: *"Stage 2 received light PR feedback — the instructor's review affirmed scope and framing; no commits needed in response. Reviewed PR at {URL}."* That demonstrates awareness and earns most of the 5% line.

---

## Where to go next

- **Need the underlying GitHub mechanics?** [`github-mba-guide.md`](github-mba-guide.md) covers commits, branches, GitHub Desktop, and the PR mechanics this guide assumes.
- **Stuck on a specific PR action?** Paste the situation into [claude.ai](https://claude.ai): *"I'm responding to a PR on my GitHub repo. The instructor left a comment that {summary}. What's the cleanest way to {accept / modify / reject} it visibly so a grader can see my response?"* Claude is a competent PR-mechanics tutor.
