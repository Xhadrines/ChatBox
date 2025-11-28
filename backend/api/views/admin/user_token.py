from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...data_access.user_token import UserTokenAccessor
from ...data_access.users import UsersAccessor
from ...serializers.admin.user_token import AdminUserTokenSerializer


class AdminUserTokenView(APIView):
    accessor = UserTokenAccessor()
    users_accessor = UsersAccessor()

    def get(self, request, pk=None):
        if pk:
            user = self.users_accessor.get_by_id(pk)
            if not user:
                return Response(
                    {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

            token = self.accessor.get_by_user(user)
            if not token:
                return Response(
                    {"error": "Token not found"}, status=status.HTTP_404_NOT_FOUND
                )

            return Response(AdminUserTokenSerializer(token).data)

        tokens = self.accessor.get_all()
        return Response(AdminUserTokenSerializer(tokens, many=True).data)

    def post(self, request):
        serializer = AdminUserTokenSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data["user"].id
            user = self.users_accessor.get_by_id(user_id)

            if not user:
                return Response(
                    {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

            token = self.accessor.create_or_get(user)
            return Response(
                AdminUserTokenSerializer(token).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "Token key required"}, status=status.HTTP_400_BAD_REQUEST
            )

        token = self.accessor.update(pk, **request.data)
        if not token:
            return Response(
                {"error": "Token not found"}, status=status.HTTP_404_NOT_FOUND
            )

        return Response(AdminUserTokenSerializer(token).data)

    def delete(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "User ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = self.users_accessor.get_by_id(pk)
        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        deleted = self.accessor.delete(user)
        if deleted == 0:
            return Response(
                {"error": "Token not found"}, status=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
