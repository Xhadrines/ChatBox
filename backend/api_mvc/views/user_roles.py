from .generic_crud import GenericCRUDView

from ..data_access.user_roles import UserRolesAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class UserRolesViews(GenericCRUDView):
    model_name = "UserRoles"
    accessor_class = UserRolesAccessor
    fk_fields = {}
    auto_fields = ["created_at", "updated_at"]
    list_url = "/api-mvc/user-roles/"
    create_url = "/api-mvc/user-roles/create"
    detail_url_prefix = "/api-mvc/user-roles"
    edit_url_prefix = "/api-mvc/user-roles"
    delete_url_prefix = "/api-mvc/user-roles"

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
