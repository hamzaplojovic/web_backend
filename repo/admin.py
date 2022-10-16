from db import deta_db
from schemas import user
from utils.constants import USER_ROLES
from utils.hashed import hashed_password
from .approve_actions import WriteApproval

db = deta_db.connect_to_deta_db("users")

def user_action(username, is_active, status) -> user.User:
    user = db.get(username)
    user["is_active"] = is_active
    user["status"] = status
    approval = WriteApproval(user, status)
    approval.write_approval()
    return db.put(user, key=user["username"])



def login(username, password) -> int:
    user = db.fetch({"username": username, "password": hashed_password(password)}).items
    return 200 if user[0]["role"] == USER_ROLES["ADMIN"] else 404
