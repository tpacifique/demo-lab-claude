# lab-claude

A minimal FastAPI application exposing a health-check endpoint.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Installation

```bash
uv sync
```

This creates a `.venv/` and installs runtime and dev dependencies from `uv.lock`.

## Running the API

No ASGI server is declared as a dependency, so pull in `uvicorn` on the fly:

```bash
./run.sh
```

Additional Uvicorn options can be passed to the script, for example:

```bash
./run.sh --host 0.0.0.0 --port 8080
```

Then check the endpoint:

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

Interactive docs open at the root URL: http://localhost:8000/.

## Endpoints

| Method | Path      | Response             |
| ------ | --------- | -------------------- |
| GET    | `/health` | `{"status": "ok"}`   |

## Tests

```bash
uv run pytest
```

## Linting

```bash
uv run ruff check .
uv run ruff format .
```

## Project structure

```
.
├── pyproject.toml           # Project metadata and dependencies
├── uv.lock                  # Locked dependency versions
├── src/lab_claude/
│   ├── __init__.py          # CLI entry point (`uv run lab-claude`)
│   └── app/
│       └── main.py          # FastAPI app and routes
└── tests/
    └── test_health.py       # /health endpoint test
```
