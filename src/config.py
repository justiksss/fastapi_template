from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


settings = SettingsConfigDict(env_file=find_dotenv(".env.example"), env_file_encoding="utf-8", extra="ignore")


class DatabaseConfig(BaseSettings):
    """Pydantic model for get db settings, auto read all variables from .env.example"""
    model_config = settings

    # add pydantic.Field() for alias e.t.c
    database_host: str
    database_name: str

    database_port: int | str

    database_password: str
    database_user: str



