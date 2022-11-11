from database.db import connect_to_db

db = connect_to_db("coworking")


class CoworkingLayer:

    def get_all(self) -> list[dict]:
        return db.find({})

    def get_floor_by_name(self, floor_number: int):
        return db.find_one({"name": floor_number})

    def create_floor(self, item: dict):
        return db.insert_one(item)

    def delete_floor(self, floor_number: int):
        return db.delete_one({"floor_number": floor_number})

    def create_table(self, item: dict):
        return db.insert_one(item)

    def delete_table(self, table_number: int):
        return db.find_one_and_delete({"table_number": table_number})

    def update_table(self, item: dict):
        pass

    def assing_to_table(self, table_number: int, username: str):
        pass

    def remove_from_table(self, table_number: int, username: str):
        pass
