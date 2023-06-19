from django.urls import path, re_path

from api.views import create_tiny_url, redirect_from_tiny_url_code

urlpatterns = [
    path("shorten_url", create_tiny_url),
    re_path(r"(?P<code>[a-z0-9]*)", redirect_from_tiny_url_code),
]