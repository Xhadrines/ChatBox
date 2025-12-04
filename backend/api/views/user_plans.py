from .generic_crud import GenericCRUDView

from ..data_access.user_plans import UserPlansAccessor
from ..data_access.users import UsersAccessor
from ..data_access.plans import PlansAccessor
from ..serializers.user_plans import UserPlansSerializer


class UserPlansViews(GenericCRUDView):
    accessor_class = UserPlansAccessor
    serializer_class = UserPlansSerializer

    fk_fields = {
        "user": UsersAccessor,
        "plan": PlansAccessor,
    }
