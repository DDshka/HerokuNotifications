import re
from enum import Enum

from django.conf import settings
from telegram import ParseMode
from telegram.ext import CommandHandler, Updater, CallbackContext
from telegram.utils.types import HandlerArg

from .service import TelegramConfigService
from .utils import escape_telegram_message_with_markdown


class TelegramBot:
    class CommandsEnum(Enum):
        START_COMMAND = 'start'
        ACTIVATE_COMMAND = 'activate'

    def __init__(self):
        self.updater = Updater(token=settings.TELEGRAM_BOT_TOKEN)
        self.bot = self.updater.bot
        self.dispatcher = self.updater.dispatcher

        self.dispatcher.add_handler(CommandHandler(
            self.CommandsEnum.START_COMMAND.value,
            self._start_command
        ))
        self.dispatcher.add_handler(CommandHandler(
            self.CommandsEnum.ACTIVATE_COMMAND.value,
            self._activate_command
        ))

    def start(self):
        self.updater.start_polling()

    def _start_command(self, update: HandlerArg, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=escape_telegram_message_with_markdown(
                'Hi there. Please tell me your config name and the secret.\n'
                'Send `/activate` with config name and secret token.\n'
                'E.g. `/activate test 123`'),
            parse_mode=ParseMode.MARKDOWN_V2,
        )

    def _activate_command(self, update: HandlerArg, context: CallbackContext):
        chat_id = update.effective_chat.id
        text = update.effective_message.text
        text = self._clean_text(text)

        try:
            config_name, secret = text.split(' ')
        except ValueError:
            return context.bot.send_message(chat_id, 'Invalid data provided.')

        try:
            TelegramConfigService.create_or_update_config(config_name, secret, chat_id)
        except TelegramConfigService.NotFoundException:
            return context.bot.send_message(chat_id, 'You have provided invalid credentials.')
        except TelegramConfigService.ChatHasBeenAlreadyActivatedException:
            return context.bot.send_message(chat_id, 'Bot has been already activated in this chat.')

        return context.bot.send_message(chat_id, 'Successfully setup notifications.')

    def _clean_text(self, text: str) -> str:
        commands = [entity.value for entity in self.CommandsEnum]
        commands_re = '|'.join(commands)
        return re.sub(r'\s{2,}|/|' + commands_re, '', text).strip()
