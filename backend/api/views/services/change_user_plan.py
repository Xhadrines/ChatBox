from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from ...data_access.user_plans import UserPlansAccessor
from ...data_access.plans import PlansAccessor


class ChangeUserPlanView(APIView):
    user_plans_accessor = UserPlansAccessor()
    plans_accessor = PlansAccessor()

    def post(self, request, user_id):
        new_plan_id = request.data.get("plan_id")
        if not new_plan_id:
            return Response({"error": "plan_id required"}, status=400)

        new_plan = self.plans_accessor.get_by_id(new_plan_id)
        if not new_plan:
            return Response({"error": "Plan not found"}, status=404)

        start_date = timezone.now()

        if new_plan.duration_days:
            end_date = start_date + timedelta(days=new_plan.duration_days)
        else:
            end_date = None

        from common.models.user_plans import UserPlans

        UserPlans.objects.filter(user_id=user_id, end_date__isnull=True).update(
            end_date=start_date
        )

        active_plan = UserPlans(
            user_id=user_id,
            plan=new_plan,
            start_date=start_date,
            end_date=end_date,
        )
        active_plan.save()

        from ...serializers.user_plans import UserPlansSerializer

        serializer = UserPlansSerializer(active_plan)
        return Response({"active_plan": serializer.data}, status=200)
