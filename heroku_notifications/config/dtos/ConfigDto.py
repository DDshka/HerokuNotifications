from typing import Dict, List, Union

from pydantic import BaseModel, root_validator, validator, conlist

from ..models import NotificationConfig


class ProviderDto(BaseModel):
    provider: str
    args: Dict[str, Union[str, int]] = None


class Entity(BaseModel):
    name: NotificationConfig.HerokuEntitiesEnum
    events: conlist(NotificationConfig.HerokuEventTypesEnum, min_items=1)

    @validator('events', pre=True, always=True)
    def remove_duplicates(cls, events: List[str]):
        return list(set(events))

    @validator('events')
    def validate_events(cls, events: List[str], values, **kwargs):
        entity_name = values['name']
        possible_events_set = set(NotificationConfig.HerokuEntitiesToEventsMapping[entity_name])

        unexpected_events = set(events).difference(possible_events_set)
        if unexpected_events:
            possible_events_names_str = ', '.join(event.value for event in possible_events_set)
            unexpected_events_str = ', '.join(event.value for event in unexpected_events)
            raise ValueError(
                f'Unexpected entity types ({unexpected_events_str}) specified. '
                f'Allowed options are: {possible_events_names_str}'
            )

        return events


class WebhookDto(BaseModel):
    name: str
    provider: str
    entities: conlist(Entity, min_items=1)


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
                    "entities": [
                        {
                            'name': "api:build",
                            'events': ["create", "update"],
                        },
                        {
                            'name': "api:addon-attachment",
                            'events': ["create", "update"],
                        },
                        {
                            'name': "api:addon",
                            'events': ["create", "destroy", "update"],
                        },
                        {
                            'name': "api:app",
                            'events': ["create", "destroy", "update"],
                        },
                        {
                            'name': "api:dyno",
                            'events': ["create"],
                        },
                        {
                            'name': "api:formation",
                            'events': ["destroy", "update"],
                        },
                        {
                            'name': "api:release",
                            'events': ["create", "update"],
                        },
                    ]
                }
            ]
        }
    """

    providers: Dict[str, ProviderDto]
    webhooks: conlist(WebhookDto, min_items=1)

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
