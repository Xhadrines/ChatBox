from django.db import models
from .users import Users


class UserUsage(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    messages_sent = models.IntegerField()
    files_uploaded = models.IntegerField()

    class Meta:
        db_table = "user_usage"
        unique_together = ("user", "date")
