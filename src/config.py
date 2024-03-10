from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    """Pydantic model for get db settings, auto read all variables from .env"""
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")




