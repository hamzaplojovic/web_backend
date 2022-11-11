from schemas.course import Course
from database.data_access.courses import CoursesLayer

data_layer = CoursesLayer()


class CoursesLogic:

    @staticmethod
    def _parse_course(course: Course):
        course = dict(course)
        course["_id"] = course["name"]
        return course

    @staticmethod
    def get_all_courses() -> list[dict]:
        return data_layer.get_all_courses()

    @staticmethod
    def get_course_by_name(course_name: str):
        return data_layer.get_course_by_name(course_name)

    def create_course(self, course: Course):
        course = self._parse_course(course)
        return data_layer.create_course(course)

    @staticmethod
    def update_course(course: Course):
        return data_layer.update_course(dict(course))

    @staticmethod
    def delete_course(course_name: str):
        return data_layer.delete_course(course_name)

    @staticmethod
    def hard_delete_course(course_name):
        return data_layer.hard_delete_course(course_name)

    @staticmethod
    def get_students_from_course(course_name):
        return data_layer.get_course_by_name(course_name)["students"]

    @staticmethod
    def assign_user_to_course(course_name, username):
        course = data_layer.get_course_by_name(course_name)
        course["students"].append(username)
        return data_layer.update_course(course)

    @staticmethod
    def remove_user_from_course(course_name, username):
        course = data_layer.get_course_by_name(course_name)
        course["students"].remove(username)
        return data_layer.update_course(course)

    @staticmethod
    def add_lecture_to_course(course_name: str, lecture: dict):
        course = data_layer.get_course_by_name(course_name)
        course["plan"].append(dict(lecture))
        return data_layer.update_course(course)

    @staticmethod
    def change_lecture_status(course_name: str, lecture_name: str,
                              lecture_status: str):
        course = data_layer.get_course_by_name(course_name)
        for x in course["plan"]:
            if x["name"] == lecture_name:
                x["status"] = lecture_status
        return data_layer.update_course(course)

    @staticmethod
    def user_presence(request: any):
        course = data_layer.get_course_by_name(request["course_name"])
        for x in course["plan"]:
            if (x["name"] == request["lecture_name"]
                    and x["status"] == "started"):
                present: list = x["present"] if request[
                    "is_present"] is True else x["not_present"]
                not_present: list = x["not_present"] if request[
                    "is_present"] is True else x["present"]
                present.append(request["username"])
                try:
                    not_present.remove(request["username"])
                except (SyntaxError, RuntimeError, ValueError, TypeError):
                    pass
                return data_layer.update_course(course)
        return None
