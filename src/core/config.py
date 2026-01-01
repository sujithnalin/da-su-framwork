from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    GCP_PROJECT_ID: str = os.getenv('GCP_PROJECT_ID') 
    SPANNER_INSTANCE_ID: str = os.getenv('SPANNER_INSTANCE_ID') 
    SPANNER_DATABASE_ID: str = os.getenv('SPANNER_DATABASE_ID') 

settings = Settings()
