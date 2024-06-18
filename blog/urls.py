from django.contrib import admin
from .views import BlogView
from django.urls import path

urlpatterns = [
    path('', BlogView.as_view())
]
