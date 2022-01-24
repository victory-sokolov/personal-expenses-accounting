from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from celery import Celery

from config import settings
from api.api import api_router

app = FastAPI(
    openapi_url=f"{settings.API_V1}/openapi.json"
)

celery = Celery(
    __name__,
    backend=settings.CELERY_BROKER_URL,
    broker=settings.CELERY_BROKER_URL,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1)
