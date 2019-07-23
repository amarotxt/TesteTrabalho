from .models import Produto
from model_mommy import mommy

class ProdutoFactory():
    def create_produto(self):
        produto = mommy.make(Produto)
        return produto

