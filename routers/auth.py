from repo import auth
from schemas import user
from fastapi import APIRouter, status,Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)




@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.login(form_data)

@router.get("/me")
async def users_me(current_user: user.User = Depends(auth.get_current_user)):
    return current_user["role"]