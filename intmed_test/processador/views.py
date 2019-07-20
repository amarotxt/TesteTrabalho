from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProcessadorSerializer
from .models import Processador
# Create your views here.

class Processador(viewsets.ModelViewset):
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer 
