FROM docker.io/library/python:3.13-slim-bookworm

WORKDIR /app

ENV UV_PYTHON_DOWNLOADS=0 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    OPENBLAS_NUM_THREADS=1 \
    PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock ./

RUN --mount=type=bind,from=ghcr.io/astral-sh/uv:0.13.0,source=/uv,target=/bin/uv \
    uv sync --locked --no-dev --no-install-project --no-cache

COPY . .

USER 10001:10001

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
