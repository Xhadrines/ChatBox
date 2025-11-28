from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..data_access.user_plans import UserPlansAccessor
from ..serializers.user_plans import UserPlansSerializer


class UserPlansViews(APIView):
    accessor = UserPlansAccessor()

    def get(self, request, pk=None):
        if pk:
            user_plan = self.accessor.get_by_id(pk)
            if not user_plan:
                return Response(
                    {"error": "User plan not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = UserPlansSerializer(user_plan)
            return Response(serializer.data)

        user_plans = self.accessor.get_all()
        serializer = UserPlansSerializer(user_plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserPlansSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            user_plan = self.accessor.add(
                user=data["user"],
                plan=data["plan"],
                end_date=data.get("end_date"),
            )
            return Response(
                UserPlansSerializer(user_plan).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user_plan = self.accessor.get_by_id(pk)
        if not user_plan:
            return Response(
                {"error": "User plan not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserPlansSerializer(user_plan, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_plan = self.accessor.update(pk, **data)
            return Response(UserPlansSerializer(updated_plan).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user_plan = self.accessor.get_by_id(pk)
        if not user_plan:
            return Response(
                {"error": "User plan not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserPlansSerializer(user_plan, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_plan = self.accessor.update(pk, **data)
            return Response(UserPlansSerializer(updated_plan).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "User plan not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
