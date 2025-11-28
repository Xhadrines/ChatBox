from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...data_access.user_usage import UserUsageAccessor
from ...serializers.admin.user_usage import AdminUserUsageSerializer


class AdminUserUsageViews(APIView):
    accessor = UserUsageAccessor()

    def get(self, request, pk=None):
        if pk:
            usage = self.accessor.get_by_id(pk)
            if not usage:
                return Response(
                    {"error": "User usage not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = AdminUserUsageSerializer(usage)
            return Response(serializer.data)

        usages = self.accessor.get_all()
        serializer = AdminUserUsageSerializer(usages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminUserUsageSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            usage = self.accessor.add(
                user=data["user"],
                messages_sent=data["messages_sent"],
                files_uploaded=data["files_uploaded"],
            )
            return Response(
                AdminUserUsageSerializer(usage).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        usage = self.accessor.get_by_id(pk)
        if not usage:
            return Response(
                {"error": "User usage not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminUserUsageSerializer(usage, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_usage = self.accessor.update(pk, **data)
            return Response(AdminUserUsageSerializer(updated_usage).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        usage = self.accessor.get_by_id(pk)
        if not usage:
            return Response(
                {"error": "User usage not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminUserUsageSerializer(usage, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_usage = self.accessor.update(pk, **data)
            return Response(AdminUserUsageSerializer(updated_usage).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "User usage not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
