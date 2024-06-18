from rest_framework import serializers
from about.models import Service

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
