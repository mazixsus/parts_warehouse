from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from rest_framework import filters


from .serializers import CategoriesSerializer
from .models import Category


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        print(request)
        name = request.query_params.get('name')
        parent = request.query_params.get('parent')

        if name:
            queryset = queryset.filter(name=name)

        if parent:
            queryset = queryset.filter(parent=parent)

        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    lookup_field = 'name'
    filter_backends = [IsOwnerFilterBackend]
    
    def get_queryset(self):
        return Category.objects.all()