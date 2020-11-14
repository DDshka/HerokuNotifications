from django.core.management import BaseCommand

from heroku_notifications.providers.telegram.bot import TelegramBot


class Command(BaseCommand):
    help = "Telegram bot polling"
    requires_migrations_checks = True
    requires_system_checks = False

    def handle(self, *args, **options):
        bot = TelegramBot()
        bot.start()
