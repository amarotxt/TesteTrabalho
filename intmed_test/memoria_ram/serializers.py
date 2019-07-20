from .models import MomoriaRam
from rest_framework import serializers

class MomoriaRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomoriaRam
        fields = ('__all__')



