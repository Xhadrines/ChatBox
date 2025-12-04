from .generic_crud import AdminGenericCRUDView

from ...data_access.user_token import UserTokenAccessor
from ...data_access.users import UsersAccessor
from ...serializers.admin.user_token import AdminUserTokenSerializer


class AdminUserTokenView(AdminGenericCRUDView):
    accessor_class = UserTokenAccessor
    serializer_class = AdminUserTokenSerializer

    lookup_method = "get_by_user"
    create_method = "create_or_get"
    delete_method = "delete"

    lookup_param_is_user = True
    user_accessor_class = UsersAccessor
