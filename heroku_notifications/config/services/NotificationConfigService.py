from typing import Dict
from uuid import UUID

from django.db import transaction

from ..dtos import ConfigDto
from ..exceptions import ConfigException
from ..models import NotificationConfig


class NotificationConfigService:
    @classmethod
    @transaction.atomic
    def create(cls, config_dto: ConfigDto) -> Dict[str, UUID]:
        created_configs = dict()
        for webhook in config_dto.webhooks:
            provider = config_dto.providers[webhook.provider]

            notification_config = NotificationConfig.objects.create(
                name=webhook.name,
                provider_name=provider.name,
                provider_args=provider.args,
                secret=webhook.secret,
                entities=webhook.entities,
            )
            created_configs[notification_config.name] = notification_config.pk

        return created_configs

    @classmethod
    def delete(cls, config_id: UUID, secret: str):
        try:
            NotificationConfig.objects.get(pk=config_id, secret=secret).delete()
        except NotificationConfig.DoesNotExist as e:
            raise cls.NotFoundException from e

    @classmethod
    def update(cls, config_id: UUID, secret: str, update_data):
        try:
            config = NotificationConfig.objects.get(pk=config_id, secret=secret)
        except NotificationConfig.DoesNotExist as e:
            raise cls.NotFoundException from e

        # TODO: do update.

    class NotFoundException(ConfigException):
        pass
