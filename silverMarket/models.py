from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    price = models.FloatField()
    image = models.CharField(max_length=1024)