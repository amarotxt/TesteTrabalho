import random
from .models import Processador 
from produto.factories import ProdutoFactory
from model_mommy import mommy

class ProcessadorFactory():
    def create_processador(self):
        choice_ram = ['Intel', 'AMD']
        processador = mommy.make(
            Processador,
            marca=random.choices(choice_ram),
            produto=ProdutoFactory().create_produto()
             )
            
        
        return processador

    def list_processadores(self):
        mommy.make(
            Processador,
            marca='Intel',
            produto=ProdutoFactory().create_produto()
        )
        mommy.make(
            Processador,
            marca='AMD',
            produto=ProdutoFactory().create_produto()
        )            
        processador = Processador.objects.all()
        
        return processador