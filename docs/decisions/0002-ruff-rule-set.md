# 0002 — Lint with ruff at line length 100, rules E/F/I/UP/B

- **Date:** 2026-08-19
- **Status:** Accepted

## Context

Issue #1 called for ruff as the linter with "standard rules" and a line length
of 100. Ruff's own default (`E`, `F`) is thin, and its full rule catalogue is
large enough that switching everything on generates churn unrelated to real
defects — a bad trade on a solo learning project where every warning should
teach something.

## Decision

`line-length = 100`, with `select = ["E", "F", "I", "UP", "B"]`:

- `E` pycodestyle and `F` pyflakes — ruff's defaults, real errors
- `I` isort — import ordering, so import diffs stay deterministic
- `UP` pyupgrade — keeps syntax current with the project's Python 3.13 floor
- `B` flake8-bugbear — catches genuine bug patterns (mutable default arguments,
  loop variable capture) that pyflakes alone misses

## Alternatives considered

- **Defaults only (`E`, `F`)** — least noise, but misses import ordering and
  the bugbear checks, which are the ones most likely to catch a real mistake.
- **`select = ["ALL"]`** — maximal coverage, but pulls in opinionated and
  mutually redundant rule families (docstring style, annotations, one-true-way
  formatting) that would need a long per-rule ignore list to be usable.

## Consequences

Lint output stays short enough to read and act on. Rule families can be added
later one at a time as the codebase justifies them (for example `ANN` for type
annotations once mypy is configured, per CLAUDE.md). Because `I` is enabled,
`uv run ruff check --fix .` will reorder imports.
