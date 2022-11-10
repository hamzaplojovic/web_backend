from logic import auth
from fastapi import Request, Depends
from fastapi.security import OAuth2PasswordRequestForm

auth_logic = auth.AuthLogic()


def get_current_user(request: Request, _: str = Depends(auth.oauth2_scheme)):
    return auth_logic.get_current_user(request)


def login(form_data: OAuth2PasswordRequestForm):
    return auth_logic.login(form_data)


def approve_code(username: str):
    return auth_logic.approve_code(username)
