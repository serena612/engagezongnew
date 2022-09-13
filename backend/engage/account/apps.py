from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engage.account'

    def ready(self):
        from . import signals
        from . import schedulers


