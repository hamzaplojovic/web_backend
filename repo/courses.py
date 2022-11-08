from schemas import course
from logic.courses import CoursesLogic

course_logic = CoursesLogic()

def get_all():
    return course_logic.get_all_courses()

def create_course(course: course.Course):
    return course_logic.create_course(course)

def get_by_name(course_name:str):
    return course_logic.get_course_by_name(course_name)

def update_course(course: course.Course):
    return course_logic.update_course(course)

def delete_course(course_name:str):
    return course_logic.delete_course(course_name)

def hard_delete_course(course_name:str):
    return course_logic.hard_delete_course(course_name)

def get_students_from_course(course_name:str):
    return course_logic.get_students_from_course(course_name)

def assign_to_course(course_name:str, username:str):
    return course_logic.assign_user_to_course(course_name, username)

def remove_from_course(course_name:str, username:str):
    return course_logic.remove_user_from_course(course_name, username)

def add_lecture(course_name:str, lecture:course.Lecture):
    return course_logic.add_lecture_to_course(course_name, lecture)

def start_lecture(course_name:str, lecture_name:str):
    return course_logic.change_lecture_status(course_name, lecture_name, "started")

def complete_lecture(course_name:str, lecture_name:str):
    return course_logic.change_lecture_status(course_name, lecture_name, "ended")

def user_presence(course_name:str, lecture_name:str, username:str, is_present:bool):
    return course_logic.user_presence(course_name, lecture_name, username, is_present)