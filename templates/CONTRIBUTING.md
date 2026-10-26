# Contributing to [PROJECT NAME]

Thanks for considering a patch. This file is the merge contract for strangers.

## Before you write code

1. Read the README: shipped behaviors and non-goals for the current version.
2. Search open issues and pull requests for the same leftover pain.
3. For behavior changes, open an issue first unless the change is a documented good-first-issue.
4. Security reports go through SECURITY.md, never through a public issue.

## Local setup

1. Clone the repository.
2. [Install steps: package manager, install command].
3. Run the demo from the README on a cold checkout.
4. Run the quality commands below and confirm they pass before you open a PR.

## Quality checks (required before review)

    [format-check command]
    [lint command]
    [test command]
    [optional: audit / secrets-check]

Pull requests that change behavior must update tests and the README (or CHANGELOG) so a stranger can see the new claim.

## Pull requests

1. Use the pull request template.
2. Keep the change inside the README fences unless an accepted RFC says otherwise.
3. One concern per PR when you can; do not bundle a refactor with a feature ask.
4. Required checks must be green.
5. License of contributions: unless we agree otherwise in writing, patches are offered under the same license as the project ([SPDX id]).

## Support envelope (for contributors too)

- [Channel]: issues on this repository.
- Mentorship: async by default; maintainers may coach at most [N] active newcomer PR at a time.
- Out-of-scope requests may be closed with a pointer to non-goals.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
