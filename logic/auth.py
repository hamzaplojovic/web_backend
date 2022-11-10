from fastapi import Request
from datetime import timedelta
from database.data_access.users import UsersLayer
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from utils.jwt_handler import get_username_from_current_user, create_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class AuthLogic:

    @staticmethod
    def _update_on_confirm(user: dict):
        user["status"] = "received"
        UsersLayer.update_user("username", user)
        return user["username"] + " has confirmed email address"

    @staticmethod
    def _parse_token(credentials: OAuth2PasswordRequestForm):
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"username": credentials.username},
            expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    def get_current_user(request: Request):
        return UsersLayer.get_user_by_username(
            get_username_from_current_user(request))

    def login(self, form_data: OAuth2PasswordRequestForm):
        return self._parse_token(form_data)

    def approve_code(self, username: str) -> str:
        user = UsersLayer.get_user_by_username(username)
        return self._update_on_confirm(user)
