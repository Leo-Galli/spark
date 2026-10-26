# Governance -- [PROJECT NAME]

Status: [draft | locked] as of [YYYY-MM-DD]
Applies to: version line [0.x / 1.x]

## Model

[Solo maintainer (BDFL-style) | shared maintainers | committee]

For [0.x], [NAME] is the sole person with merge rights on the default branch.

## Merge rights

- Merge to default branch: [list names or "NAME only"]
- Release tags and registry publish: [same person / named publisher]
- SECURITY mailbox owner: [name + contact path]

## Stuck calls

If discussion stalls past [N] days on an in-scope decision, [NAME] posts a public decision comment on the issue or RFC. That comment is the record until a revisit trigger fires.

## Maintainer path

[Closed until revisit | open with written criteria]

Criteria if open:

1. [Example: multiple merged PRs that respected fences]
2. [Example: willingness to share the support hours note]
3. [Example: accepted by current merge-right holders]

## Revisit triggers

Any of the following reopens this document for a dated rewrite:

- Adding a second merge right
- Triage time above [N] hours/week for [two] consecutive weeks
- Unparking a major non-goal (example: plugins) or breaking a documented public contract
- Moving SECURITY or publish keys to a new owner

## What this file is not

This file is not a foundation charter, election code, or Contributor License Agreement. Contribution license terms live in CONTRIBUTING.md and LICENSE.
