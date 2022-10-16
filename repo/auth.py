from db import deta_db
from utils.hashed import hashed_password

db = deta_db.connect_to_deta_db('users')


def login(username, password):
    query =  db.fetch({"username":username, "password": hashed_password(password)}).items
    return 200 if query[0] else 404
