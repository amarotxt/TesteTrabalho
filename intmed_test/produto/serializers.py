from .models import Produto
from rest_framework import serializers
from pedido.serializer import PedidoSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('__all__')



