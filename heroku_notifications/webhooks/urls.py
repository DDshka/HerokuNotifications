from django.urls import path

from .views import WebhookView

urlpatterns = [
    path('<uuid:config_id>', WebhookView.as_view()),
]
