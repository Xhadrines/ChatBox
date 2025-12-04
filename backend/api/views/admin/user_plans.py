from .generic_crud import AdminGenericCRUDView

from ...data_access.user_plans import UserPlansAccessor
from ...data_access.users import UsersAccessor
from ...data_access.plans import PlansAccessor
from ...serializers.admin.user_plans import AdminUserPlansSerializer


class AdminUserPlansViews(AdminGenericCRUDView):
    accessor_class = UserPlansAccessor
    serializer_class = AdminUserPlansSerializer

    fk_fields = {
        "user": UsersAccessor,
        "plan": PlansAccessor,
    }
