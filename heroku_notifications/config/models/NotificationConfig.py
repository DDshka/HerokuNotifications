from enum import Enum
from typing import List, NamedTuple, Tuple

from django.db import models
from django.utils.functional import cached_property

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

    class HerokuEntity(NamedTuple):
        name: str
        events: List[str]

    # https://devcenter.heroku.com/articles/app-webhooks#step-2-determine-which-events-to-subscribe-to
    HerokuEntitiesToEventsMapping = {
        HerokuEntitiesEnum.AddonAttachment: (
            HerokuEventTypesEnum.Create,
            HerokuEventTypesEnum.Destroy
        ),
        HerokuEntitiesEnum.Addon: (
            HerokuEventTypesEnum.Create,
            HerokuEventTypesEnum.Destroy,
            HerokuEventTypesEnum.Update,
        ),
        HerokuEntitiesEnum.App: (
            HerokuEventTypesEnum.Create,
            HerokuEventTypesEnum.Destroy,
            HerokuEventTypesEnum.Update,
        ),
        HerokuEntitiesEnum.Build: (
            HerokuEventTypesEnum.Create,
            HerokuEventTypesEnum.Update,
        ),
        HerokuEntitiesEnum.Dyno: (
            HerokuEventTypesEnum.Create,
        ),
        HerokuEntitiesEnum.Formation: (
            HerokuEventTypesEnum.Destroy,
            HerokuEventTypesEnum.Update,
        ),
        HerokuEntitiesEnum.Release: (
            HerokuEventTypesEnum.Create,
            HerokuEventTypesEnum.Update,
        ),
    }

    class ProvidersEnum(ChoiceEnum):
        pass

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    provider_name = models.CharField(max_length=128, choices=ProvidersEnum.to_choices())
    provider_args = models.JSONField(null=True)

    secret = models.CharField(max_length=SECRET_MAX_LENGTH, unique=True)

    _entities = models.JSONField()

    @cached_property
    def entities(self) -> Tuple[HerokuEntity]:
        return tuple(
            self.HerokuEntity(**data)
            for data in self._entities
        )
