---
name: brand-guidelines
description: Applies University of Hawaiʻi at Mānoa official brand colors, typography, and design standards to any artifact that benefits from UH Mānoa's institutional look-and-feel. Use when brand colors or style guidelines, visual formatting, document styling, presentation design, or university design standards apply. Also use when creating materials for Shidler College of Business courses.
license: Complete terms in LICENSE.txt
---

# University of Hawaiʻi at Mānoa Brand Styling

## Overview

To apply UH Mānoa's official brand identity and style resources, use this skill. All materials should reflect institutional quality and create pride of place. For the full design token system, see `docs/_branding/design.json` in the project root.

**Keywords**: branding, UH Mānoa, university identity, visual identity, styling, brand colors, typography, Shidler College of Business, institutional design, ADA accessibility

## Brand Guidelines

### Colors

**Primary Colors:**

- UH Green: `#024731` (Pantone 3435 C) — Primary brand green; logos, headings, key UI elements
- Black: `#000000` — Primary text, borders, contrast

**Secondary Colors:**

- Silver: `#B2B2B2` (Cool Gray 5 C) — Borders, subtle accents, disabled states
- White: `#FFFFFF` — Backgrounds, inverse text, cards on dark

**UH Green Scale (for tints and shades):**

- 50: `#E6F2EF` — Lightest tint, subtle backgrounds
- 100: `#B3D9CF`
- 200: `#80C0AF`
- 300: `#4DA78F`
- 400: `#1A8E6F`
- 500: `#024731` — Primary (full brand green)
- 600: `#023D29`
- 700: `#012E1F`
- 800: `#011E14`
- 900: `#000F0A` — Darkest shade

**Status Colors:**

- Success: `#024731` (UH Green)
- Error: `#B43232`
- Warning: `#B2B2B2` (Silver)
- Info: `#024731`

**Rules:**
- Use only approved palettes — do not create custom palettes or gradients
- Ensure ADA-compliant contrast ratios for all text and UI elements
- Never use red type for body or primary content
- Avoid layouts that are too dark for readability

### Typography

**Heading Fonts:**
- Print: Avenir Bold
- Web/Digital: Open Sans Bold (H1/H2), Open Sans Semibold (H3/H4)
- Fallback: Helvetica, Arial, sans-serif

**Body Fonts:**
- Print: Avenir Book
- Web/Digital: Open Sans Regular
- Fallback: Helvetica, Arial, sans-serif

**Specialized Fonts (limited use):**
- Serif: Minion Pro (print) / Crimson Text (web)
- Collegiate: Freshman
- Script: Gloss & Bloom

**Sizing:**
- Never set body text smaller than 10pt
- Use 11–12pt for audiences that may include older readers
- Generous leading: 3–5pt greater than type size for print
- Alignment: Flush left, ragged right for body text; avoid center or justify for body

### Typography in Documents and Presentations

| Element | Font | Weight | Size |
|---------|------|--------|------|
| H1/H2 | Open Sans | Bold (700) | 24–36pt |
| H3/H4 | Open Sans | Semibold (600) | 18–24pt |
| Body | Open Sans | Regular (400) | 11–14pt |
| Captions | Open Sans | Regular (400) | 10–12pt |

## Features

### Smart Font Application

- Apply Open Sans to headings (Bold for major, Semibold for minor)
- Apply Open Sans Regular to body text
- Fall back to Helvetica or Arial if Open Sans unavailable
- Preserve readability across all systems

### Color Application

- Use UH Green (`#024731`) for primary accents, headings, and key UI elements
- Use Black for body text and borders
- Use Silver (`#B2B2B2`) for secondary/subtle elements
- Use the UH Green scale (50–900) for tints in backgrounds, hover states, etc.
- Maintain ADA-compliant contrast at all times

### Shape and Accent Colors

- Non-text shapes and decorative elements use UH Green and Silver
- Charts and data visualizations should use the UH Green scale for a cohesive palette
- Maintain visual interest while staying on-brand

## Design Principles

1. **Brand Consistency** — Every element should reinforce UH Mānoa's shared identity
2. **Accessibility** — Meet ADA standards in contrast, type size, and layout
3. **Quality and Legibility** — Typography and layout should reflect institutional quality
4. **Pride of Place** — Design supports the university's mission and creates pride in place

## Technical Details

### Font Management

- Use system-installed Open Sans when available
- Provide automatic fallback to Helvetica/Arial
- For best results, pre-install Open Sans in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Primary green RGB: (2, 71, 49)
- Maintains color fidelity across different systems

### Component Defaults

- **Buttons**: UH Green background (`#024731`), white text
- **Focus states**: `0 0 0 3px rgba(2, 71, 49, 0.25)` box shadow
- **Cards**: White background, 1rem border radius, `#E5E5E5` border
- **Links**: UH Green (`#024731`), darker on hover (`#013D26`)

### Reference

For the complete design token system including spacing, shadows, responsive breakpoints, and dark/light mode specifications, see `docs/_branding/design.json`.
