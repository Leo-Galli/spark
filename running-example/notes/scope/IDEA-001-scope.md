# Scope: IDEA-001 (Tickdown)

## Problem statement
Developers who keep work in Markdown checklists still lose time in
standups because task lines have no stable IDs, status is hard to
summarize, and duplicates hide in plain sight. Grep and memory leave
the same leftover pain. They need a local, read-oriented way to report
status and assign stable IDs without moving work into a new system.

## One-sentence pitch
For developers who track work in Markdown checklists, Tickdown is a
local CLI that reports task status with stable IDs and clear errors
without accounts or a new home for the work.

## MVP behaviors
1. status -- IDs + checked state; clear error on bad path
2. check -- duplicates / structural refusals
3. ID rule -- markers optional; unmarked fallback documented
4. clear errors -- no stack-trace-only costume

## Demo script
sample sprint file -> status -> duplicate+check -> bad path -> README match

## Done when
Demo green on locked runtime story; README claims match demo; tests
cover status/check/errors once The Repository exists.

## Non-goals
(accounts; year-one plugins; Jira parity; auto-invent tasks; cloud
primary; watch required for demo; immortal unmarked IDs; every Markdown
flavor day one)

## Risks and constraints
ID immortality assumption -> documented rule + markers; no cloud identity

## First public release shape
0.1.0; npm tickdown; issues-only; needs-repro; 7-day first response;
MIT story lock (not legal advice)

## Parked for later
dry-run / --json -- after two real standups on 0.1.0

## Status
scoped (2026-10-26); next: Choosing a Stack; no git init yet
