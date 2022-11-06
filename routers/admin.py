from repo import admin
from schemas import user
from utils.constants import USER_STATUS
from repo.role_checker import RoleChecker
from fastapi import APIRouter, status, Depends

approved_roles = RoleChecker(["admin"])

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(approved_roles)]
)

@router.get("/activate/{username}", status_code=status.HTTP_200_OK)
async def activate(username: str) -> user.User:
    return admin.user_action(username, True, USER_STATUS["APPROVED"])


@router.get("/deactivate/{username}", status_code=status.HTTP_200_OK)
async def deactivate(username: str) -> user.User:
    return admin.user_action(username, False, USER_STATUS["REJECTED"])

@router.get("/instructor/{username}", status_code=status.HTTP_200_OK)
async def make_instructor(username:str) -> user.User:
    return admin.make_instructor(username)