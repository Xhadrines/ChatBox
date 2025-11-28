from django.utils import timezone

from common.models.user_token import UserToken
from common.models.users import Users


class UserTokenAccessor:
    def get_all(self):
        return UserToken.objects.all()

    def get_by_user(self, user: Users):
        try:
            return UserToken.objects.get(user=user)
        except UserToken.DoesNotExist:
            return None

    def create_or_get(self, user: Users):

        token, created = UserToken.objects.get_or_create(user=user)
        if not created:
            token.created = timezone.now()
            token.save()
        return token

    def delete(self, user: Users):
        deleted, _ = UserToken.objects.filter(user=user).delete()
        return deleted

    def update(self, token_key: str, **kwargs):
        try:
            token = UserToken.objects.get(key=token_key)
        except UserToken.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(token, key, value)
        token.save()
        return token
