from django.shortcuts import render
from rest_framework_mongoengine import viewsets

from .serializers import PartsSerializer
from .models import Parts

class PartsViewSet(viewsets.ModelViewSet):
    serializer_class = PartsSerializer
    queryset = Parts.objects.all()

    
