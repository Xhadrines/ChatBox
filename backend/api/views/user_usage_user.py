from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..data_access.user_usage import UserUsageAccessor
from ..serializers.user_usage import UserUsageSerializer


class UserUsageByUserView(APIView):
    accessor = UserUsageAccessor()

    def get(self, request, user_id=None):
        if not user_id:
            return Response(
                {"error": "User ID este necesar"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        usages = self.accessor.get_all().filter(user__id=user_id).order_by("date")
        serializer = UserUsageSerializer(usages, many=True)
        return Response(serializer.data)
