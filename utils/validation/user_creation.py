from db import db
from schemas.user import User

db = db.connect_to_db("users")

def validate_existence(user:User) -> bool:
    number_of_users = db.count_documents({"username":user.username})
    return True if number_of_users > 0 else False

def validate_user_data(user: User) -> bool:
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
        
    return True if counter_field == len(requirements) else False