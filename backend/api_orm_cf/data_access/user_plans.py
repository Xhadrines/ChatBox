from django.utils import timezone
from datetime import timedelta

from common.models.user_plans import UserPlans
from .plans import PlansAccessor


class UserPlansAccessor:
    def add(self, user, plan_id, end_date=None):
        plans_accessor = PlansAccessor()
        plan = plans_accessor.get_by_id(plan_id)
        if not plan:
            return None

        if plan.duration_days:
            end_date = timezone.now() + timedelta(days=plan.duration_days)
        else:
            end_date = None

        user_plan = UserPlans(
            user=user,
            plan=plan,
            end_date=end_date,
        )
        user_plan.save()
        return user_plan

    def get_all(self):
        return UserPlans.objects.all()

    def get_by_id(self, plan_id):
        try:
            return UserPlans.objects.get(id=plan_id)
        except UserPlans.DoesNotExist:
            return None

    def update(self, plan_id, **kwargs):
        try:
            user_plan = UserPlans.objects.get(id=plan_id)
        except UserPlans.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(user_plan, key, value)
        user_plan.save()
        return user_plan

    def delete(self, plan_id):
        deleted, _ = UserPlans.objects.filter(id=plan_id).delete()
        return deleted
