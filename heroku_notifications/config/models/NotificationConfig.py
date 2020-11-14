from enum import Enum

from django.contrib.postgres.fields import ArrayField
from django.db import models

from heroku_notifications.common.enum import ChoiceEnum
from heroku_notifications.common.models import UUIDModel


class NotificationConfig(UUIDModel):
    NAME_MAX_LENGTH = 256
    SECRET_MAX_LENGTH = 1024

    class HerokuEntitiesEnum(str, Enum):
        AddonAttachment = 'api:addon-attachment'
        Addon = 'api:addon'
        App = 'api:app'
        Build = 'api:build'
        Dyno = 'api:dyno'
        Formation = 'api:formation'
        Release = 'api:release'

    class HerokuEventTypesEnum(str, Enum):
        Create = 'create'
        Update = 'update'
        Destroy = 'destroy'

    class ProvidersEnum(ChoiceEnum):
        pass

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    provider_name = models.CharField(max_length=128, choices=ProvidersEnum.to_choices())
    provider_args = models.JSONField(null=True)

    secret = models.CharField(max_length=SECRET_MAX_LENGTH)

    entities = ArrayField(base_field=models.CharField(max_length=32))
