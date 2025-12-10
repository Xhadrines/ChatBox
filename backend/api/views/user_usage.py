from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .generic_crud import GenericCRUDView

from ..services.user_usage import UserUsageService
from ..serializers.user_usage import UserUsageSerializer


class UserUsageViews(GenericCRUDView):
    service_class = UserUsageService
    serializer_class = UserUsageSerializer


class UserUsageByUserView(APIView):
    service = UserUsageService()

    def get(self, request, user_id=None):
        if not user_id:
            return Response(
                {"error": "User ID este necesar"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        usages = self.service.get_by_user(user_id)
        return Response(usages)


class LogUserActivityView(APIView):
    service = UserUsageService()

    def post(self, request, user_id):
        data = self.service.log_activity_today(
            user_id=user_id,
            messages_sent=request.data.get("messages_sent", 0),
            files_uploaded=request.data.get("files_uploaded", 0),
        )
        return Response(data, status=status.HTTP_200_OK)
