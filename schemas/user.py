from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    full_name: str
    github: str
    email: str
    age: str
    job: str
    role: str
    status:str
    is_active: str



class User(UserBase):
    avatar: Optional[str] = None
    languages: Optional[list] = None

    class Config:
        orm_mode = True
