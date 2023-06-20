from django.urls import re_path

from api.views import redirect

urlpatterns = [
    re_path(r"^(?P<code>[a-z0-9]{5})/$", redirect, name="redirection"),
]
