from fastapi import HTTPException
from deta import Deta

deta = Deta("a063wuxg_k8zsfQrTEriaLdJwXbGRrE5DfcQYuaXd")
db = deta.Base("users")


def activate_user(username, value):
    user = db.fetch({"username": username}).items[0]
    user["is_active"] = value
    return user
