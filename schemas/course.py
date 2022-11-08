from pydantic import BaseModel

class Course(BaseModel):
    name:str
    description:str
    duration:str
    plan:list
    instructors:list
    students:list
    time:str
    appointment:str
    cover_image:str

class Lecture(BaseModel):
    name:str
    description:str
    present:list
    not_present:list