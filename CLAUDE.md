# CO Housing Dashboard

Housing market dashboard for Colorado: data pipeline, ML models, API, frontend.
Solo project. Primary goals: learn data engineering and MLOps properly. No shortcuts
that a real team would reject in review.

## Workflow (non-negotiable)
- All work starts from a GitHub issue. No issue, no branch.
- Branch naming: Branch naming: <type>/<issue-number>-short-description where type is feature, bug, or chore
- Never commit or push to main. All changes merge via PR.
- One issue = one PR. Keep PRs small and reviewable.
- PR descriptions must link the issue with "Closes #N".
- Before merging a PR (`gh pr merge`), run `gh pr view <N> --json commits` and check the list
  against what the PR description and its comments actually describe. Any commit they don't
  cover — one from another session or author, or one you added yourself after opening the PR —
  gets summarized in a PR comment, what it changed and why, before the merge. The question is
  whether the merged state has a written description, not who wrote the commit. Don't merge past
  changes that have no written trace.
- Commit as you go, conventional commits: feat:, fix:, chore:, docs:, test:

## Docs (keep current, in the same PR as the change)
- `ARCHITECTURE.md` — update when a PR changes the shape of the system: a component added,
  removed, or renamed; a change in how data flows; something moving from planned to built.
- `STATE.md` — update in every PR that changes what's done, in flight, blocked, or next.
  Keep it to ten lines and refresh the "Last updated" date.
- `docs/decisions/NNNN-*.md` — add an ADR whenever a choice had a reasonable alternative
  (library, storage engine, schema shape, workflow rule). Copy `docs/decisions/TEMPLATE.md`,
  take the next number, and add a row to the `docs/DECISIONS.md` index.
- Never edit a merged ADR's body. To change a decision, write a new ADR and set the old one's
  status to `Superseded by NNNN`.

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