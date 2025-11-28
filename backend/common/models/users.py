from django.db import models
from .user_roles import UserRoles
from .user_status import UserStatus


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(UserRoles, models.DO_NOTHING)
    status = models.ForeignKey(UserStatus, models.DO_NOTHING)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "users"
