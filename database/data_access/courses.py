from database.db import connect_to_db
from pymongo import ReturnDocument

db = connect_to_db("courses")


class CoursesLayer:

    @staticmethod
    def get_all_courses() -> list[dict]:
        return list(db.find({}))

    @staticmethod
    def update_course_attribute(course_name: str, attribute: str,
                                value: any):
        return db.find_one_and_update({"name": course_name},
                                      {"$set": {
                                          attribute: value
                                      }},
                                      return_document=ReturnDocument.AFTER)

    def create_course(item: dict) -> dict:
        return db.insert_one(item)

    def update_course(new_item: dict):
        db.update_one({"name": new_item["name"]}, {"$set": new_item})
        return new_item

    def get_course_by_name(course_name: str):
        return db.find_one({"name": course_name})

    def delete_course(course_name: str):
        course = db.find_one({"name": course_name})
        course["is_active"] = False
        db.update_one({"name": course_name}, {"$set": course})
        return course

    def hard_delete_course(course_name: str):
        return db.find_one_and_delete({"name": course_name})
