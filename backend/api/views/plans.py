from .generic_crud import GenericCRUDView

from ..data_access.plans import PlansAccessor
from ..data_access.plan_types import PlanTypesAccessor
from ..serializers.plans import PlansSerializer


class PlansViews(GenericCRUDView):
    accessor_class = PlansAccessor
    serializer_class = PlansSerializer

    fk_fields = {"type": PlanTypesAccessor}
