# MLOps course

- `lab01/`: Iris API, training, tests, and containers from the first lab.
- `homework/lab01/`: separate uv project for the sentiment-analysis homework.

Each project has its own dependencies, lockfile, and virtual environment.

## Lab 1

Restore dependencies and run the tests:

```bash
uv --directory lab01 sync --locked
uv --directory lab01 run pytest
```

Run the API from `lab01/` with `uv run uvicorn app:app --reload`, or run
`podman compose up --build` there. Docker Compose is also supported.

Local environment files and secrets stay inside `lab01/` and remain ignored.

## Homework

```bash
uv --directory homework/lab01 sync --locked
```

The homework starts with an empty environment. Add its dependencies there;
PyTorch and the sentiment models have not been downloaded yet.

## Git hooks

The shared hook configuration stays at the repository root. Install the
runner independently of either project's environment:

```bash
uvx --from pre-commit==4.6.2 pre-commit install
```
