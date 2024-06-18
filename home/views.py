from django.shortcuts import render, redirect
from django.views import View
from shop.models import Shop
from django.contrib.auth import authenticate

class LandingView(View):
    def get(self, request):
        shop = Shop.objects.all()[:3]
        context = {
            "shop": shop
        }
        return render(request, "index.html", context)

