from django.contrib.auth.models import User
from django.test import TestCase
from placa_mae.factories import PlacaMaeFactory
from placa_video.factories import PlacaVideoFactory
from processador.factories import ProcessadorFactory
from memoria_ram.factories import MemoriaRamFactory
from placa_mae.factories import PlacaMaeFactory
from django.urls import reverse
from django.urls import reverse_lazy
from placa_video.models import PlacaVideo
from processador.models import Processador
from memoria_ram.models import MemoriaRam
from placa_mae.models import PlacaMae
import requests

# Create your tests here.
class PedidoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', email='test@test.com')
        self.cliente = self.client.force_login(self.user)
        self.placa_mae = PlacaMaeFactory().create_placa_mae()
        self.processador = Processador.objects.all().first()
        self.memoria = MemoriaRamFactory().create_memoria_ram()
        self.placa_video = PlacaVideoFactory().create_placa_video()

    def test_create_pedido(self):
        data = { 
            'placa_mae' : self.placa_mae.pk, 
            'placa_video' : self.placa_video.pk, 
            'memoria_ram' : [self.memoria.pk], 
            'processador' : self.processador.first().pk, 
        }
        resposta = requests.post(reverse_lazy('pedido-list'), data=data)
        
        import ipdb; ipdb.set_trace()
        pass