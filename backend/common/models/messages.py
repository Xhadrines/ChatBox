from django.db import models
from .users import Users


class Messages(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    user_msg = models.TextField()
    llm_resp = models.TextField()
    llm_used = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
