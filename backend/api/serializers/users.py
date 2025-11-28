from rest_framework import serializers

from common.models.users import Users


class UsersSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source="role.name", read_only=True)
    status_name = serializers.CharField(source="status.name", read_only=True)

    class Meta:
        model = Users
        fields = [
            "id",
            "username",
            "email",
            "password",
            "role",
            "role_name",
            "status",
            "status_name",
            "last_login",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")
        extra_kwargs = {
            "password": {"write_only": True},
            "role": {"required": False},
            "status": {"required": False},
        }
