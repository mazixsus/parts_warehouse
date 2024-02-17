from rest_framework_mongoengine import serializers as mongoengine_serializers
from rest_framework import serializers
from rest_framework_mongoengine.validators import UniqueValidator

from .models import Category

class CategoriesSerializer(mongoengine_serializers.DocumentSerializer):
    name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Category.objects.all())])

    class Meta:
        model = Category
        fields = ['name', 'parent']