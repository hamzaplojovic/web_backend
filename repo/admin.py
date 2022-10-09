from hashlib import sha256
from deta import Base
from db import deta_db

db = deta_db.connect_to_deta_db("users")

def user_action(username, is_active, status):
    user = db.fetch({"username": username}).items[0]
    user["is_active"] = is_active
    user["status"] = status
    return db.put(user, key=user["username"])


def login(username, password):
    user = db.fetch({"username": username, "password": sha256(
        password.encode("utf-8")).hexdigest()}).items
    return 200 if user[0]["role"] == "Admin" else 404
