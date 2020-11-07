from django.urls import path

from .views import BaseWebhookView

urlpatterns = [
    path('<uuid:config_id>', BaseWebhookView.as_view()),
]
