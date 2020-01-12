from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'created', 'is_active']


# class ProductListSerializer(serializers.ModelSerializer):
#     descript = serializers.SerializerMethodField()
#
#     def get_descript(self, product):
#         return product.short_description()
#
#     class Meta:
#         model = Product
#         fields = ['name', 'price', 'created', 'descript']
