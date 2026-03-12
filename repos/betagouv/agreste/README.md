# agreste

Python project managed with `uv`, using a `src/` layout.

## Requirements

- Python 3.11+
- `uv` installed (`pipx install uv` or see the uv docs)

## Setup

```bash
cd agreste

# Create a virtual environment and install dependencies
uv sync
```

This will create a `.venv` in the project and install the `dev` dependencies specified in `pyproject.toml`.

## Common commands

- Install dependencies (including dev group):

  ```bash
  uv sync
  ```

- Add a runtime dependency:

  ```bash
  uv add <package>
  ```

- Add a dev-only dependency:

  ```bash
  uv add --group dev <package>
  ```

- Run tests:

  ```bash
  uv run pytest
  ```

## Project layout

- `pyproject.toml` – project metadata and uv configuration
- `src/agreste` – main package code
- `tests` – test suite

