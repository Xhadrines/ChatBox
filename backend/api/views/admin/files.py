from .generic_crud import AdminGenericCRUDView

from ...data_access.files import FilesAccessor
from ...data_access.users import UsersAccessor
from ...serializers.admin.files import AdminFilesSerializer


class AdminFilesViews(AdminGenericCRUDView):
    accessor_class = FilesAccessor
    serializer_class = AdminFilesSerializer

    fk_fields = {"user": UsersAccessor}
