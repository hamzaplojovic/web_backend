from fastapi import APIRouter, status
from repo import admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/login", status_code=status.HTTP_200_OK)
async def admin_login(username: str, password: str):
    return admin.login(username, password)


@router.get("/activate", status_code=status.HTTP_200_OK)
async def activate(username: str):
    return admin.user_action(username, True)


@router.get("/deactivate", status_code=status.HTTP_200_OK)
async def deactivate(username: str):
    return admin.user_action(username, False)
