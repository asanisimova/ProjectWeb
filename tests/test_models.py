from django.contrib.auth import get_user_model
from  django.test import TestCase

from products.models import Product


User = get_user_model()


class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(name='ТераФлю лесные ягоды пакетики 10 шт.', price=315.00)
        Product.objects.create(name='Шалфей таблетки для рассасывания 20 шт.', price=214.00)

    def test_product_filtering(self):
        product = Product.objects.filter(price=315.00)
        print(product.count())
        self.assertEqual(product.count(), 1)