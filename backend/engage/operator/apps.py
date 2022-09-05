from django.apps import AppConfig


class OperatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engage.operator'

    def ready(self):
        from . import signals
