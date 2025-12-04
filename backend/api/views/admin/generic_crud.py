from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password


class AdminGenericCRUDView(APIView):
    accessor_class = None
    serializer_class = None
    fk_fields = {}
    password_field = None

    lookup_method = "get_by_id"
    create_method = "add"
    delete_method = "delete"

    lookup_param_is_user = False
    user_accessor_class = None

    def get_accessor(self):
        return self.accessor_class()

    def get_lookup_fn(self):
        return getattr(self.get_accessor(), self.lookup_method)

    def get_create_fn(self):
        return getattr(self.get_accessor(), self.create_method)

    def get_delete_fn(self):
        return getattr(self.get_accessor(), self.delete_method)

    def get(self, request, pk=None):
        accessor = self.get_accessor()

        if pk:
            obj = accessor.get_by_id(pk)
            if not obj:
                return Response(
                    {"error": "Not found"}, status=status.HTTP_404_NOT_FOUND
                )

            serializer = self.serializer_class(obj)
            return Response(serializer.data)

        objs = accessor.get_all()
        serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data)

    def handle_fk_fields(self, data):
        for field, accessor_cls in self.fk_fields.items():
            if field in data and data[field]:
                accessor = accessor_cls()
                data[field] = accessor.get_by_id(data[field])
        return data

    def handle_password(self, data):
        if self.password_field and self.password_field in data:
            if data[self.password_field]:
                data[self.password_field] = make_password(data[self.password_field])
            else:
                data.pop(self.password_field)
        return data

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            data = self.handle_fk_fields(data)
            data = self.handle_password(data)

            obj = self.get_accessor().add(**data)
            return Response(
                self.serializer_class(obj).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        accessor = self.get_accessor()
        obj = accessor.get_by_id(pk)

        if not obj:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            data = self.handle_fk_fields(data)
            data = self.handle_password(data)

            updated = accessor.update(pk, **data)
            return Response(self.serializer_class(updated).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        accessor = self.get_accessor()
        obj = accessor.get_by_id(pk)

        if not obj:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data

            data = self.handle_fk_fields(data)
            data = self.handle_password(data)

            updated = accessor.update(pk, **data)
            return Response(self.serializer_class(updated).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        accessor = self.get_accessor()
        deleted = accessor.delete(pk)

        if deleted == 0:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
