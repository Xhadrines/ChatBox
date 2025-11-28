from .generic_crud import GenericCRUDView

from ..data_access.plans import PlansAccessor
from ..data_access.plan_types import PlanTypesAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class PlansViews(GenericCRUDView):
    model_name = "Plans"
    accessor_class = PlansAccessor
    fk_fields = {"type": PlanTypesAccessor}
    auto_fields = ["created_at", "updated_at"]
    list_url = "/api-mvc/plans/"
    create_url = "/api-mvc/plans/create"
    detail_url_prefix = "/api-mvc/plans"
    edit_url_prefix = "/api-mvc/plans"
    delete_url_prefix = "/api-mvc/plans"

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
