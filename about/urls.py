from django.contrib import admin
from .views import AboutView
from django.urls import path

urlpatterns = [

    path("", AboutView.as_view(), name="about"),
]