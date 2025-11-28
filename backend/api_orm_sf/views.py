from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .data_access.user_roles import UserRolesAccessor
from .data_access.user_status import UserStatusAccessor
from .data_access.users import UsersAccessor
from .data_access.plan_types import PlanTypesAccessor
from .data_access.plans import PlansAccessor
from .data_access.user_plans import UserPlansAccessor
from .data_access.files import FilesAccessor
from .data_access.messages import MessagesAccessor
from .data_access.user_usage import UserUsageAccessor


class GenericListView(View):
    accessor_class = None
    fields = []

    def get(self, request):
        accessor = self.accessor_class()
        items = accessor.get_all()
        data = []
        for item in items:
            record = {}
            for field in self.fields:
                value = getattr(item, field)
                if hasattr(value, "isoformat"):
                    value = value.isoformat()
                elif hasattr(value, "id"):
                    value = value.id
                record[field] = value
            data.append(record)
        return JsonResponse(data, safe=False)


class UserRolesListView(GenericListView):
    accessor_class = UserRolesAccessor
    fields = ["id", "name", "description", "created_at", "updated_at"]


class UserStatusListView(GenericListView):
    accessor_class = UserStatusAccessor
    fields = ["id", "name", "description", "created_at", "updated_at"]


class UsersListView(GenericListView):
    accessor_class = UsersAccessor
    fields = [
        "id",
        "username",
        "email",
        "role",
        "status",
        "last_login",
        "created_at",
        "updated_at",
    ]


class PlanTypesListView(GenericListView):
    accessor_class = PlanTypesAccessor
    fields = ["id", "name", "description", "created_at", "updated_at"]


class PlansListView(GenericListView):
    accessor_class = PlansAccessor
    fields = [
        "id",
        "name",
        "price",
        "type",
        "duration_days",
        "name_llm_prm",
        "daily_prm_msg",
        "name_llm_std",
        "daily_std_msg",
        "daily_file_limit",
        "created_at",
        "updated_at",
    ]


class UserPlansListView(GenericListView):
    accessor_class = UserPlansAccessor
    fields = ["id", "user", "plan", "start_date", "end_date"]


class FilesListView(GenericListView):
    accessor_class = FilesAccessor
    fields = ["id", "user", "file_name", "file_path", "uploaded_at"]


class MessagesListView(GenericListView):
    accessor_class = MessagesAccessor
    fields = ["id", "user", "user_msg", "llm_resp", "llm_used", "uploaded_at"]


class UserUsageListView(GenericListView):
    accessor_class = UserUsageAccessor
    fields = ["id", "user", "date", "messages_sent", "files_uploaded"]


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["endpoints"] = [
            ("User Roles", "/api-orm/sf/user-roles/"),
            ("User Status", "/api-orm/sf/user-status/"),
            ("Users", "/api-orm/sf/users/"),
            ("Plan Types", "/api-orm/sf/plan-types/"),
            ("Plans", "/api-orm/sf/plans/"),
            ("User Plans", "/api-orm/sf/user-plans/"),
            ("Files", "/api-orm/sf/files/"),
            ("Messages", "/api-orm/sf/messages/"),
            ("User Usage", "/api-orm/sf/user-usage/"),
        ]

        return context
