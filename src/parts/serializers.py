from rest_framework_mongoengine import serializers as mongoserializers
from rest_framework import serializers
from rest_framework_mongoengine.validators import UniqueValidator

from .models import Parts
from categories.models import Category

class PartsSerializer(mongoserializers.DocumentSerializer):
    serial_number = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Parts.objects.all())])
    class Meta:
        model = Parts
        fields = ['serial_number', 'name', 'description', 'category', 'quantity', 'price', 'location_option']

    def validate_category(self, value):
        category = Category.objects.filter(name=value.id).first()

        if category.parent is None:
            raise serializers.ValidationError("Part cannot be assigned to base category.") 
        else:
            return value