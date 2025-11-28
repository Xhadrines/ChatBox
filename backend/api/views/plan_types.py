from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..data_access.plan_types import PlanTypesAccessor
from ..serializers.plan_types import PlanTypesSerializer


class PlanTypesViews(APIView):
    accessor = PlanTypesAccessor()

    def get(self, request, pk=None):
        if pk:
            plan_type = self.accessor.get_by_id(pk)
            if not plan_type:
                return Response(
                    {"error": "Plan type not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = PlanTypesSerializer(plan_type)
            return Response(serializer.data)

        plan_types = self.accessor.get_all()
        serializer = PlanTypesSerializer(plan_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanTypesSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            plan_type = self.accessor.add(
                name=data["name"], description=data["description"]
            )
            return Response(
                PlanTypesSerializer(plan_type).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        plan_type = self.accessor.get_by_id(pk)
        if not plan_type:
            return Response(
                {"error": "Plan type not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PlanTypesSerializer(plan_type, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_plan_type = self.accessor.update(pk, **data)
            return Response(PlanTypesSerializer(updated_plan_type).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST
            )

        plan_type = self.accessor.get_by_id(pk)
        if not plan_type:
            return Response(
                {"error": "Plan type not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PlanTypesSerializer(plan_type, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_plan_type = self.accessor.update(pk, **data)
            return Response(PlanTypesSerializer(updated_plan_type).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        deleted = self.accessor.delete(pk)
        if deleted == 0:
            return Response(
                {"error": "Plan type not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
