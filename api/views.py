from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from api.serializers import ShopSerializers, BlogSerializers, ContactSerializers, ServicesSerializers, UsersSerializers
from shop.models import Shop
from blog.models import Blog
from contact.models import Subscribe_to_Newsletter
from services.models import Services
from users.models import User


class ShopApiViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    pagination_class = LimitOffsetPagination


class BlogApiViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("first_name",)
    pagination_class = LimitOffsetPagination


class ContactApiViewSet(ModelViewSet):
    queryset = Subscribe_to_Newsletter.objects.all()
    serializer_class = ContactSerializers
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    pagination_class = LimitOffsetPagination


class ServicesApiViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("servise_name",)
    pagination_class = LimitOffsetPagination


class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializers
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("telegram_id",)
    pagination_class = LimitOffsetPagination

