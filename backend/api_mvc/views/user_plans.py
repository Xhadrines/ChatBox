from .generic_crud import GenericCRUDView

from ..data_access.users import UsersAccessor
from ..data_access.user_plans import UserPlansAccessor
from ..data_access.plans import PlansAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class UserPlansViews(GenericCRUDView):
    model_name = "UserPlans"
    accessor_class = UserPlansAccessor
    fk_fields = {"user": UsersAccessor, "plan": PlansAccessor}
    auto_fields = ["start_date", "end_date"]
    list_url = "/api-mvc/user-plans/"
    create_url = "/api-mvc/user-plans/create"
    detail_url_prefix = "/api-mvc/user-plans"
    edit_url_prefix = "/api-mvc/user-plans"
    delete_url_prefix = "/api-mvc/user-plans"

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
