import json
from uuid import UUID

from django.core.handlers.wsgi import WSGIRequest
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.base import View
from pydantic import ValidationError

from heroku_notifications.common.responses import HttpResponseBadRequest, HttpResponseAccepted
from ..dtos import ConfigDto
from ..services import NotificationConfigService


class ConfigView(View):
    SECRET_HEADER_NAME = 'Secret'

    def post(self, request: WSGIRequest):
        data = json.loads(request.body)

        try:
            config_dto = ConfigDto(**data)
        except ValidationError as e:
            return HttpResponseBadRequest(content=e.json())

        configs = NotificationConfigService.create(config_dto)
        return HttpResponseAccepted(content=json.dumps(configs, cls=DjangoJSONEncoder))

    def put(self, request: WSGIRequest, config_id: UUID):
        secret = request.headers.get(self.SECRET_HEADER_NAME)
        try:
            NotificationConfigService.update(config_id, secret, {})
        except NotificationConfigService.NotFoundException:
            return HttpResponseBadRequest(
                content='Configuration with provided ID does not exist '
                        'or you have provided wrong secret.'
            )

    def delete(self, request: WSGIRequest, config_id: UUID):
        secret = request.headers.get(self.SECRET_HEADER_NAME)
        try:
            NotificationConfigService.delete(config_id, secret)
        except NotificationConfigService.NotFoundException:
            return HttpResponseBadRequest(
                content='Configuration with provided ID does not exist '
                        'or you have provided wrong secret.'
            )
