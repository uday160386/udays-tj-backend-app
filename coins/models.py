from django.db import models


class Coin(models.Model):
    symbol = models.TextField(max_length=5)
    nameid = models.TextField(max_length=30)
    name = models.TextField(max_length=30)
    rank = models.TextField(max_length=5)
