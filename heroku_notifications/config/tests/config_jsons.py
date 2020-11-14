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
                    "api:build",
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
                    "api:build",
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
                    "noname"
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
