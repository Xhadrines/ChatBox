import os
from django.conf import settings
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

from ...data_access.files import FilesAccessor
from ...data_access.users import UsersAccessor
from ...data_access.user_plans import (
    UserPlansAccessor,
)


class FilesUploadView(APIView):
    accessor = FilesAccessor()
    users_accessor = UsersAccessor()
    user_plans_accessor = UserPlansAccessor()

    def post(self, request):
        file_obj = request.FILES.get("file")
        user_id = request.data.get("user")

        if not file_obj or not user_id:
            return Response({"error": "File și user sunt necesare"}, status=400)

        user = self.users_accessor.get_by_id(user_id)
        if not user:
            return Response({"error": "User nu există"}, status=404)

        now = timezone.now()
        user_plans = self.user_plans_accessor.get_by_user(user.id)
        active_plan = None
        for plan in user_plans:
            if plan.end_date is None or plan.end_date >= now:
                active_plan = plan
                break

        if not active_plan:
            return Response({"error": "Userul nu are plan activ"}, status=400)

        daily_file_limit = getattr(active_plan.plan, "daily_file_limit", None)

        files_today_count = self.accessor.count_files_uploaded_today(user.id)

        if daily_file_limit is not None and files_today_count >= daily_file_limit:
            return Response(
                {
                    "error": "Ai atins limita zilnică de fișiere pentru planul tău",
                    "active_plan_id": active_plan.id,
                    "daily_file_limit": daily_file_limit,
                    "uploaded_today": files_today_count,
                },
                status=403,
            )

        user_dir = os.path.join(settings.BASE_DIR, "user_files", str(user.id))
        os.makedirs(user_dir, exist_ok=True)

        file_path = os.path.join(user_dir, file_obj.name)

        with open(file_path, "wb+") as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        file_record = self.accessor.add(
            user=user, file_name=file_obj.name, file_path=file_path
        )

        file_url = f"{settings.MEDIA_URL}{user.id}/{file_obj.name}"

        return Response(
            {
                "id": file_record.id,
                "user": user.id,
                "file_name": file_obj.name,
                "file_path": file_record.file_path,
                "file_url": file_url,
                "active_plan_id": active_plan.id,
                "uploaded_today": files_today_count + 1,
                "daily_file_limit": daily_file_limit,
            },
            status=201,
        )
