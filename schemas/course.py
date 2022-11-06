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
