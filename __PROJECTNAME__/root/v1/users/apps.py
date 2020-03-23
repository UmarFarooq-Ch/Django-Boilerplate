from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'root.v1.users'

    def ready(self):
        from . import signals
