from .models import MemoriaRam
from rest_framework import serializers
from produto import Produto
class MemoriaRamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MemoriaRam
        fields = ('nome', 'tamanho')
        extra_kwargs = {
            'nome': {'allow_null': False, 'required': True},
            'tamanho': {'allow_null': False,'required': True,},     
        }




