from django.contrib.auth.models import User
from django.test import TestCase
from placa_mae.factories import PlacaMaeFactory
from placa_video.factories import PlacaVideoFactory
from processador.factories import ProcessadorFactory
from memora_ram.factories import MemoriaRamFactory
from placa_mae.factories import PlacaMaeFactory

from placa_video.models import PlacaVideo
from processador.models import Processador
from memora_ram.models import MemoriaRam
from placa_mae.models import PlacaMae
import requests

# Create your tests here.
class PedidoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', email='test@test.com')
        self.cliente = self.client.force_login(self.user)
        self.placa_mae = PlacaMaeFactory().create_placa_mae()
        self.processador = Processador.objects.all() 
        self.memoria = MemoriaFactory().create_memoria_ram()
        self.placa_video = PlacaVideoFactory().create_memoria_ram()

    def test_create_pedido(self):
        data = {
            'placa_mae' : self.placa_mae.pk,
            'placa_video' : self.placa_videio.pk,
            'memoriaram' : [self.memoria.pk],
            'processador' : self.processador,
        }
        import ipdb; ipdb.set_trace()
        pass