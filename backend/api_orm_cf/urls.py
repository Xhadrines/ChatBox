from django.urls import path

from .views import (
    UserRolesListView,
    UserStatusListView,
    UsersListView,
    PlanTypesListView,
    PlansListView,
    UserPlansListView,
    FilesListView,
    MessagesListView,
    UserUsageListView,
    HomeView,
)

urlpatterns = [
    path("user-roles/", UserRolesListView.as_view(), name="user_roles_list"),
    path("user-status/", UserStatusListView.as_view(), name="user_status_list"),
    path("users/", UsersListView.as_view(), name="users_list"),
    path("plan-types/", PlanTypesListView.as_view(), name="plan_types_list"),
    path("plans/", PlansListView.as_view(), name="plans_list"),
    path("user-plans/", UserPlansListView.as_view(), name="user_plans_list"),
    path("files/", FilesListView.as_view(), name="files_list"),
    path("messages/", MessagesListView.as_view(), name="messages_list"),
    path("user-usage/", UserUsageListView.as_view(), name="user_usage_list"),
    path("", HomeView.as_view(), name="home"),
]
