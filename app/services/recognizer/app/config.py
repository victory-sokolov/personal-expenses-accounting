import os
from typing import List, Union
from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, validator

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Settings(BaseSettings):
    """Base configuration"""
    BASE_URL : str = os.getenv("BASE_URL", "http://localhost:5000")
    API_V1: str = "/api/v1"
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    UPLOAD_FOLDER = os.path.abspath(os.curdir) + str(os.getenv('UPLOAD_FOLDER', "data"))
    ALLOWED_IMAGE_EXTENSIONS = os.getenv('ALLOWED_IMAGE_EXTENSIONS')
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQLALCHEMY_DATABASE_URI: Union[str, None] = os.getenv('DATABASE_URL')
    MYSQL_USERNAME: Union[str, None] = os.getenv('MYSQL_USERNAME')
    MYSQL_PASSWORD: Union[str, None] = os.getenv('MYSQL_PASSWORD')

    # Celery
    CELERY_BROKER_URL="redis://localhost:6379"

settings = Settings()
