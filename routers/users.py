from fastapi import APIRouter, status,HTTPException
from repo import users
from schemas import user
from validation import user_creation

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users():
    return users.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(request: user.User):
    if user_creation.validate_user_data(dict(request)) == 200:
        return users.create_user(request)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Requirements not met!")


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def find_user(username):
    return users.find_user_by_username(username)


@router.put("/{username}", status_code=status.HTTP_202_ACCEPTED)
async def change_user(request: user.User):
    if user_creation.validate_user_data(dict(request)) == 200:
        return users.change_user(request)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Requirements not met!")
    


@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(username):
    return users.delete_user(username)
