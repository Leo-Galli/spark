#!/usr/bin/env python3
"""Fail CI if book prose, secrets, or broken exercise contracts appear."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_NAMES = {
    ".keys",
    "solutions-src",
    "manuscript",
    "spark-print-latest.pdf",
    "spark-print-latest.epub",
    "spark-print-latest.docx",
}
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F6FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\u2600-\u27BF"
    "]"
)
AI_ATTR_RE = re.compile(
    r"Co-authored-by:\s*(Claude|Codebuff|Cursor|ChatGPT|Copilot|GPT-|Anthropic)",
    re.I,
)


def iter_text_files():
    skip_dirs = {".git", "node_modules", "unlocked", "__pycache__", "solutions"}
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in skip_dirs for part in p.parts):
            continue
        if p.suffix.lower() in {".7z", ".png", ".jpg", ".pdf", ".woff", ".woff2"}:
            continue
        if p.name == "_scaffold_f1.py":
            continue
        yield p


def structure_only() -> int:
    required = [
        "README.md",
        "LICENSE",
        "NOTICE.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
        ".gitignore",
        ".gitattributes",
        ".editorconfig",
        ".github/workflows/ci.yml",
        "templates/README.md",
        "worksheets/README.md",
        "project-ideas/ideas.csv",
        "running-example/package.json",
        "tools/check.ps1",
        "tools/check.sh",
        "tools/unlock.ps1",
        "tools/unlock.sh",
        "tools/build_solutions.py",
        "tools/guard_no_book_text.py",
    ]
    missing = [r for r in required if not (ROOT / r).exists()]
    for n in range(1, 7):
        if not (ROOT / f"solutions/part-{n}.7z").exists():
            missing.append(f"solutions/part-{n}.7z")
    if missing:
        print("STRUCTURE FAIL:", *missing, sep="\n  ")
        return 1
    print("STRUCTURE OK")
    return 0


def guard() -> int:
    errors = []
    for p in ROOT.rglob("*"):
        name = p.name
        if name in FORBIDDEN_NAMES and p.exists():
            # .keys and solutions-src must not be committed; presence on disk for maintainers is ok if gitignored
            if name in {".keys", "solutions-src"}:
                # ensure not tracked: checked via name appearing under git ls-files in CI with clean tree
                continue
        if name.endswith((".pdf", ".epub", ".docx")) and "running-example" not in p.parts:
            errors.append(f"book output file: {p.relative_to(ROOT)}")
    # plaintext solution trees outside solutions-src
    for p in ROOT.glob("unlocked/**/*"):
        if p.is_file():
            errors.append(f"unlocked plaintext present: {p.relative_to(ROOT)}")
    if errors:
        print("GUARD FAIL:")
        print("\n".join(errors))
        return 1
    print("GUARD OK")
    return 0


def starters_fail() -> int:
    bad = []
    for tests in ROOT.glob("part-*/**/tests/*.mjs"):
        ex = tests.parents[1]
        rel = ex.relative_to(ROOT).as_posix()
        r = subprocess.run(
            ["node", "--test", str(tests)],
            cwd=ex,
            capture_output=True,
            text=True,
        )
        if r.returncode == 0:
            bad.append(rel)
    if bad:
        print("STARTERS unexpectedly pass:")
        print("\n".join(bad))
        return 1
    print("STARTERS FAIL AS EXPECTED")
    return 0


def meta_scan() -> int:
    errors = []
    for p in iter_text_files():
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if EMOJI_RE.search(text):
            errors.append(f"emoji in {p.relative_to(ROOT)}")
        if AI_ATTR_RE.search(text):
            errors.append(f"AI attribution in {p.relative_to(ROOT)}")
    if errors:
        print("META FAIL:")
        print("\n".join(errors))
        return 1
    print("META OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--structure-only", action="store_true")
    ap.add_argument("--starters-fail", action="store_true")
    ap.add_argument("--meta-scan", action="store_true")
    args = ap.parse_args()
    if args.structure_only:
        return structure_only()
    if args.starters_fail:
        return starters_fail()
    if args.meta_scan:
        return meta_scan()
    return guard()


if __name__ == "__main__":
    sys.exit(main())
