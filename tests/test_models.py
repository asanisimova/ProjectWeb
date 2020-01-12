from  django.test import TestCase

from products.models import Product


class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(name='ТераФлю лесные ягоды пакетики 10 шт.', is_active=False, price=315.00)
        Product.objects.create(name='Шалфей таблетки для рассасывания 20 шт.', is_active=True, price=214.00)
        Product.objects.create(name='Шалфей таблетки для рассасывания 30 шт.', is_active=True, price=214.00)

    def test_active_filtering(self):
        product = Product.objects.get(name='ТераФлю лесные ягоды пакетики 10 шт.')
        self.assertEqual(product.is_active, False)
        products = Product.active.all()
        self.assertEqual(products.count(), 2)