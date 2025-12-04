from .generic_crud import GenericCRUDView

from ..data_access.user_roles import UserRolesAccessor
from ..serializers.user_roles import UserRolesSerializer


class UserRolesViews(GenericCRUDView):
    accessor_class = UserRolesAccessor
    serializer_class = UserRolesSerializer
