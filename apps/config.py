from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    db_url: str



if os.getenv("ENV") == "production":
    settings = Settings()
elif os.getenv("ENV") == "testing":
    settings = Settings(_env_file=".env.testing", _env_file_encoding="utf-8")
else:
    settings = Settings(_env_file=".env.local", _env_file_encoding="utf-8")