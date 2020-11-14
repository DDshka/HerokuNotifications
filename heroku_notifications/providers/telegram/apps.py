from django.apps import AppConfig


class Config(AppConfig):
    name = 'heroku_notifications.providers.telegram'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from .provider import TelegramProvider
