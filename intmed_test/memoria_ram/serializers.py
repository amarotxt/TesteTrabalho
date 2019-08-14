from .models import MemoriaRam
from rest_framework import serializers
from produto.serializers import ProdutoSerializer

class MemoriaRamSerializer(serializers.ModelSerializer):
    produto =  serializers.PrimaryKeyRelatedField(null=True, allow_null=True)
    class Meta:
        model = MemoriaRam
        fields = ('tamanho','nome')
        # extra_kwargs = {
        #     'nome': {'allow_null': False, 'required': True},
        #     'tamanho': {'allow_null': False,'required': True,},     
        # }

        # def create(self, validated_data):
        #     raise Exception(validated_data)


