from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import ViewSet

# Create your views here.
from  rest_framework.generics import CreateAPIView

from MyTinyUrl.settings import CONFIG
from api.serializers import UrlSerializer


@api_view(['POST'])
def create_tiny_url(request):
    """
        To shorten the url
    """
    serializer = UrlSerializer(data=request.data)
    print('czesc2123221121')
    if serializer.is_valid():
        serializer.save()
        return Response(f"{CONFIG.HOST}/{serializer.data.get('code')}", HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)