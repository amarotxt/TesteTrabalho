from django.db import models
from produto.models import Produto

# Create your models here.
class PlacaVideo(models.Model):
    produto = models.ForeingKey(Produto)
    nome = models.CharField(max_length=30)