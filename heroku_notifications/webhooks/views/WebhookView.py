import base64
import hashlib
import hmac
import json
import logging

from uuid import UUID

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.views.generic.base import View

from heroku_notifications.config.models import NotificationConfig
from heroku_notifications.common.responses import HttpResponseUnauthorized, HttpResponseAccepted
from heroku_notifications.providers.registry import ProviderRegistry
from ..exceptions import SecretMismatchException

logger = logging.getLogger(__name__)


class WebhookView(View):
    HEROKU_SECRET_HEADER_NAME = 'Heroku-Webhook-Hmac-SHA256'

    def dispatch(self, request, *args, **kwargs):
        heroku_secret = request.headers.get(self.HEROKU_SECRET_HEADER_NAME, '')

        try:
            if not heroku_secret:
                return HttpResponseUnauthorized(content=b'Secret token not provided.')

            config_id: UUID = kwargs.get('config_id')
            notification_config = NotificationConfig.objects.get(pk=config_id)
            self._check_heroku_secret(heroku_secret, request.body, notification_config)
        except NotificationConfig.DoesNotExist:
            return HttpResponseNotFound()
        except SecretMismatchException:
            return HttpResponseUnauthorized(content=b'Secret token mismatch.')

        return super().dispatch(request, notification_config, *args, **kwargs)

    def post(self, request: WSGIRequest, notification_config: NotificationConfig, **kwargs):
        self._handle_request(notification_config=notification_config, data=json.loads(request.body))
        return HttpResponseAccepted()

    def _handle_request(self, notification_config: NotificationConfig, data: dict):
        logger.debug(f'{notification_config}. Data: {data}')
        provider = ProviderRegistry.get_provider(notification_config.provider_name)
        provider.send_notification(notification_config, data)

    def _check_heroku_secret(self, given_secret: str, data: bytes, notification_config: NotificationConfig):
        calculated_secret = hmac.new(key=notification_config.secret.encode(), msg=data, digestmod=hashlib.sha256).digest()
        calculated_secret = base64.b64encode(calculated_secret).decode()
        if given_secret != calculated_secret:
            raise SecretMismatchException
