from .generic_crud import GenericCRUDView

from ..data_access.users import UsersAccessor
from ..data_access.user_roles import UserRolesAccessor
from ..data_access.user_status import UserStatusAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class UsersViews(GenericCRUDView):
    model_name = "Users"
    accessor_class = UsersAccessor
    fk_fields = {"role": UserRolesAccessor, "status": UserStatusAccessor}
    auto_fields = ["created_at", "updated_at", "last_login"]
    password_field = "password"
    list_url = "/api-mvc/users/"
    create_url = "/api-mvc/users/create"
    detail_url_prefix = "/api-mvc/users"
    edit_url_prefix = "/api-mvc/users"
    delete_url_prefix = "/api-mvc/users"

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
