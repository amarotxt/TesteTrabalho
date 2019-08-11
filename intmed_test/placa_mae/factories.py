import random
from .models import PlacaMae 
from produto.factories import ProdutoFactory
from processador.factories import ProcessadorFactory
 
from model_mommy import mommy

class PlacaMaeFactory():
    def create_placa_mae(self):
        placa_mae = mommy.make(
            PlacaMae,
            processador=ProcessadorFactory.create_processador(),
            qtd_memoria_slots=random.coices([2,4]),
            qtd_memoria_total=random.coices([16,64]),
            produto=ProdutoFactory.create_produto()
             )
        return placa_mae