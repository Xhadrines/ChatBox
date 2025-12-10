from ..data_access.user_usage import UserUsageAccessor
from ..admin_serializers.user_usage import AdminUserUsageSerializer


class AdminUserUsageService:
    def __init__(self):
        self.accessor = UserUsageAccessor()
        self.serializer_class = AdminUserUsageSerializer

    def get_all(self):
        objs = self.accessor.get_all()
        return self.serializer_class(objs, many=True).data

    def get_by_id(self, pk):
        obj = self.accessor.get_by_id(pk)
        if not obj:
            return None
        return self.serializer_class(obj).data

    def create(self, data):
        obj = self.accessor.add(**data)
        return self.serializer_class(obj).data

    def update(self, pk, data):
        obj = self.accessor.update(pk, **data)
        return self.serializer_class(obj).data

    def delete(self, pk):
        return self.accessor.delete(pk)

    def add_or_update_today(self, user, messages_sent=0, files_uploaded=0):
        usage = self.accessor.add_or_update_today(user, messages_sent, files_uploaded)
        return self.serializer_class(usage).data

    def add_or_update_today_by_id(self, user_id, messages_sent=0, files_uploaded=0):
        usage = self.accessor.add_or_update_today_by_id(
            user_id, messages_sent, files_uploaded
        )
        if not usage:
            return None
        return self.serializer_class(usage).data
