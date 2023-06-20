from rest_framework.serializers import ModelSerializer

from api.models import TinyUrl


class UrlSerializer(ModelSerializer):
    class Meta:
        model = TinyUrl
        fields = ("code", "url")
