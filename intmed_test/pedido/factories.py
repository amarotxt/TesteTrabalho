import random
from .models import Pedido 
# from processador.factories import ProcessadorFactory
 
from model_mommy import mommy

class PlacaMaeFactory():
    def create_placa_mae(self):
        placa_mae = mommy.make(
            Pedido
            )
        return placa_mae
