from rest_framework import serializers

from common.models.plan_types import PlanTypes


class PlanTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanTypes
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ("created_at", "updated_at")
