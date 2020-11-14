from typing import Dict, Union

from pydantic import BaseModel, root_validator, validator, conlist, constr

from ..models import NotificationConfig


class ProviderDto(BaseModel):
    name: str
    args: Dict[str, Union[str, int]] = None


class WebhookDto(BaseModel):
    name: constr(max_length=NotificationConfig.NAME_MAX_LENGTH)
    provider: str
    secret: constr(min_length=8, max_length=NotificationConfig.SECRET_MAX_LENGTH)
    entities: conlist(NotificationConfig.HerokuEntitiesEnum, min_items=1)

    @validator('name', always=True)
    def validate_name(cls, name: str, **kwargs):
        if NotificationConfig.objects.filter(name__iexact=name).exists():
            raise ValueError(f'Webhook configuration with name "{name}" already exists.')
        return name


class ConfigDto(BaseModel):
    """
        Example of expected DTO:
        {
            "providers": {
                "TelegramProvider": {
                    "name": "Telegram",
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
                        "api:build",
                        "api:addon-attachment",
                        "api:addon",
                        "api:app",
                        "api:dyno",
                        "api:formation",
                        "api:release",
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
