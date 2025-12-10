from rest_framework import serializers

from common.models.plans import Plans


class AdminPlansSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source="type.name", read_only=True)

    class Meta:
        model = Plans
        fields = [
            "id",
            "name",
            "price",
            "type",
            "type_name",
            "duration_days",
            "name_llm_prm",
            "daily_prm_msg",
            "name_llm_std",
            "daily_std_msg",
            "daily_file_limit",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")
