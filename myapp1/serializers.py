from rest_framework import serializers

from .models import customer

class customerserializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    number = serializers.IntegerField()


