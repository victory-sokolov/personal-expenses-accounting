from datetime import date
from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
def get_healthcheck():
    return { 
        "status": "Alive",
        "date": date.today()
    }
