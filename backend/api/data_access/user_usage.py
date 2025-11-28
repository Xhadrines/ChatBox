from datetime import date
from django.db.models import F

from common.models.users import Users
from common.models.user_usage import UserUsage


class UserUsageAccessor:
    def add(self, user, messages_sent, files_uploaded):
        usage = UserUsage(
            user=user,
            messages_sent=messages_sent,
            files_uploaded=files_uploaded,
        )
        usage.save()
        return usage

    def get_all(self):
        return UserUsage.objects.all()

    def get_by_id(self, usage_id):
        try:
            return UserUsage.objects.get(id=usage_id)
        except UserUsage.DoesNotExist:
            return None

    def update(self, usage_id, **kwargs):
        try:
            usage = UserUsage.objects.get(id=usage_id)
        except UserUsage.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(usage, key, value)
        usage.save()
        return usage

    def delete(self, usage_id):
        deleted, _ = UserUsage.objects.filter(id=usage_id).delete()
        return deleted

    def add_or_update_today(self, user, messages_sent=0, files_uploaded=0):
        today = date.today()
        usage, created = UserUsage.objects.get_or_create(
            user=user,
            date=today,
            defaults={"messages_sent": messages_sent, "files_uploaded": files_uploaded},
        )
        if not created:
            usage.messages_sent += messages_sent
            usage.files_uploaded += files_uploaded
            usage.save()
        return usage

    def add_or_update_today_by_id(self, user_id, messages_sent=0, files_uploaded=0):
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return None

        today = date.today()

        usage, created = UserUsage.objects.get_or_create(
            user=user,
            date=today,
            defaults={"messages_sent": messages_sent, "files_uploaded": files_uploaded},
        )

        if not created:
            usage.messages_sent = F("messages_sent") + messages_sent
            usage.files_uploaded = F("files_uploaded") + files_uploaded
            usage.save()
            usage.refresh_from_db()

        return usage
