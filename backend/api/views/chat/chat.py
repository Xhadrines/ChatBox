from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...services.chat.chat import ChatService
from ...serializers.messages import MessagesSerializer


class ChatEventsView(APIView):
    service = ChatService()

    def get(self, request, user_id):
        events = self.service.get_chat_events(user_id)
        return Response(events, status=status.HTTP_200_OK)


class ChatView(APIView):
    service = ChatService()

    def post(self, request, user_id):
        prompt = request.data.get("prompt", "")
        if not prompt:
            return Response(
                {"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        result, error = self.service.send_message(user_id, prompt)
        if error:
            return Response(
                {"error": error},
                status=(
                    status.HTTP_403_FORBIDDEN
                    if error == "No active plan"
                    else status.HTTP_404_NOT_FOUND
                ),
            )

        result["saved_message"] = MessagesSerializer(result["saved_message"]).data

        return Response(result, status=status.HTTP_200_OK)
