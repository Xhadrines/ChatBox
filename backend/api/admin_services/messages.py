from ..data_access.messages import MessagesAccessor
from ..admin_serializers.messages import AdminMessagesSerializer


class AdminMessagesService:
    def __init__(self):
        self.accessor = MessagesAccessor()
        self.serializer_class = AdminMessagesSerializer

    def get_all(self):
        objs = self.accessor.get_all()
        return self.serializer_class(objs, many=True).data

    def get_by_id(self, pk):
        obj = self.accessor.get_by_id(pk)
        if not obj:
            return None
        return self.serializer_class(obj).data

    def get_by_user_id(self, user_id):
        objs = self.accessor.get_by_user_id(user_id)
        return self.serializer_class(objs, many=True).data

    def create(self, data):
        obj = self.accessor.add(**data)
        return self.serializer_class(obj).data

    def update(self, pk, data):
        obj = self.accessor.update(pk, **data)
        return self.serializer_class(obj).data

    def delete(self, pk):
        return self.accessor.delete(pk)

    def count_messages_today(self, user, llm_used):
        return self.accessor.count_messages_today(user, llm_used)
