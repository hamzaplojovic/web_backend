from database.data_access.coworking import CoworkingLayer

data_layer = CoworkingLayer()


class CoworkingLogic:

    def get_all(self) -> list[dict]:
        return data_layer.get_all()

    def get_all_from_floor(self, floor_number: int):
        return data_layer.get_floor_by_name(floor_number)
