from db import db
from schemas import course

db = db.connect_to_db("courses")

def get_all():
    return db.fetch().items

def create_course(course: course.Course):
    return db.put(dict(course), key=course.name)

def get_by_name(name:str):
    course = db.get(name)
    return 200 if course else 404

def change_course(course: course.Course):
    return db.put(dict(course), key=course.name)

def delete_course(name):
    return db.delete(name)