from database.data_access.coworking import CoworkingLayer

data_layer = CoworkingLayer()


class CoworkingLogic:

    @staticmethod
    def get_all() -> list[dict]:
        return data_layer.get_all()

    @staticmethod
    def get_all_from_floor(floor_number: int):
        return data_layer.get_floor_by_name(floor_number)
