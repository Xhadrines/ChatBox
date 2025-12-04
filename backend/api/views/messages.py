from .generic_crud import GenericCRUDView

from ..data_access.messages import MessagesAccessor
from ..data_access.users import UsersAccessor
from ..serializers.messages import MessagesSerializer


class MessagesViews(GenericCRUDView):
    accessor_class = MessagesAccessor
    serializer_class = MessagesSerializer

    fk_fields = {"user": UsersAccessor}
