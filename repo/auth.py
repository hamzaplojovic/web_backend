from db import deta_db
from utils.hashed import hashed_password
from utils.token import JWTToken

db = deta_db.connect_to_deta_db('users')


def login(username, password):
    query =  db.fetch({"username":username, "password": hashed_password(password)}).items
    token = JWTToken.generate_token({"sub":query[0]["username"]})
    return token
