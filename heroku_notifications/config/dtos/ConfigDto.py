from typing import Dict, List, Union

from pydantic import BaseModel, root_validator, validator, conlist, constr

from ..models import NotificationConfig


class ProviderDto(BaseModel):
    name: str
    args: Dict[str, Union[str, int]] = None


class EntityDto(BaseModel):
    name: NotificationConfig.HerokuEntitiesEnum
    events: conlist(NotificationConfig.HerokuEventTypesEnum, min_items=1)

    @validator('events', pre=True, always=True)
    def remove_duplicates(cls, events: List[str]):
        return list(set(events))

    @validator('events', each_item=True)
    def validate_events(cls, event: NotificationConfig.HerokuEventTypesEnum, values, **kwargs):
        entity_name = values.get('name')
        if not entity_name:
            return event

        possible_events = NotificationConfig.HerokuEntitiesToEventsMapping.get(entity_name)
        if event not in possible_events:
            possible_events_names_str = ', '.join(event.value for event in possible_events)
            raise ValueError(
                f'Unexpected entity type ({event}) specified. '
                f'Allowed options are: {possible_events_names_str}'
            )

        return event


class WebhookDto(BaseModel):
    name: constr(max_length=NotificationConfig.NAME_MAX_LENGTH)
    provider: str
    secret: constr(min_length=8, max_length=NotificationConfig.SECRET_MAX_LENGTH)
    entities: conlist(EntityDto, min_items=1)


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
                    "secret": "secret key",
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

    @root_validator(skip_on_failure=True)
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
