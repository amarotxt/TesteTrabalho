from django.db import models
from produto.models import Produto

# Create your models here.
class PlacaMae(models.Model):
    nome = models.CharField(max_length=30)
    produto = models.ForengKey(Produto, on_delete=models.PROTECT)
    processador = models.ForengKey(Processador)
    qtd_memoria = models.PositiveSmallIntegerField()
    qtd_ram = models.PositiveSmallIntegerField()
    video_integrado = models.BooleanField()
    #TODO: Variáveis para produtos ex: preço, ...

