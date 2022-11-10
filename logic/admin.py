from schemas import user
from utils.constants import USER_ROLES
from utils.exceptions import UserExceptions
from repo.approve_actions import WriteApproval
from database.data_access.users import UsersLayer


class AdminLogic:

    @staticmethod
    def _instructor_from_user(user: dict):
        user["role"] = USER_ROLES["INSTRUCTOR"]
        UsersLayer.update_user("username", user)
        return f"{user.username} is now instructor"

    @staticmethod
    def _parse_user(username: str, is_active: bool, user_status: str):
        user = UsersLayer.get_user_by_username(username)
        user["is_active"] = is_active
        user["status"] = user_status
        approval = WriteApproval(user, user_status)
        approval.write_approval()
        return user

    @staticmethod
    def _update_parsed_user(user: dict):
        UsersLayer.update_user("username", user)
        return user["username"] + "is active: " + str(user["is_active"])

    def user_action(self, username: str, is_active: bool,
                    user_status: str) -> user.User:
        try:
            user = self._parse_user(username, is_active, user_status)
            return self._update_parsed_user(user)
        except:
            return UserExceptions.raise_conflict("Cannot apply action on user")

    def make_instructor(self, username: str) -> user.User:
        user = UsersLayer.get_user_by_username(username)
        return self._instructor_from_user(user)
