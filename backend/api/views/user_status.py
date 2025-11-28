from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..data_access.user_status import UserStatusAccessor
from ..serializers.user_status import UserStatusSerializer


class UserStatusViews(APIView):
    accessor = UserStatusAccessor()

    def get(self, request, pk=None):
        if pk:
            user_status = self.accessor.get_by_id(pk)
            if not user_status:
                return Response(
                    {"error": "User status not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = UserStatusSerializer(user_status)
            return Response(serializer.data)

        user_statuses = self.accessor.get_all()
        serializer = UserStatusSerializer(user_statuses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserStatusSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_status = self.accessor.add(
                name=data["name"], description=data["description"]
            )
            return Response(
                UserStatusSerializer(user_status).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user_status = self.accessor.get_by_id(pk)
        if not user_status:
            return Response(
                {"error": "User status not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserStatusSerializer(user_status, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_status = self.accessor.update(pk, **data)
            return Response(UserStatusSerializer(updated_status).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user_status = self.accessor.get_by_id(pk)
        if not user_status:
            return Response(
                {"error": "User status not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserStatusSerializer(user_status, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_status = self.accessor.update(pk, **data)
            return Response(UserStatusSerializer(updated_status).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "User status not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
