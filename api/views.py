from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

# Create your views here.
from rest_framework.generics import get_object_or_404

from MyTinyUrl.settings import CONFIG
from api.models import TinyUrl
from api.serializers import UrlSerializer
from api.utils import redirect_to_url


@api_view(['POST'])
def create_tiny_url(request):
    """
        To shorten the url
    """
    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(f"{CONFIG.HOST}/{serializer.data.get('code')}", HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def redirect_from_tiny_url_code(request, code=None):
    """
        To shorten the url
    """
    if not code:
        return Response("Bad request", HTTP_400_BAD_REQUEST)

    tiny_url = get_object_or_404(TinyUrl, code=code)
    return redirect_to_url(str(tiny_url.url))
