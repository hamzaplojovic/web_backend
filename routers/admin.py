from fastapi import APIRouter, status
from repo import admin
from utils.constants import USER_STATUS


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/login", status_code=status.HTTP_200_OK)
async def admin_login(username: str, password: str):
    return admin.login(username, password)


@router.get("/activate/{username}", status_code=status.HTTP_200_OK)
async def activate(username: str):
    return admin.user_action(username, True, USER_STATUS["APPROVED"])


@router.get("/deactivate/{username}", status_code=status.HTTP_200_OK)
async def deactivate(username: str):
    return admin.user_action(username, False, USER_STATUS["REJECTED"])
