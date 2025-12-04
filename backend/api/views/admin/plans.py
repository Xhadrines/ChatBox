from .generic_crud import AdminGenericCRUDView

from ...data_access.plans import PlansAccessor
from ...data_access.plan_types import PlanTypesAccessor
from ...serializers.admin.plans import AdminPlansSerializer


class AdminPlansViews(AdminGenericCRUDView):
    accessor_class = PlansAccessor
    serializer_class = AdminPlansSerializer

    fk_fields = {"type": PlanTypesAccessor}
