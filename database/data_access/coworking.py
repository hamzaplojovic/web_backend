from database.db import connect_to_db

db = connect_to_db("coworking")


class CoworkingLayer:

    @staticmethod
    def get_all() -> list[dict]:
        return db.find({})

    @staticmethod
    def get_floor_by_name(floor_number: int):
        return db.find_one({"name": floor_number})

    @staticmethod
    def create_floor(item: dict):
        return db.insert_one(item)

    @staticmethod
    def delete_floor(floor_number: int):
        return db.delete_one({"floor_number": floor_number})

    @staticmethod
    def create_table(item: dict):
        return db.insert_one(item)

    @staticmethod
    def delete_table(table_number: int):
        return db.find_one_and_delete({"table_number": table_number})

    def update_table(self, item: dict):
        raise NotImplementedError()

    def assing_to_table(self, table_number: int, username: str):
        raise NotImplementedError()

    def remove_from_table(self, table_number: int, username: str):
        raise NotImplementedError()
