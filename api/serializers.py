from rest_framework import serializers
from shop.models import Shop
from blog.models import Blog
from contact.models import Subscribe_to_Newsletter
from services.models import Services
from users.models import User

class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all"

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscribe_to_Newsletter
        fields = "__all"

class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all"

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all"


