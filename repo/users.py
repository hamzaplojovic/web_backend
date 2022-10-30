import os
from db import deta_db
from schemas import user
from utils import github
from utils.send_mail import Email
from utils.hashed import hashed_password
from utils.validation import user_creation
from utils.exceptions import UserExceptions
from utils.constants import USER_STATUS, USER_ROLES

db = deta_db.connect_to_deta_db('users')


def _parse_user(user:user.User):
    try:
        user.avatar = github.get_github_avatar_url(user.github)
        user.languages = github.get_github_language_percentages(user.github)
        user.password = hashed_password(user.password)
        user.is_active = False
        user.status = USER_STATUS["ON_HOLD"]
        user.role = USER_ROLES["STUDENT"]
        email = Email("hamzaplojovic9@gmail.com", user.email, os.environ["SMTP_PASSWORD"])
        email.send_code()
        return user
    except:
        return UserExceptions.raise_conflict("Cannot parse user")

def get_all() -> list:
    try:
        return db.fetch().items
    except:
        return UserExceptions.raise_conflict("Cannot fetch users")


def create_user(user: user.User) -> user.User:        
    if user_creation.validate_user_data(dict(user)) == 200:
        try:
            user = _parse_user(user)
            return db.put(dict(user), key=user.username)
        except:
            return UserExceptions.raise_conflict("Cannot create user")



def find_user_by_username(username:str) -> user.User or int:
    user = db.get(username)
    if not user:
        return UserExceptions.raise_not_found("User not found")
    return user

def update_user(user: user.User) -> user.User:
    user = db.update(dict(user), key=user.username)
    if not user:
        return UserExceptions.raise_not_found("User not found")


def delete_user(username:str) -> any:
    user = db.get(username)
    if not user:
        return UserExceptions.raise_not_found("User not found")
    user["is_active"] = False
    db.update(user, key=user["username"])



def login(username:str, password:str) -> user.User or str:
    user =  db.fetch({"username":username, "password": hashed_password(password)}).items[0]
    if not user:
        return UserExceptions.raise_not_found("User not found")
    return user