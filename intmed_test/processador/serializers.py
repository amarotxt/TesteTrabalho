from .models import Processador
from rest_framework import serializers
# from produto.serializers import ProdutoSerializer

class ProcessadorSerializer(serializers.ModelSerializer):
    # produto = ProdutoSerializer()
    class Meta:
        model = Processador
        fields = ('nome', 'tamanho')


