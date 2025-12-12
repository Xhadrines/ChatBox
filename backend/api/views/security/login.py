from rest_framework.views import APIView
from rest_framework.response import Response

from ...services.security.login import LoginService

import logging

logger = logging.getLogger(__name__)


class LoginView(APIView):
    service = LoginService()

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        logger.info(f"[LOGIN ATTEMPT] Email: {email}")

        data, error, status_code = self.service.login(email, password)
        if error:
            logger.warning(f"[LOGIN FAILED] Email: {email} | Error: {error}")
            return Response({"error": error}, status=status_code)

        logger.info(f"[LOGIN SUCCESS] Email: {email} | UserID: {data['user']['id']}")

        return Response({"message": "Login successful", **data}, status=status_code)
