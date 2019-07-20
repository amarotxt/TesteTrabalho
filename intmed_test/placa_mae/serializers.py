from .models import PlacaMae
from rest_framework import serializers

class PlacaMaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaMae
        fields = ('__all__')
