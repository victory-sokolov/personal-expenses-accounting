from fastapi.routing  import APIRouter

from .v1.endpoints import recognizer
from . import healthcheck

api_router = APIRouter()
api_router.include_router(recognizer.router)
api_router.include_router(healthcheck.router)
