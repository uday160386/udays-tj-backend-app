from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Coin
from .serializers import CoinSerializer


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @api_view(['GET', 'POST', 'DELETE'])
    def coins_list(request):
        if request.method == 'GET':
            coins = Coin.objects.all()

            title = request.query_params.get('title', None)
            if title is not None:
                coins = coins.filter(title__icontains=title)

            coins_serializer = Coin(coins, many=True)
            return JsonResponse(coins_serializer.data, safe=False)
            # 'safe=False' for objects serialization

        elif request.method == 'POST':
            tutorial_data = JSONParser().parse(request)
            coins_serializer = CoinSerializer(data=tutorial_data)
            if coins_serializer.is_valid():
                coins_serializer.save()
                return JsonResponse(coins_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(coins_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            count = Coin.objects.all().delete()
            return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)

