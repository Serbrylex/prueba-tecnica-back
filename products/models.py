from django.db import models

# Create your models here.


class Product(models.Model):
    item_name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    stock = models.IntegerField()
    price_without_tax = models.IntegerField()
    shipping_fee = models.IntegerField()
    image = models.CharField(max_length=500)