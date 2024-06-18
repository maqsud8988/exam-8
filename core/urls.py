from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('auth/', include('users.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
    path('services/', include('services.urls')),
    path('shop/', include('shop.urls')),
    path('about/', include('about.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)