from schemas import user
from utils.constants import USER_ROLES
from utils.hashed import hashed_password
from repo.role_checker import RoleChecker
from .approve_actions import WriteApproval
from utils.exceptions import UserExceptions
from database.data_access.users import UsersLayer

allow_create_resource = RoleChecker(["admin"])

def _instructor_from_user(user:dict):
    user["role"] = USER_ROLES["INSTRUCTOR"]
    UsersLayer.update_user("username", user)
    return f"{user.username} is now instructor"

def _parse_user(username:str, is_active:bool, user_status:str):
    user = UsersLayer.get_user_by_username(username)
    user["is_active"] = is_active
    user["status"] = user_status
    approval = WriteApproval(user, user_status)
    approval.write_approval()
    return user

def _update_parsed_user(user:dict):
    UsersLayer.update_user("username", user)
    return user["username"] + "is active: " + str(user["is_active"])


def user_action(username:str, is_active:bool, user_status:str) -> user.User:
    try:
        user = _parse_user(username, is_active, user_status)
        return _update_parsed_user(user)
    except:
        return UserExceptions.raise_conflict("Cannot apply action on user")


def login(username:str, password:str) -> int:
    user = UsersLayer.login(username, hashed_password(password))
    return 200 if allow_create_resource(user[0]["role"]) else 404


def make_instructor(username:str) -> user.User:
    user = UsersLayer.get_user_by_username(username)
    return _instructor_from_user(user)