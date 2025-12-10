from django.contrib.auth.hashers import make_password

from ...data_access.users import UsersAccessor
from ...data_access.user_roles import UserRolesAccessor
from ...data_access.user_status import UserStatusAccessor
from ...data_access.user_plans import UserPlansAccessor
from ...data_access.plans import PlansAccessor
from ...serializers.users import UsersSerializer


class RegisterService:
    def __init__(self):
        self.accessor = UsersAccessor()
        self.role_accessor = UserRolesAccessor()
        self.status_accessor = UserStatusAccessor()
        self.user_plan_accessor = UserPlansAccessor()
        self.plan_accessor = PlansAccessor()
        self.serializer_class = UsersSerializer

    def register_user(self, data):
        if "password" not in data or not data["password"]:
            return None, "Password is required"

        data["password"] = make_password(data["password"])

        role_obj = next(
            (r for r in self.role_accessor.get_all() if r.name.lower() == "utilizator"),
            None,
        )
        if not role_obj:
            return None, "User role not found"
        data["role"] = role_obj

        status_obj = next(
            (s for s in self.status_accessor.get_all() if s.name.lower() == "activ"),
            None,
        )
        if not status_obj:
            return None, "User status not found"
        data["status"] = status_obj

        user = self.accessor.add(**data)

        free_plan = next(
            (p for p in self.plan_accessor.get_all() if p.name.lower() == "buddy"),
            None,
        )
        if free_plan:
            self.user_plan_accessor.add(user=user, plan=free_plan)

        user_data = self.serializer_class(user).data
        return user_data, None
