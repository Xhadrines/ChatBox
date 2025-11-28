from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from django.contrib.auth.hashers import make_password

from .default_data import (
    default_user_roles,
    default_user_status,
    default_users,
    default_plan_types,
    default_plans,
    default_user_plans,
    default_files,
    default_messages,
    default_user_usage,
)

# APPS = ["api_orm_sf", "api_orm_cf", "api_mvc", "api"]
APPS = ["api_orm_sf", "common"]


@receiver(post_migrate)
def insert_default_data(sender, **kwargs):
    app_name = sender.name.split(".")[-1]
    if app_name not in APPS:
        return

    UserRoles = apps.get_model(app_name, "UserRoles")
    for data in default_user_roles():
        UserRoles.objects.get_or_create(name=data["name"], defaults=data)

    UserStatus = apps.get_model(app_name, "UserStatus")
    for data in default_user_status():
        UserStatus.objects.get_or_create(name=data["name"], defaults=data)

    PlanTypes = apps.get_model(app_name, "PlanTypes")
    for data in default_plan_types():
        PlanTypes.objects.get_or_create(name=data["name"], defaults=data)

    Plans = apps.get_model(app_name, "Plans")
    for data in default_plans():
        plan_type = PlanTypes.objects.filter(name=data.pop("type")).first()
        if plan_type:
            data["type"] = plan_type
            Plans.objects.get_or_create(name=data["name"], defaults=data)

    Users = apps.get_model(app_name, "Users")
    for data in default_users():
        role = UserRoles.objects.filter(name=data.pop("role")).first()
        status = UserStatus.objects.filter(name=data.pop("status")).first()
        if role and status:
            data["password"] = make_password(data.pop("password"))
            data["role"] = role
            data["status"] = status
            Users.objects.get_or_create(email=data["email"], defaults=data)

    UserPlans = apps.get_model(app_name, "UserPlans")
    for data in default_user_plans():
        user = Users.objects.filter(username=data.pop("user")).first()
        plan = Plans.objects.filter(name=data.pop("plan")).first()
        if user and plan:
            data["user"] = user
            data["plan"] = plan
            UserPlans.objects.get_or_create(user=user, plan=plan, defaults=data)

    Files = apps.get_model(app_name, "Files")
    for data in default_files():
        user = Users.objects.filter(username=data.pop("user")).first()
        if user:
            data["user"] = user
            Files.objects.get_or_create(file_name=data["file_name"], defaults=data)

    Messages = apps.get_model(app_name, "Messages")
    for data in default_messages():
        user = Users.objects.filter(username=data.pop("user")).first()
        if user:
            data["user"] = user
            Messages.objects.get_or_create(
                user=user, user_msg=data["user_msg"], defaults=data
            )

    UserUsage = apps.get_model(app_name, "UserUsage")
    for data in default_user_usage():
        user = Users.objects.filter(username=data.pop("user")).first()
        if user:
            data["user"] = user
            UserUsage.objects.get_or_create(user=user, date=data["date"], defaults=data)
