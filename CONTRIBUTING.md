# Contributing

This project runs like a team repo even when worked solo. The workflow below is
non-negotiable.

## Workflow: issue → branch → PR → review → merge

1. **Issue** — all work starts from a GitHub issue. No issue, no branch. Use the
   task issue template; make acceptance criteria concrete enough to verify.
2. **Branch** — branch off `main`, named for the issue:
   `feature/`, `bug/`, or `chore/` + `<issue-number>-<short-description>`
   (e.g. `feature/12-add-listing-schema`). Never commit or push to `main`.
3. **PR** — one issue = one PR; keep it small and reviewable. The description
   must link the issue with `Closes #N` and follow the PR template (summary of
   changes + testing note).
4. **Review** — PRs are reviewed before merge. Fix findings on the same branch.
5. **Merge** — merge only when acceptance criteria are met and checks pass,
   then delete the branch. Before merging, re-check the PR's commit list for anything
   added since it was opened or last reviewed (`gh pr view <N> --json commits`) and
   call it out — a PR branch can pick up commits from a later PR targeting it.

## Commits

Commit as you go — one logical change per commit, not a batch at the end.
Use [Conventional Commits](https://www.conventionalcommits.org/):
`feat:`, `fix:`, `chore:`, `docs:`, `test:`. Imperative subject under 72
characters; the body explains *why*, not what.

## Definition of done

- Acceptance criteria in the issue are met
- `uv run pytest` passes
- `uv run ruff check .` passes
- README or docs updated if behaviour changed
- No secrets, data files, or model artifacts in the diff

## Ground rules

- Python is managed with uv: `uv add` (or `uv add --dev`), never pip.
- Config and secrets come from environment variables; `.env` is gitignored.
- Every module gets tests. If it's hard to test, the design is wrong.
- When acceptance criteria are ambiguous, ask on the issue before implementing.
