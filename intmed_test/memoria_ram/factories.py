import random
from .models import MemoriaRam
from produto.factories import ProdutoFactory
 
from model_mommy import mommy

class MemoriaRamFactory():
    def create_memoria_ram(self):
        memoria_ram = mommy.make(
            MemoriaRam,
            tamanho=random.choices([16,64])[0],
            produto=ProdutoFactory().create_produto()
            
             )
        return memoria_ram