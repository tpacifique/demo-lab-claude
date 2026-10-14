#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"
exec uv run --with uvicorn uvicorn lab_claude.app.main:app --reload "$@"
