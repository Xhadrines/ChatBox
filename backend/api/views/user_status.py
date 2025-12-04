from .generic_crud import GenericCRUDView

from ..data_access.user_status import UserStatusAccessor
from ..serializers.user_status import UserStatusSerializer


class UserStatusViews(GenericCRUDView):
    accessor_class = UserStatusAccessor
    serializer_class = UserStatusSerializer
