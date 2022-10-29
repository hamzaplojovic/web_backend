from repo import auth
from schemas import user
from fastapi import APIRouter, Request, status, Depends
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.login(form_data)

@router.get("/me")
async def users_me(request:Request,current_user: user.User = Depends(auth.get_current_user)):
    return auth.get_current_user(request)

@router.get("/code/{username}")
async def approve_code(username):
    return auth.approve_code(username)