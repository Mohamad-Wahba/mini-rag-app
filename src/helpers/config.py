from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Mini RAG App"
    APP_VERSION: str = "0.1"
    OPENAI_API_KEY: str = ""
    FILE_ALLOWED_TYPES: List[str] = ["text/plain", "application/pdf"]
    FILE_MAX_SIZE: int = 10  # 10MB
    FILE_DEFAULT_CHUNK_SIZE: int = 512000  # 512KB

    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()
