from .generic_crud import AdminGenericCRUDView

from ..admin_services.plans import AdminPlansService
from ..admin_serializers.plans import AdminPlansSerializer


class AdminPlansViews(AdminGenericCRUDView):
    service_class = AdminPlansService
    serializer_class = AdminPlansSerializer
