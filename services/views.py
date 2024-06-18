from django.shortcuts import render
from django.views import View
from .models import Services


class ServicesView(View):
    def get(self, request):
        services = Services.objects.all()
        context = {
            "services": services
        }
        return render(request, "services.html", context)

    def post(self, request):
        search = request.POST.get("search")
        services = Services.objects.filter(name__icontains=search)
        context = {
            "services": services
        }
        return render(request, "services.html", context)

