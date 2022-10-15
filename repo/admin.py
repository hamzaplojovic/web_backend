from hashlib import sha256
from db import deta_db
from utils.approve_actions import WriteApproval

db = deta_db.connect_to_deta_db("users")

def user_action(username, is_active, status):
    user = db.fetch({"username": username}).items[0]
    user["is_active"] = is_active
    user["status"] = status
    approval = WriteApproval(user, status)
    approval.write_approval()
    return db.put(user, key=user["username"])



def login(username, password) -> int:
    user = db.fetch({"username": username, "password": sha256(
        password.encode("utf-8")).hexdigest()}).items
    return 200 if user[0]["role"] == "Admin" else 404
