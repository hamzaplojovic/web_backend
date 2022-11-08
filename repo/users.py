from schemas import user
from logic.users import UserLogic

user_logic = UserLogic()

def get_all() -> list[dict]:
    return user_logic.get_all_users()

def create_user(user: user.User) -> user.User:        
    return user_logic.create_user(user)

def find_user_by_username(username:str) -> user.User or int:
    return user_logic.find_user_by_username(username)

def update_user(user: user.User) -> user.User:
    return user_logic.update_user(user)

def delete_user(username:str) -> any:
    return user_logic.delete_user(username)
    
def hard_delete_user(username:str) -> str:
    return user_logic.hard_delete_user(username)

def login(username:str, password:str) -> any:
    return user_logic.login(username, password)


