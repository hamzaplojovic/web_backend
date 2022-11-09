from schemas import user
from pymongo import ReturnDocument
from database.db import connect_to_db
from utils.hashed import hashed_password

db = connect_to_db("users")

class UsersLayer:
    def get_all_users() -> list[dict]:
        return [x for x in db.find({})]

    def create_user(item: dict) -> dict:
        return db.insert_one(item)
    
    def update_user(query:str,item: dict) -> dict:
        db.find_one_and_update({query: item[query]}, {
            "$set": item
        },return_document=ReturnDocument.AFTER)

    def hard_delete_user(username:str) -> str:
        return db.find_one_and_delete({"username":username})

    def get_user_by_username(username:str) -> dict:
        return db.find_one({"username":username})
    
    def delete_user(username:str) -> any:
        return db.find_one_and_update({"username":username}, {
            "$set":{
                "is_active": False
            }
        },return_document=ReturnDocument.AFTER)

    def login(username:str, password: str) -> user.User:
        return db.find_one({"username":username, "password": str(hashed_password(password))})

