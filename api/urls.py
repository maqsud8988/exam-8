from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ShopApiViewSet, BlogApiViewSet, ContactApiViewSet, ServicesApiViewSet, UserApiViewSet
from django.urls import path
from rest_framework.authtoken import views
router = DefaultRouter()
router.register("shop", viewset=ShopApiViewSet)
router.register("blog", viewset=BlogApiViewSet)
router.register("contact", viewset=ContactApiViewSet)
router.register("services", viewset=ServicesApiViewSet)
router.register("user", viewset=UserApiViewSet)




urlpatterns = [
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token),

]


