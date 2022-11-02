from schemas import user
from db.data_access import UsersLayer
from utils.constants import USER_ROLES
from utils.hashed import hashed_password
from utils.exceptions import UserExceptions
from repo.role_checker import RoleChecker
from .approve_actions import WriteApproval

data_layer = UsersLayer
allow_create_resource = RoleChecker(["admin"])

def _parse_user(username:str, is_active:bool, user_status:str):
    user = data_layer.get_user_by_username(username)
    user["is_active"] = is_active
    user["status"] = user_status
    approval = WriteApproval(user, user_status)
    approval.write_approval()
    return user


def user_action(username:str, is_active:bool, user_status:str) -> user.User:
    try:
        user = _parse_user(username, is_active, user_status)
        data_layer.update_user("username", user)
        return f"{username} is active: {str(is_active)}"
    except:
        return UserExceptions.raise_conflict("Cannot apply action on user")


def login(username:str, password:str) -> int:
    user = data_layer.login(username, hashed_password(password))
    return 200 if allow_create_resource(user[0]["role"]) else 404


def make_instructor(username:str) -> user.User:
    user = data_layer.get_user_by_username(username)
    user["role"] = USER_ROLES["INSTRUCTOR"]
    return data_layer.update_user("username", user)