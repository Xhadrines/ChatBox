from rest_framework.views import APIView
from rest_framework.response import Response

from ...services.security.login import LoginService


class LoginView(APIView):
    service = LoginService()

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        data, error, status_code = self.service.login(email, password)
        if error:
            return Response({"error": error}, status=status_code)

        return Response({"message": "Login successful", **data}, status=status_code)
