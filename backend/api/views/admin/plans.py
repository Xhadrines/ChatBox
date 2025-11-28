from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...data_access.plans import PlansAccessor
from ...serializers.admin.plans import AdminPlansSerializer


class AdminPlansViews(APIView):
    accessor = PlansAccessor()

    def get(self, request, pk=None):
        if pk:
            plan = self.accessor.get_by_id(pk)
            if not plan:
                return Response(
                    {"error": "Plan not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = AdminPlansSerializer(plan)
            return Response(serializer.data)

        plans = self.accessor.get_all()
        serializer = AdminPlansSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminPlansSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            plan = self.accessor.add(
                name=data["name"],
                price=data["price"],
                type=data["type"],
                duration_days=data.get("duration_days"),
                name_llm_prm=data["name_llm_prm"],
                daily_prm_msg=data.get("daily_prm_msg"),
                name_llm_std=data["name_llm_std"],
                daily_std_msg=data.get("daily_std_msg"),
                daily_file_limit=data.get("daily_file_limit"),
            )
            return Response(
                AdminPlansSerializer(plan).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        plan = self.accessor.get_by_id(pk)
        if not plan:
            return Response(
                {"error": "Plan not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminPlansSerializer(plan, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_plan = self.accessor.update(pk, **data)
            return Response(AdminPlansSerializer(updated_plan).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        plan = self.accessor.get_by_id(pk)
        if not plan:
            return Response(
                {"error": "Plan not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminPlansSerializer(plan, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data

            updated_plan = self.accessor.update(pk, **data)
            return Response(AdminPlansSerializer(updated_plan).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "Plan not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
