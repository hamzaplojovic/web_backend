from datetime import timedelta
from fastapi import Depends, Request
from database.data_access.users import UsersLayer
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from utils.jwt_handler import get_username_from_current_user, create_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def _update_on_confirm(user:dict):
    user["status"] = "received"
    UsersLayer.update_user("username", user)
    return f"Approved {user.username} that has confirmed email address"


def _parse_token(credentials: OAuth2PasswordRequestForm):
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"username": credentials.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(request:Request, _:str = Depends(oauth2_scheme)):
    return UsersLayer.get_user_by_username(get_username_from_current_user(request))

def login(form_data: OAuth2PasswordRequestForm):
    return _parse_token(form_data)

def approve_code(username:str) -> str:
    user = UsersLayer.get_user_by_username(username)
    return _update_on_confirm(user)
