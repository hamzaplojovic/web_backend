from fastapi import APIRouter, status
from repo import users
from schemas import user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users():
    return users.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(request: user.User):
    # TODO: add valdiation where is needed
    return users.create_user(request)


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def find_user(username):
    return users.find_user(username)


@router.put("/{username}", status_code=status.HTTP_202_ACCEPTED)
async def change_user(request: user.User):
    return users.change_user(request)


@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def change_user(username):
    return users.delete_user(username)
