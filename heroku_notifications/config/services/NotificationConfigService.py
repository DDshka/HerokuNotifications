from typing import Dict
from uuid import UUID

from django.db import transaction

from ..dtos import ConfigDto
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
                _entities=[entity.json() for entity in webhook.entities],
            )
            created_configs[notification_config.name] = notification_config.pk

        return created_configs
