from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .serializers import MemoriaRamSerializer
from .models import MemoriaRam
from produto.models import Produto

from rest_framework.response import Response
# Create your views here.

class MemoriaRamViewSet(viewsets.ModelViewSet):
    queryset = MemoriaRam.objects.all()
    serializer_class = MemoriaRamSerializer 

    # def create(self, request, *args, **kwargs):
    #     response = super(MemoriaRamViewSet, self).create(request, *args, **kwargs)
    #     if response.status == 201:
    #         produto = Produto.objects.create()
    #         memoria = Memoriaram.objects.get(response.data)
    #     return response