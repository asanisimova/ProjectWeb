from django.template.defaultfilters import truncatewords
from django.db import models
from ProjectWeb.managers import ProductActiveManager, ProductManager


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категория товаров"


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default='default')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    # short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    # is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name="Активный товар?")

    objects = ProductManager()
    active = ProductActiveManager()

    def short_description(self):
        return truncatewords(self.description, 50)

    def __str__(self):
        return "%s, %s" %(self.price, self.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/media/products_images/")
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.id

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
