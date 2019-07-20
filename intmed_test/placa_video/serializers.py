from .models import PlacaVideo
from rest_framework import serializers

class PlacaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaVideo
        fields = ('__all__')
