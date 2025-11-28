from rest_framework import serializers


class UserUsageLogSerializer(serializers.Serializer):
    messages_sent = serializers.IntegerField(default=0)
    files_uploaded = serializers.IntegerField(default=0)
