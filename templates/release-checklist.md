# Release checklist -- [PROJECT] [X.Y.Z]

Date started: [YYYY-MM-DD]
Owner: [NAME]
Tag name: v[X.Y.Z]
Registry publish planned: [yes / no]

## Scope and claims

- [ ] README shipped behaviors match this version only
- [ ] Non-goals unchanged unless CHANGELOG says otherwise
- [ ] CHANGELOG section for [X.Y.Z] lists user-visible changes only
- [ ] Version in package metadata matches the tag

## Quality

- [ ] Cold clone: install + README demo succeeds in five minutes
- [ ] `format` / `lint` / `test` green locally
- [ ] CI green on the commit you will tag
- [ ] `audit` (or equivalent) reviewed; no ignored high findings without a written accept risk
- [ ] Secrets check clean; no tokens in tree

## Security and keys

- [ ] SECURITY.md supported-versions table includes this line
- [ ] SECURITY contact is a live mailbox (not a placeholder)
- [ ] Publish token exists only in host CI secrets (if publishing)
- [ ] No "signed" or provenance claims in README unless verify steps are documented

## Tag and publish

- [ ] Annotated tag `v[X.Y.Z]` on the green commit
- [ ] Host Release notes equal CHANGELOG (no extra hype claims)
- [ ] Registry publish rehearsed on a dry account or documented one-shot steps
- [ ] Install from the published artifact matches the README demo

## Aftercare

- [ ] Support envelope still visible in README
- [ ] Announce draft (if any) cites only demoable claims
- [ ] Cost gate hours still believable for the next [30] days
