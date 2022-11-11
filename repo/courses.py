from schemas.course import Course, Lecture
from logic.courses import CoursesLogic



def get_all():
    return CoursesLogic.get_all_courses()


def create_course(course: Course):
    return CoursesLogic.create_course(course)


def get_by_name(course_name: str):
    return CoursesLogic.get_course_by_name(course_name)


def update_course(course: Course):
    return CoursesLogic.update_course(course)


def delete_course(course_name: str):
    return CoursesLogic.delete_course(course_name)


def hard_delete_course(course_name: str):
    return CoursesLogic.hard_delete_course(course_name)


def get_students_from_course(course_name: str):
    return CoursesLogic.get_students_from_course(course_name)


def assign_to_course(course_name: str, username: str):
    return CoursesLogic.assign_user_to_course(course_name, username)


def remove_from_course(course_name: str, username: str):
    return CoursesLogic.remove_user_from_course(course_name, username)


def add_lecture(course_name: str, lecture: Lecture):
    return CoursesLogic.add_lecture_to_course(course_name, lecture)


def start_lecture(course_name: str, lecture_name: str):
    return CoursesLogic.change_lecture_status(course_name, lecture_name,
                                              "started")


def complete_lecture(course_name: str, lecture_name: str):
    return CoursesLogic.change_lecture_status(course_name, lecture_name,
                                              "ended")


def user_presence(request: any):
    return CoursesLogic.user_presence(dict(request))
