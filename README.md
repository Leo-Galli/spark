# Spark companion repository

[![ci](https://github.com/Leo-Galli/spark/actions/workflows/ci.yml/badge.svg)](https://github.com/Leo-Galli/spark/actions/workflows/ci.yml)

This repository accompanies **Spark: From Idea to Open Source That Lasts** by Leonardo Galli.

Instructions for exercises and the solution archive keys are printed in the book only. This repository does not contain the manuscript.

## Quick start

### Windows (PowerShell)
```powershell
git clone https://github.com/Leo-Galli/spark.git
cd spark
powershell -File tools/check.ps1 -Exercise part-2-designing-and-building/the-repository/ex-01-parse-task-line
```

### macOS / Linux
```bash
git clone https://github.com/Leo-Galli/spark.git
cd spark
chmod +x tools/check.sh tools/unlock.sh
./tools/check.sh part-2-designing-and-building/the-repository/ex-01-parse-task-line
```

Starters are expected to fail until you complete the exercise using the book.

### Unlock a Part's solutions
Keys are in the book at the end of each Part. Example:
```powershell
powershell -File tools/unlock.ps1 -Part 2 -Key "word1 word2 word3 word4"
```
```bash
./tools/unlock.sh 2 'word1 word2 word3 word4'
```

## Folder map
| Path | Purpose |
| --- | --- |
| `part-N-*/<chapter>/ex-NN-*/` | Exercise starter, tests, optional data/templates |
| `running-example/` | Tickdown running example (TypeScript/Node) |
| `templates/` | Paste-ready community and checklist templates |
| `worksheets/` | Blank printable worksheets |
| `project-ideas/ideas.csv` | Structured idea rows (no book prose) |
| `solutions/part-N.7z` | Encrypted solution archives |
| `tools/` | check, unlock, build_solutions, guard |

## Finding an exercise
1. Open the Part folder that matches the book Part QR or table in How to Use This Book.
2. Open the chapter folder named after the chapter title slug.
3. Open `ex-NN-<slug>/README.md` for the title and book location only.
4. Edit files under `starter/`. Run `tools/check.*` against that exercise path.

## License
MIT for repository code and templates. See NOTICE.md for book-text rights.
