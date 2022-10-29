from db import deta_db
from schemas import user
from utils.constants import USER_ROLES
from utils.hashed import hashed_password
from repo.role_checker import RoleChecker
from .approve_actions import WriteApproval


db = deta_db.connect_to_deta_db("users")
allow_create_resource = RoleChecker(["admin"])


def user_action(username:str, is_active:bool, status:str) -> user.User:
    user = db.get(username)
    user["is_active"] = is_active
    user["status"] = status
    approval = WriteApproval(user, status)
    approval.write_approval()
    return db.put(user, key=user["username"])



def login(username:str, password:str) -> int:
    user = db.fetch({"username": username, "password": hashed_password(password)}).items
    return 200 if allow_create_resource(user[0]["role"]) else 404


def make_instructor(username:str) -> user.User:
    user = db.get(username)
    user["role"] = USER_ROLES["INSTRUCTOR"]
    return db.put(user, key=user["key"])