# Lab 1 homework

[Assignment](https://github.com/j-adamczyk/MLOps_course_AGH/blob/master/lab01/HOMEWORK.md)

## PyTorch

```bash
uv run --locked python -c 'import torch; print(torch.__version__); print(torch.ones(2) + 1)'
```

The version should include `+cpu` on Linux, and the tensor should contain `[2., 2.]`.

## Type checking

```bash
uv run --locked --only-group dev mypy .
```
