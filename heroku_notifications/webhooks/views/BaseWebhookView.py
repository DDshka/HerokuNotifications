import base64
import hashlib
import hmac
import json
import logging

from http import HTTPStatus
from uuid import UUID

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from heroku_notifications.config.models import NotificationConfig
from .responses import HttpResponseUnauthorized, HttpResponseAccepted
from ..exceptions import SecretMismatchException

logger = logging.getLogger(__name__)


class BaseWebhookView(View):
    HEROKU_SECRET_HEADER_NAME = 'Heroku-Webhook-Hmac-SHA256'

    @csrf_exempt
    def dispatch(self, request, config_id: UUID, *args, **kwargs):
        heroku_secret = request.headers.get(self.HEROKU_SECRET_HEADER_NAME, '')

        try:
            if not heroku_secret:
                return HttpResponseUnauthorized(content=b'Secret token not provided.')

            notification_config = NotificationConfig.objects.get(pk=config_id)
            self._check_heroku_secret(heroku_secret, request.body, notification_config)
        except NotificationConfig.DoesNotExist:
            return HttpResponseNotFound()
        except SecretMismatchException:
            return HttpResponseUnauthorized(content=b'Secret token mismatch.')

        return super().dispatch(request, notification_config, *args, **kwargs)

    def post(self, request: WSGIRequest, notification_config: NotificationConfig, **kwargs):
        self._handle_request(notification_config=notification_config, data=json.loads(request.body))
        return HttpResponseAccepted(status=HTTPStatus.ACCEPTED.value)

    def _handle_request(self, notification_config: NotificationConfig, data: dict):
        logger.debug(f'{notification_config}. Data: {data}')

    def _check_heroku_secret(self, given_secret: str, data: bytes, notification_config: NotificationConfig):
        calculated_secret = hmac.new(key=notification_config.secret.encode(), msg=data, digestmod=hashlib.sha256).digest()
        calculated_secret = base64.b64encode(calculated_secret).decode()
        if given_secret != calculated_secret:
            raise SecretMismatchException
