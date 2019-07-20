from rest_framework import routers
from produto.views import ProdutoViewSet
from memoria_ram.views import MemoriaRamViewSet
from produto.views import PlacaMaeViewSet
from produto.views import PlacaVideoViewSet
from produto.views import ProcessadorViewSet

router = routers.DefaultRouter()
router.register('produto',ProdutoViewSet, base_name='produto')
