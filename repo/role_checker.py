from repo import auth
from typing import List
from schemas.user import User
from fastapi import Depends
from utils.exceptions import UserExceptions


class RoleChecker:

    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(auth.get_current_user)):
        if user["role"] not in self.allowed_roles:
            return UserExceptions().raise_forbidden("Operation forbidden")
        return 200
