from rest_framework import serializers

from common.models.files import Files


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ["id", "user", "file_name", "file_path", "uploaded_at"]
        read_only_fields = ("uploaded_at",)
