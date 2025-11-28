from rest_framework import serializers

from common.models.messages import Messages


class AdminMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ["id", "user", "user_msg", "llm_resp", "llm_used", "uploaded_at"]
        read_only_fields = ("uploaded_at",)
