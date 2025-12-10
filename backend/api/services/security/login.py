from django.contrib.auth.hashers import check_password
from django.utils import timezone

from ...data_access.users import UsersAccessor
from ...data_access.user_token import UserTokenAccessor
from ...data_access.user_plans import UserPlansAccessor
from ...data_access.user_status import UserStatusAccessor
from ...serializers.users import UsersSerializer


class LoginService:
    def __init__(self):
        self.users_accessor = UsersAccessor()
        self.token_accessor = UserTokenAccessor()
        self.user_plans_accessor = UserPlansAccessor()
        self.user_status_accessor = UserStatusAccessor()
        self.serializer_class = UsersSerializer

    def login(self, email, password):
        if not email or not password:
            return None, "Email and password required", 400

        user = self.users_accessor.get_by_email(email)
        if not user or not check_password(password, user.password):
            return None, "Invalid credentials", 401

        status_obj = self.user_status_accessor.get_by_id(user.status_id)
        if status_obj and status_obj.name.lower() == "sters":
            return None, "This account has been deleted", 403

        user.last_login = timezone.now()
        self.users_accessor.update(user.id, last_login=user.last_login)

        self.user_plans_accessor.expire_plans()

        token_obj = self.token_accessor.create_or_get(user)
        user_data = self.serializer_class(user).data

        return {"user": user_data, "token": token_obj.key}, None, 200
