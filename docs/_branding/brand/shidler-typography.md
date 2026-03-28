# Shidler Finance — Typography Guide

## Font Pairing

| Role | Font | Rationale |
|---|---|---|
| **Headings** | Garamond | Classic serif — authoritative, academic, reads well at large sizes. Evokes established financial institutions (think annual reports, prospectuses). |
| **Body / UI** | Source Sans Pro | Clean humanist sans-serif — high legibility at small sizes, free via Google Fonts, pairs without competing with Garamond. |

---

## Size Scale

Use these exact sizes. Do not freestyle — consistency across a deck
matters more than any individual slide looking "better" with a different size.

| Element | Size | Weight | Color |
|---|---|---|---|
| Cover title | 44pt | Bold | Title color |
| Cover subtitle / course code | 20pt | Regular | Gold accent |
| Cover meta (professor, semester) | 18pt / 16pt | Bold / Regular | Body / Meta |
| Slide title | 32pt | Bold | Title color |
| Section divider title | 36pt | Bold | Title color |
| Section description | 16pt | Regular | Accent / subtitle |
| Body bullet (level 1) | 18pt | Regular | Body color |
| Body bullet (level 2 / sub-point) | 16pt | Regular | Meta color |
| Inline emphasis | 18pt | **Bold** | Gold accent |
| Table header | 14pt | Bold | White on green |
| Table body | 14pt | Regular | Body color |
| Caption / footnote / source | 14pt | Italic | Meta color |
| Footer / confidentiality | 12pt | Regular | Footer text color |

> **14pt is the absolute minimum** for any text that appears on screen.
> Never go below 14pt — it becomes illegible when projected.

---

## Bullet Style

Level 1 bullets use a **filled small square** (U+25AA) rather than
the standard circle bullet. This reads as more structured and formal.

Level 2 sub-points use an **en dash** (U+2013) indented to 0.4".

```
Main point                     (18pt, body color)
   Supporting sub-point        (16pt, meta color, indented)
```

Do **not** use:
- Standard round bullets — too casual
- Numbered lists unless you are explicitly sequencing steps
- Emoji or Unicode symbols as icons — use the Microsoft icon library instead

---

## Emphasis Convention

For **inline emphasis** within a bullet (a key term, a formula variable,
a highlighted finding), use **bold + gold accent color**. Do not use
italics alone for emphasis — it is too subtle on projected slides.

Example:
> The net present value equals **NPV** when the discount rate equals the
> internal rate of return, i.e., **IRR = r**.

---

## Font Availability

### Garamond
- Bundled with Microsoft Office on Windows and macOS
- If unavailable, acceptable fallbacks in order: **EB Garamond** (Google
  Fonts, free), **Palatino Linotype**, **Book Antiqua**

### Source Sans Pro
- Free via Google Fonts
- Also available as **Source Sans 3** (updated version, same metrics)
- If unavailable, acceptable fallbacks: **Calibri**, **Open Sans**

### Embedding Fonts for Distribution
Before sharing a `.pptx` or `.potx`:
**File → Options → Save → check "Embed fonts in the file"**
Select "Embed only the characters used in the presentation" to keep
file size manageable.

---

## Heading Alignment by Layout

| Layout | Title Alignment |
|---|---|
| Cover / Title Slide | Centered |
| Section Divider | Centered |
| Title & Content | Left |
| Comparison | Left |
| Data Visualization | Left |
| Title Only | Left |

> Centered titles on cover/divider slides feel ceremonial.
> Left-aligned titles on content slides anchor the eye for reading.

---

## Line Spacing

| Context | Setting |
|---|---|
| Slide titles | Single (auto) |
| Body bullets level 1 | 28pt exact (`<a:spcPts val="2800"/>`) |
| Body bullets level 2 | 24pt exact (`<a:spcPts val="2400"/>`) |
| Space before each paragraph | 2pt (`<a:spcPts val="200"/>`) |
| Cover subtitle lines | 4pt before each (`<a:spcPts val="400"/>`) |

Generous line spacing is intentional — slides projected in a 200-seat
lecture hall need more breathing room than a printed document.
