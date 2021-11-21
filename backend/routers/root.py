from fastapi import APIRouter
from backend.db import message

router = APIRouter()

@router.get("/")
async def root():
    return {"message": message}
