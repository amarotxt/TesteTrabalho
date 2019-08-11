from rest_framework import viewsets
from .serializers import PedidoSerializer
from .models import Pedido
# Create your views here.

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer 

