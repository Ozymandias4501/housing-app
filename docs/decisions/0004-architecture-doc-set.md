# 0004 — Keep architecture, state, and decisions in three separate docs

- **Date:** 2026-08-19
- **Status:** Accepted

## Context

Issue #7 asked for a way to understand this project quickly — specifically so a
Claude chat could be pointed at the repo and be useful for brainstorming next
steps without first reading every file and every PR. Three different questions
were getting conflated in one place: *what is this system*, *how far along is
it*, and *why was it built this way*. They change at different rates, so folding
them into README (or into each other) guarantees at least one of them is stale.

There was also an existing `docs/DECISIONS.md` holding three one-line bullets,
which the issue's request for per-decision ADR files had to reconcile with.

## Decision

Three docs, each answering one question and each carrying its own update rule in
a header line:

- `ARCHITECTURE.md` — components, data flow, built vs planned. Changes when the
  system's shape changes.
- `STATE.md` — phase, done, in flight, blocked, next. Ten lines. Changes almost
  every PR.
- `docs/decisions/NNNN-*.md` — one immutable ADR per non-obvious decision, with
  `docs/DECISIONS.md` as the index table. Append-only.

The update rules are stated in three places on purpose: CLAUDE.md (read at the
start of every Claude session), CONTRIBUTING.md's definition of done (read by a
human contributor), and a `## Docs` checklist in the pull request template (seen
at the moment of action, which is the lesson of [ADR 0003](0003-pre-merge-drift-check.md)).

## Alternatives considered

- **Migrate fully to ADR files, delete `docs/DECISIONS.md`** — a single source
  of truth with no index to drift. Rejected because surveying decisions would
  then mean opening N files, and a one-file overview is precisely what makes the
  set useful to someone (or something) reading the repo cold. The index holds
  only number, date, title, and status, so its drift surface is small.
- **Keep both, split by weight** — one-line bullets for routine calls, full ADRs
  for weighty ones. Rejected because it requires judging, every time, which file
  a decision belongs in, and leaves two places to search later.
- **Update rules documented but not in the PR template** — less ceremony per PR.
  Rejected for the same reason ADR 0003 exists: a rule that isn't visible at the
  moment of action is a rule that gets skipped.

## Consequences

Every PR now carries a small docs obligation, and the template makes skipping it
a visible choice rather than an oversight. `STATE.md` is the one most likely to
rot, which is why it's deliberately tiny and dated. Adding an ADR means touching
two files (the record and the index) — accepted as the cost of the overview.
