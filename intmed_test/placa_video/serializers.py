from .models import PlacaVideo
from rest_framework import serializers
# from produto.serializers import ProdutoSerializer

class PlacaVideoSerializer(serializers.ModelSerializer):
    # produto = ProdutoSerializer()
    class Meta:
        model = PlacaVideo
        fields = ('__all__')
