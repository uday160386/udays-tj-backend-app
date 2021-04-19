from rest_framework import serializers

from coins.models import Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('symbol', 'nameid', 'rank', 'name')
