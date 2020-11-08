from http import HTTPStatus

from django.http import HttpResponse
from django.views.generic.base import View
from pydantic import ValidationError

from heroku_notifications.config.dtos import ConfigDto


class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=HTTPStatus.OK.value, content=b'Pong!')
