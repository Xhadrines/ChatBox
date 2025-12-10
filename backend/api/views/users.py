from .generic_crud import GenericCRUDView

from ..services.users import UsersService
from ..serializers.users import UsersSerializer


class UsersViews(GenericCRUDView):
    service_class = UsersService
    serializer_class = UsersSerializer

    password_field = "password"
