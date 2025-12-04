from .generic_crud import AdminGenericCRUDView

from ...data_access.user_usage import UserUsageAccessor
from ...data_access.users import UsersAccessor
from ...serializers.admin.user_usage import AdminUserUsageSerializer


class AdminUserUsageViews(AdminGenericCRUDView):
    accessor_class = UserUsageAccessor
    serializer_class = AdminUserUsageSerializer

    fk_fields = {"user": UsersAccessor}
