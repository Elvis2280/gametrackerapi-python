from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = SettingsConfigDict(env_file=".env")["POSTGRESQL_URL"]


settings = Settings()
