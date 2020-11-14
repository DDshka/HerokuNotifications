from heroku_notifications.config.models import NotificationConfig


class BaseProvider:
    def send_notification(self, config: NotificationConfig, data: dict):
        raise NotImplementedError
