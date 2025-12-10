from .generic_crud import GenericCRUDView

from ..services.messages import MessagesService
from ..serializers.messages import MessagesSerializer


class MessagesViews(GenericCRUDView):
    service_class = MessagesService
    serializer_class = MessagesSerializer
