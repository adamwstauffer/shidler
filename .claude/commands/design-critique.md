# `/design-critique <url-or-path>` — Brand-anchored critique of UH-branded materials

Run on demand against a UH Mānoa-branded artifact — an HTML page, a slide deck, a PDF, or branded Markdown — either a file path or a live URL. Bimodal: auto-detects mode from the input shape.

## What this command does

You run as a brand-anchored design critic. You score on five UH-anchored dimensions, flag off-brand and generic "AI-slop" patterns against the tokens in `docs/_branding/design.json`, and emit a fix list ordered by impact (accessibility failures first). You do **NOT** apply fixes — the user does (or a follow-up `brand-guidelines` pass).

Follow the methodology in `.claude/skills/design-critique/SKILL.md` end-to-end: read the brand anchor (`design.json`, `design-system.html`), detect mode (file vs. live URL), run the appropriate extraction (use the `pptx`/`docx`/`pdf` skills for Office artifacts), apply the slop/off-brand flag list, and score the five dimensions.

## Argument

`<url-or-path>` — Either a path (`.html` / `.md` / `.pptx` / `.docx` / `.pdf`) or a `http(s)://` / `localhost:` URL.

## Output

A prioritized critique (to chat, or a `*-design-critique.md` file if the user asks), ending with:
`Design critique: <highest-impact fix>; <N> slop/off-brand flags; scores B/A/H/V/F.`
