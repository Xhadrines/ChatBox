import os
from django.conf import settings
from django.utils import timezone

from ..data_access.files import FilesAccessor
from ..data_access.users import UsersAccessor
from ..data_access.user_plans import UserPlansAccessor
from ..serializers.files import FilesSerializer


class FilesService:
    def __init__(self):
        self.files_accessor = FilesAccessor()
        self.users_accessor = UsersAccessor()
        self.user_plans_accessor = UserPlansAccessor()
        self.serializer_class = FilesSerializer

    def get_all(self):
        objs = self.files_accessor.get_all()
        return self.serializer_class(objs, many=True).data

    def get_by_id(self, pk):
        obj = self.files_accessor.get_by_id(pk)
        if not obj:
            return None
        return self.serializer_class(obj).data

    def create(self, data):
        obj = self.files_accessor.add(**data)
        return self.serializer_class(obj).data

    def update(self, pk, data):
        obj = self.files_accessor.update(pk, **data)
        return self.serializer_class(obj).data

    def delete(self, pk):
        return self.files_accessor.delete(pk)

    def count_files_uploaded_today(self, user_id: int) -> int:
        return self.files_accessor.count_files_uploaded_today(user_id)

    def upload_file(self, user_id, file_obj):
        user = self.users_accessor.get_by_id(user_id)
        if not user:
            return None, "User nu există"

        now = timezone.now()
        user_plans = self.user_plans_accessor.get_by_user(user.id)

        paid_plan = next(
            (p for p in user_plans if p.end_date and p.start_date <= now <= p.end_date),
            None,
        )

        if paid_plan:
            active_plan = paid_plan
        else:
            free_plan = next((p for p in user_plans if p.end_date is None), None)
            active_plan = free_plan

        if not active_plan:
            return None, "Userul nu are plan activ"

        daily_file_limit = getattr(active_plan.plan, "daily_file_limit", None)
        files_today_count = self.files_accessor.count_files_uploaded_today(user.id)

        if daily_file_limit is not None and files_today_count >= daily_file_limit:
            return (
                None,
                f"Ai atins limita zilnică de fișiere pentru planul tău ({daily_file_limit})",
            )

        user_dir = os.path.join(settings.BASE_DIR, "user_files", str(user.id))
        os.makedirs(user_dir, exist_ok=True)
        file_path = os.path.join(user_dir, file_obj.name)

        with open(file_path, "wb+") as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        file_record = self.files_accessor.add(
            user=user, file_name=file_obj.name, file_path=file_path
        )
        return file_record, None

    def read_txt_file(self, file_id):
        file_record = self.files_accessor.get_by_id(file_id)
        if not file_record:
            return None, "File not found"

        if not file_record.file_path.lower().endswith(".txt"):
            return None, "Nu este fișier TXT"

        try:
            with open(file_record.file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            return None, f"Cannot read file: {str(e)}"

        return content, None
