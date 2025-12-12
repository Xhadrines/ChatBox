from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...services.security.register import RegisterService

import logging

logger = logging.getLogger(__name__)


class RegisterView(APIView):
    service = RegisterService()

    def post(self, request):
        logger.info(f"[REGISTER ATTEMPT] Email: {request.data.get('email')}")
        user_data, error = self.service.register_user(request.data)

        if error:
            logger.warning(
                f"[REGISTER FAILED] Email: {request.data.get('email')} | Error: {error}"
            )
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        logger.info(
            f"[REGISTER SUCCESS] Email: {user_data.get('email')} | UserID: {user_data.get('id')}"
        )

        return Response(
            {"message": "User created successfully", "user": user_data},
            status=status.HTTP_201_CREATED,
        )
