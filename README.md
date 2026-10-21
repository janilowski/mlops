# mlops

Restore dependencies and run tests:

```bash
uv --directory <DIR> sync --locked
uv --directory <DIR> run pytest
```

## Git hooks

The shared hook configuration stays at the repository root. Install the
runner independently of either project's environment:

```bash
uv tool install pre-commit==4.6.2
pre-commit install
```

Ruff checks and formats staged Python files across all labs and homework.
The mypy hook checks only `homework/lab01/`.
