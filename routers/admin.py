from fastapi import APIRouter, status
from repo import admin
from utils.constants import USER_STATUS
from schemas import user


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/login", status_code=status.HTTP_200_OK)
async def admin_login(username: str, password: str) -> 200 or 404:
    return admin.login(username, password)


@router.get("/activate/{username}", status_code=status.HTTP_200_OK)
async def activate(username: str) -> user.User:
    return admin.user_action(username, True, USER_STATUS["APPROVED"])


@router.get("/deactivate/{username}", status_code=status.HTTP_200_OK)
async def deactivate(username: str) -> user.User:
    return admin.user_action(username, False, USER_STATUS["REJECTED"])
