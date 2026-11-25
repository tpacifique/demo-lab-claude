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
# {"status":"ok","message":"Server is alive and working"}
```

Interactive docs open at the root URL: http://localhost:8000/.

## Endpoints

| Method | Path      | Response |
| ------ | --------- | -------- |
| GET    | `/health` | `{"status": "ok", "message": "Server is alive and working"}` |

## Tests

```bash
uv run pytest
```

## Linting

```bash
uv run ruff check .
uv run ruff format .
```

## Scanning for secrets with Gitleaks

[Gitleaks](https://github.com/gitleaks/gitleaks) scans Git repositories for
potentially exposed secrets, such as API tokens, passwords, and private keys.
Install Gitleaks separately, then run this from the repository root:

```bash
gitleaks detect --source .
```

`detect` runs a repository scan, and `--source .` tells Gitleaks to use the
current directory as its source. Review the findings rather than assuming every
match is a real credential; verify suspected false positives before adding a
narrow allowlist exception.

Run the scan regularly and before pushing changes. Treat any confirmed secret
as compromised: revoke or rotate it promptly, remove it from the relevant
files, and follow your team's process for addressing it in Git history. Do not
paste scan output into public issues or logs, or commit a report that could
contain sensitive details. For CI, fail the job when the scan reports a
finding, and use Gitleaks' redaction option if output might be exposed.

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
