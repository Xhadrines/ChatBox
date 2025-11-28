from .generic_crud import GenericCRUDView

from ..data_access.plan_types import PlanTypesAccessor

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class PlanTypesViews(GenericCRUDView):
    model_name = "PlanTypes"
    accessor_class = PlanTypesAccessor
    fk_fields = {}
    auto_fields = ["created_at", "updated_at"]
    list_url = "/api-mvc/plan-types/"
    create_url = "/api-mvc/plan-types/create"
    detail_url_prefix = "/api-mvc/plan-types"
    edit_url_prefix = "/api-mvc/plan-types"
    delete_url_prefix = "/api-mvc/plan-types"

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
