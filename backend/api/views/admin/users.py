from .generic_crud import AdminGenericCRUDView

from ...data_access.users import UsersAccessor
from ...data_access.user_roles import UserRolesAccessor
from ...data_access.user_status import UserStatusAccessor
from ...serializers.admin.users import AdminUsersSerializer


class AdminUsersViews(AdminGenericCRUDView):
    accessor_class = UsersAccessor
    serializer_class = AdminUsersSerializer

    fk_fields = {
        "role": UserRolesAccessor,
        "status": UserStatusAccessor,
    }

    password_field = "password"
