from .generic_crud import AdminGenericCRUDView

from ..admin_services.users import AdminUsersService
from ..admin_serializers.users import AdminUsersSerializer


class AdminUsersViews(AdminGenericCRUDView):
    service_class = AdminUsersService
    serializer_class = AdminUsersSerializer

    password_field = "password"
