from .generic_crud import AdminGenericCRUDView

from ..admin_services.messages import AdminMessagesService
from ..admin_serializers.messages import AdminMessagesSerializer


class AdminMessagesViews(AdminGenericCRUDView):
    service_class = AdminMessagesService
    serializer_class = AdminMessagesSerializer
