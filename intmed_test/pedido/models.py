from django.db import models
from placa_mae.models import PlacaMae
from placa_video.models import PlacaVideo
from processador.models import Processador
from memoria_ram import MemoriaRam
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    placa_mae = models.ForeingKey(PlacaMae, on_delete=models.PROTECT) 
    placa_video = models.ForeingKey(PlacaVideo, on_delete=models.PROTECT) 
    processador = models.ForeingKey(Processador, on_delete=models.PROTECT) 
    memoria_ram = models.ManyToManyField(MemoriaRam, on_delete=models.PROTECT) 
    cliente = models.ForeingKey(User, on_delete=models.PROTECT)
