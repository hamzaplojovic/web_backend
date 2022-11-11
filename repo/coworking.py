from logic.coworking import CoworkingLogic

coworking_logic = CoworkingLogic()

def get_all():
    return coworking_logic.get_all()

def get_all_from_floor(floor_number:int):
    return coworking_logic.get_all_from_floor(floor_number)