from django.shortcuts import render
from rest_framework_mongoengine import viewsets

from .filters import PartsFilterBackend
from .serializers import PartsSerializer
from .models import Parts

class PartsViewSet(viewsets.ModelViewSet):
    serializer_class = PartsSerializer
    queryset = Parts.objects.all()
    filter_backends = [PartsFilterBackend]

    def get_queryset(self):
        return Parts.objects.all()

    
