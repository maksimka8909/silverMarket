from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    price = models.FloatField()
    image = models.CharField(max_length=1024)

class Bucket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)