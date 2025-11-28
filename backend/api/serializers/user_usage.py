from rest_framework import serializers

from common.models.user_usage import UserUsage


class UserUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUsage
        fields = ["id", "user", "date", "messages_sent", "files_uploaded"]
        read_only_fields = ("date",)
