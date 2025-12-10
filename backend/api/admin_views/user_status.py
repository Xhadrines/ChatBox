from .generic_crud import AdminGenericCRUDView

from ..admin_services.user_status import AdminUserStatusService
from ..admin_serializers.user_status import AdminUserStatusSerializer


class AdminUserStatusViews(AdminGenericCRUDView):
    service_class = AdminUserStatusService
    serializer_class = AdminUserStatusSerializer
