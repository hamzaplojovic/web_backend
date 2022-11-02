import os
from schemas import user
from utils import github
from utils.send_mail import Email
from db.data_access import UsersLayer
from utils.hashed import hashed_password
from utils.validation import user_creation
from utils.exceptions import UserExceptions
from utils.constants import USER_STATUS, USER_ROLES

data_layer = UsersLayer

def _parse_user(user:user.User):
    user.avatar = github.get_github_avatar_url(user.github)
    user.languages = github.get_github_language_percentages(user.github)
    user.password = hashed_password(user.password)
    user.is_active = False
    user.status = USER_STATUS["ON_HOLD"]
    user.role = USER_ROLES["STUDENT"]
    email = Email("hamzaplojovic9@gmail.com", user.email, os.environ["SMTP_PASSWORD"])
    email.send_code()
    user = dict(user)
    user["_id"] = user["username"]

    return user


def get_all() -> list[dict]:
    try:
        return data_layer.get_all_users()
    except:
        return UserExceptions.raise_conflict("Cannot fetch users")


def create_user(user: user.User) -> user.User:        
    if user_creation.validate_existence(user) != False:
        return UserExceptions.raise_conflict("User already exists")
    try:
        parsed_user = _parse_user(user)
        return data_layer.create_user(parsed_user)
    except:
        parsed_user = _parse_user(user)
        return data_layer.create_user(parsed_user)


def find_user_by_username(username:str) -> user.User or int:
    try:
        return data_layer.get_user_by_username(username)
    except:
        return UserExceptions.raise_not_found("User not found")


def update_user(user: user.User) -> user.User:
    try:
        return data_layer.update_user("username", dict(user))

    except:
        return UserExceptions.raise_conflict("Cannot update user")



def delete_user(username:str) -> any:
    try:
        return data_layer.update_user_part(username, "is_active", False) 
    except:
        return UserExceptions.raise_conflict("Cannot delete user")

    
    
def hard_delete_user(username:str) -> str:
    try:
        return data_layer.delete_user(username)
    except:
        return UserExceptions.raise_conflict("Cannot delete user")



def login(username:str, password:str) -> any:
    try:
        return data_layer.login(username, password)
    except:
        return UserExceptions.raise_not_found("User not found")