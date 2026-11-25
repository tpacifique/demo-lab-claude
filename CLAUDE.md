# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Dependencies and the virtualenv are managed by `uv` (Python 3.12, see `.python-version`).

```bash
uv sync                              # create .venv and install deps from uv.lock
./run.sh                             # start the API with uvicorn --reload (port 8000)
./run.sh --host 0.0.0.0 --port 8080  # extra args are passed through to uvicorn
uv run pytest                        # full test suite
uv run pytest tests/test_health.py::test_health   # single test
uv run ruff check .                  # lint
uv run ruff format .                 # format (ruff format --check . to verify only)
```

`uv run lab-claude` runs the console entry point, which only prints a greeting. It does **not** start the API.

## Architecture

- **Two separate entry points.** The HTTP app is `lab_claude.app.main:app` (a FastAPI instance), served by uvicorn. The `lab-claude` script maps to `lab_claude:main` in `src/lab_claude/__init__.py`, which is an unrelated stub. Don't wire the server into `main()` without a reason.
- **uvicorn is not a declared dependency.** `run.sh` supplies it at runtime via `uv run --with uvicorn`. Add it to `pyproject.toml` only if the project decides to depend on it directly.
- **Docs live at the root URL.** `FastAPI(docs_url="/")` serves Swagger UI at `/`, so there is no root route handler. Routes are defined in `app/main.py`; add new ones there or in a module that gets included into `app`.
- **Tests use an in-process client.** `tests/test_health.py` builds a `TestClient` from the app object directly, so no server needs to be running. It needs `httpx`, which comes in through the dev dependency group.
- **No ruff or pytest configuration in `pyproject.toml`.** Both tools use their defaults. Any new settings belong in `pyproject.toml`.
