# Contributing

This repository accompanies a printed book. Please keep contributions narrow.

## Welcome changes
- Bug fixes in exercise starters or tests
- Fixes that make a starter fail incorrectly or a documented tool script crash
- Typos in repository-facing files (README, templates, worksheets blanks)
- CI reliability fixes

## Out of scope
- Pasting book prose, exercise statements, hints, or solution keys
- Adding manuscript chapters, PDFs, EPUBs, or page images
- Expanding exercises with instructions that belong only in the book
- Marketing or SEO noise

## How to propose a fix
1. Open an issue with the exercise path and the failing command.
2. Keep pull requests small and evidence-based.
3. Do not commit `.keys`, `solutions-src/`, or decrypted solution trees.

## Tests
Use `tools/check.ps1` or `tools/check.sh` with an exercise path. Starters are expected to fail their tests until you complete the work described in the book.
