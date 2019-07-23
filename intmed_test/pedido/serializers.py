from .models import Pedido
from rest_framework import serializers


def validar_memoria_ram(instance):
    pass

def validar_processador(instance):
    pass 

def validar_placa_mae(instance):
    pass

def validar_placa_video(instance):
    pass

class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(
    read_only=True, 
    default=serializers.CurrentUserDefault()
    ) 
    class Meta:
        model = Pedido
        fields = ('__all__')
  
    def validate(self, data):
         