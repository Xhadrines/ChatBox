from .generic_crud import AdminGenericCRUDView

from ...data_access.user_roles import UserRolesAccessor
from ...serializers.admin.user_roles import AdminUserRolesSerializer


class AdminUserRolesViews(AdminGenericCRUDView):
    accessor_class = UserRolesAccessor
    serializer_class = AdminUserRolesSerializer
