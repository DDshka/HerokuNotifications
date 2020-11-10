from http import HTTPStatus

from django.http import HttpResponse
from django.views.generic.base import View


class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=HTTPStatus.OK.value, content=b'Pong!')
