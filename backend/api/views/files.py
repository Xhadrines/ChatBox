from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .generic_crud import GenericCRUDView

from ..services.files import FilesService
from ..serializers.files import FilesSerializer


class FilesViews(GenericCRUDView):
    service_class = FilesService
    serializer_class = FilesSerializer


class FilesUploadView(APIView):
    service = FilesService()

    def post(self, request):
        file_obj = request.FILES.get("file")
        user_id = request.data.get("user")

        if not file_obj or not user_id:
            return Response({"error": "File și user sunt necesare"}, status=400)

        file_record, error = self.service.upload_file(user_id, file_obj)
        if error:
            return Response({"error": error}, status=400)

        file_url = f"{settings.MEDIA_URL}{file_record.user.id}/{file_record.file_name}"

        return Response(
            {
                "id": file_record.id,
                "user": file_record.user.id,
                "file_name": file_record.file_name,
                "file_path": file_record.file_path,
                "file_url": file_url,
            },
            status=201,
        )


class ReadTxtFileView(APIView):
    service = FilesService()

    def get(self, request, file_id=None, **kwargs):
        file_id = file_id or kwargs.get("user_id")
        if not file_id:
            return Response({"error": "File ID missing"}, status=400)

        content, error = self.service.read_txt_file(file_id)
        if error:
            if "TXT" in error:
                return Response({"error": error}, status=400)
            return Response({"error": error}, status=404)

        return Response({"content": content}, status=200)
