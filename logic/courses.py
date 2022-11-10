from schemas import course
from database.data_access.courses import CoursesLayer

class CoursesLogic:
    def _parse_course(self, course: course.Course):
        course = dict(course)
        course["_id"] = course["name"]
        return course
    
    def get_all_courses(self) -> list[dict]:
        return CoursesLayer.get_all_courses()
    
    def get_course_by_name(self, course_name:str):
        return CoursesLayer.get_course_by_name(course_name)

    def create_course(self, course:course.Course):
        course = self._parse_course(course)
        return CoursesLayer.create_course(course)
    
    def update_course(self, course:course.Course):
        return CoursesLayer.update_course(dict(course))
    
    def delete_course(self, course_name:str):
        return CoursesLayer.delete_course(course_name)
    
    def hard_delete_course(self, course_name):
        return CoursesLayer.hard_delete_course(course_name)
    
    def get_students_from_course(self, course_name):
        return CoursesLayer.get_course_by_name(course_name)["students"]

    def assign_user_to_course(self, course_name, username):
        course = CoursesLayer.get_course_by_name(course_name)
        course["students"].append(username)
        return CoursesLayer.update_course(course)
    
    def remove_user_from_course(self, course_name, username):
        course = CoursesLayer.get_course_by_name(course_name)
        course["students"].remove(username)
        return CoursesLayer.update_course(course)

    def add_lecture_to_course(self, course_name:str, lecture:dict):
        course = CoursesLayer.get_course_by_name(course_name)
        course["plan"].append(dict(lecture))
        return CoursesLayer.update_course(course)
    
    def change_lecture_status(self, course_name: str, lecture_name:str, lecture_status:str):
        course = CoursesLayer.get_course_by_name(course_name)
        for x in course["plan"]:
            if x["name"] == lecture_name:
                x["status"] = lecture_status
        return CoursesLayer.update_course(course)
    
    def user_presence(self, request:any):
        course = CoursesLayer.get_course_by_name(request["course_name"])
        for x in course["plan"]:
            if x["name"] == request["lecture_name"]:
                if x["status"] == "started":
                    present:list = x["present"] if request["is_present"] == True else x["not_present"]
                    not_present:list = x["not_present"] if request["is_present"] == True else x["present"]
                    [present.remove(x) for x in present if x == request["username"]]
                    present.append(request["username"])
                    try:
                        not_present.remove(request["username"])
                    except:
                        pass
                    return CoursesLayer.update_course(course)
        return None