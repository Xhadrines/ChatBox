from rest_framework import authentication
from rest_framework import exceptions

from .models.user_token import UserToken


class CustomTokenAuthentication(authentication.BaseAuthentication):
    keyword = "Token"

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None

        try:
            keyword, token_key = auth_header.split()
        except ValueError:
            raise exceptions.AuthenticationFailed("Invalid token header format.")

        if keyword != self.keyword:
            return None

        try:
            user_token = UserToken.objects.get(key=token_key)
        except UserToken.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid token.")

        return (user_token.user, None)
