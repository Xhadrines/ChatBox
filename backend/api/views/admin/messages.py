from .generic_crud import AdminGenericCRUDView

from ...data_access.messages import MessagesAccessor
from ...data_access.users import UsersAccessor
from ...serializers.admin.messages import AdminMessagesSerializer


class AdminMessagesViews(AdminGenericCRUDView):
    accessor_class = MessagesAccessor
    serializer_class = AdminMessagesSerializer

    fk_fields = {"user": UsersAccessor}
