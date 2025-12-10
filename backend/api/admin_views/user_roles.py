from .generic_crud import AdminGenericCRUDView

from ..admin_services.user_roles import AdminUserRolesService
from ..admin_serializers.user_roles import AdminUserRolesSerializer


class AdminUserRolesViews(AdminGenericCRUDView):
    service_class = AdminUserRolesService
    serializer_class = AdminUserRolesSerializer
