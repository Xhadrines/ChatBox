from ..data_access.files import FilesAccessor
from ..admin_serializers.files import AdminFilesSerializer


class AdminFilesService:
    def __init__(self):
        self.accessor = FilesAccessor()
        self.serializer_class = AdminFilesSerializer

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

    def count_files_uploaded_today(self, user_id: int) -> int:
        return self.accessor.count_files_uploaded_today(user_id)
