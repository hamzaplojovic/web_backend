from pydantic import BaseModel

class CourseBase(BaseModel):
    name:str
    description:str
    plan:list
    instructors:list
    time:str
    appointment:str
    cover_image:str

class Course(CourseBase):
    class Config:
        orm_mode = True