from django.shortcuts import render
from django.views import View
from .models import OurTeam  #about orniga OurTeam yozdim ozgaruvchini oti bir xil bolishi uchun

class AboutView(View):
    def get(self, request):
        about = OurTeam.objects.all()
        context = {
            "about": about
        }
        return render(request, "about.html", context)

    def post(self, request):
        search = request.POST.get("search")
        about = OurTeam.objects.filter(name__icontains=search)
        context = {
            "about": about
        }
        return render(request, "shop.html", context)

