from .generic_crud import GenericCRUDView

from ..services.user_status import UserStatusService
from ..serializers.user_status import UserStatusSerializer


class UserStatusViews(GenericCRUDView):
    service_class = UserStatusService
    serializer_class = UserStatusSerializer
