from django.db import models
from .users import Users
from .plans import Plans


class UserPlans(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    plan = models.ForeignKey(Plans, models.DO_NOTHING)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "user_plans"
