valid_cases = {
    'full': {
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
                    {
                        'name': "api:build",
                        'events': ["create", "update"],
                    },
                    {
                        'name': "api:addon-attachment",
                        'events': ["create", "destroy"],
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
    },
    'without several entities': {
        "providers": {
            "TelegramProvider": {
                "name": "Telegram",
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
                ]
            }
        ]
    },
    'without several events': {
        "providers": {
            "TelegramProvider": {
                "name": "Telegram",
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
                        'events': ["update"],
                    },
                ]
            }
        ]
    },
}

# ------------------------------------------------------------------------------------------------------

invalid_cases = {
    'empty request': {},
    'empty webhooks': {
        "webhooks": []
    },
    'unspecified provider': {
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
                "provider": "UnknownProvider",
                "entities": [
                    {
                        'name': "api:build",
                        'events': ["create", "update"],
                    },
                ]
            }
        ]
    },
    'invalid entity name': {
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
                    {
                        'name': "noname",
                        'events': ["create", "update"],
                    },
                ]
            }
        ]
    },
    'invalid event name': {
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
                    {
                        'name': "api:build",
                        'events': ["invalid", "update"],
                    },
                ]
            }
        ]
    },
    'prohibited event name': {
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
                    {
                        'name': "api:build",
                        'events': ["destroy", "update"],
                    },
                ]
            }
        ]
    },
    'empty entities': {
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
                "entities": []
            }
        ]
    },
    'empty events': {
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
                    {
                        'name': "api:build",
                        'events': [],
                    }
                ]
            }
        ]
    },
    'no name provided': {
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
                "secret": "secret key",
                "provider": "TelegramProvider",
                "entities": [
                    {
                        'name': "api:build",
                        'events': [],
                    }
                ]
            }
        ]
    },
    'no secret provided': {
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
                "provider": "TelegramProvider",
                "entities": [
                    {
                        'name': "api:build",
                        'events': [],
                    }
                ]
            }
        ]
    },
}
