from django.conf import settings
from telegram.ext import CommandHandler, Updater, CallbackContext
from telegram.utils.types import HandlerArg

from heroku_notifications.config.models import NotificationConfig
from heroku_notifications.providers.telegram.models import TelegramConfig


class TelegramBot:
    def __init__(self):
        self.updater = Updater(token=settings.TELEGRAM_BOT_TOKEN)
        self.bot = self.updater.bot
        self.dispatcher = self.updater.dispatcher

        self.dispatcher.add_handler(CommandHandler('start', self._start_command))
        self.dispatcher.add_handler(CommandHandler('activate', self._activate_command))

    def start(self):
        self.updater.start_polling()

    def _start_command(self, update: HandlerArg, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Hi there. Please tell me your config name and the secret.\n'
                 'Send `/activate` with config name and secret token.\n'
                 'E.g. `/activate test 123`'
        )

    def _activate_command(self, update: HandlerArg, context: CallbackContext):
        chat_id = update.effective_chat.id
        text = update.message.text
        config_name, secret = text.replace('/activate ', '').split(' ')

        config = NotificationConfig.objects.get(name=config_name, secret=secret)
        config_telegram_data, created = TelegramConfig.objects.get_or_create(config_id=config.pk, defaults={'chat_ids': []})
        config_telegram_data.chat_ids = [*config_telegram_data.chat_ids, chat_id]
        config_telegram_data.save(update_fields=['chat_ids'])

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Successfully setup notifications.'
        )
