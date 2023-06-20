from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ViewSet

from api.models import TinyUrl
from api.serializers import UrlSerializer
from api.utils import redirect_to_url, generate_url_for_redirection


class TinyUrlViewSet(ViewSet):
    lookup_field = 'code'

    @action(methods=['post'], detail=False)
    def create_tiny_url(self, request):
        """
            To shorten the url
        """
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(generate_url_for_redirection(serializer.data.get('code', '')), HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def reverse(self, request, code=None):
        """
            To shorten the url
        """
        tiny_url = get_object_or_404(TinyUrl, code=code)
        return Response(tiny_url.url, HTTP_200_OK)


@api_view(['GET'])
def redirect(request, code=None):
        """
            Endpoint for redirecting when client type in browser shorten url like
        """
        if not code:
            return Response("Bad request", HTTP_400_BAD_REQUEST)

        tiny_url = get_object_or_404(TinyUrl, code=code)
        return redirect_to_url(str(tiny_url.url))
