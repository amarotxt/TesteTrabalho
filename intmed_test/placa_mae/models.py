from django.db import models
from produto.models import Produto
from processador.models import Processador
# Create your models here.
class PlacaMae(models.Model):
    nome = models.CharField(max_length=30)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    processador = models.ManyToManyField(Processador, on_delete=models.PROTECT)
    qtd_memoria_ram_slots = models.PositiveSmallIntegerField()
    qtd_memoria_ram_total = models.PositiveSmallIntegerField()
    video_integrado = models.BooleanField()
    #TODO: Variáveis para produtos ex: preço, ...

