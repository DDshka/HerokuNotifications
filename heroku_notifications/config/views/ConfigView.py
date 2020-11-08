from django.core.handlers.wsgi import WSGIRequest
from django.views.generic.base import View


class ConfigView(View):
    def post(self, request: WSGIRequest):
        pass
