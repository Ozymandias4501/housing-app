# 0006 — Check commits against the PR's written description before merging

- **Date:** 2026-08-19
- **Status:** Accepted
- **Supersedes:** [0003](0003-pre-merge-drift-check.md)

## Context

[ADR 0003](0003-pre-merge-drift-check.md) set the pre-merge check as: compare the
PR's commit list against the commits authored in the current session, and
summarise anything authored elsewhere. That test was shaped by the incident that
prompted it — a second session's PR merging into an open PR's branch — so it
asks *who wrote this commit*.

PR #11 (CI workflow, issue #10) showed the test is too narrow. Three commits
landed after the PR description was written: a fix pinning
`astral-sh/setup-uv` to an exact release after the first CI run failed to
resolve `@v10`, plus a deliberately failing test and its revert, added to verify
the red path. All three were authored in the merging session, so the ADR 0003
check ran, found nothing, and passed. The PR merged carrying a description that
covered only its first commit and referred readers to "the commit history" for
the rest. The reason for the version pin — a change to the merged
implementation, not just to its verification — appeared nowhere in the issue or
PR thread until it was written up after the merge.

Authorship was never the property worth checking. A commit nobody has described
is equally opaque whether it came from another session or from the last ten
minutes of this one.

## Decision

Before `gh pr merge`, run `gh pr view <N> --json commits` and check the list
against what the PR description **and its comments** describe. Any commit they
don't cover gets summarised in a PR comment — what it changed and why — before
the merge, regardless of who authored it or when.

The test is whether the merged state has a written description a reader can find
from the PR, not whether the commits are trusted. Recorded in CLAUDE.md, in
CONTRIBUTING.md step 5, and as a line in the PR template so the check has a
visible home in the PR itself.

## Alternatives considered

- **Keep ADR 0003's rule and rely on updating the PR description in place** as
  commits land. Equivalent in principle and produces a tidier PR, but it depends
  on remembering at the moment a fix is pushed, when attention is on the fix.
  The pre-merge check is a single fixed point where the question is always asked.
- **Amend the ADR 0003 rule to "commits added since the PR was opened."**
  Narrower and still wrong at the edge: a commit pushed *before* the description
  was written but never mentioned in it is undescribed too.
- **Mechanical enforcement — a CI check or merge gate.** Rejected in ADR 0003
  because the check needs to know which commits were already described, which
  isn't state a script has. Widening the rule doesn't change that; if anything
  "is this commit described in prose?" is less mechanisable than the SHA
  comparison ADR 0003 was rejecting.

## Consequences

More PRs will need a comment before merging, since pushing fixes after opening a
PR is normal rather than exceptional — that is the point, and it is the common
case ADR 0003 missed. The comment is also the artifact that makes a merged PR
readable later, which the commit list alone never was. Enforcement is still
procedural: nothing blocks a merge that skips the step.
