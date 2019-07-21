from rest_framework import routers
from produto.views import ProdutoViewSet
from memoria_ram.views import MemoriaRamViewSet
from produto.views import PlacaMaeViewSet
from produto.views import PlacaVideoViewSet
from produto.views import ProcessadorViewSet

router = routers.DefaultRouter()
router.register('memoriaram',MemoriaRamViewSet, base_name='memoriaram')
router.register('produto',ProdutoViewSet, base_name='produto')
router.register('placa_mae',ProdutoViewSet, base_name='placa_mae')
router.register('placa_video',ProdutoViewSet, base_name='placa_video')
router.register('processador',ProdutoViewSet, base_name='processador')
