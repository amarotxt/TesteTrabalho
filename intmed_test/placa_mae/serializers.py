from .models import PlacaMae
from rest_framework import serializers
from processador.models import Processador
# from produto.serializers import ProdutoSerializer

class PlacaMaeSerializer(serializers.ModelSerializer):
    processador = serializers.PrimaryKeyRelatedField(queryset=Processador.objects.all() ,many=True)
    # produto = ProdutoSerializer()

    class Meta:
        model = PlacaMae
        fields = ('__all__')
