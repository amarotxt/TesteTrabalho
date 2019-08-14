from .models import MemoriaRam
from rest_framework import serializers
from produto.serializers import ProdutoSerializer

class MemoriaRamSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    class Meta:
        model = MemoriaRam
        fields = ('__all__')
        # extra_kwargs = {
        #     'nome': {'allow_null': False, 'required': True},
        #     'tamanho': {'allow_null': False,'required': True,},     
        # }

        def create(self, validated_data):
            raise Exception(validated_data)


