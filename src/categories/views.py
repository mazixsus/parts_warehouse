from django.shortcuts import render
from rest_framework_mongoengine import viewsets

from .serializers import CategoriesSerializer
from .models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    lookup_field = 'name'
    
    # queryset = Category.objects.all()
    def get_queryset(self):
        return Category.objects.all()