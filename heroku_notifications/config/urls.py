from django.urls import path

from .views import ConfigView

urlpatterns = [
    path('', ConfigView.as_view()),
    path('uuid:config_id', ConfigView.as_view()),
]
