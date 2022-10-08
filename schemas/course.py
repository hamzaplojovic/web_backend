from pydantic import BaseModel

class CourseBase(BaseModel):
    name:str
    desc:str
    date:str

class Course(CourseBase):
    class Config:
        orm_mode = True