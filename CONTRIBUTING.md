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
   then delete the branch. Before merging, check the PR's commit list
   (`gh pr view <N> --json commits`) against what the description and its comments
   describe, and summarize anything they don't cover in a PR comment first. Two ways
   a commit goes undescribed: the branch picks up work from a later PR targeting it,
   or you push fixes after writing the description. Both leave the same hole.

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
- `ARCHITECTURE.md` updated if the change altered the system's shape (component
  added/removed/renamed, data flow changed, something moved from planned to built)
- `STATE.md` reflects reality after the merge, with its date refreshed
- An ADR added under `docs/decisions/` if the change involved a choice with a
  reasonable alternative, and indexed in `docs/DECISIONS.md`
- No secrets, data files, or model artifacts in the diff

## Ground rules

- Python is managed with uv: `uv add` (or `uv add --dev`), never pip.
- Config and secrets come from environment variables; `.env` is gitignored.
- Every module gets tests. If it's hard to test, the design is wrong.
- When acceptance criteria are ambiguous, ask on the issue before implementing.
