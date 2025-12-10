from .generic_crud import GenericCRUDView

from ..services.plan_types import PlanTypesService
from ..serializers.plan_types import PlanTypesSerializer


class PlanTypesViews(GenericCRUDView):
    service_class = PlanTypesService
    serializer_class = PlanTypesSerializer
