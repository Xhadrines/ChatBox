from rest_framework import serializers

from common.models.user_status import UserStatus


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ("created_at", "updated_at")
