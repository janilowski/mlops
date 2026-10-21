# settings.py
from pydantic_settings import BaseSettings
from pydantic import SecretStr, field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    MY_PRECIOUS: SecretStr

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        if value not in ("dev", "test", "prod"):
            raise ValueError("ENVIRONMENT must be dev, test, or prod")

        return value
