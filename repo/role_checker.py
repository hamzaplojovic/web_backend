from repo import auth
from schemas import user
from typing import List
from fastapi import HTTPException,Depends

class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: user.User = Depends(auth.get_current_user)):
        if user["role"] not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return 200
    