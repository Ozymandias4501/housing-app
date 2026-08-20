# 0005 — CI installs uv and reads the Python pin from `.python-version`

- **Date:** 2026-08-19
- **Status:** Accepted

## Context

Issue #10 called for CI that runs the test suite and the linter on every pull
request, since CLAUDE.md and CONTRIBUTING.md both make "tests pass, lint passes"
part of done while nothing enforced it. The project manages Python and its
dependencies entirely with uv (ADR 0001), and the interpreter version is pinned
in `.python-version`. The open question was how the workflow should obtain a
Python interpreter and the dev dependencies.

## Decision

`.github/workflows/ci.yml` uses `astral-sh/setup-uv` with its cache enabled,
then `uv sync --locked`, then `uv run ruff check .` and `uv run pytest`.

The workflow deliberately does **not** declare a Python version. uv resolves the
interpreter from `.python-version` and installs it if the runner lacks it, so
the pin lives in one file. `--locked` fails the run if `uv.lock` is out of date
with `pyproject.toml`, so a dependency added without re-locking is caught in CI
rather than after a merge.

## Alternatives considered

- **`actions/setup-python` with a pinned `python-version`, then pip** — the
  conventional setup, but it duplicates the version pin in a second file where
  it can silently drift from `.python-version`, and it installs dependencies
  through a tool the project has otherwise standardised away from.
- **`actions/setup-python` plus uv** — removes the pip half of the problem but
  keeps the duplicated version pin, and setup-uv already installs interpreters.
- **`uv sync` without `--locked`** — tolerant of a stale lock file, which is the
  failure this check exists to surface.

## Consequences

Adding a dependency now requires committing the refreshed `uv.lock`, or CI
fails — the intended behaviour, but it will be the first surprise. Bumping the
Python version is a one-line change to `.python-version` and needs no workflow
edit. The workflow depends on a third-party action (`astral-sh/setup-uv`);
replacing it with a raw install script is a small, self-contained change if
that dependency ever becomes unwelcome.
