from db import deta_db
from schemas.user import User

db = deta_db.connect_to_deta_db("users")

def validate_existence(username:str) -> 200 or 404:
    user = db.fetch({"username":username}).items
    if len(user):
        return 404
    return 200

def validate_user_data(user: User) -> 200 or 404:
    if validate_existence(user["username"]) == 200: 
        requirements = {
            "username": True,
            "password": True,
            "full_name": True,
            "email": True,
            "github": True,
            "job": True,
        }
        counter_field = 0
        for field in requirements:
            if user[field]:
                counter_field += 1
        
        return 200 if counter_field == len(requirements) else 404