import json

from django.conf import settings
from telegram.ext import Updater

from heroku_notifications.config.models import NotificationConfig
from ..base import BaseProvider


class TelegramProvider(BaseProvider):
    def __init__(self):
        self.updater = Updater(token=settings.TELEGRAM_BOT_TOKEN)
        self.bot = self.updater.bot
        self.dispatcher = self.updater.dispatcher

    def send_notification(self, config: NotificationConfig, data: dict):
        chat_ids = config.telegram.chat_ids
        for chat_id in chat_ids:
            self.bot.send_message(chat_id=chat_id, text=json.dumps(data))
