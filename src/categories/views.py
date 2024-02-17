from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from rest_framework.exceptions import ValidationError

from .serializers import CategoriesSerializer
from .models import Category
from .filters import CategoriesFilterBackend
from parts.models import Parts

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    lookup_field = 'name'
    filter_backends = [CategoriesFilterBackend]
    
    def get_queryset(self):
        return Category.objects.all()
    
    def destroy(self, request, *args, **kwargs):

        if Category.objects.filter(parent=kwargs['name']):
            raise ValidationError('There are child categories assigned to the category. You cannot delete it.')
        
        if Parts.objects.filter(category=kwargs['name']):
            raise ValidationError('There are parts assigned to the category. You cannot delete it.')

        return super().destroy(request, *args, **kwargs)