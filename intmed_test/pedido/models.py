from django.db import models
from placa_mae.models import PlacaMae
from placa_video.models import PlacaVideo
from processador.models import Processador
from memoria_ram.models import MemoriaRam
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    placa_mae = models.ForeignKey(PlacaMae, on_delete=models.PROTECT) 
    placa_video = models.ForeignKey(PlacaVideo, on_delete=models.PROTECT) 
    processador = models.ForeignKey(Processador, on_delete=models.PROTECT) 
    memoria_ram = models.ManyToManyField(MemoriaRam, on_delete=models.PROTECT) 
    cliente = models.ForeignKey(User, on_delete=models.PROTECT)
