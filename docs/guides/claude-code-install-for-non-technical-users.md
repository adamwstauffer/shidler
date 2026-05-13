---
title: "Installing Claude Code — A Plain-English Guide for Non-Technical Users"
audience: Students (especially VEMBA) who have never used a command line
status: optional / supplementary
last_updated: 2026-05-13
related:
  - claude-code-plugins.md
  - student-ai-enhancements.md
---

# Installing Claude Code — A Plain-English Guide

This guide is for students who:

- Have **never used a "terminal" or "command line"** before
- Want to try **Claude Code** (the version of Claude that can read files in your portfolio repo)
- Use **Windows** or **Mac** (the steps differ slightly between them — pick your section)

You **do not need Claude Code to do well in this course.** Every graded assignment can be completed using Claude.ai or ChatGPT in your web browser (this is "Workflow A" in the Stage 4 assignment). Claude Code is faster once you're set up, but it adds steps you can skip.

If you decide it's worth setting up, this guide walks you through it in **about 30 minutes**, with no prior technical experience.

---

## Before you start — what you'll need

- [ ] **A computer** running Windows 10/11 or macOS 12 or newer
- [ ] **About 30 minutes** of uninterrupted time
- [ ] **A Claude account** — free to create, but for Claude Code you'll want **Claude Pro ($20/month)** because the free tier has tight usage limits. Sign up at [claude.ai](https://claude.ai) → click "Upgrade to Pro" in your account settings.
- [ ] **Your GitHub repo URL** from Stage 0 (something like `https://github.com/yourname/shidler`)

> **A note on the $20/month cost.** Claude Pro is optional. If you don't want to pay, you can still complete every course assignment using the free web version of Claude at [claude.ai](https://claude.ai). The CLI (Claude Code) requires a paid Claude account to be useful — the free tier hits rate limits very quickly.

---

## What is a "terminal" and why do I need it?

A **terminal** is a black-and-white window where you type commands one at a time, and the computer types back. It looks intimidating but it's just text in, text out.

Claude Code runs *inside* a terminal. When you "use Claude Code," you:

1. Open the terminal.
2. Type `cd` followed by the path to your repo folder (this moves the terminal into that folder).
3. Type `claude` and press Enter — a Claude conversation appears, *inside* the terminal.
4. Type your prompt. Claude can now read and edit the files in your repo.

That's it. Most of what makes terminals feel scary is just unfamiliarity.

---

## Windows installation

### Step 1 — Open PowerShell

PowerShell is Windows' built-in terminal. You don't need to install it.

1. Click the **Start** button (Windows logo, bottom-left).
2. Type `PowerShell`.
3. Click **Windows PowerShell** in the results — a **normal click**. Do **not** "Run as administrator." Modern Node.js installs put `npm` global packages under your user profile (`%APPDATA%\npm`); an elevated PowerShell can install to a different location that your normal shell can't see later — exactly the "command not found" symptom this guide troubleshoots below. Run everything in a normal PowerShell window unless a step explicitly tells you otherwise.
4. A black-and-blue window opens. You'll see something like `PS C:\Users\YourName>` — that's the **prompt**. It means PowerShell is waiting for you to type a command.

**Success looks like:** A dark window with text. The cursor blinks after a `>` symbol.

### Step 2 — Install Node.js (Claude Code needs this)

Claude Code is built on a tool called Node.js. You install it once.

1. Open your web browser and go to: **[https://nodejs.org](https://nodejs.org)**
2. Click the big green button that says **"LTS"** (Long-Term Support — the stable version, not the experimental one).
3. The installer (`node-vXX.X.X-x64.msi`) downloads to your **Downloads** folder.
4. Double-click the installer.
5. Click **Next** through every screen, accepting defaults. **Do not change any settings.**
6. Click **Install**, then **Finish** when it's done.

**To verify it worked:** Close the PowerShell window and open a **new** one (Step 1 again). Type:

```powershell
node --version
```

Press Enter. You should see something like `v22.10.0`. The exact number doesn't matter — what matters is that you see a number, not an error.

**If you see an error like "command not found":** Restart your computer and try again. Windows sometimes needs a reboot to recognize newly installed programs.

### Step 3 — Install Claude Code

In the same PowerShell window, type **exactly**:

```powershell
npm install -g @anthropic-ai/claude-code
```

Press Enter. You'll see scrolling text for 30 seconds to 2 minutes. Wait until you see the prompt (`PS C:\...>`) appear again.

**To verify it worked**, type:

```powershell
claude --version
```

Press Enter. You should see a version number.

**If you see "claude: command not found":** Close PowerShell and open a fresh window, then try again.

### Step 4 — Sign in to Claude

Type:

```powershell
claude
```

Press Enter. The first time you run it, Claude Code will:

1. Show you a welcome message.
2. Open your default web browser to a Claude sign-in page.
3. Ask you to log in to your Claude account.
4. After you sign in, the browser shows "You can close this window" — close it.
5. Return to PowerShell. Claude Code is now signed in.

**Success looks like:** A prompt appears inside PowerShell showing `> ` and waiting for your input. You're now talking to Claude.

To exit, type `/exit` and press Enter, or just close the PowerShell window.

### Step 5 — Try Claude in your repo

You're set up. Now use it inside your portfolio repo.

1. Find your repo folder on your computer. It's wherever you cloned it from GitHub (often `C:\Users\YourName\Documents\GitHub\shidler` or similar).
2. In PowerShell, **change directory** to your repo. Type:

   ```powershell
   cd "C:\Users\YourName\Documents\GitHub\shidler"
   ```

   (Replace the path with your actual repo path. The quotes are needed if your path has spaces.)

   Press Enter. The prompt should now show your repo path: `PS C:\Users\YourName\Documents\GitHub\shidler>`

3. Start Claude:

   ```powershell
   claude
   ```

4. Once Claude opens, ask it:

   ```
   List the files in this repo and tell me what kind of project it is.
   ```

   Claude will read your repo and answer.

You're done.

---

## Mac installation

### Step 1 — Open Terminal

Terminal is Mac's built-in command line. You don't need to install it.

1. Press **Command (⌘) + Space** to open Spotlight search.
2. Type `Terminal` and press Enter.
3. A white (or dark) window opens. You'll see a prompt ending in `$` — Terminal is ready.

**Success looks like:** A window with text. The cursor blinks after a `$` symbol.

### Step 2 — Install Node.js (Claude Code needs this)

The easiest way on Mac is to use **Homebrew**, a package manager. (If you've never heard of it, that's fine — follow the steps.)

1. In Terminal, paste this **exactly**, then press Enter:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Homebrew will install. It may ask for your Mac password — type it and press Enter (the password won't appear as you type — this is normal).
3. When it finishes (5–10 minutes), Homebrew prints two lines you need to copy and paste. They look like:

   ```bash
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

   Copy both lines from the output of *your* Homebrew install (not these — these are examples), paste them into Terminal, press Enter.

4. Now install Node.js:

   ```bash
   brew install node
   ```

5. Press Enter and wait (1–2 minutes).

**To verify it worked**, type:

```bash
node --version
```

Press Enter. You should see something like `v22.10.0`. If you see a number, you're done with Step 2.

### Step 3 — Install Claude Code

In Terminal:

```bash
npm install -g @anthropic-ai/claude-code
```

Press Enter. You'll see scrolling text for 30 seconds to 2 minutes. Wait until the `$` prompt reappears.

**Verify** with:

```bash
claude --version
```

You should see a version number.

### Step 4 — Sign in to Claude

```bash
claude
```

Same flow as Windows: a browser opens, sign in to Claude, close the browser tab, return to Terminal. Claude Code is now signed in.

### Step 5 — Try Claude in your repo

1. Find your repo. On Mac it's usually at `~/Documents/GitHub/shidler` or wherever you cloned it.
2. Change directory:

   ```bash
   cd ~/Documents/GitHub/shidler
   ```

3. Start Claude:

   ```bash
   claude
   ```

4. Ask:

   ```
   List the files in this repo and tell me what kind of project it is.
   ```

Done.

---

## Vietnam-specific notes

- **VPN may be needed** to install `npm` packages from corporate networks where outbound traffic is filtered. If `npm install` hangs for more than 5 minutes with no output, try from a personal network.
- **VAS-formatted financial statements** are fine to feed Claude Code; it will not assume U.S. GAAP unless you tell it to.
- **Bilingual prompts** work. You can prompt Claude in Vietnamese; the output will be in Vietnamese unless you ask for English. For graded course deliverables, however, output must be **in English** (per the syllabus AI policy).

---

## Common errors and how to fix them

### "command not found: claude"

**Cause:** The installer didn't add Claude Code to your system's command path, or you ran the install and then tried `claude` without opening a new terminal.

**Fix:** Close the terminal window entirely. Open a fresh one. Try `claude --version`. If still broken, run the install command (Step 3) again.

### "Permission denied" during install

**Cause (Windows):** Your global `npm` directory is in a system-protected location (this happens with some older Node.js installs, or if Node was installed via a non-default method). Modern Node.js LTS installs *should* put npm-global under `%APPDATA%\npm` and not need elevation — if you're hitting this, that's the exception, not the rule.
**Fix (in order):**

1. **Don't reach for "Run as administrator" first.** Elevated installs frequently install packages to a different path your normal PowerShell can't see, which causes the "command not found" symptom right after a "successful" install.
2. **First try:** close all PowerShell windows, open a fresh **normal** one, and re-run the install. The original error sometimes goes away on retry.
3. **If it still fails:** copy the full error text, paste it into [claude.ai](https://claude.ai), and ask: *"I'm installing Claude Code on Windows and getting this Permission denied error. What is the safest way to fix this without breaking my npm configuration?"* Claude will walk you through reconfiguring the npm global directory (`npm config set prefix`).
4. **Last resort:** run PowerShell as administrator (right-click → Run as administrator), run `npm install -g @anthropic-ai/claude-code`, **close that elevated window**, and open a fresh normal PowerShell to test `claude --version`. If the normal shell can't find `claude` after this, the elevated install went to the wrong directory — use option 3 to clean up.

**Cause (Mac):** Homebrew or `npm` doesn't have permission to write to the install directory.
**Fix:** Prefix the install command with `sudo`:

```bash
sudo npm install -g @anthropic-ai/claude-code
```

Mac will ask for your password. Type it (it won't show on screen), press Enter.

### "rate limit exceeded" or "you've used your daily Claude usage"

**Cause:** You're on Claude's free tier and hit the daily limit. Free-tier Claude Code is rate-limited tightly.

**Fix:** Either wait until tomorrow, or upgrade to Claude Pro ($20/month) at [claude.ai](https://claude.ai) → Settings → Plans. The Pro tier dramatically increases your usage allowance.

### Claude opens but says it can't see my files

**Cause:** You're not running Claude from inside your repo folder. Claude Code only sees files in the directory you launched it from (and subdirectories).

**Fix:** Exit Claude (`/exit`). In the terminal, run `cd` followed by the path to your repo, then re-run `claude`.

### "node: command not found" after I just installed Node

**Cause:** Your terminal is using a cached idea of which programs exist.

**Fix:** Close the terminal entirely. Open a new one. Try `node --version` again.

### Browser sign-in opens but Claude Code doesn't notice I signed in

**Cause:** The sign-in handshake failed, often due to firewall or browser settings.

**Fix:** In the terminal, press Ctrl+C to cancel. Restart `claude`. When the browser opens, make sure pop-ups are not blocked. After signing in, return to the terminal — if it still shows "waiting," cancel and try once more.

### "I see a screen full of error text I don't understand"

**The most useful debugging move:** Copy the entire error text, paste it into [claude.ai](https://claude.ai) in your browser, and ask:

> "I'm trying to install Claude Code on [Windows/Mac]. I got this error. What should I do?"

Claude is good at diagnosing install errors. Treat the web version of Claude as your support desk.

---

## What's next

Once Claude Code is working:

- For your **course assignments**, you don't need anything more. Claude Code reads files in your repo; ask it questions, ask it to draft documents.
- If you're curious about **Claude Skills** and **Claude-for-Financial-Services plugins**, see [`student-ai-enhancements.md`](student-ai-enhancements.md) for the next paths.

---

## When to give up and use the browser instead

If after 60 minutes of trying you still can't get Claude Code installed, **stop**. Use the web version at [claude.ai](https://claude.ai) instead. Every assignment in this course can be completed via the browser. Claude Code is a convenience, not a requirement.

If you do give up, that is **not a failure** — it is a reasonable resource allocation. Your time is better spent on the finance analysis than on debugging an install. The web version of Claude is a fully capable tool. The Stage 4 "Workflow A" (Claude desktop / ChatGPT) path is specifically designed to work without any CLI setup.
