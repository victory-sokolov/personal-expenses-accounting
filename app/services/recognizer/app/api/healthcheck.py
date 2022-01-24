from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
def get_healthcheck():
    return { "status" : "Alive"}
