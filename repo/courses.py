from db import db
from schemas import course

db = db.connect_to_db("courses")

def get_all():
    pass

def create_course(course: course.Course):
    pass

def get_by_name(name:str):
    pass

def change_course(course: course.Course):
    pass

def delete_course(name):
    pass