from django.shortcuts import render
from contact.forms import GetInTouchForm
from django.views import View


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, "contact.html")
