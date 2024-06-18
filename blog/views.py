from django.shortcuts import render
from django.views import View
from .models import Blog

class BlogView(View):
    def get(self, request):
        blog = Blog.objects.all()
        context  ={
            "blog": blog
        }
        return render(request, 'blog.html', context)

    def post(self, request):
        search = request.POST.get("search")
        blog = Blog.objects.filter(name__icontains=search)
        context = {
            "blog": blog
        }
        return render(request, "blog.html", context)