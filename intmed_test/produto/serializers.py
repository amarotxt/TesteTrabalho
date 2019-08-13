from .models import Produto
from rest_framework import serializers
from produto.serializers import ProdutoSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    class Meta:
        model = Produto
        fields = ('__all__')



