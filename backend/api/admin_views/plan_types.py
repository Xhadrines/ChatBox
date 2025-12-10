from .generic_crud import AdminGenericCRUDView

from ..admin_services.plan_types import AdminPlanTypesService
from ..admin_serializers.plan_types import AdminPlanTypesSerializer


class AdminPlanTypesViews(AdminGenericCRUDView):
    service_class = AdminPlanTypesService
    serializer_class = AdminPlanTypesSerializer
