from fastapi import APIRouter, status
from repo import admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/activate", status_code=status.HTTP_200_OK)
async def activate(username: str):
    return admin.activate_user(username, True)


@router.get("/deactivate", status_code=status.HTTP_200_OK)
async def deactivate(username: str):
    return admin.activate_user(username, False)
