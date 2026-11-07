# Lab 2: Databases and file formats

[Instructions](https://github.com/j-adamczyk/MLOps_course_AGH/blob/master/lab02/LAB_INSTRUCTION.md).
Completed notebooks include saved outputs. Run commands from this directory.

```bash
uv sync --locked
export PODMAN_COMPOSE_PROVIDER="$PWD/.venv/bin/podman-compose"
podman compose up --detach
```

PostgreSQL: `localhost:5432`, database/user/password `postgres`; 512 MiB, 2 CPUs.

Download inputs once:

```bash
curl -fL -o data/services-2024.csv.gz \
  https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz
gzip -d data/services-2024.csv.gz
curl -fL -o data/disruptions-2023.csv \
  https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-2023.csv
curl -fL -o data/disruptions-2024.csv \
  https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-2024.csv
```

Once PostgreSQL is ready, initialize/import once. The SQL resets `services`;
repeating the import duplicates rows.

```bash
podman compose exec -T postgres psql -U postgres -v ON_ERROR_STOP=1 < data/services_table.sql
podman compose exec -T postgres psql -U postgres -v ON_ERROR_STOP=1 \
  -c '\copy services FROM STDIN WITH (FORMAT csv, HEADER true)' < data/services-2024.csv
```

Execute sequentially on Linux/systemd (1.5 GiB RAM cap, no swap):

```bash
systemd-run --user --scope --quiet \
  -p MemoryHigh=1G -p MemoryMax=1536M -p MemorySwapMax=0 \
  uv run --locked jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=3600 notebook_01_psycopg.ipynb notebook_02_duckdb.ipynb
```

Inputs and exports use about 35 GB under ignored `data/`.
Stop with `podman compose down`; delete the database with `podman compose down --volumes`.
Remove the unused image with `podman image rm localhost/mlops-lab02-postgres:17-alpine`.

Sources: [course starters](https://github.com/j-adamczyk/MLOps_course_AGH/tree/3e7c266a5026576326a1c592524417a2f6231331/lab02)
(MIT, `LICENSE.upstream`); [Rijden de Treinen](https://www.rijdendetreinen.nl/en/open-data)
([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)).
