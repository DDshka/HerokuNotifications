from typing import Dict, List

from pydantic import BaseModel, root_validator, validator

from ..models import NotificationConfig


class ProviderDto(BaseModel):
    provider: str
    args: dict = None


class WebhookDto(BaseModel):
    name: str
    provider: str
    entities: Dict[str, List[str]]

    @validator('entities')
    def validate_entities(cls, entities: Dict[str, List[str]]):
        entity_names = set(entities.keys())
        possible_entity_names = set([entity.value for entity in NotificationConfig.HerokuEntitiesEnum])

        unexpected_entities = entity_names.difference(possible_entity_names)
        if unexpected_entities:
            possible_entity_names_str = ', '.join(possible_entity_names)
            unexpected_entities_str = ', '.join(unexpected_entities)
            raise ValueError(
                f'Unexpected entity types ({unexpected_entities_str}) specified. '
                f'Allowed options are: {possible_entity_names_str}')

        event_errors = dict()
        for entity, events in entities.items():
            events_set = set(events)
            possible_events_set = set(NotificationConfig.HerokuEntitiesToEventsMapping[entity])
            unexpected_events = events_set.difference(possible_events_set)
            if unexpected_events:
                event_errors[entity] = unexpected_events

        if event_errors:
            errors = []
            for entity, unexpected_events in event_errors.items():
                possible_events_set = set(NotificationConfig.HerokuEntitiesToEventsMapping[entity])
                possible_events_str = ', '.join(possible_events_set)
                unexpected_events_str = ', '.join(unexpected_events)
                errors.append(
                    f'Unexpected events types ({unexpected_events_str}) specified for {entity}. '
                    f'Allowed options are: {possible_events_str}'
                )

            raise ValueError('\n'.join(errors))

        return entities


class ConfigDto(BaseModel):
    """
        Example of expected DTO:
        {
            "providers": {
                "TelegramProvider": {
                    "provider": "Telegram",
                    "args": {
                        "chat_id": 123123
                    }
                }
            },
            "webhooks": [
                {
                    "name": "test",
                    "provider": "TelegramProvider",
                    "entities": {
                        "api:addon-attachment": ["create", "destroy"],
                        "api:addon": ["create", "destroy", "update"],
                        "api:app": ["create", "destroy", "update"],
                        "api:build": ["create", "update"],
                        "api:dyno": ["create"],
                        "api:formation": ["destroy", "update"],
                        "api:release": ["create", "update"]
                    }
                }
            ]
        }
    """

    providers: Dict[str, ProviderDto]
    webhooks: List[WebhookDto]

    @root_validator
    def validate_providers(cls, data):
        provider_names = data.get('providers').keys()
        for webhook_config in data.get('webhooks'):
            if webhook_config.provider not in provider_names:
                raise ValueError(
                    f'Unexpected provider "{webhook_config.provider}" specified '
                    f'for "{webhook_config.name}" webhook config. '
                    f'Specify desired provider and it\'s config in "providers" section. '
                    f'For example: '
                    '''
                        "providers": {
                                "TelegramProvider": {
                                "provider": "Telegram",
                                "args": {
                                    "chat_id": 123123
                                }
                            }
                        },
                    '''
                )
        return data
