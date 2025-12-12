from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password

import logging

logger = logging.getLogger(__name__)


class AdminGenericCRUDView(APIView):
    service_class = None
    serializer_class = None
    password_field = None

    def get_service(self):
        return self.service_class()

    def handle_password(self, data):
        if self.password_field and self.password_field in data:
            if data[self.password_field]:
                data[self.password_field] = make_password(data[self.password_field])
            else:
                data.pop(self.password_field)
        return data

    def get(self, request, pk=None):
        service = self.get_service()

        if pk:
            obj = service.get_by_id(pk)
            if not obj:
                logger.warning(
                    f"[ADMIN GET FAILED] User: {request.user.id} | PK: {pk} | Not found"
                )
                return Response(
                    {"error": "Not found"}, status=status.HTTP_404_NOT_FOUND
                )
            logger.info(f"[ADMIN GET SUCCESS] User: {request.user.id} | PK: {pk}")
            return Response(obj)

        objs = service.get_all()
        logger.info(f"[ADMIN GET ALL] User: {request.user.id} | Count: {len(objs)}")
        return Response(objs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            data = self.handle_password(data)
            service = self.get_service()
            obj = service.create(data)
            logger.info(
                f"[ADMIN CREATE] User: {request.user.id} | Created ID: {obj.get('id')}"
            )
            return Response(obj, status=status.HTTP_201_CREATED)

        logger.warning(
            f"[ADMIN CREATE FAILED] User: {request.user.id} | Errors: {serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            logger.warning(
                f"[ADMIN UPDATE FAILED] User: {request.user.id} | Reason: ID missing"
            )
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data = self.handle_password(data)
            service = self.get_service()
            updated = service.update(pk, data)
            if not updated:
                logger.warning(
                    f"[ADMIN UPDATE FAILED] User: {request.user.id} | PK: {pk} | Not found"
                )
                return Response(
                    {"error": "Not found"}, status=status.HTTP_404_NOT_FOUND
                )

            logger.info(f"[ADMIN UPDATE SUCCESS] User: {request.user.id} | PK: {pk}")
            return Response(updated)

        logger.warning(
            f"[ADMIN UPDATE FAILED] User: {request.user.id} | Errors: {serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            logger.warning(
                f"[ADMIN PATCH FAILED] User: {request.user.id} | Reason: ID missing"
            )
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data
            data = self.handle_password(data)
            service = self.get_service()
            updated = service.update(pk, data)
            if not updated:
                logger.warning(
                    f"[ADMIN PATCH FAILED] User: {request.user.id} | PK: {pk} | Not found"
                )
                return Response(
                    {"error": "Not found"}, status=status.HTTP_404_NOT_FOUND
                )

            logger.info(
                f"[ADMIN PATCH SUCCESS] User: {request.user.id} | PK: {pk} | Fields updated: {list(data.keys())}"
            )
            return Response(updated)

        logger.warning(
            f"[ADMIN PATCH FAILED] User: {request.user.id} | Errors: {serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        service = self.get_service()
        deleted = service.delete(pk)
        if deleted == 0:
            logger.warning(
                f"[ADMIN DELETE FAILED] User: {request.user.id} | PK: {pk} | Not found"
            )
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        logger.info(f"[ADMIN DELETE SUCCESS] User: {request.user.id} | PK: {pk}")
        return Response(status=status.HTTP_204_NO_CONTENT)
