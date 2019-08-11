from .models import Produto
from model_mommy import mommy

class ProdutoFactory():
    def create_produto(self):
        produto = mommy.make(Produto)
        import ipdb; ipdb.set_trace()
        return produto

