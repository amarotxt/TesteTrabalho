from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlacaMaeSerializer
from .models import PlacaMae
# Create your views here.

class PlacaMaeViewSet(viewsets.ModelViewSet):
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer 

# Create your views here.
