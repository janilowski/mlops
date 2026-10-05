# mlops

hello world

## Local settings

Copy `config/.env.example` to `config/.env.dev`, `.env.test`, or `.env.prod`.
Set `ENVIRONMENT` to match the filename and fill in `APP_NAME`.

The loader expects a decrypted, local `secrets.yaml`:

```yaml
secrets:
  - MY_PRECIOUS: "replace-with-your-secret"
```

Run `uv run main.py --environment dev`. The loader does not decrypt SOPS
files. Keep encrypted backups separately; `secrets.yaml`, local `.env`
files, and private keys are ignored. `.sops.yaml` and `public_key.asc`
contain public encryption configuration only.
