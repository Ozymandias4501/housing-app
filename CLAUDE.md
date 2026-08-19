# CO Housing Dashboard

Housing market dashboard for Colorado: data pipeline, ML models, API, frontend.
Solo project. Primary goals: learn data engineering and MLOps properly. No shortcuts
that a real team would reject in review.

## Workflow (non-negotiable)
- All work starts from a GitHub issue. No issue, no branch.
- Branch naming: `feature/, bug/, /chore then <issue-number>-short-description` (e.g. `feature/12-add-listing-schema`)
- Never commit or push to main. All changes merge via PR.
- One issue = one PR. Keep PRs small and reviewable.
- PR descriptions must link the issue with "Closes #N".
- Commit as you go, conventional commits: feat:, fix:, chore:, docs:, test:

## Tech
- Python managed with uv. Add deps with `uv add`, never pip.
- Run tests: `uv run pytest`
- Type check: `uv run mypy .` (add when configured)
- Lint/format: `uv run ruff check` and `uv run ruff format`

## Principles
- Config and secrets via environment variables, never hardcoded. `.env` is gitignored.
- Every module gets tests. If it's hard to test, the design is wrong.
- Prefer boring, well-documented tools over clever ones.
- When acceptance criteria in an issue are ambiguous, ask before implementing.

## Definition of done
- Acceptance criteria in the issue are met
- Tests pass, lint passes
- README or docs updated if behaviour changed