from .generic_crud import GenericCRUDView

from ..data_access.users import UsersAccessor
from ..data_access.user_roles import UserRolesAccessor
from ..data_access.user_status import UserStatusAccessor
from ..serializers.users import UsersSerializer


class UsersViews(GenericCRUDView):
    accessor_class = UsersAccessor
    serializer_class = UsersSerializer

    fk_fields = {
        "role": UserRolesAccessor,
        "status": UserStatusAccessor,
    }

    password_field = "password"
