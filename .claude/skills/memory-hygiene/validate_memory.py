#!/usr/bin/env python3
"""Validate the Claude auto-memory store for this repo.

Checks:
  ERROR   - MEMORY.md index line points at a missing file
  ERROR   - a memory file is missing required frontmatter (name)
  WARNING - a memory file is not referenced in MEMORY.md (orphan)
  WARNING - a [[slug]] cross-ref in a memory body has no matching file (dangling)
  WARNING - missing description / metadata.type in frontmatter

Usage:
  python validate_memory.py [--memory-dir DIR] [--strict] [--json]

--memory-dir defaults to ~/.claude/projects/C--GitHub-shidler/memory
--strict makes warnings count toward a non-zero exit
--json prints a machine-readable report instead of text
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

DEFAULT_DIR = Path.home() / ".claude" / "projects" / "C--GitHub-shidler" / "memory"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# MEMORY.md index lines look like: - [Title](file.md) — hook
INDEX_LINK_RE = re.compile(r"\]\(([^)]+\.md)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def parse_frontmatter(text: str) -> dict:
    """Very small YAML-ish frontmatter parser (flat keys + one nested 'metadata')."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm: dict = {}
    current_parent = None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if indent == 0:
            current_parent = None
            if val == "":
                fm[key] = {}
                current_parent = key
            else:
                fm[key] = val.strip('"').strip("'")
        elif current_parent and isinstance(fm.get(current_parent), dict):
            fm[current_parent][key] = val.strip('"').strip("'")
    return fm


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--memory-dir", type=Path, default=DEFAULT_DIR)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    mem_dir: Path = args.memory_dir
    errors: list[str] = []
    warnings: list[str] = []

    if not mem_dir.is_dir():
        print(f"ERROR: memory dir not found: {mem_dir}", file=sys.stderr)
        return 2

    index_path = mem_dir / "MEMORY.md"
    index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    if not index_text:
        errors.append(f"MEMORY.md missing or empty at {index_path}")

    # files on disk (exclude the index itself)
    fact_files = sorted(
        p for p in mem_dir.glob("*.md") if p.name != "MEMORY.md"
    )
    fact_names = {p.name for p in fact_files}
    # A [[slug]] cross-ref points at another memory's frontmatter `name:` slug
    # (per the memory convention), so resolve against those. Fall back to file
    # stems for stores that haven't adopted the name: field yet.
    fact_slugs = {p.stem for p in fact_files}
    for p in fact_files:
        fm_name = parse_frontmatter(p.read_text(encoding="utf-8")).get("name")
        if isinstance(fm_name, str) and fm_name:
            fact_slugs.add(fm_name)

    # 1. index links -> file exists
    indexed = set()
    for link in INDEX_LINK_RE.findall(index_text):
        target = link.split("/")[-1]
        indexed.add(target)
        if target not in fact_names:
            errors.append(f"MEMORY.md links to missing file: {target}")

    # 2. per-file frontmatter + orphan check
    for p in fact_files:
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if "name" not in fm:
            errors.append(f"{p.name}: missing required frontmatter key 'name'")
        if "description" not in fm:
            warnings.append(f"{p.name}: missing description")
        meta = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
        if "type" not in meta:
            warnings.append(f"{p.name}: missing metadata.type")
        if p.name not in indexed:
            warnings.append(f"{p.name}: not referenced in MEMORY.md (orphan)")

        # 3. dangling [[wikilinks]]
        body = FRONTMATTER_RE.sub("", text)
        for slug in WIKILINK_RE.findall(body):
            slug = slug.strip()
            if slug not in fact_slugs:
                warnings.append(f"{p.name}: dangling [[{slug}]]")

    if args.json:
        print(json.dumps({"errors": errors, "warnings": warnings}, indent=2))
    else:
        for e in errors:
            print(f"ERROR   {e}")
        for w in warnings:
            print(f"WARNING {w}")
        print(
            f"\n{len(fact_files)} memories, {len(errors)} errors, {len(warnings)} warnings."
        )

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
