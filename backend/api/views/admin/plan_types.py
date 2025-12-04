from .generic_crud import AdminGenericCRUDView

from ...data_access.plan_types import PlanTypesAccessor
from ...serializers.admin.plan_types import AdminPlanTypesSerializer


class AdminPlanTypesViews(AdminGenericCRUDView):
    accessor_class = PlanTypesAccessor
    serializer_class = AdminPlanTypesSerializer
