from django.shortcuts import render
from django.views import View
from .models import Shop

class ShopView(View):
    def get(self, request):
        shop = Shop.objects.all()
        context = {
            "shop": shop
        }
        return render(request, "shop.html", context)

    def post(self, request):
        search = request.POST.get("search")
        shop = Shop.objects.filter(name__icontains=search)
        context = {
            "shop": shop
        }
        return render(request, "shop.html", context)

