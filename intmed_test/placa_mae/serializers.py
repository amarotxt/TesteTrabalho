from .models import PlacaMae
from rest_framework import serializers
from Processador.models import Processador

class PlacaMaeSerializer(serializers.ModelSerializer):
    processador = serializers.PrimaryKeyRelatedField(queryset=Processador.objects.all() ,many=True)
    class Meta:
        model = PlacaMae
        fields = ('__all__')
