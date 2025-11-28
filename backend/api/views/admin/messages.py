from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...data_access.messages import MessagesAccessor
from ...serializers.admin.messages import AdminMessagesSerializer


class AdminMessagesViews(APIView):
    accessor = MessagesAccessor()

    def get(self, request, pk=None):
        if pk:
            message = self.accessor.get_by_id(pk)
            if not message:
                return Response(
                    {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = AdminMessagesSerializer(message)
            return Response(serializer.data)

        messages = self.accessor.get_all()
        serializer = AdminMessagesSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminMessagesSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            message = self.accessor.add(
                user=data["user"],
                user_msg=data["user_msg"],
                llm_resp=data["llm_resp"],
                llm_used=data["llm_used"],
            )
            return Response(
                AdminMessagesSerializer(message).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        message = self.accessor.get_by_id(pk)
        if not message:
            return Response(
                {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminMessagesSerializer(message, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_message = self.accessor.update(pk, **data)
            return Response(AdminMessagesSerializer(updated_message).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        message = self.accessor.get_by_id(pk)
        if not message:
            return Response(
                {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminMessagesSerializer(message, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_message = self.accessor.update(pk, **data)
            return Response(AdminMessagesSerializer(updated_message).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
