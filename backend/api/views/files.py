from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .generic_crud import GenericCRUDView

from ..services.files import FilesService
from ..serializers.files import FilesSerializer

import logging

logger = logging.getLogger(__name__)


class FilesViews(GenericCRUDView):
    service_class = FilesService
    serializer_class = FilesSerializer


class FilesUploadView(APIView):
    service = FilesService()

    def post(self, request):
        file_obj = request.FILES.get("file")
        user_id = request.data.get("user")

        if not file_obj or not user_id:
            logger.warning(
                f"[FILE UPLOAD FAILED] UserID: {user_id} | Reason: file or user missing"
            )
            return Response({"error": "File și user sunt necesare"}, status=400)

        logger.info(
            f"[FILE UPLOAD ATTEMPT] UserID: {user_id} | FileName: {file_obj.name}"
        )

        file_record, error = self.service.upload_file(user_id, file_obj)
        if error:
            logger.warning(
                f"[FILE UPLOAD FAILED] UserID: {user_id} | FileName: {file_obj.name} | Error: {error}"
            )
            return Response({"error": error}, status=400)

        file_url = f"{settings.MEDIA_URL}{file_record.user.id}/{file_record.file_name}"
        logger.info(
            f"[FILE UPLOAD SUCCESS] UserID: {user_id} | FileName: {file_obj.name} | FileID: {file_record.id}"
        )

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
            logger.warning("[FILE READ FAILED] File ID missing")
            return Response({"error": "File ID missing"}, status=400)

        logger.info(f"[FILE READ ATTEMPT] FileID: {file_id}")

        content, error = self.service.read_txt_file(file_id)
        if error:
            logger.info(f"[FILE READ ATTEMPT] FileID: {file_id}")
            if "TXT" in error:
                return Response({"error": error}, status=400)
            return Response({"error": error}, status=404)

        logger.info(f"[FILE READ SUCCESS] FileID: {file_id}")
        return Response({"content": content}, status=200)
