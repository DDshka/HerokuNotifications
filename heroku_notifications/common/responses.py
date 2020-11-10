from http import HTTPStatus

from django.http import HttpResponse


class HttpResponseOk(HttpResponse):
    status_code = HTTPStatus.OK.value


class HttpResponseAccepted(HttpResponse):
    status_code = HTTPStatus.ACCEPTED.value


class HttpResponseBadRequest(HttpResponse):
    status_code = HTTPStatus.BAD_REQUEST.value


class HttpResponseUnauthorized(HttpResponse):
    status_code = HTTPStatus.UNAUTHORIZED.value
