# IDEA-001 succession
Status: succession-draft
Date: <today>
Owner today: Sam (solo BDFL-style per GOVERNANCE.md)
Cost gate: ~3 h/week; issues-only; 7-day first reply
Related: notes/governance/IDEA-001-governance.md
         notes/burnout/IDEA-001-support-hours.md
         notes/funding/IDEA-001-funding.md

## Preferred order if I must stop
1) Succession: second merge right under GOVERNANCE revisit triggers
2) Archive: README banner + forge archive; last tag remains installable
3) Transfer: only with written key checklist + LICENSE/MIT unchanged story

## Public excerpt (paste-ready)
If Tickdown becomes unstaffed:
- We will publish a README status line within 14 days of that decision.
- Default if no successor: archive the repository; last release remains the contract.
- SECURITY contact and npm publish owners will be named in that notice.
- Sponsors tip jar (if any) will pause; gifts never bought merge priority.

## Successor accept criteria (if someone asks)
- Demonstrated PR merges under current CONTRIBUTING + CI bar
- Willing to keep non-goals / local-file ADR / MIT story for 0.1.x
- Real SECURITY mailbox and publish-token custody plan
- Hours note published (or explicit maintenance-mode / archive choice)

## Private key checklist (do not commit secrets)
- [ ] GitHub owner/admin transfer or co-owner steps (verify host UI)
- [ ] npm package `tickdown` owner / 2FA / tokens rotated
- [ ] SECURITY mailbox forwarding or new address live
- [ ] Sponsors profile paused or retargeted per current platform docs
- [ ] Domain/DNS if any (none for Tickdown 0.1.x)
- [ ] CI secrets inventory emptied or re-owned

## Communication plan
Channels: README + GitHub Release note for last staffed tag era
Claim ceiling: no "temporary hiatus" if we mean archive
Jordan: accountability reread only -- not unpaid successor

## Revisit
Review this note when GOVERNANCE revisit triggers fire, when hours stay red two months,
or before any sponsor/admin change that implies new owners.
