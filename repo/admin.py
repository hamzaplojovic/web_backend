from db import db
from schemas import user
from utils.constants import USER_ROLES
from utils.hashed import hashed_password
from utils.exceptions import UserExceptions
from repo.role_checker import RoleChecker
from .approve_actions import WriteApproval


db = db.connect_to_db("users")
allow_create_resource = RoleChecker(["admin"])

def _parse_user(username:str, is_active:bool, user_status:str):
    user = dict(db.find_one({"username":username}))
    user["is_active"] = is_active
    user["status"] = user_status
    approval = WriteApproval(user, user_status)
    approval.write_approval()
    return user


def user_action(username:str, is_active:bool, user_status:str) -> user.User:
    try:
        user = _parse_user(username, is_active, user_status)
        db.update_one({"username":username}, {"$set":dict(user)})
        return f"{username} is active: {str(is_active)}"
    except:
        return UserExceptions.raise_conflict("Cannot apply action on user")


def login(username:str, password:str) -> int:
    user = db.fetch({"username": username, "password": hashed_password(password)}).items
    return 200 if allow_create_resource(user[0]["role"]) else 404


def make_instructor(username:str) -> user.User:
    user = db.get(username)
    user["role"] = USER_ROLES["INSTRUCTOR"]
    return db.put(user, key=user["key"])