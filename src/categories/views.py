from django.shortcuts import render
from rest_framework_mongoengine import viewsets

from .serializers import CategoriesSerializer
from .models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()