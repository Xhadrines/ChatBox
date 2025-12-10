from ..data_access.user_token import UserTokenAccessor
from ..data_access.users import UsersAccessor
from ..admin_serializers.user_token import AdminUserTokenSerializer


class AdminUserTokenService:
    def __init__(self):
        self.accessor = UserTokenAccessor()
        self.user_accessor = UsersAccessor()
        self.serializer_class = AdminUserTokenSerializer

    def get_all(self):
        tokens = self.accessor.get_all()
        return self.serializer_class(tokens, many=True).data

    def get_by_id(self, user_id):
        user = self.user_accessor.get_by_id(user_id)
        if not user:
            return None
        token = self.accessor.get_by_user(user)
        if not token:
            return None
        return self.serializer_class(token).data

    def get_by_user_id(self, user_id):
        user = self.user_accessor.get_by_id(user_id)
        if not user:
            return None
        token = self.accessor.get_by_user(user)
        if not token:
            return None
        return self.serializer_class(token).data

    def create(self, user_id):
        return self.create_or_get(user_id)

    def create_or_get(self, user_id):
        user = self.user_accessor.get_by_id(user_id)
        if not user:
            return None
        token = self.accessor.create_or_get(user)
        return self.serializer_class(token).data

    def delete(self, user_id):
        return self.delete_by_user_id(user_id)

    def delete_by_user_id(self, user_id):
        user = self.user_accessor.get_by_id(user_id)
        if not user:
            return 0
        return self.accessor.delete(user)

    def update(self, token_key, data):
        token = self.accessor.update(token_key, **data)
        if not token:
            return None
        return self.serializer_class(token).data
