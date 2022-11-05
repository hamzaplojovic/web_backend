from db import db
from schemas import course

db = db.connect_to_db("courses")

def _parse_course(course: course.Course):
    course = dict(course)
    course["_id"] = course["name"]

    return course

def get_all():
    return [x for x in db.find({})]

def create_course(course: course.Course):
    course = _parse_course(course)
    db.insert_one(course)
    return course

def get_by_name(name:str):
    pass

def change_course(course: course.Course):
    pass

def delete_course(name):
    db.delete_one({"name":name})
    return "Deleted"

def get_students_from_course(name:str):
    course = db.find_one({"name":name})
    return course["students"]

def assign_to_course(course_name:str, username:str):
    course = db.find_one({"name":course_name})
    course["students"].append(username)
    db.update_one({"name": course_name}, {
            "$set": course
    })
    return course

def remove_student_from_course(username:str):
    pass

def add_lecture(course_name, lecture_name:str, lecture_description:str):
    pass

def user_presence(course_name:str, username:str, is_present:bool):
    pass

def complete_lecture(course_name, lecture_name):
    pass