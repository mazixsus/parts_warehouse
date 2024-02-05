from rest_framework_mongoengine import serializers as mongoserializers
from rest_framework import serializers

from .models import Parts
from categories.models import Category

class PartsSerializer(mongoserializers.DocumentSerializer):
    

    class Meta:
        model = Parts
        # fields = '__all__'
        exclude= ('category_reference', 'id')
        
    # serial_number = fields.StringField(required=True, reqmax_length=20, unique=True)
    # name = fields.StringField(required=True, max_length=20, unique=True)
    # description = fields.StringField(required=True, max_length=255)
    # category = fields.StringField(required=True)
    # category_reference = fields.ReferenceField(Category, required=True)
    # quantity = fields.IntField(required=True)
    # price= fields.DecimalField(required=True, decimal_places=2)
    # location_option

    # def create(self, validated_data):
    #     category_name = validated_data.get('category', None)
        
    #     if category_name:
    #         category = Category.objects.filter(name=category_name).first()
    #         print(category)
    #         if category:
    #             for field, value in vars(category).items():
    #                 print(f"{field}: {value}")
    #             validated_data['category_reference'] = category
    #         else:
    #             raise serializers.ValidationError(f"Category '{category_name}' not found.")
        
    #     part = Parts(**validated_data)
    #     part.save()
    #     return part