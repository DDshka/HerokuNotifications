from enum import Enum

from django.db import models

from heroku_notifications.common.enum import ChoiceEnum
from heroku_notifications.common.models import UUIDModel


class NotificationConfig(UUIDModel):
    class ProvidersEnum(ChoiceEnum):
        pass


    provider_name = models.CharField(max_length=128, choices=ProvidersEnum.to_choices())
    provider_args = models.JSONField(null=True)

    secret = models.CharField(max_length=1024, unique=True)

    class HerokuEntitiesEnum(Enum):
        AddonAttachment = 'api:addon-attachment'
        Addon = 'api:addon'
        App = 'api:app'
        Build = 'api:build'
        Dyno = 'api:dyno'
        Formation = 'api:formation'
        Release = 'api:release'

    class HerokuEventTypesEnum(Enum):
        Create = 'create'
        Update = 'update'
        Destroy = 'destroy'

    # https://devcenter.heroku.com/articles/app-webhooks#step-2-determine-which-events-to-subscribe-to
    HerokuEntitiesToEventsMapping = {
        HerokuEntitiesEnum.AddonAttachment.value: (
            HerokuEventTypesEnum.Create.value,
            HerokuEventTypesEnum.Destroy.value
        ),
        HerokuEntitiesEnum.Addon.value: (
            HerokuEventTypesEnum.Create.value,
            HerokuEventTypesEnum.Destroy.value,
            HerokuEventTypesEnum.Update.value,
        ),
        HerokuEntitiesEnum.App.value: (
            HerokuEventTypesEnum.Create.value,
            HerokuEventTypesEnum.Destroy.value,
            HerokuEventTypesEnum.Update.value,
        ),
        HerokuEntitiesEnum.Build.value: (
            HerokuEventTypesEnum.Create.value,
            HerokuEventTypesEnum.Update.value,
        ),
        HerokuEntitiesEnum.Dyno.value: (
            HerokuEventTypesEnum.Create.value,
        ),
        HerokuEntitiesEnum.Formation.value: (
            HerokuEventTypesEnum.Destroy.value,
            HerokuEventTypesEnum.Update.value,
        ),
        HerokuEntitiesEnum.Release.value: (
            HerokuEventTypesEnum.Create.value,
            HerokuEventTypesEnum.Update.value,
        ),
    }
