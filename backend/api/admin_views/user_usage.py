from .generic_crud import AdminGenericCRUDView

from ..admin_services.user_usage import AdminUserUsageService
from ..admin_serializers.user_usage import AdminUserUsageSerializer


class AdminUserUsageViews(AdminGenericCRUDView):
    service_class = AdminUserUsageService
    serializer_class = AdminUserUsageSerializer
