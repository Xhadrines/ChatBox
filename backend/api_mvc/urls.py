from django.urls import path

from .views.user_roles import UserRolesViews
from .views.user_status import UserStatusViews
from .views.users import UsersViews
from .views.plan_types import PlanTypesViews
from .views.plans import PlansViews
from .views.user_plans import UserPlansViews
from .views.files import FilesViews
from .views.messages import MessagesViews
from .views.user_usage import UserUsageViews
from .views.home import HomeView


urlpatterns = [
    path("user-roles/", UserRolesViews.as_view(), name="user-roles-list"),
    path("user-roles/create/", UserRolesViews.as_view(), name="user-roles-create"),
    path("user-roles/<int:pk>/", UserRolesViews.as_view(), name="user-roles-detail"),
    path("user-roles/<int:pk>/edit/", UserRolesViews.as_view(), name="user-roles-edit"),
    path(
        "user-roles/<int:pk>/delete/",
        UserRolesViews.as_view(),
        name="user-roles-delete",
    ),
    path("user-status/", UserStatusViews.as_view(), name="user-status-list"),
    path("user-status/create/", UserStatusViews.as_view(), name="user-status-create"),
    path("user-status/<int:pk>/", UserStatusViews.as_view(), name="user-status-detail"),
    path(
        "user-status/<int:pk>/edit/", UserStatusViews.as_view(), name="user-status-edit"
    ),
    path(
        "user-status/<int:pk>/delete/",
        UserStatusViews.as_view(),
        name="user-status-delete",
    ),
    path("users/", UsersViews.as_view(), name="users-list"),
    path("users/create/", UsersViews.as_view(), name="users-create"),
    path("users/<int:pk>/", UsersViews.as_view(), name="users-detail"),
    path("users/<int:pk>/edit/", UsersViews.as_view(), name="users-edit"),
    path("users/<int:pk>/delete/", UsersViews.as_view(), name="users-delete"),
    path("plan-types/", PlanTypesViews.as_view(), name="plan-types-list"),
    path("plan-types/create/", PlanTypesViews.as_view(), name="plan-types-create"),
    path("plan-types/<int:pk>/", PlanTypesViews.as_view(), name="plan-types-detail"),
    path("plan-types/<int:pk>/edit/", PlanTypesViews.as_view(), name="plan-types-edit"),
    path(
        "plan-types/<int:pk>/delete/",
        PlanTypesViews.as_view(),
        name="plan-types-delete",
    ),
    path("plans/", PlansViews.as_view(), name="plans-list"),
    path("plans/create/", PlansViews.as_view(), name="plans-create"),
    path("plans/<int:pk>/", PlansViews.as_view(), name="plans-detail"),
    path("plans/<int:pk>/edit/", PlansViews.as_view(), name="plans-edit"),
    path("plans/<int:pk>/delete/", PlansViews.as_view(), name="plans-delete"),
    path("user-plans/", UserPlansViews.as_view(), name="user-plans-list"),
    path("user-plans/create/", UserPlansViews.as_view(), name="user-plans-create"),
    path("user-plans/<int:pk>/", UserPlansViews.as_view(), name="user-plans-detail"),
    path("user-plans/<int:pk>/edit/", UserPlansViews.as_view(), name="user-plans-edit"),
    path(
        "user-plans/<int:pk>/delete/",
        UserPlansViews.as_view(),
        name="user-plans-delete",
    ),
    path("files/", FilesViews.as_view(), name="files-list"),
    path("files/create/", FilesViews.as_view(), name="files-create"),
    path("files/<int:pk>/", FilesViews.as_view(), name="files-detail"),
    path("files/<int:pk>/edit/", FilesViews.as_view(), name="files-edit"),
    path("files/<int:pk>/delete/", FilesViews.as_view(), name="files-delete"),
    path("messages/", MessagesViews.as_view(), name="messages-list"),
    path("messages/create/", MessagesViews.as_view(), name="messages-create"),
    path("messages/<int:pk>/", MessagesViews.as_view(), name="messages-detail"),
    path("messages/<int:pk>/edit/", MessagesViews.as_view(), name="messages-edit"),
    path("messages/<int:pk>/delete/", MessagesViews.as_view(), name="messages-delete"),
    path("user-usage/", UserUsageViews.as_view(), name="user-usage-list"),
    path("user-usage/create/", UserUsageViews.as_view(), name="user-usage-create"),
    path("user-usage/<int:pk>/", UserUsageViews.as_view(), name="user-usage-detail"),
    path("user-usage/<int:pk>/edit/", UserUsageViews.as_view(), name="user-usage-edit"),
    path(
        "user-usage/<int:pk>/delete/",
        UserUsageViews.as_view(),
        name="user-usage-delete",
    ),
    path("", HomeView.as_view(), name="home"),
]
