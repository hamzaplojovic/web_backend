from db import db
from schemas import user
from datetime import datetime
from utils.constants import USER_STATUS

db = db.connect_to_db("users")

class WriteApproval:
    def __init__(self, user:user.User, status):
        self.user = user
        self.status = status

    def _approve_approval(self) -> int:
        self.user["approved_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.user["rejected_at"] = ""
        self.user["rejected_counter"] = 0
        return 200

    def _ban(self) -> int:
        self.user["status"] = USER_STATUS["BANNED"]
        self.user["approved_at"] = ""
        self.user["rejected_at"] = ""
        return 200

    def _reject_approval(self) -> int:
        if self.user["rejected_counter"] < 3:
            self.user["rejected_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            self.user["approved_at"] = ""
            self.user["rejected_counter"] += 1
            return 200
        else:
            return self._ban()

    def write_approval(self) -> int:
        if self.status == "approved":
            return self._approve_approval()
        return self._reject_approval()

