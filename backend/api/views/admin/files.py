from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...data_access.files import FilesAccessor
from ...serializers.admin.files import AdminFilesSerializer


class AdminFilesViews(APIView):
    accessor = FilesAccessor()

    def get(self, request, pk=None):
        if pk:
            file = self.accessor.get_by_id(pk)
            if not file:
                return Response(
                    {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = AdminFilesSerializer(file)
            return Response(serializer.data)

        files = self.accessor.get_all()
        serializer = AdminFilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminFilesSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            file = self.accessor.add(
                user=data["user"],
                file_name=data["file_name"],
                file_path=data["file_path"],
            )
            return Response(
                AdminFilesSerializer(file).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        file = self.accessor.get_by_id(pk)
        if not file:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminFilesSerializer(file, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_file = self.accessor.update(pk, **data)
            return Response(AdminFilesSerializer(updated_file).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        file = self.accessor.get_by_id(pk)
        if not file:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminFilesSerializer(file, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_file = self.accessor.update(pk, **data)
            return Response(AdminFilesSerializer(updated_file).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
