# CO Housing Dashboard

Housing market dashboard for Colorado: data pipeline, ML models, API, frontend.
Solo project. Primary goals: learn data engineering and MLOps properly. No shortcuts
that a real team would reject in review.

## Workflow (non-negotiable)
- All work starts from a GitHub issue. No issue, no branch. Exception: the fast path below.
- Fast path (no issue needed): the change touches only docs or config text, makes no
  behaviour change, touches nothing in `src/`, `tests/`, or `.github/workflows/`, and is one
  commit. The PR description must still state, in one sentence, what changed and why. If that
  explanation runs past one sentence, or the change involves a judgement call, stop and open
  an issue instead — use the normal flow.
- Branch naming: `<type>/<issue-number>-short-description` where type is feature, bug, or
  chore (e.g. `feature/12-add-listing-schema`). Fast-path branches drop the issue number:
  `<type>/short-description` (e.g. `docs/fix-branch-naming-typo`).
- Never commit or push to main. All changes merge via PR.
- One issue = one PR. Keep PRs small and reviewable.
- PR descriptions must link the issue with "Closes #N" — fast-path PRs have no issue to link;
  the one-sentence summary above stands in its place.
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
- Reasoning for a decision belongs in the GitHub issue by default. That's where the work is
  scoped and it's read at the start of every session. Don't open a new file for it.
- `docs/decisions/NNNN-*.md` — write an ADR only when a decision constrains future work and
  would be expensive to reverse: storage engine, data source, schema shape, external
  dependency the whole pipeline sits on. If reversing it means editing a config line and
  moving on, it isn't an ADR. Do not write ADRs about tooling defaults, formatting, or the
  documentation process itself.
- If unsure whether something clears the bar, leave it in the issue and ask. A decision can
  be promoted to an ADR later, once it's clear it mattered.
- To write one: copy `docs/decisions/TEMPLATE.md`, take the next number, add a row to the
  `docs/DECISIONS.md` index. To change a past decision, write a new ADR and mark the old one
  `Superseded by NNNN` rather than rewriting history.

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