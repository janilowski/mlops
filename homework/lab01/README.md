# Lab 1 homework

[Assignment](https://github.com/j-adamczyk/MLOps_course_AGH/blob/master/lab01/HOMEWORK.md)

## Server

```bash
uv run --locked uvicorn app:app --reload
```

## Tests

```bash
uv run --locked pytest
```

## Podman

```bash
uv tool install podman-compose
PODMAN_COMPOSE_PROVIDER=podman-compose podman compose up --build
```

Stop and remove the service:

```bash
PODMAN_COMPOSE_PROVIDER=podman-compose podman compose down
```

## PyTorch

```bash
uv run --locked python -c 'import torch; print(torch.__version__); print(torch.ones(2) + 1)'
```

The version should include `+cpu` on Linux, and the tensor should contain `[2., 2.]`.

## Type checking

```bash
uv run --locked mypy .
```
