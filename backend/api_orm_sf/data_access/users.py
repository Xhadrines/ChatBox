from ..models import Users


class UsersAccessor:
    def add(self, username, email, password, role, status):
        user = Users(
            username=username,
            email=email,
            password=password,
            role=role,
            status=status,
        )
        user.save()
        return user

    def get_all(self):
        return Users.objects.all()

    def get_by_id(self, user_id):
        try:
            return Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return None

    def update(self, user_id, **kwargs):
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    def delete(self, user_id):
        deleted, _ = Users.objects.filter(id=user_id).delete()
        return deleted
