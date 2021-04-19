import requests
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class TestEndpoint(APIView):
    permission_classes = (IsAuthenticated)

    @api_view(['GET'])
    @renderer_classes((JSONRenderer,))
    def external_api_view(request):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)
        url = 'https://api.coinlore.net/api/exchange/?id=5'
        r = requests.get(url)
        data = r.json()
        return Response(data, status=status.HTTP_200_OK)