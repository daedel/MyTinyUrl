from django.urls import path

from api.views import create_tiny_url

urlpatterns = [
    path("shorten_url", create_tiny_url),
]