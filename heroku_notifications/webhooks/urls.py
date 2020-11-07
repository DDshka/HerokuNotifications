from django.urls import re_path

from .views import BaseWebhookView

urlpatterns = [
    re_path('^', BaseWebhookView.as_view()),
]
