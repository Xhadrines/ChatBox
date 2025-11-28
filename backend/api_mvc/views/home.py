from django.views.generic import TemplateView

from django.utils.decorators import method_decorator
from backend.decorators import admin_required


@method_decorator(admin_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["endpoints"] = [
            ("User Roles", "/api-mvc/user-roles/"),
            ("User Status", "/api-mvc/user-status/"),
            ("Users", "/api-mvc/users/"),
            ("Plan Types", "/api-mvc/plan-types/"),
            ("Plans", "/api-mvc/plans/"),
            ("User Plans", "/api-mvc/user-plans/"),
            ("Files", "/api-mvc/files/"),
            ("Messages", "/api-mvc/messages/"),
            ("User Usage", "/api-mvc/user-usage/"),
        ]

        return context
