import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from landing.serializers import ProductSerializer

from products.models import Product

client = Client()


class GetAllProductsTest(TestCase):
    def setUp(self):
        Product.objects.create(name='ТераФлю лесные ягоды пакетики 10 шт.', price=200, description='ТераФлю лесные ягоды пакетики 10 шт.', is_active=True)
        Product.objects.create(name='ТераФлю лесные ягоды пакетики 20 шт.', price=200, description='ТераФлю лесные ягоды пакетики 20 шт.', is_active=True)
        Product.objects.create(name='ТераФлю лесные ягоды пакетики 30 шт.', price=200, description='ТераФлю лесные ягоды пакетики 30 шт.', is_active=False)

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('product-list'))
        # get data from db
        products = Product.active.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GetSingleProductTest(TestCase):
#     def setUp(self):
#         self.product = Product.objects.create(name='ТераФлю лесные ягоды пакетики 10 шт.', price=200)
#
#     def test_get_valid_single_product(self):
#         response = client.get(
#             reverse('product-detail', kwargs={'pk': self.product.pk}))
#         product = Product.objects.get(pk=self.product.pk)
#         serializer = ProductListSerializer(product)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_invalid_single_product(self):
#         response = client.get(reverse('post-detail', kwargs={'pk': 9999}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPostTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'ТераФлю лесные ягоды пакетики 20 шт.', 'price': 200, 'is_active': True,
        }
        self.invalid_payload = {
             'name': '', 'price': 200, 'is_active': True,
        }

    def test_create_valid_single_post(self):
        response = client.post(reverse('product-list'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_post(self):
        response = client.post(reverse('product-list'),
                               data=json.dumps(self.invalid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProductInBasketTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='ТераФлю лесные ягоды пакетики 10 шт.', price=200, is_active=True)
        self.valid_payload = {
            'name': 'ТераФлю лесные ягоды пакетики 20 шт.', 'price': 200, 'is_active': True,
        }
        self.invalid_payload = {
            'name': '', 'price': 200,  'is_active': True,
        }

    def test_valid_update_ProductInBasket(self):
        response = client.put(reverse('product-detail',
                                      kwargs={'pk': self.product.pk}),
                              data=json.dumps(self.valid_payload),
                              content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_ProductInBasket(self):
        response = client.put(reverse('product-detail',
                                      kwargs={'pk': self.product.pk}),
                              data=json.dumps(self.invalid_payload),
                              content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='ТераФлю лесные ягоды пакетики 10 шт.', price=200, is_active=True)

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('product-detail', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(reverse('product-detail', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

