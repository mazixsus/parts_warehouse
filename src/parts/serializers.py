from rest_framework_mongoengine import serializers as mongoserializers
from rest_framework import serializers

from .models import Parts
from categories.models import Category

class PartsSerializer(mongoserializers.DocumentSerializer):
    serial_number = serializers.CharField(required=True)
    class Meta:
        model = Parts
        fields = ['serial_number', 'name', 'description', 'category', 'quantity', 'price', 'location_option']
