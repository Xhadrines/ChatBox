from django.db import models
from .plan_types import PlanTypes


class Plans(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.ForeignKey(PlanTypes, models.DO_NOTHING)
    duration_days = models.IntegerField(blank=True, null=True)
    name_llm_prm = models.CharField(max_length=50)
    daily_prm_msg = models.IntegerField(blank=True, null=True)
    name_llm_std = models.CharField(max_length=50)
    daily_std_msg = models.IntegerField(blank=True, null=True)
    daily_file_limit = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.type.name}"

    class Meta:
        db_table = "plans"
