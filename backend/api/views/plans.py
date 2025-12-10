from .generic_crud import GenericCRUDView

from ..services.plans import PlansService
from ..serializers.plans import PlansSerializer


class PlansViews(GenericCRUDView):
    service_class = PlansService
    serializer_class = PlansSerializer
