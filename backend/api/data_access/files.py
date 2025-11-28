from django.utils import timezone

from common.models.files import Files


class FilesAccessor:
    def add(self, user, file_name, file_path):
        file = Files(
            user=user,
            file_name=file_name,
            file_path=file_path,
        )
        file.save()
        return file

    def get_all(self):
        return Files.objects.all()

    def get_by_id(self, file_id):
        try:
            return Files.objects.get(id=file_id)
        except Files.DoesNotExist:
            return None

    def update(self, file_id, **kwargs):
        try:
            file = Files.objects.get(id=file_id)
        except Files.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(file, key, value)
        file.save()
        return file

    def delete(self, file_id):
        deleted, _ = Files.objects.filter(id=file_id).delete()
        return deleted

    def count_files_uploaded_today(self, user_id: int) -> int:
        today = timezone.localdate()
        return Files.objects.filter(user_id=user_id, uploaded_at__date=today).count()
