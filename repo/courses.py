from schemas import course
from database.data_access.courses import CoursesLayer

def _parse_course(course: course.Course):
    course = dict(course)
    course["_id"] = course["name"]

    return course

def get_all():
    return CoursesLayer.get_all_courses()

def create_course(course: course.Course):
    course = _parse_course(course)
    return CoursesLayer.create_course(course)

def get_by_name(name:str):
    return CoursesLayer.get_course_by_name(name)

def update_course(course: course.Course):
    return CoursesLayer.update_course(dict(course))

def delete_course(name:str):
    return CoursesLayer.delete_course(name)

def hard_delete_course(name:str):
    return CoursesLayer.hard_delete_course(name)

def get_students_from_course(course_name:str):
    return CoursesLayer.get_students_from_course(course_name)

def assign_to_course(course_name:str, username:str):
    return CoursesLayer.assign_user_to_course(course_name, username)

def remove_student_from_course(username:str):
    pass

def add_lecture(course_name:str, lecture_name:str, lecture_description:str):
    pass

def start_lecture(course_name:str, lecture_name:str):
    pass

def user_presence(course_name:str, username:str, is_present:bool):
    pass

def complete_lecture(course_name:str, lecture_name:str):
    pass

def accept_payment():
    pass

