from .models import PlacaMae
from rest_framework import serializers
from memoria_ram.models import MemoriaRam

class PlacaMaeSerializer(serializers.ModelSerializer):
    memoria_ram = serializers.PrimaryKeyRelatedField(queryset=MemoriaRam.objects.all() ,many=True)
    class Meta:
        model = PlacaMae
        fields = ('__all__')
