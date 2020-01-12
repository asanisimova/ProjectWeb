from django.shortcuts import render
from .forms import SubscriberForm
from products.models import*
from rest_framework import viewsets
from .serializers import ProductSerializer


def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_new = products_images.filter(product__category=1)
    return render(request, 'landing/home.html', locals())


def contact(request):

    return render(request, 'landing/contact.html', locals())


# class ProductViewSet(viewsets.ModelViewSet):
# #     """
# #     API endpoint that allows users to be viewed or edited.
# #     """
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
# #
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(category__is_active=True)