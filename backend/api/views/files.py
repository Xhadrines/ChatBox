from .generic_crud import GenericCRUDView

from ..data_access.files import FilesAccessor
from ..data_access.users import UsersAccessor
from ..serializers.files import FilesSerializer


class FilesViews(GenericCRUDView):
    accessor_class = FilesAccessor
    serializer_class = FilesSerializer

    fk_fields = {"user": UsersAccessor}
