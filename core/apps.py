from django.apps import AppConfig


# This is a Django AppConfig class for the 'core' app with a default auto field set to
# 'django.db.models.BigAutoField'.
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
