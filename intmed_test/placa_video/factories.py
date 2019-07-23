import random
from .models import PlacaVideo 
from produto.factories import ProdutoFactory
from model_mommy import mommy

class PlacaVideoFactory():
    def create_placa_video(self):
        placa_video = mommy.make(
            PlacaVideo,
            produto=ProdutoFactory.create_produto()
             )
        return placa_video