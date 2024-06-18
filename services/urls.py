from django.contrib import admin
from .views import ServicesView
from django.urls import path

urlpatterns = [
    path('', ServicesView.as_view())
]
