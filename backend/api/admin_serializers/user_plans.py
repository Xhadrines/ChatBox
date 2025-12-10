from rest_framework import serializers

from common.models.user_plans import UserPlans


class AdminUserPlansSerializer(serializers.ModelSerializer):
    plan_name = serializers.SerializerMethodField()

    class Meta:
        model = UserPlans
        fields = ["id", "user", "plan", "plan_name", "start_date", "end_date"]
        read_only_fields = ("start_date", "end_date")

    def get_plan_name(self, obj):
        return obj.plan.name if obj.plan else None
