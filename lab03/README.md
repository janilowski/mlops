# Lab 3

```bash
cd lab03
uv sync --locked
uv run --locked jupyter lab notebook_polars.ipynb

systemd-run --user --scope -p MemoryMax=1536M -p MemorySwapMax=0 \
  -p CPUQuota=200% uv run --locked jupyter nbconvert \
  --execute --to notebook --inplace notebook_polars.ipynb
```

[Source](https://github.com/j-adamczyk/MLOps_course_AGH/tree/2bb2e845b9d9b989b8f114a20cb38fc94aaa456c/lab03)
