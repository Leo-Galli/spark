# Tickdown

Local CLI for Markdown checklists with stable IDs. Running example for Spark by Leonardo Galli.

## What it does (version 0.1.0)
- `status` summarizes open and done tasks
- `check` reports duplicate IDs and parse errors
- Optional in-file ID markers; honest unmarked fallback

## What it will not do
- Accounts, cloud sync, plugins, or Jira-like boards

## Install / run
```bash
npm install
npm run build
node dist/cli.js status examples/sprint.md
node dist/cli.js check examples/sprint.md
```

Requires Node.js >= 20.
