# UH Mānoa Design System

**Version:** 1.0  
**Last Updated:** 2026-02-13  
**Status:** Active  
**Source:** [University of Hawaiʻi at Mānoa Brand Style Guide](https://manoa.hawaii.edu/brand/)

---

## Overview

This directory includes the **University of Hawaiʻi at Mānoa** design tokens and interactive design gallery. Use them when building UH-branded interfaces (e.g., campus tools, institutional sites, or UH-specific features within this repo).

| File | Purpose |
|------|---------|
| [design.json](./design.json) | Design tokens: colors, typography, spacing, components (SSOT for UH branding) |
| [design-system.html](./design-system.html) | Interactive design gallery: brand principles, color swatches, typography, and UI components |

---

## How to Use

### Design tokens (`design.json`)

- **In code:** Read the JSON for colors, font families, spacing, and component specs. Use values directly in CSS, Tailwind config, or component props.
- **In specs:** Reference `design.json` when writing UX specs or mockups that must follow UH branding.
- **Key tokens:**
  - **Primary:** Green `#024731`, Black `#000000`
  - **Secondary:** Silver `#B2B2B2`, White `#FFFFFF`
  - **Typography (web):** Open Sans (Bold H1/H2, Semibold H3/H4, Regular body)
  - **Components:** Buttons, inputs, cards, badges, tabs (see `components` in the JSON)

### Interactive gallery (`design-system.html`)

- **Local:** Open in a browser (no server required). Double-click the file or run:
  ```bash
  # Windows (PowerShell)
  start docs/specs/05-frontend/ui/design-system.html

  # macOS / Linux
  open docs/specs/05-frontend/ui/design-system.html
  ```
- **Content:** Brand principles, primary/secondary colors, UH green scale, typography samples, buttons, badges, inputs, tabs, sample cards/table, and accessibility notes.

---

## How to Integrate into `.claude/skills`

You can surface UH branding to Claude in two ways.

### Option A: New skill for UH branding (recommended)

Create a dedicated skill so Claude uses UH tokens only when working on UH-branded UI.

1. **Create the skill directory and file:**
   ```
   .claude/skills/brand-guidelines/
   └── SKILL.md
   ```

2. **In `SKILL.md`**, set:
   - **name:** `brand-guidelines`
   - **description:** e.g. *"Enforces University of Hawaiʻi at Mānoa design system (design_uh.json) when creating or modifying UH-branded frontend components, styles, or interfaces."*
   - **Design system location:** `docs/specs/05-frontend/ui/design_uh.json`
   - **When to use:** Creating UH-branded pages, campus tools, or any UI that must follow UH Mānoa brand (colors, typography, accessibility).
   - **Instructions:** Tell Claude to read `design_uh.json` before implementing UH UI; use primary green `#024731`, black, silver, white; Open Sans for web; and ADA contrast/accessibility rules from the JSON.

3. **Register the skill** in your Cursor/Claude config (e.g. in `.cursor/settings` or your agents’ skill list) so it appears in the skill list. Reference the skill by name (e.g. `brand-guidelines`) in prompts or command files when the task is UH-specific.

### Option B: Extend the existing `brand-guidelines` skill

If you want a single “brand guidelines” skill that can switch context:

1. **Edit** `.claude/skills/brand-guidelines/SKILL.md`.
2. **Add a section** such as “Alternate design system: UH Mānoa” that states:
   - When the user or task specifies **UH** or **University of Hawaii** branding, use **`docs/specs/05-frontend/ui/design_uh.json`** as the SSOT instead of `design.json`.
   - List UH primary colors (#024731, #000000), secondary (silver, white), and Open Sans.
   - Link to this README and to `design-system.html` for reference.

3. **Optional:** In commands that generate UI (e.g. `/scaffold-ui`, `/preview-ux`), add a note or flag: “For UH branding, use design.json and brand principles.”

Use **Option A** when you have distinct UH vs lioS flows; use **Option B** when you want one skill and context-dependent behavior.

---

## How to View the HTML File via GitHub

GitHub shows HTML as source code, not as a rendered page. To view **design-system.html** as a live page:

### 1. GitHub HTML preview services

Use a viewer that fetches the **raw** file URL:

1. On GitHub, open **design-system.html** and click **Raw** (or copy the raw URL).
2. Raw URL shape:
   ```
   https://raw.githubusercontent.com/<owner>/<repo>/<branch>/docs/specs/05-frontend/ui/design-system.html
   ```
3. Use one of these (replace with your repo’s raw URL as needed):
   - **htmlpreview.github.io:**  
     `https://htmlpreview.github.io/?https://raw.githubusercontent.com/<owner>/<repo>/<branch>/docs/specs/05-frontend/ui/design-system.html`
   - **htmlviewer.github.io:**  
     Open [htmlviewer.github.io](https://htmlviewer.github.io/) and paste the raw URL, or try:  
     `http://htmlviewer.github.io/?<raw-url>`

**Note:** Some viewers block mixed content or strict CSP. If the page doesn’t load (e.g. Tailwind CDN), try “Download” and open the file locally.

### 2. GitHub Pages (if you use it)

If the repo has GitHub Pages:

- Put the file in the Pages source (e.g. `docs/` or a branch), or
- Build a small site that links to `design-system.html`.

Then open:  
`https://<owner>.github.io/<repo>/path/to/design-system.html`

### 3. Open locally after clone

```bash
git clone <repo-url>
cd <repo>
# then open the file in your browser (see “How to Use” above)
```

---

## Quick Reference

| Item | Value |
|------|--------|
| Primary green | `#024731` |
| Black | `#000000` |
| Silver | `#B2B2B2` |
| Web font | Open Sans (Bold / Semibold / Regular) |
| Design tokens | [design.json](./design.json) |
| Interactive gallery | [design-system.html](./design-system.html) |
| Official brand guide | [manoa.hawaii.edu/brand](https://manoa.hawaii.edu/brand/) |

---

## Related Docs

- **UH brand source:** [University of Hawaiʻi at Mānoa Brand Style Guide](https://manoa.hawaii.edu/brand/)

