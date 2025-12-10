from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...services.security.register import RegisterService


class RegisterView(APIView):
    service = RegisterService()

    def post(self, request):
        user_data, error = self.service.register_user(request.data)
        if error:
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"message": "User created successfully", "user": user_data},
            status=status.HTTP_201_CREATED,
        )
