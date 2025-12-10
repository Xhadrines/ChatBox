from ..data_access.user_plans import UserPlansAccessor
from ..admin_serializers.user_plans import AdminUserPlansSerializer


class AdminUserPlansService:
    def __init__(self):
        self.accessor = UserPlansAccessor()
        self.serializer_class = AdminUserPlansSerializer

    def get_all(self):
        objs = self.accessor.get_all()
        return self.serializer_class(objs, many=True).data

    def get_by_id(self, pk):
        obj = self.accessor.get_by_id(pk)
        if not obj:
            return None
        return self.serializer_class(obj).data

    def get_by_user(self, user_id):
        objs = self.accessor.get_by_user(user_id)
        return self.serializer_class(objs, many=True).data

    def create(self, data):
        obj = self.accessor.add(**data)
        return self.serializer_class(obj).data

    def update(self, pk, data):
        obj = self.accessor.update(pk, **data)
        return self.serializer_class(obj).data

    def delete(self, pk):
        return self.accessor.delete(pk)

    def expire_plans(self):
        self.accessor.expire_plans()
