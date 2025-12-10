from rest_framework import serializers

from common.models.user_token import UserToken


class AdminUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = ["user", "key", "created"]
        read_only_fields = (
            "key",
            "created",
        )
