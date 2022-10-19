from fastapi import Depends
from db.deta_db import connect_to_deta_db
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer

db = connect_to_deta_db("users")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(username:str = Depends(oauth2_scheme)):
    user = db.get(username)
    return user


def login(form_data: OAuth2PasswordRequestForm):
    user = db.get(form_data.username)
    return {"access_token": user["username"], "token_type": "bearer"}