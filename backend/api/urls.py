from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.user_roles import UserRolesViews
from .views.user_status import UserStatusViews
from .views.users import UsersViews
from .views.messages import MessagesViews
from .views.files import FilesViews, FilesUploadView, ReadTxtFileView
from .views.user_usage import UserUsageViews, UserUsageByUserView, LogUserActivityView
from .views.plan_types import PlanTypesViews
from .views.plans import PlansViews
from .views.user_plans import UserPlansViews, ChangeUserPlanView, UserActivePlanView

from .views.home import HomeView

from .admin_views.user_roles import AdminUserRolesViews
from .admin_views.user_status import AdminUserStatusViews
from .admin_views.users import AdminUsersViews
from .admin_views.messages import AdminMessagesViews
from .admin_views.files import AdminFilesViews
from .admin_views.user_usage import AdminUserUsageViews
from .admin_views.plan_types import AdminPlanTypesViews
from .admin_views.plans import AdminPlansViews
from .admin_views.user_plans import AdminUserPlansViews
from .admin_views.user_token import AdminUserTokenView

from .views.security.register import RegisterView
from .views.security.login import LoginView

from .views.chat.chat import ChatEventsView, ChatView

urlpatterns = [
    path("user-roles/", UserRolesViews.as_view()),
    path("user-roles/<int:pk>/", UserRolesViews.as_view()),
    path("admin/user-roles/", AdminUserRolesViews.as_view()),
    path("admin/user-roles/<int:pk>/", AdminUserRolesViews.as_view()),
    path("user-status/", UserStatusViews.as_view()),
    path("user-status/<int:pk>/", UserStatusViews.as_view()),
    path("admin/user-status/", AdminUserStatusViews.as_view()),
    path("admin/user-status/<int:pk>/", AdminUserStatusViews.as_view()),
    path("users/", UsersViews.as_view()),
    path("users/<int:pk>/", UsersViews.as_view()),
    path("admin/users/", AdminUsersViews.as_view()),
    path("admin/users/<int:pk>/", AdminUsersViews.as_view()),
    path("messages/", MessagesViews.as_view()),
    path("messages/<int:pk>/", MessagesViews.as_view()),
    path("admin/messages/", AdminMessagesViews.as_view()),
    path("admin/messages/<int:pk>/", AdminMessagesViews.as_view()),
    path("files/", FilesViews.as_view()),
    path("files/<int:pk>/", FilesViews.as_view()),
    path("files/upload-file/", FilesUploadView.as_view()),
    path("files/read-txt/<int:file_id>/", ReadTxtFileView.as_view()),
    path("admin/files/", AdminFilesViews.as_view()),
    path("admin/files/<int:pk>/", AdminFilesViews.as_view()),
    path("user-usage/", UserUsageViews.as_view()),
    path("user-usage/<int:pk>/", UserUsageViews.as_view()),
    path("user-usage/user/<int:user_id>/", UserUsageByUserView.as_view()),
    path("user-usage/log-user-activity/<int:user_id>/", LogUserActivityView.as_view()),
    path("admin/user-usage/", AdminUserUsageViews.as_view()),
    path("admin/user-usage/<int:pk>/", AdminUserUsageViews.as_view()),
    path("plan-types/", PlanTypesViews.as_view()),
    path("plan-types/<int:pk>/", PlanTypesViews.as_view()),
    path("admin/plan-types/", AdminPlanTypesViews.as_view()),
    path("admin/plan-types/<int:pk>/", AdminPlanTypesViews.as_view()),
    path("plans/", PlansViews.as_view()),
    path("plans/<int:pk>/", PlansViews.as_view()),
    path("admin/plans/", AdminPlansViews.as_view()),
    path("admin/plans/<int:pk>/", AdminPlansViews.as_view()),
    path("user-plans/", UserPlansViews.as_view()),
    path("user-plans/<int:pk>/", UserPlansViews.as_view()),
    path("user-plans/user-active-plan/<int:user_id>/", UserActivePlanView.as_view()),
    path("user-plans/change-user-plan/<int:user_id>/", ChangeUserPlanView.as_view()),
    path("admin/user-plans/", AdminUserPlansViews.as_view()),
    path("admin/user-plans/<int:pk>/", AdminUserPlansViews.as_view()),
    path("admin/user-token/", AdminUserTokenView.as_view()),
    path("admin/user-token/<int:pk>/", AdminUserTokenView.as_view()),
    path("", HomeView.as_view(), name="home"),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("chat/<int:user_id>/", ChatView.as_view()),
    path("chat/events/<int:user_id>/", ChatEventsView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
