from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    database_host: Optional[str] = None
    database_port: Optional[str] = None
    database_name: Optional[str] = None
    database_username: Optional[str] = None
    database_password: Optional[str] = None
    database_version: Optional[str] = None
    algorithm: Optional[str] = None
    secret_key: Optional[str]
    access_token_expire_minutes: Optional[int] = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = AppSettings()  # type: ignore
