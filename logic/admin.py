from schemas.user import User
from utils.constants import USER_ROLES
from utils.exceptions import UserExceptions
from repo.approve_actions import WriteApproval
from database.data_access.users import UsersLayer

data_layer = UsersLayer()


class AdminLogic:

    @staticmethod
    def _instructor_from_user(user: dict):
        user["role"] = USER_ROLES["INSTRUCTOR"]
        data_layer.update_user("username", user)
        return f"{user.username} is now instructor"

    @staticmethod
    def _parse_user(username: str, is_active: bool, user_status: str):
        user = data_layer.get_user_by_username(username)
        user["is_active"] = is_active
        user["status"] = user_status
        approval = WriteApproval(user, user_status)
        approval.write_approval()
        return user

    @staticmethod
    def _update_parsed_user(user: dict):
        data_layer.update_user("username", user)
        return user["username"] + "is active: " + str(user["is_active"])

    def user_action(self, username: str, is_active: bool,
                    user_status: str) -> User:
        try:
            user = self._parse_user(username, is_active, user_status)
            return self._update_parsed_user(user)
        except (RuntimeError, ValueError, TypeError, NameError):
            return UserExceptions.raise_conflict("Cannot apply action on user")

    def make_instructor(self, username: str) -> User:
        user = data_layer.get_user_by_username(username)
        return self._instructor_from_user(user)
