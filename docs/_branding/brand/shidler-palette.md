# Shidler Finance — Color Palette

## Design Philosophy

The palette is derived from **University of Hawaiʻi at Mānoa's official
brand colors** (forest green + white) and extended with investment-banking
conservative tones: charcoal backgrounds, muted gold accents, and slate
neutrals. Colors are intentionally subdued — no primaries, no neons.

---

## Primary Brand Colors

| Role | Name | Hex | Usage |
|---|---|---|---|
| **UH Green** | Forest Green | `#1B5E40` | Header bands, badges, accent strips — both variants |
| **Muted Gold** (dark) | Antique Gold | `#B39B5E` | Accent text, divider lines on dark backgrounds |
| **Muted Gold** (light) | Deep Gold | `#8A6F3A` | Accent text, divider lines on light backgrounds |

> The gold is inspired by UH Mānoa's secondary palette and deliberately
> desaturated to read as "serious" rather than celebratory.

---

## Dark Variant (`shidler-finance-dark.potx`)

| Role | Hex | Notes |
|---|---|---|
| Slide background | `#1C1F26` | Deep charcoal — not pure black |
| Gradient end | `#15171D` | Subtle top-to-bottom darkening |
| Title text | `#E8E6E1` | Warm off-white — easier on eyes than pure white |
| Body text | `#C5C0B8` | Warm light gray |
| Sub-point / meta text | `#B0AAA0` | Slightly dimmer than body |
| Emphasis (bold inline) | `#B39B5E` | Antique gold — draws eye without shocking |
| Footer bar bg | `#152018` | Near-black with green undertone |
| Footer text | `#7A7568` | Muted gray — legal/confidentiality note level |
| Left accent strip | `#1B5E40` → transparent | Fade-to-transparent green gradient |
| Bottom rule | `#B39B5E` at 60% opacity | Subtle gold hairline |

### Dark Theme Roles (OOXML `<a:clrScheme>`)

| Slot | Hex | Mapped To |
|---|---|---|
| `dk1` | `E8E6E1` | Primary text |
| `lt1` | `1C1F26` | Primary background |
| `dk2` | `B0AAA0` | Secondary text |
| `lt2` | `2D3340` | Secondary background / card bg |
| `accent1` | `1B5E40` | UH Green |
| `accent2` | `B39B5E` | Antique Gold |
| `accent3` | `4A6274` | Slate Blue |
| `accent4` | `7A7568` | Warm Gray |
| `accent5` | `3D7A6E` | Muted Teal |
| `accent6` | `7A3B3F` | Deep Burgundy |

---

## Light Variant (`shidler-finance-light.potx`)

| Role | Hex | Notes |
|---|---|---|
| Slide background | `#F0F2F5` | Soft blue-grey — cooler than warm white |
| Title text | `#1C2733` | Near-black with blue undertone |
| Body text | `#2D3A47` | Dark slate |
| Sub-point / meta text | `#374151` | Mid slate — still clearly readable |
| Emphasis (bold inline) | `#8A6F3A` | Deep gold — higher contrast than `#B39B5E` on light bg |
| Subtitle / section desc | `#2D6A4F` | Dark green — readable on light bg |
| Footer bar bg | `#CBD5E1` | Light blue-grey rule |
| Footer text | `#4A5568` | Dark slate — legible on light bar |
| Column divider | `#1B5E40` | Solid UH green for visibility |
| Divider rules | `#1B5E40` | Green replaces gold on light backgrounds |

---

## Contrast Ratios (WCAG Reference)

| Foreground | Background | Ratio | AA Pass |
|---|---|---|---|
| `#E8E6E1` on `#1C1F26` | Dark title | ~12:1 | AAA |
| `#C5C0B8` on `#1C1F26` | Dark body | ~8:1 | AAA |
| `#B39B5E` on `#1C1F26` | Dark gold accent | ~4.6:1 | AA |
| `#1C2733` on `#F0F2F5` | Light title | ~14:1 | AAA |
| `#2D3A47` on `#F0F2F5` | Light body | ~10:1 | AAA |
| `#8A6F3A` on `#F0F2F5` | Light gold accent | ~4.8:1 | AA |
| `#2D6A4F` on `#F0F2F5` | Light green text | ~6.2:1 | AA |

---

## Chart Color Sequence

When creating charts, use accent colors in this order so series are
visually distinct and consistent across all decks:

1. `#1B5E40` — UH Green (primary series)
2. `#B39B5E` — Antique Gold (secondary series)
3. `#4A6274` — Slate Blue (tertiary series)
4. `#3D7A6E` — Muted Teal (quaternary series)
5. `#7A3B3F` — Deep Burgundy (fifth series)
6. `#7A7568` — Warm Gray (sixth / reference series)

> For single-series charts (most common in finance courses), always use
> `#1B5E40`. For two-series comparisons, use Green + Gold.

---

## Do / Don't

**Do**
- Use UH Green (`#1B5E40`) for the header band on every slide
- Use gold sparingly — emphasis text, dividers, and chart accents only
- Keep body text in the designated grays; do not introduce new text colors

**Don't**
- Don't use pure black (`#000000`) or pure white (`#FFFFFF`) as primary
  text colors — they read as harsh in presentation environments
- Don't add new colors outside this palette without updating this file
- Don't use the bright accent colors (`accent5`, `accent6`) for body text
