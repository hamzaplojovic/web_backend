from schemas.user import User

def validate_user_data(user: User):
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