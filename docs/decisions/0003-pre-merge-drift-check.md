# 0003 — Check a PR's commit list for drift before merging

- **Date:** 2026-08-19
- **Status:** Accepted

## Context

While PR #2 (repo scaffolding) was open, a separate Claude Code session opened
PR #4 targeting PR #2's branch rather than `main`. PR #4 merged into that branch
at 23:42, and PR #2 was merged into `main` at 23:44 — so a `.gitignore` change
nobody had reviewed in the merging session rode into `main`. It was noticed two
minutes later, while summarising the pull, instead of before the merge.

Nothing malfunctioned: `gh pr merge` merged exactly what was on the branch. The
gap was procedural — the merging session never re-checked whether the branch
still contained only what it had authored. Issue #5 asked for that gap to close.

## Decision

Before running `gh pr merge`, run `gh pr view <N> --json commits` and compare
the result against the commits authored in the current session. Any commit that
wasn't authored in-session is drift: summarise what it changed and why *before*
merging, rather than reporting it afterwards. The rule is recorded in CLAUDE.md
(governing Claude) and CONTRIBUTING.md step 5 (governing anyone merging), since
the root cause — a later PR targeting an open PR's branch — isn't specific to
Claude.

## Alternatives considered

- **A CI check or script that blocks the merge on drift** — the check needs to
  know which commits were *already reviewed*, and that state exists only in the
  merging session's own context. A script can compare SHAs against the branch
  point, which is exactly what `gh pr view --json commits` already shows a human
  or agent directly. It would add machinery without adding capability.
- **Require PRs to always target `main`** — would have prevented this specific
  incident, but stacked PRs targeting an open branch are a legitimate pattern,
  and the rule would silently fail the next time drift arrives some other way
  (a force-push, a suggestion committed from the GitHub UI).

## Consequences

One extra command before every merge, and the merging session has to actually
read the output. Drift is surfaced to the user as a decision point rather than
as an after-the-fact apology. Nothing enforces this mechanically — it depends
on the rule being followed, which is why it lives in the files Claude reads at
the start of every session.
