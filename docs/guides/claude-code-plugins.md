# Claude Code Plugins — Install & Scope Guide

How to install Claude Code plugins from a marketplace and scope them correctly
(per-repo vs. per-user). Captured from the `claude-for-financial-services`
marketplace install in this repo on 2026-05-10.

## TL;DR — Two layers of scope

Claude Code plugins live in **two settings files**, and each layer is
configured separately:

| Layer | File | Scope | What it stores |
|---|---|---|---|
| Marketplace registration | `~/.claude/settings.json` (user) | **All repos on this machine** | Where to find a marketplace (git URL) |
| Plugin enablement | `<repo>/.claude/settings.json` (project) | **This repo only** | Which plugins from that marketplace are active |

Registering a marketplace globally is fine — it doesn't activate anything; it
just makes plugins from that marketplace *available to install*. Enabling
plugins per-repo is what controls activation.

## The install process (what worked)

### 1. Add the marketplace

The marketplace's GitHub repo is `anthropics/financial-services`. The
shorthand `owner/repo` form defaults to SSH, which fails on a machine without
SSH keys configured for GitHub:

```text
git@github.com: Permission denied (publickey).
```

**Fix: use the explicit HTTPS URL:**

```powershell
claude plugin marketplace add https://github.com/anthropics/financial-services
```

Output should end with:

```text
✔ Successfully added marketplace: claude-for-financial-services (declared in user settings)
```

Note: the marketplace's *display name* (`claude-for-financial-services`) is
different from the GitHub repo name (`financial-services`). The display name
is what you reference in `plugin install` commands.

**Verify:** `~/.claude/settings.json` should now contain:

```json
{
  "extraKnownMarketplaces": {
    "claude-for-financial-services": {
      "source": {
        "source": "git",
        "url": "https://github.com/anthropics/financial-services.git"
      }
    }
  }
}
```

### 2. Install plugins to project scope

From inside the repo, install each plugin with `--scope project` so the
enablement entry goes into the repo's `.claude/settings.json` (not your user
profile):

```powershell
claude plugin install financial-analysis@claude-for-financial-services --scope project
claude plugin install investment-banking@claude-for-financial-services --scope project
claude plugin install equity-research@claude-for-financial-services --scope project
claude plugin install pitch-agent@claude-for-financial-services --scope project
claude plugin install gl-reconciler@claude-for-financial-services --scope project
claude plugin install market-researcher@claude-for-financial-services --scope project
```

You can also use the interactive picker — type `/plugin` in Claude Code, open
**Discover**, select each plugin, and choose **Project scope**.

**Verify:** `<repo>/.claude/settings.json` should now have an `enabledPlugins`
block:

```json
{
  "enabledPlugins": {
    "financial-analysis@claude-for-financial-services": true,
    "investment-banking@claude-for-financial-services": true,
    "...": true
  }
}
```

### 3. Reload (don't restart)

```text
/reload-plugins
```

If you see `1 error during load`, run `/doctor` for details. Common causes:
missing plugin in the marketplace (typo in name), or a plugin that requires
auth setup before its MCP servers can come up.

### 4. Commit `.claude/settings.json` to git

```powershell
git add .claude/settings.json
git commit -m "Enable financial-services plugins"
```

Don't commit `.claude/settings.local.json` — that's machine-only overrides.

## What "scoped to this repo" actually means

Once you've done the above:

- **In this repo (`shidler/`):** all 6 plugins activate when you launch
  Claude Code. Their slash commands, skills, and MCP servers are loaded.
- **In any other repo on the same machine:** the marketplace is *known* (so
  you could install plugins from it without re-adding), but no plugins
  activate unless that repo's `.claude/settings.json` also enables them.
- **On a new machine (or for a teammate):** when they clone this repo, Claude
  Code reads `.claude/settings.json`, sees plugins enabled from
  `@claude-for-financial-services`, and prompts them once to trust the
  marketplace. After that the plugins install and load automatically.

In other words: enablement travels with the repo via Git; the marketplace
trust is a per-machine prompt.

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| `Permission denied (publickey)` on marketplace add | CLI tried SSH; you have no GitHub SSH key set up | Use the HTTPS URL: `https://github.com/<owner>/<repo>` |
| `Repository not found` on marketplace add | Wrong repo name (e.g. used display name instead of GitHub repo) | Check the actual GitHub repo name; marketplace display name is in `marketplace.json` inside the repo |
| `Marketplace "X" not found` on plugin install | Marketplace not registered yet, or wrong display name | Run `claude plugin marketplace list` to see registered names |
| Plugin commands don't appear after install | Forgot to reload | Run `/reload-plugins` (or restart Claude Code) |
| `1 error during load` after reload | Plugin MCP server failed (often needs auth) | Run `/doctor`; for finance plugins, many MCP servers require auth via `mcp__plugin_..._authenticate` before they work |
| Plugin available in shidler but not another repo | Enablement is per-repo by design | Run the same `plugin install --scope project` commands in the other repo |

## Quick reference: relevant commands

| Action | Command |
|---|---|
| List registered marketplaces | `claude plugin marketplace list` |
| Add marketplace | `claude plugin marketplace add <url>` |
| Remove marketplace | `claude plugin marketplace remove <name>` |
| List installed plugins | `claude plugin list` |
| Install (project scope) | `claude plugin install <plugin>@<marketplace> --scope project` |
| Install (user scope, all repos) | `claude plugin install <plugin>@<marketplace> --scope user` |
| Uninstall | `claude plugin uninstall <plugin>@<marketplace>` |
| Reload after install/uninstall | `/reload-plugins` (slash command inside session) |
| Open interactive plugin picker | `/plugin` |
| Diagnose load errors | `/doctor` |

## Reference: which plugins are enabled in this repo

See `<repo>/.claude/settings.json`. As of 2026-05-10, this repo enables:

- From `claude-plugins-official`: `superpowers`, `skill-creator`, `github`,
  `claude-md-management`
- From `claude-for-financial-services`: `financial-analysis`,
  `investment-banking`, `pitch-agent`, `gl-reconciler`, `market-researcher`

The full set of plugins available in `claude-for-financial-services` is
listed in that repo's `.claude-plugin/marketplace.json` —
[github.com/anthropics/financial-services](https://github.com/anthropics/financial-services).
Other notable plugins not yet enabled here:
`equity-research`, `private-equity`, `wealth-management`, `fund-admin`,
`operations`, `earnings-reviewer`, `meeting-prep-agent`, `model-builder`,
`kyc-screener`, `valuation-reviewer`, `month-end-closer`, `statement-auditor`,
`lseg`, `sp-global`.
