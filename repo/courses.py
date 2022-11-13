from schemas.course import Course, Lecture
from logic.courses import CoursesLogic

courses_logic = CoursesLogic()


def get_all():
    return courses_logic.get_all_courses()


def create_course(course: Course):
    return courses_logic.create_course(course)


def get_by_name(course_name: str):
    return courses_logic.get_course_by_name(course_name)


def update_course(course: Course):
    return courses_logic.update_course(course)


def delete_course(course_name: str):
    return courses_logic.delete_course(course_name)


def hard_delete_course(course_name: str):
    return courses_logic.hard_delete_course(course_name)


def get_students_from_course(course_name: str):
    return courses_logic.get_students_from_course(course_name)


def assign_to_course(course_name: str, username: str):
    return courses_logic.assign_user_to_course(course_name, username)


def remove_from_course(course_name: str, username: str):
    return courses_logic.remove_user_from_course(course_name, username)


def add_lecture(course_name: str, lecture: Lecture):
    return courses_logic.add_lecture_to_course(course_name, lecture)


def start_lecture(course_name: str, lecture_name: str):
    return courses_logic.change_lecture_status(course_name, lecture_name,
                                               "started")


def complete_lecture(course_name: str, lecture_name: str):
    return courses_logic.change_lecture_status(course_name, lecture_name,
                                               "ended")


def user_presence(request: any):
    return courses_logic.user_presence(dict(request))
