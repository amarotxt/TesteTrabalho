from django.db import models
from produto.models import Produto
# Create your models here.
class Processador(models.Model):
    nome = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    produto = models.ForeingKey(Produto)