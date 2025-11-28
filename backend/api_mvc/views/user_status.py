from .generic_crud import GenericCRUDView

from ..data_access.user_status import UserStatusAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class UserStatusViews(GenericCRUDView):
    model_name = "UserStatus"
    accessor_class = UserStatusAccessor
    fk_fields = {}
    auto_fields = ["created_at", "updated_at"]
    list_url = "/api-mvc/user-status/"
    create_url = "/api-mvc/user-status/create"
    detail_url_prefix = "/api-mvc/user-status"
    edit_url_prefix = "/api-mvc/user-status"
    delete_url_prefix = "/api-mvc/user-status"

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
