import json

from django.conf import settings
from telegram.ext import Updater

from heroku_notifications.config.models import NotificationConfig
from ..base import BaseProvider
from ..registry import ProviderRegistry


@ProviderRegistry.register
class TelegramProvider(BaseProvider):
    name = NotificationConfig.ProvidersEnum.Telegram.value

    def __init__(self):
        self.updater = Updater(token=settings.TELEGRAM_BOT_TOKEN)
        self.bot = self.updater.bot
        self.dispatcher = self.updater.dispatcher

    def send_notification(self, config: NotificationConfig, data: dict):
        chat_ids = config.telegram.chat_ids
        for chat_id in chat_ids:
            self.bot.send_message(chat_id=chat_id, text=self._get_message_from_data(data))

    def _get_message_from_data(self, heroku_data: dict):
        resource: str = heroku_data['resource']
        user_email: str = heroku_data['actor']['email']

        data: dict = heroku_data['data']
        application_name: str = data['app']['name']
        status: str = data['status']

        return f'{resource.capitalize()} {status} for {application_name}\n' \
               f'Initiator: {user_email}.'
