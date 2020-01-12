from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price',  'is_active']

    def get_descript(self, product):
        return product.short_description()

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'is_active']
