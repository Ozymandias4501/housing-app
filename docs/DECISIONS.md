# Architecture decisions

Index of decision records. One file per non-obvious decision, in
[`docs/decisions/`](decisions/) — numbered, dated, and immutable once merged.

| ADR | Date | Decision | Status |
| --- | --- | --- | --- |
| [0001](decisions/0001-src-layout.md) | 2026-08-19 | src layout with an installable package | Accepted |
| [0002](decisions/0002-ruff-rule-set.md) | 2026-08-19 | ruff at line length 100, rules E/F/I/UP/B | Accepted |
| [0003](decisions/0003-pre-merge-drift-check.md) | 2026-08-19 | check a PR's commit list for drift before merging | Superseded by [0006](decisions/0006-pre-merge-commit-description-check.md) |
| [0004](decisions/0004-architecture-doc-set.md) | 2026-08-19 | architecture, state, and decisions in three separate docs | Accepted |
| [0005](decisions/0005-ci-runs-uv-natively.md) | 2026-08-19 | CI installs uv and takes the Python pin from `.python-version` | Accepted |
| [0006](decisions/0006-pre-merge-commit-description-check.md) | 2026-08-19 | check commits against the PR's written description before merging | Accepted |

## Writing a new one

Copy [`decisions/TEMPLATE.md`](decisions/TEMPLATE.md) to
`decisions/NNNN-short-title.md` using the next free number, fill it in, and add
a row above — in the same PR as the change it describes.

Write one whenever a choice had a reasonable alternative: a library, a storage
engine, a schema shape, a workflow rule. Routine choices that any reviewer would
have made the same way don't need one.

## Immutability

A merged ADR's body is never edited — it's a record of what was decided and why,
at a point in time, and rewriting it destroys the only thing it's for. When a
decision changes, write a new ADR that supersedes it. The only line that may
change on the old one is its status, which becomes `Superseded by NNNN`; update
its row here to match.
