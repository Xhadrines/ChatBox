from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ApiOrmSfConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api_orm_sf"

    def ready(self):
        from common.signals import insert_default_data

        post_migrate.connect(insert_default_data, sender=self)
