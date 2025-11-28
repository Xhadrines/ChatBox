from ..models import Plans


class PlansAccessor:
    def add(
        self,
        name,
        price,
        type,
        duration_days=None,
        name_llm_prm=None,
        daily_prm_msg=None,
        name_llm_std=None,
        daily_std_msg=None,
        daily_file_limit=None,
    ):
        plan = Plans(
            name=name,
            price=price,
            type=type,
            duration_days=duration_days,
            name_llm_prm=name_llm_prm,
            daily_prm_msg=daily_prm_msg,
            name_llm_std=name_llm_std,
            daily_std_msg=daily_std_msg,
            daily_file_limit=daily_file_limit,
        )
        plan.save()
        return plan

    def get_all(self):
        return Plans.objects.all()

    def get_by_id(self, plan_id):
        try:
            return Plans.objects.get(id=plan_id)
        except Plans.DoesNotExist:
            return None

    def update(self, plan_id, **kwargs):
        try:
            plan = Plans.objects.get(id=plan_id)
        except Plans.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(plan, key, value)
        plan.save()
        return plan

    def delete(self, plan_id):
        deleted, _ = Plans.objects.filter(id=plan_id).delete()
        return deleted
