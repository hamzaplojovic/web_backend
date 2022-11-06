from schemas import user
from database.db import connect_to_db
from utils.hashed import hashed_password

db = connect_to_db("users")

class UsersLayer:
    def get_all_users() -> list[dict]:
        return [x for x in db.find({})]

    def create_user(item: dict) -> dict:
        db.insert_one(item)
        return item
    
    def update_user(query:str,item: dict) -> dict:
        db.update_one({query: item[query]}, {
            "$set": item
        })
        return item

    def hard_delete_user(username:str) -> str:
        return db.find_one_and_delete({"username":username})

    def get_user_by_username(username:str) -> dict:
        return db.find_one({"username":username})
    
    def delete_user(username:str) -> any:
        return db.find_one_and_update({"username":username}, {
            "$set":{
                "is_active": False
            }
        })

    def login(username:str, password: str) -> user.User:
        user = db.find_one({"username":username, "password": str(hashed_password(password))})
        return user

