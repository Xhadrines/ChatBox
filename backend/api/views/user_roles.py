from .generic_crud import GenericCRUDView

from ..services.user_roles import UserRolesService
from ..serializers.user_roles import UserRolesSerializer


class UserRolesViews(GenericCRUDView):
    service_class = UserRolesService
    serializer_class = UserRolesSerializer
