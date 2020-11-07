from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views.generic.base import View

from heroku_notifications.config.models import NotificationConfig
from .. import exceptions


class BaseWebhookView(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: WSGIRequest, *args, **kwargs):
        self._handle_request(request, notification_config=self._get_notification_config(request))
        return HttpResponse(status=HTTPStatus.ACCEPTED.value)

    def _handle_request(self, request: WSGIRequest, notification_config: NotificationConfig):
        pass

    def _get_notification_config(self, request: WSGIRequest) -> NotificationConfig:
        secret = request.POST.get('secret')
        path = request.path

        if not secret:
            raise exceptions.SecretException

        try:
            return NotificationConfig.objects.get(webhook_url=path, secret=secret)
        except NotificationConfig.DoesNotExist:
            raise exceptions.SecretMismatchException
