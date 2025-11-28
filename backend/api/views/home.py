from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["endpoints"] = [
            ("User Roles", "/api/user-roles/"),
            ("User Status", "/api/user-status/"),
            ("Users", "/api/users/"),
            ("Register", "/api/register/"),
            ("Login", "/api/login/"),
            ("Plan Types", "/api/plan-types/"),
            ("Plans", "/api/plans/"),
            ("User Plans", "/api/user-plans/"),
            ("Files", "/api/files/"),
            ("Messages", "/api/messages/"),
            ("User Usage", "/api/user-usage/"),
        ]

        return context
