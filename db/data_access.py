from . import db
from schemas import user
from utils.hashed import hashed_password

users_db = db.connect_to_db("users")
courses_db = db.connect_to_db("courses")

class UsersLayer:
    def get_all_users() -> list[dict]:
        return [x for x in users_db.find({})]

    def create_user(item: dict) -> dict:
        users_db.insert_one(item)
        return item
    
    def update_user(query:str,item: dict) -> dict:
        users_db.update_one({query: item[query]}, {
            "$set": item
        })
        return item

    def delete_user(username:str) -> str:
        users_db.delete_one({"username":username})
        return f"User with username: {username} deleted"

    def get_user_by_username(username:str) -> dict:
        return users_db.find_one({"username":username})
    
    def update_user_part(username:str, property: str, value:any) -> dict:
        users_db.update_one({"username":username},{
            "$set":{
                property: value
            }
        })
        return f"User with username: {username} deleted"

    def login(username:str, password: str) -> user.User:
        user = users_db.find_one({"username":username, "password": str(hashed_password(password))})
        return user



class CoursesLayer:
    def get_all_courses() -> list[dict]:
        return [x for x in courses_db.find({})]
    
    def create_course(item:dict) -> dict:
        courses_db.insert_one(item)
        return item