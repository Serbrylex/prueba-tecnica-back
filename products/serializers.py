from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'pk', 'item_name', 'short_description', 'stock', 
            'price_without_tax', 'shipping_fee', 'image'
        )