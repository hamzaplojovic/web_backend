from typing import List
from fastapi import HTTPException

class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, role:str):
        if role not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")