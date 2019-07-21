from .models import MemoriaRam
from rest_framework import serializers

class MemoriaRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoriaRam
        fields = ('__all__')



