from django.contrib import admin
from django.urls import path
from shop.views import ShopView


urlpatterns = [
    path('', ShopView.as_view())
]

