from rest_framework import serializers

from common.models.user_status import UserStatus


class AdminUserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ("created_at", "updated_at")
