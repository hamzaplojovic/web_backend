from schemas import course
from database.data_access.courses import CoursesLayer


class CoursesLogic:

    @staticmethod
    def _parse_course(course: course.Course):
        course = dict(course)
        course["_id"] = course["name"]
        return course

    @staticmethod
    def get_all_courses() -> list[dict]:
        return CoursesLayer.get_all_courses()

    @staticmethod
    def get_course_by_name(course_name: str):
        return CoursesLayer.get_course_by_name(course_name)

    def create_course(self, course: course.Course):
        course = self._parse_course(course)
        return CoursesLayer.create_course(course)

    @staticmethod
    def update_course(course: course.Course):
        return CoursesLayer.update_course(dict(course))

    @staticmethod
    def delete_course(course_name: str):
        return CoursesLayer.delete_course(course_name)

    @staticmethod
    def hard_delete_course(course_name):
        return CoursesLayer.hard_delete_course(course_name)

    @staticmethod
    def get_students_from_course(course_name):
        return CoursesLayer.get_course_by_name(course_name)["students"]

    @staticmethod
    def assign_user_to_course(course_name, username):
        course = CoursesLayer.get_course_by_name(course_name)
        course["students"].append(username)
        return CoursesLayer.update_course(course)

    @staticmethod
    def remove_user_from_course(course_name, username):
        course = CoursesLayer.get_course_by_name(course_name)
        course["students"].remove(username)
        return CoursesLayer.update_course(course)

    @staticmethod
    def add_lecture_to_course(course_name: str, lecture: dict):
        course = CoursesLayer.get_course_by_name(course_name)
        course["plan"].append(dict(lecture))
        return CoursesLayer.update_course(course)

    @staticmethod
    def change_lecture_status(course_name: str, lecture_name: str,
                              lecture_status: str):
        course = CoursesLayer.get_course_by_name(course_name)
        for x in course["plan"]:
            if x["name"] == lecture_name:
                x["status"] = lecture_status
        return CoursesLayer.update_course(course)

    @staticmethod
    def user_presence(request: any):
        course = CoursesLayer.get_course_by_name(request["course_name"])
        for x in course["plan"]:
            if (x["name"] == request["lecture_name"]
                    and x["status"] == "started"):
                present: list = x["present"] if request[
                    "is_present"] is True else x["not_present"]
                not_present: list = x["not_present"] if request[
                    "is_present"] is True else x["present"]
                for x in present:
                    if x == request["username"]:
                        present.remove(x)
                present.append(request["username"])
                try:
                    not_present.remove(request["username"])
                except:
                    pass
                return CoursesLayer.update_course(course)
        return None
