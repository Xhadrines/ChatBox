from .generic_crud import AdminGenericCRUDView

from ..admin_services.user_token import AdminUserTokenService
from ..admin_serializers.user_token import AdminUserTokenSerializer


class AdminUserTokenView(AdminGenericCRUDView):
    service_class = AdminUserTokenService
    serializer_class = AdminUserTokenSerializer
