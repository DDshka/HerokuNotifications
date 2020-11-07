from django.db import models

from heroku_notifications.common.enum import ChoiceEnum
from heroku_notifications.common.models import UUIDModel


class NotificationConfig(UUIDModel):
    class ProvidersEnum(ChoiceEnum):
        pass

    webhook_url = models.CharField(max_length=1024, unique=True)
    provider_name = models.CharField(max_length=128, choices=ProvidersEnum.to_choices())
    provider_args = models.JSONField(null=True)

    secret = models.CharField(max_length=1024, unique=True)