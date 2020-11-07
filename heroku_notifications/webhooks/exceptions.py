from heroku_notifications.common.exceptions import BaseHerokuNotificationException


class WebhookException(BaseHerokuNotificationException):
    pass


class SecretMismatchException(WebhookException):
    pass
