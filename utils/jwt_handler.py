from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from datetime import datetime, timedelta
from pydantic import BaseModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class TokenData(BaseModel):
    username: str | None = None

ACCESS_TOKEN_EXPIRE_MINUTES = 30 
ALGORITHM = "HS256"
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current(request):
    payload = jwt.decode(request.headers['authorization'].
                         split(' ')[1], SECRET_KEY, algorithms=[ALGORITHM])
    return dict(payload)["username"]