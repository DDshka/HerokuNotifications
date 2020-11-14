from heroku_notifications.config.models import NotificationConfig

from .exceptions import TelegramProviderException
from .models import TelegramConfig


class TelegramConfigService:
    @classmethod
    def create_or_update_config(cls, config_name: str, secret: str, chat_id: str):
        try:
            config = NotificationConfig.objects.get(name=config_name, secret=secret)
        except NotificationConfig.DoesNotExist as e:
            raise cls.NotFoundException from e

        config_telegram_data, created = TelegramConfig.objects.get_or_create(
            config_id=config.pk,
            defaults={'chat_ids': [chat_id]}
        )

        if not created:
            if chat_id in config_telegram_data.chat_ids:
                raise cls.ChatHasBeenAlreadyActivatedException

            config_telegram_data.chat_ids = [*config_telegram_data.chat_ids, chat_id]
            config_telegram_data.save(update_fields=['chat_ids'])

        return config_telegram_data

    class NotFoundException(TelegramProviderException):
        pass

    class ChatHasBeenAlreadyActivatedException(TelegramProviderException):
        pass
