from django.db import models
from .users import Users


class Files(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "files"
