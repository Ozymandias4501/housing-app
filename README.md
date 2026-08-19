# CO Housing Dashboard

A Colorado housing market dashboard. The goal of the project is to learn data
engineering and MLOps by building the whole stack properly: ingestion, modeling,
serving, and UI — with the discipline a real team would expect in review.

## Planned architecture

A data pipeline ingests and cleans Colorado housing market data into versioned,
analysis-ready datasets. ML models train on those datasets to produce price and
trend predictions. An API serves the predictions and aggregate statistics. A
frontend dashboard consumes the API to visualize the market.

## Local setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.13 (uv will fetch it if missing).

```sh
uv sync            # create .venv and install all dependencies (incl. dev)
uv run pytest      # run the test suite
uv run ruff check .    # lint
uv run ruff format .   # format
```

Configuration and secrets are loaded from environment variables; `.env` is
gitignored and never committed.

## Contributing

All work flows through GitHub issues and PRs — see [CONTRIBUTING.md](CONTRIBUTING.md).
