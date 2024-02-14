from django.shortcuts import render
from rest_framework_mongoengine import viewsets

from .serializers import CategoriesSerializer
from .models import Category
from .filters import CategoriesFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    lookup_field = 'name'
    filter_backends = [CategoriesFilterBackend]
    
    def get_queryset(self):
        return Category.objects.all()