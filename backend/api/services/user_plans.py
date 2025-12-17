from datetime import timedelta
from django.utils import timezone

from ..data_access.user_plans import UserPlansAccessor
from ..data_access.plans import PlansAccessor
from ..data_access.users import UsersAccessor
from ..serializers.user_plans import UserPlansSerializer

from common.cache.invalidate import invalidate_all_policy_caches


class UserPlansService:
    def __init__(self):
        self.user_plans_accessor = UserPlansAccessor()
        self.plans_accessor = PlansAccessor()
        self.users_accessor = UsersAccessor()
        self.serializer_class = UserPlansSerializer

    def get_all(self):
        objs = self.user_plans_accessor.get_all()
        return self.serializer_class(objs, many=True).data

    def get_by_id(self, pk):
        obj = self.user_plans_accessor.get_by_id(pk)
        if not obj:
            return None
        return self.serializer_class(obj).data

    def get_by_user(self, user_id):
        objs = self.user_plans_accessor.get_by_user(user_id)
        return self.serializer_class(objs, many=True).data

    def create(self, data):
        obj = self.user_plans_accessor.add(**data)
        return self.serializer_class(obj).data

    def update(self, pk, data):
        obj = self.user_plans_accessor.update(pk, **data)
        return self.serializer_class(obj).data

    def delete(self, pk):
        return self.user_plans_accessor.delete(pk)

    def expire_plans(self):
        self.user_plans_accessor.expire_plans()

    def change_user_plan(self, user_id, new_plan_id):
        user = self.users_accessor.get_by_id(user_id)
        if not user:
            return None, "User not found"

        new_plan = self.plans_accessor.get_by_id(new_plan_id)
        if not new_plan:
            return None, "Plan not found"

        start_date = timezone.now()
        end_date = (
            start_date + timedelta(days=new_plan.duration_days)
            if new_plan.duration_days
            else None
        )

        self.user_plans_accessor.end_active_plan(user_id, end_date=start_date)

        active_plan = self.user_plans_accessor.add(
            user=user,
            plan=new_plan,
            end_date=end_date,
        )

        invalidate_all_policy_caches(user_id=user_id)

        serialized = self.serializer_class(active_plan).data
        return serialized, None

    def get_active_plan(self, user_id):
        user_plans = self.user_plans_accessor.get_by_user(user_id).order_by(
            "-start_date"
        )
        if not user_plans:
            return None

        now = timezone.now()

        paid_plan = next(
            (p for p in user_plans if p.end_date and p.start_date <= now <= p.end_date),
            None,
        )
        if paid_plan:
            return self.serializer_class(paid_plan).data

        free_plan = next((p for p in user_plans if p.end_date is None), None)
        if free_plan:
            return self.serializer_class(free_plan).data

        return None
