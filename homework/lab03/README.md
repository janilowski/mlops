# Homework 3

```bash
cd homework/lab03
uv sync --locked
uv run --locked jupyter lab mlops-3-2.ipynb

systemd-run --user --scope -p MemoryMax=1536M -p MemorySwapMax=0 \
  -p CPUQuota=200% uv run --locked jupyter nbconvert \
  --execute --to notebook --inplace mlops-3-2.ipynb
```
