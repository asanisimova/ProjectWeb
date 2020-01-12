from django.urls import path, include
from django.contrib import admin
from landing import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', views.home, name='Главная'),
    path('landing123/', views.landing, name='landing'),
    path('contact/', views.contact, name='contact'),
    path('', include(router.urls))
]