# from schemas import course
from database.db import connect_to_db

db = connect_to_db("courses")

class CoursesLayer:
    def get_all_courses() -> list[dict]:
        return [x for x in db.find({})]

    def create_course(item:dict) -> dict:
        db.insert_one(item)
        return item

    def update_course(new_item:dict):
        db.update_one({"name": new_item["name"]}, {
            "$set": new_item
        })
        return new_item
    
    def assign_user_to_course(course_name, username):
        course = db.find_one({"name":course_name})
        course["students"].append(username)
        db.update_one({"name": course_name}, {
                "$set": course
        })
        return course
    
    def get_students_from_course(course_name):
        course = db.find_one({"name":course_name})
        return course["students"]

    def get_course_by_name(course_name:str):
        return db.find_one({"name":course_name})
    
    def delete_course(course_name:str):
        return db.find_one_and_update({"name":course_name}, {
            "$set":{
                "is_active": False
            }
        })

    def hard_delete_course(course_name:str):
        return db.find_one_and_delete({"name":course_name})