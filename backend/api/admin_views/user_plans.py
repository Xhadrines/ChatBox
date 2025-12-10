from .generic_crud import AdminGenericCRUDView

from ..admin_services.user_plans import AdminUserPlansService
from ..admin_serializers.user_plans import AdminUserPlansSerializer


class AdminUserPlansViews(AdminGenericCRUDView):
    service_class = AdminUserPlansService
    serializer_class = AdminUserPlansSerializer
