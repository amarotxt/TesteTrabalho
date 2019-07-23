from django.db import models

# Create your models here.
class Produto(models.Model):
    fornecedor = models.CharField(max_length=30)
    preco = models.FloatField()
    #TODO: Variáveis para produtos ex: preço, ...