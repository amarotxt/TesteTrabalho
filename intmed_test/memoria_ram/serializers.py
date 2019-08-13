from .models import MemoriaRam
from rest_framework import serializers
from produto.serializers import ProdutoSerializer

class MemoriaRamSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    class Meta:
        model = MemoriaRam
        fields = ('nome', 'tamanho', 'produto')
        # extra_kwargs = {
        #     'nome': {'allow_null': False, 'required': True},
        #     'tamanho': {'allow_null': False,'required': True,},     
        # }
    
  



