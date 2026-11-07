#!/bin/sh
set -eu

# Initialize only an empty volume; later starts preserve the database.
if [ ! -s "$PGDATA/PG_VERSION" ]; then
    : "${POSTGRES_PASSWORD:?Set POSTGRES_PASSWORD}"
    printf '%s\n' "$POSTGRES_PASSWORD" | initdb \
        --encoding=UTF8 --auth-local=trust --auth-host=scram-sha-256 \
        --pwfile=/dev/stdin
    printf 'host all all all scram-sha-256\n' >> "$PGDATA/pg_hba.conf"
fi

exec postgres -c listen_addresses='*'
