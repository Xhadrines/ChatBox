from django.utils import timezone
from datetime import timedelta

from common.models.user_plans import UserPlans
from common.models.plans import Plans


class UserPlansAccessor:
    def add(self, user, plan, end_date=None):
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

    def get_by_user(self, user_id):
        return UserPlans.objects.filter(user_id=user_id).order_by("-start_date")

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

    def expire_plans(self):
        now = timezone.now()

        free_plan = Plans.objects.filter(price="0.00").first()
        if not free_plan:
            return

        expired_plans = UserPlans.objects.filter(end_date__lt=now)

        for user_plan in expired_plans:
            user_plan.plan = free_plan
            user_plan.start_date = now
            user_plan.end_date = None
            user_plan.save()
