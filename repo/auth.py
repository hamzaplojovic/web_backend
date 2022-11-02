from datetime import timedelta
from db.data_access import UsersLayer
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from utils.jwt_handler import get_username_from_current_user, create_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
data_layer = UsersLayer

def get_current_user(request:Request, _:str = Depends(oauth2_scheme)):
    return data_layer.get_user_by_username(get_username_from_current_user(request))


def login(form_data: OAuth2PasswordRequestForm):
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"username": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def approve_code(username:str) -> str:
    user = data_layer.get_user_by_username(username)
    user["status"] = "received"
    data_layer.update_user("username", user)
    return f"Approved {username} that has confirmed email address"
