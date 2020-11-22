from django.contrib.postgres.fields import ArrayField
from django.db import models

from heroku_notifications.common.models import UUIDModel


class TelegramConfig(UUIDModel):
    config = models.OneToOneField('config.NotificationConfig', related_name='telegram', on_delete=models.CASCADE)
    chat_ids = ArrayField(base_field=models.PositiveIntegerField())