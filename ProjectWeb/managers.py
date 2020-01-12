from django.db.models import Manager, QuerySet


class ProductQuerySet(QuerySet):
    def product_set(self):
        return self.all()


class ProductManager(Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class ProductActiveManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

