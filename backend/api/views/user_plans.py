from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .generic_crud import GenericCRUDView

from ..services.user_plans import UserPlansService
from ..serializers.user_plans import UserPlansSerializer


class UserPlansViews(GenericCRUDView):
    service_class = UserPlansService
    serializer_class = UserPlansSerializer


class ChangeUserPlanView(APIView):
    service = UserPlansService()

    def post(self, request, user_id):
        new_plan_id = request.data.get("plan_id")
        if not new_plan_id:
            return Response(
                {"error": "plan_id required"}, status=status.HTTP_400_BAD_REQUEST
            )

        active_plan, error = self.service.change_user_plan(user_id, new_plan_id)
        if error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        return Response({"active_plan": active_plan}, status=status.HTTP_200_OK)


class UserActivePlanView(APIView):
    service = UserPlansService()

    def get(self, request, user_id):
        active_plan = self.service.get_active_plan(user_id)
        return Response({"active_plan": active_plan}, status=status.HTTP_200_OK)
