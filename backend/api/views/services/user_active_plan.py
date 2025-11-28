from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from ...data_access.user_plans import UserPlansAccessor
from ...serializers.user_plans import UserPlansSerializer


class UserActivePlanView(APIView):
    accessor = UserPlansAccessor()

    def get(self, request, user_id):
        user_plans = self.accessor.get_by_user(user_id).order_by("-start_date")
        if not user_plans:
            return Response({"active_plan": None}, status=200)

        now = timezone.now()

        paid_plan = next(
            (p for p in user_plans if p.end_date and p.start_date <= now <= p.end_date),
            None,
        )

        if paid_plan:
            serializer = UserPlansSerializer(paid_plan)
            return Response({"active_plan": serializer.data}, status=200)

        free_plan = next((p for p in user_plans if p.end_date is None), None)

        if free_plan:
            serializer = UserPlansSerializer(free_plan)
            return Response({"active_plan": serializer.data}, status=200)

        return Response({"active_plan": None}, status=200)
