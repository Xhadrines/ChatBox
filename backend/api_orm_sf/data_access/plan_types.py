from ..models import PlanTypes


class PlanTypesAccessor:
    def add(self, name, description):
        plan_type = PlanTypes(name=name, description=description)
        plan_type.save()
        return plan_type

    def get_all(self):
        return PlanTypes.objects.all()

    def get_by_id(self, plan_type_id):
        try:
            return PlanTypes.objects.get(id=plan_type_id)
        except PlanTypes.DoesNotExist:
            return None

    def update(self, plan_type_id, **kwargs):
        try:
            plan_type = PlanTypes.objects.get(id=plan_type_id)
        except PlanTypes.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(plan_type, key, value)
        plan_type.save()
        return plan_type

    def delete(self, plan_type_id):
        deleted, _ = PlanTypes.objects.filter(id=plan_type_id).delete()
        return deleted
