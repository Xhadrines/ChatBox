from ..models import UserRoles


class UserRolesAccessor:
    def add(self, name, description):
        role = UserRoles(name=name, description=description)
        role.save()
        return role

    def get_all(self):
        return UserRoles.objects.all()

    def get_by_id(self, role_id):
        try:
            return UserRoles.objects.get(id=role_id)
        except UserRoles.DoesNotExist:
            return None

    def update(self, role_id, **kwargs):
        try:
            role = UserRoles.objects.get(id=role_id)
        except UserRoles.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(role, key, value)
        role.save()
        return role

    def delete(self, role_id):
        deleted, _ = UserRoles.objects.filter(id=role_id).delete()
        return deleted
