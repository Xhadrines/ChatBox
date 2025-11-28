from rest_framework.views import APIView
from rest_framework.response import Response

from ...data_access.files import FilesAccessor


class ReadTxtFileView(APIView):
    accessor = FilesAccessor()

    def get(self, request, *args, **kwargs):
        file_id = kwargs.get("file_id")
        if not file_id:
            return Response({"error": "File ID missing"}, status=400)

        file_record = self.accessor.get_by_id(file_id)
        if not file_record:
            return Response({"error": "File not found"}, status=404)

        if not file_record.file_path.lower().endswith(".txt"):
            return Response({"error": "Nu este fișier TXT"}, status=400)

        try:
            with open(file_record.file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            return Response({"error": f"Cannot read file: {str(e)}"}, status=500)

        return Response({"content": content}, status=200)
