import os
from schemas import user
from utils.validation import user_creation
from database.data_access.users import UsersLayer
from utils import github, hashed, send_mail, exceptions, constants

data_layer = UsersLayer
user_exceptions = exceptions.UserExceptions

class UserLogic:
    def _parse_user(self, user:user.User):
        user.avatar = github.get_github_avatar_url(user.github)
        user.languages = github.get_github_language_percentages(user.github)
        user.password = hashed.hashed_password(user.password)
        user.is_active = False
        user.status = constants.USER_STATUS["ON_HOLD"]
        user.role = constants.USER_ROLES["STUDENT"]
        email = send_mail.Email("hamzaplojovic9@gmail.com", user.email, os.environ["SMTP_PASSWORD"])
        email.send_code()
        user = dict(user)
        user["_id"] = user["username"]

        return user

    def _user_in_db(self, user: dict):
        user_in_db = {
            "username":user["username"],
            "full_name":user["full_name"],
            "email":user["email"],
            "job":user["job"],
            "languages":user["languages"],
            "avatar":user["avatar"],
            "is_active":user["is_active"],
            "role":user["role"]
        }

        return user_in_db

    def get_all_users(self) -> list[dict]:
        try:
            return [self._user_in_db(x) for x in data_layer.get_all_users()]
        except:
            return [self._user_in_db(x) for x in data_layer.get_all_users()]

    def create_user(self, user:user.User) -> any:
        if user_creation.validate_existence(user) != False:
            return user_exceptions.raise_conflict("User already exists")
        try:
            parsed_user = self._parse_user(user)
            data_layer.create_user(parsed_user)
        except:
            return user_exceptions.raise_conflict("Cannot create user")
    
    def find_user_by_username(self, username:str):
        try:
            user = data_layer.get_user_by_username(username)
            return user
        except:
            return user_exceptions.raise_not_found("User not found")
        
    def update_user(self, user:user.User):
        try:
            user.password = hashed.hashed_password(user.password)
            data_layer.update_user("username", dict(user))

        except:
            return user_exceptions.raise_conflict("Cannot update user")

    def delete_user(self, username:str):
        try:
            data_layer.delete_user(username) 
        except:
            return user_exceptions.raise_conflict("Cannot delete user")
        
    def hard_delete_user(self, username:str):
        try:
            data_layer.hard_delete_user(username)
        except:
            return user_exceptions.raise_conflict("Cannot delete user")

    def login(self, username:str, password:str):
        try:
            return data_layer.login(username, password)
        except:
            return user_exceptions.raise_not_found("User not found")