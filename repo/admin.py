from logic.admin import AdminLogic

admin_logic = AdminLogic()

def user_action(username:str, is_active:bool, status:str):
    return admin_logic.user_action(username, is_active, status)

def make_instructor(username:str):
    return admin_logic.make_instructor(username)