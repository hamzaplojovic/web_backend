from utils import github
from utils.constants import USER_STATUS
from db import deta_db
from schemas import user
from utils.hashed import hashed_password



db = deta_db.connect_to_deta_db('users')


def get_all() -> list:
    return db.fetch().items


def create_user(user: user.User) -> user.User:        
    user.avatar = github.get_github_avatar_url(user.github)
    user.languages = github.get_github_language_percentages(user.github)
    user.password = hashed_password(user.password)
    user.is_active = False
    user.status = USER_STATUS["ON_HOLD"]
    db.put(dict(user), key=user.username)
    return user


def find_user_by_username(username:str) -> user.User or int:
    user = db.get(username)
    return user or 404

def change_user(user: user.User) -> user.User:
    db.put(dict(user), key=user.username)
    return user


def delete_user(username:str):
    return db.delete(username)


def login(username:str, password:str):
    query =  db.fetch({"username":username, "password": hashed_password(password)}).items
    return 200 if query[0] else 404