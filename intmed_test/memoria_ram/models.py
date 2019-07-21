from django.db import models
from produto.models import Produto

# Create your models here.

class MemoriaRam(models.Model):
    nome = models.CharField(max_length=30)
    tamanho = models.PositiveSmallIntegerField()
    produto = models.ForeingKey(Produto, on_delete=models.CASCADE)