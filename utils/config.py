from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()
# Load environment variables from .env file

class Settings(BaseSettings):
    database_url: str = os.getenv("POSTGRESQL_URL")


settings = Settings()
# create an instance of the Settings class to access environment variables
