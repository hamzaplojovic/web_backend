import os
from db import db
from schemas import user
from utils import github
from utils.send_mail import Email
from utils.hashed import hashed_password
from utils.validation import user_creation
from utils.exceptions import UserExceptions
from utils.constants import USER_STATUS, USER_ROLES

db = db.connect_to_db('users')

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
        return [x for x in db.find({})]
    except:
        return UserExceptions.raise_conflict("Cannot fetch users")


def create_user(user: user.User) -> user.User:        
    if user_creation.validate_existence(user) != False:
        return UserExceptions.raise_conflict("User already exists")
    try:
        parsed_user = _parse_user(user)
        db.insert_one(parsed_user)
        return parsed_user
    except:
        return UserExceptions.raise_conflict("Cannot create user")



def find_user_by_username(username:str) -> user.User or int:
    try:
        return db.find_one({"username":username})
    except:
        return UserExceptions.raise_not_found("User not found")


def update_user(user: user.User) -> user.User:
    try:
        db.update_one({"username":user.username}, {
            "$set": dict(user)
        })
        return user
    except:
        return UserExceptions.raise_conflict("Cannot update user")


def delete_user(username:str) -> any:
    try:
        db.update_one({"username":username},{
            "$set":{
                "is_active":False
            }
        })
    except:
        return UserExceptions.raise_conflict("Cannot delete user")

    
    
def hard_delete_user(username:str) -> str:
    try:
        db.delete_one({"username":username})
        return f"User with username: {username} deleted"
    except:
        return UserExceptions.raise_conflict("Cannot delete user")



def login(username:str, password:str) -> any:
    try:
        user = db.find_one({"username":username, "password": hashed_password(password)})
        return user
    except:
        return UserExceptions.raise_not_found("User not found")