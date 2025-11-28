from ..models import UserStatus


class UserStatusAccessor:
    def add(self, name, description):
        status = UserStatus(name=name, description=description)
        status.save()
        return status

    def get_all(self):
        return UserStatus.objects.all()

    def get_by_id(self, status_id):
        try:
            return UserStatus.objects.get(id=status_id)
        except UserStatus.DoesNotExist:
            return None

    def update(self, status_id, **kwargs):
        try:
            status = UserStatus.objects.get(id=status_id)
        except UserStatus.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(status, key, value)
        status.save()
        return status

    def delete(self, status_id):
        deleted, _ = UserStatus.objects.filter(id=status_id).delete()
        return deleted
