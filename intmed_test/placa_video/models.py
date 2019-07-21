from django.db import models
from produto.models import Produto

# Create your models here.
class PlacaVideo(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    nome = models.CharField(max_length=30)