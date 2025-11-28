from .generic_crud import GenericCRUDView

from ..data_access.messages import MessagesAccessor
from ..data_access.users import UsersAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class MessagesViews(GenericCRUDView):
    model_name = "Messages"
    accessor_class = MessagesAccessor
    fk_fields = {"user": UsersAccessor}
    auto_fields = ["uploaded_at"]
    list_url = "/api-mvc/messages/"
    create_url = "/api-mvc/messages/create"
    detail_url_prefix = "/api-mvc/messages"
    edit_url_prefix = "/api-mvc/messages"
    delete_url_prefix = "/api-mvc/messages"

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
