from django.contrib import admin
from .views import CardView
from django.urls import path

urlpatterns = [
    path('', CardView.as_view())
]
