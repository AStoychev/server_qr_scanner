from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017"
    database_name: str = "fastapi_db"

settings = Settings()
