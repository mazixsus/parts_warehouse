from rest_framework_mongoengine import serializers as mongoengine_serializers
from rest_framework import serializers

from .models import Category

class CategoriesSerializer(mongoengine_serializers.DocumentSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ['name', 'parent']

    

    # def create(self, validated_data):
    #     parent_name = validated_data.get('parent_name', None)
    #     parent_category = Category.objects.filter(name=parent_name).first
    #     print(parent_category)
    #     category = Category()
    #     category.name = validated_data.get('name')
    #     if parent_category:
    #         category.parent = parent_category.to_dbref()
    #     category.save()

        # category
        # print(parent_name)
        # if parent_name:
        #     parent_category = Category.objects.filter(name=parent_name).first()
        #     print(parent_category['name'])
            
        #     if parent_category:
        #         category = Category()
        #         category.name=validated_data.get('name'),
        #         category.parent_name=parent_category['name'],
        #         category.parents_tree=parent_category['parents_tree'],
        #         category.display_name=validated_data.get('display_name')
        #         category.save()

        #     else:
        #         raise serializers.ValidationError(f"Parent category '{parent_name}' not found.")
        # return category