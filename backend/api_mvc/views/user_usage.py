from .generic_crud import GenericCRUDView

from ..data_access.users import UsersAccessor
from ..data_access.user_usage import UserUsageAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class UserUsageViews(GenericCRUDView):
    model_name = "UserUsage"
    accessor_class = UserUsageAccessor
    fk_fields = {"user": UsersAccessor}
    auto_fields = ["date"]
    list_url = "/api-mvc/user-usage/"
    create_url = "/api-mvc/user-usage/create"
    detail_url_prefix = "/api-mvc/user-usage"
    edit_url_prefix = "/api-mvc/user-usage"
    delete_url_prefix = "/api-mvc/user-usage"

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
