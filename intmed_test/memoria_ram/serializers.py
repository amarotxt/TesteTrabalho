from memoria_ram.models import MemoriaRam
from rest_framework import serializers

class MemoriaRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoriaRam
        fields = ('__all__')



