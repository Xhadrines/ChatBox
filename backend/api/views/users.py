from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..data_access.users import UsersAccessor
from ..serializers.users import UsersSerializer


class UsersViews(APIView):
    accessor = UsersAccessor()

    def get(self, request, pk=None):
        if pk:
            user = self.accessor.get_by_id(pk)
            if not user:
                return Response(
                    {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

            serializer = UsersSerializer(user)
            return Response(serializer.data)

        users = self.accessor.get_all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            hashed_password = make_password(data["password"])

            user = self.accessor.add(
                username=data["username"],
                email=data["email"],
                password=hashed_password,
                role=data["role"],
                status=data["status"],
            )
            return Response(UsersSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = self.accessor.get_by_id(pk)
        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            if "password" in data:
                if data["password"]:
                    data["password"] = make_password(data["password"])
                else:
                    data.pop("password")

            updated_user = self.accessor.update(pk, **data)
            return Response(UsersSerializer(updated_user).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = self.accessor.get_by_id(pk)
        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data

            if "password" in data:
                if data["password"]:
                    data["password"] = make_password(data["password"])
                else:
                    data.pop("password")

            updated_user = self.accessor.update(pk, **data)
            return Response(UsersSerializer(updated_user).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)

        if deleted == 0:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
