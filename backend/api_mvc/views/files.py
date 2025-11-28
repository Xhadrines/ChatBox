from .generic_crud import GenericCRUDView

from ..data_access.files import FilesAccessor
from ..data_access.users import UsersAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class FilesViews(GenericCRUDView):
    model_name = "Files"
    accessor_class = FilesAccessor
    fk_fields = {"user": UsersAccessor}
    auto_fields = ["uploaded_at"]
    list_url = "/api-mvc/files/"
    create_url = "/api-mvc/files/create"
    detail_url_prefix = "/api-mvc/files"
    edit_url_prefix = "/api-mvc/files"
    delete_url_prefix = "/api-mvc/files"

    def get(self, request, pk=None):
        if pk and "edit" in request.path:
            return self.edit(request, pk)
        elif pk and "delete" in request.path:
            return self.delete(request, pk)
        elif pk:
            return self.detail(request, pk)
        elif "create" in request.path:
            return self.create(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        if pk and "edit" in request.path:
            return self.edit(request, pk)
        elif pk and "delete" in request.path:
            return self.delete(request, pk)
        elif "create" in request.path:
            return self.create(request)
        else:
            return self.list(request)
