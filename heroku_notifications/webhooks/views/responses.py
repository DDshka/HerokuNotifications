from http import HTTPStatus

from django.http import HttpResponse


class HttpResponseAccepted(HttpResponse):
    status_code = HTTPStatus.ACCEPTED.value


class HttpResponseUnauthorized(HttpResponse):
    status_code = HTTPStatus.UNAUTHORIZED.value
