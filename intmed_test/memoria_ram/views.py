from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .serializers import MemoriaRamSerializer
from .models import MemoriaRam
from produto.models import Produto
# Create your views here.

class MemoriaRamViewSet(viewsets.ModelViewSet):
    queryset = MemoriaRam.objects.all()
    serializer_class = MemoriaRamSerializer 

    def create(self, validated_data):
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            raise serializers.ValidationError()
        