from .generic_crud import AdminGenericCRUDView

from ...data_access.user_status import UserStatusAccessor
from ...serializers.admin.user_status import AdminUserStatusSerializer


class AdminUserStatusViews(AdminGenericCRUDView):
    accessor_class = UserStatusAccessor
    serializer_class = AdminUserStatusSerializer
