from db import deta_db
from datetime import datetime
from schemas import user

db = deta_db.connect_to_deta_db("users")

def _write_approval(user:user.User, field1, field2):
    user["approved_at"] = datetime.now().strftime("%H:%M:%S")
    # user[field2] = None
    # return 200
    return user

def write_approval(user:user.User, status):
    if status == "approved":
        return _write_approval(user,"approved_at", "rejected_at")
    return _write_approval(user,"rejected_at", "approved_at")