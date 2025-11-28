from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...data_access.user_usage import UserUsageAccessor
from ...serializers.user_usage import UserUsageSerializer


class LogUserActivityView(APIView):
    accessor = UserUsageAccessor()

    def post(self, request, user_id):
        usage = self.accessor.add_or_update_today_by_id(
            user_id=user_id,
            messages_sent=request.data.get("messages_sent", 0),
            files_uploaded=request.data.get("files_uploaded", 0),
        )

        return Response(UserUsageSerializer(usage).data, status=status.HTTP_200_OK)
