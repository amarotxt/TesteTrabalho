from .models import Processador
from rest_framework import serializers
from produto.serializers import ProdutoSerializer

class ProcessadorSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    class Meta:
        model = Processador
        fields = ('__all__')

    def create(self, validated_data):
        raise Exception(validated_data)
        
    # def update(isntance, validated_data):
    #     pass

