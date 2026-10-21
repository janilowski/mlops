from pathlib import Path
import argparse
import os

import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = Path(__file__).resolve().parent / "config" / f".env.{environment}"
    load_dotenv(env_file)


def export_secrets() -> None:
    secrets_file = Path(__file__).resolve().parent / "secrets.yaml"
    with secrets_file.open(encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Export secret names as defined in the YAML file.
    for secret in data["secrets"]:
        for name, value in secret.items():
            os.environ[name] = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
