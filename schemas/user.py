from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    full_name: str
    github: str
    email: str
    age: str
    status: str
    is_active: str
    role: str


class User(UserBase):
    avatar: Optional[str] = None
    languages: Optional[list] = None
    flag: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None

    class Config:
        orm_mode = True
