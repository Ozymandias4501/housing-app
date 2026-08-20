# 0001 — Use a src layout with an installable package

- **Date:** 2026-08-19
- **Status:** Accepted

## Context

Scaffolding the repo (issue #1) meant choosing where Python code lives and how
tests import it. `uv init` had left a `main.py` at the repo root, which is fine
for a script and wrong for a project that will grow a pipeline, models, an API,
and a frontend. Tests need to import project code somehow, and the two common
ways to arrange that pull in different directions.

## Decision

Code lives in `src/housing/`, and the project declares a hatchling build system
so `uv sync` installs it into the virtualenv in editable mode. Tests import it
as a normal installed package (`import housing`). Because the package name
(`housing`) differs from the project name (`housing-app`), `pyproject.toml`
tells hatchling where to look:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/housing"]
```

The `uv init` boilerplate `main.py` was deleted in the same change.

## Alternatives considered

- **Flat layout with pytest `pythonpath = ["src"]`** — works with no build
  system, but leaves the project uninstallable. Tests would import from the
  working directory rather than from an installed artifact, so packaging
  mistakes stay invisible until something else tries to depend on the package.
- **Package at the repo root (`housing/`)** — one less directory, but the root
  is on `sys.path` during test runs, so imports can succeed for the wrong
  reason and the same packaging blind spot applies.

## Consequences

Tests exercise the package as installed, so a broken build surfaces at
`uv sync` rather than much later. New contributors must run `uv sync` before
tests will import anything — that's documented in README. Adding a subpackage
needs no config change; adding a *second* top-level package would require
another entry under `[tool.hatch.build.targets.wheel]`.
