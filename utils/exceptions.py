from fastapi import HTTPException, status

class UserExceptions:
    def __init__(self):
        self.name = "user exceptions"

    def raise_not_found(self, message):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=message)
    
    def raise_conflict(self, message):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=message)
    
    def raise_forbidden(self, message):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=message)