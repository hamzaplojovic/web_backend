from hashlib import sha256
from schemas import user
from utils import github
from deta import Base
from validation import user_creation
from fastapi import status,HTTPException

db = Base("users")


def get_all():
    return db.fetch().items


def create_user(user: user.User):
    if user_creation.validate_user_data(dict(user)) == 200:
        user.avatar = github.get_github_avatar_url(user.github)
        user.languages = github.get_github_language_percentages(user.github)
        user.password = sha256(user.password.encode("utf-8")).hexdigest()
        user.is_active = False
        user.status = "on hold"

        return db.put(dict(user), key=user.email)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Requirements not met!")


def find_user_by_username(username):
    user = db.get(username)
    return user or 404

def change_user(request):
    return db.put(dict(request), key=request.username)


def delete_user(username):
    return db.delete(username)
