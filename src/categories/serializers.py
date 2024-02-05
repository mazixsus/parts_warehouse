from rest_framework_mongoengine import serializers as mongoengine_serializers
from rest_framework import serializers

from .models import Category

class CategoriesSerializer(mongoengine_serializers.DocumentSerializer):
    class Meta:
        model = Category
        fields = ('name', 'parent_name')
    
    # def create(self, validated_data):
    #     parent_name = validated_data.get('parent_name', None)

    #     if parent_name:
    #         parent_category = Category.objects.filter(name=parent_name).first()
    #         print(parent_category)
            
    #         if parent_category:
    #             validated_data['parent'] = parent_category
    #         else:
    #             raise serializers.ValidationError(f"Parent category '{parent_name}' not found.")
        
    #     category = Category(**validated_data)
    #     category.save()
    #     return category