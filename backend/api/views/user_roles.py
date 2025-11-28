from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..data_access.user_roles import UserRolesAccessor
from ..serializers.user_roles import UserRolesSerializer


class UserRolesViews(APIView):
    accessor = UserRolesAccessor()

    def get(self, request, pk=None):
        if pk:
            user_role = self.accessor.get_by_id(pk)
            if not user_role:
                return Response(
                    {"error": "User role not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = UserRolesSerializer(user_role)
            return Response(serializer.data)

        user_roles = self.accessor.get_all()
        serializer = UserRolesSerializer(user_roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserRolesSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_role = self.accessor.add(
                name=data["name"], description=data["description"]
            )
            return Response(
                UserRolesSerializer(user_role).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user_role = self.accessor.get_by_id(pk)
        if not user_role:
            return Response(
                {"error": "User role not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserRolesSerializer(user_role, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_role = self.accessor.update(pk, **data)
            return Response(UserRolesSerializer(updated_role).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user_role = self.accessor.get_by_id(pk)
        if not user_role:
            return Response(
                {"error": "User role not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserRolesSerializer(user_role, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_role = self.accessor.update(pk, **data)
            return Response(UserRolesSerializer(updated_role).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "User role not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
