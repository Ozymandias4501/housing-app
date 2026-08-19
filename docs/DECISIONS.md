# Architecture decisions

One bullet per structural choice: date · decision · alternative rejected · why.

- 2026-08-19 · src layout with an installable package (`src/housing/`, hatchling
  build backend) · rejected pytest `pythonpath = ["src"]` config · installing the
  package editable via `uv sync` lets tests and future API/pipeline code
  `import housing` without path hacks, and keeps the project publishable.
- 2026-08-19 · ruff rule set `E, F, I, UP, B` at line length 100 · rejected
  default-only `E, F` · import sorting (I), pyupgrade (UP), and bugbear (B) catch
  real issues cheaply without the churn of an exhaustive rule set.
- 2026-08-19 · pre-merge commit-drift check (`gh pr view <N> --json commits`) required
  in CLAUDE.md/CONTRIBUTING.md before running `gh pr merge` · rejected a script/CI
  check enforcing it · a follow-up PR (#4) merged into an open PR's (#2) branch went
  unnoticed until after merge; only the merging session's own context knows which
  commits it already reviewed, so a script can't add anything a manual check can't.
