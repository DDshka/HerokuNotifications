from heroku_notifications.common.exceptions import BaseHerokuNotificationException


class WebhookException(BaseHerokuNotificationException):
    pass


class SecretException(WebhookException):
    pass


class SecretNotProvidedException(SecretException):
    pass


class SecretMismatchException(SecretException):
    pass
