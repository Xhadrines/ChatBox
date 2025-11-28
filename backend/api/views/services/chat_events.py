from rest_framework.views import APIView
from rest_framework.response import Response

from ...data_access.messages import MessagesAccessor
from ...data_access.files import FilesAccessor


class ChatEventsView(APIView):
    messages_accessor = MessagesAccessor()
    files_accessor = FilesAccessor()

    def get(self, request, user_id):

        messages = self.messages_accessor.get_by_user_id(user_id)
        files = self.files_accessor.get_all().filter(user_id=user_id)

        events = []

        for m in messages:
            events.append(
                {
                    "type": "message",
                    "text": m.user_msg,
                    "llm_resp": m.llm_resp,
                    "llm_used": m.llm_used,
                    "created_at": m.uploaded_at,
                }
            )

        for f in files:
            events.append(
                {
                    "type": "file",
                    "file_name": f.file_name,
                    "file_url": f"/media/{f.user.id}/{f.file_name}",
                    "created_at": f.uploaded_at,
                }
            )

        events.sort(key=lambda x: x["created_at"])

        return Response(events, status=200)
