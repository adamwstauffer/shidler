# UH Shidler Finance & Economics — Presentation Branding

This directory contains the official slide deck templates and brand
guidelines for Finance and Economics courses at the University of
Hawaiʻi at Mānoa, Shidler College of Business.

The design system is calibrated for **academic course delivery** with an
**investment-banking-conservative aesthetic**: authoritative typography,
subdued color palette, and clean information hierarchy.

---

## Quick Start

### New Deck
1. Navigate to `templates/`
2. Double-click `shidler-finance-dark.potx` **or** `shidler-finance-light.potx`
3. PowerPoint opens a fresh untitled copy — your template is never modified
4. Choose your starting slide layout from the Layout gallery

### Existing Deck — Apply Theme Only (safest)
1. Open your existing `.pptx`
2. **Design tab → Variants dropdown (▾) → Browse for Themes**
3. Select the `.potx` file
4. Colors and fonts update; your layouts and content are preserved

### Existing Deck — Full Master Import
1. Open your existing `.pptx`
2. **View → Slide Master → Insert Slide Master**
3. Browse to and select the `.potx` file
4. The Shidler master is added alongside your existing one
5. Select slides → right-click → **Layout** to reassign to the new master

---

## Which Variant to Use

| Variant | File | Best For |
|---|---|---|
| **Dark** | `shidler-finance-dark.potx` | Lecture delivery, projected presentations, conference talks |
| **Light** | `shidler-finance-light.potx` | Printed handouts, PDF exports, online course materials, reports |

When in doubt: **dark for the room, light for the PDF.**

---

## Slide Layout Library

Both templates include five reusable layouts:

| Layout | Use For |
|---|---|
| **Cover / Title** | Course intro, first slide of each lecture unit |
| **Title & Content** | Standard lecture slide — title + bulleted content |
| **Comparison** | Side-by-side analysis: two theories, two assets, two time periods |
| **Data Visualization** | Charts, tables, regression output, financial statements |
| **Section Divider** | Transitions between major lecture sections |

---

## File Index

```
docs/_branding/
├── README.md                          ← You are here
├── design.json                        ← UH Mānoa design tokens (SSOT for web/UI branding)
├── design-system.html                 ← Interactive design gallery (open in browser)
├── templates/
│   ├── shidler-finance-dark.potx      ← Dark charcoal template
│   ├── shidler-finance-light.potx     ← Light blue-grey template
│   └── shidler-finance-reference.pptx ← Both variants side by side (10 slides)
├── brand/
│   ├── shidler-palette.md             ← Full color specification
│   └── shidler-typography.md          ← Font pairing and sizing guide
└── assets/
    └── (place any logo .png files here)
```

---

## Contributing / Updating

- Templates are maintained in `.potx` format — do **not** commit `.pptx` working
  files as the canonical source
- When updating colors or fonts, edit the Slide Master (View → Slide Master)
  and re-export as `.potx`
- Tag releases by semester: `v2025-spring`, `v2025-fall`, etc.
- Open a PR with a screenshot of the affected slide layouts before merging
  master changes

---

## Contact

Maintained by the Shidler College of Business, Department of Finance.
Questions → open a GitHub Issue in this repository.
