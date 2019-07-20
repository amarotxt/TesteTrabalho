from .models import Processador
from rest_framework import serializers

class ProcessadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processador
        fields = ('__all__')


