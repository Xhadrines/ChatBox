from .generic_crud import AdminGenericCRUDView

from ..admin_services.files import AdminFilesService
from ..admin_serializers.files import AdminFilesSerializer


class AdminFilesViews(AdminGenericCRUDView):
    service_class = AdminFilesService
    serializer_class = AdminFilesSerializer
