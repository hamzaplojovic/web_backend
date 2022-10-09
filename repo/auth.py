from hashlib import sha256
from db import deta_db

db = deta_db.connect_to_deta_db('users')


def login(username, password):
    query =  db.fetch({"username":username, "password": sha256(
        password.encode("utf-8")).hexdigest()}).items
    return 200 if query[0] else 404
