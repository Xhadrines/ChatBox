# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Files(models.Model):
    user = models.ForeignKey("Users", models.DO_NOTHING)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "files_old"


class Messages(models.Model):
    user = models.ForeignKey("Users", models.DO_NOTHING)
    user_msg = models.TextField()
    llm_resp = models.TextField()
    llm_used = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "messages_old"


class PlanTypes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "plan_types_old"


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
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "plans_old"


class UserPlans(models.Model):
    user = models.ForeignKey("Users", models.DO_NOTHING)
    plan = models.ForeignKey(Plans, models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "user_plans_old"


class UserRoles(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "user_roles_old"


class UserStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "user_status_old"


class UserUsage(models.Model):
    user = models.ForeignKey("Users", models.DO_NOTHING)
    date = models.DateField()
    messages_sent = models.IntegerField()
    files_uploaded = models.IntegerField()

    class Meta:
        managed = True
        db_table = "user_usage_old"


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(UserRoles, models.DO_NOTHING)
    status = models.ForeignKey(UserStatus, models.DO_NOTHING)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = "users_old"
