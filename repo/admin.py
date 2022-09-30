from deta import Deta
from hashlib import sha256

deta = Deta("a063wuxg_k8zsfQrTEriaLdJwXbGRrE5DfcQYuaXd")
db = deta.Base("users")


def user_action(username, value):
    user = db.fetch({"username": username}).items
    if user[0]:
        user[0]["is_active"] = value
        return user


def login(username, password):

    user = db.fetch({"username": username, "password": sha256(
        password.encode("utf-8")).hexdigest()}).items
    return 200 if user[0]["role"] == "admin" else 404
