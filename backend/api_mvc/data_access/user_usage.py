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
