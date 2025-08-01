from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

ENV_PATH = ".env" 

class Settings(BaseSettings):
    DB_URL: str
    
    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH)
    )
        
settings = Settings()