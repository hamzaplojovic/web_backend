from repo import admin
from schemas import user
from utils.constants import USER_STATUS
from repo.role_checker import RoleChecker
from fastapi import APIRouter, status,Depends

allow_create_resource = RoleChecker(["admin"])

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(allow_create_resource)],
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
