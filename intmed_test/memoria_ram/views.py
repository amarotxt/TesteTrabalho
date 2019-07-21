from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemoriaRamSerializer
from .models import MemoriaRam
# Create your views here.

class MemoriaRamViewSet(viewsets.ModelViewSet):
    queryset = MemoriaRam.objects.all()
    serializer_class = MemoriaRamSerializer 

