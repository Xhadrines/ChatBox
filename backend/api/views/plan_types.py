from .generic_crud import GenericCRUDView

from ..data_access.plan_types import PlanTypesAccessor
from ..serializers.plan_types import PlanTypesSerializer


class PlanTypesViews(GenericCRUDView):
    accessor_class = PlanTypesAccessor
    serializer_class = PlanTypesSerializer
