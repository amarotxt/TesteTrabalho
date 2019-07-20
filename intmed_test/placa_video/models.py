from django.db import models
from produto.models import Produto

# Create your models here.
class PlacaVideo(models.Model):
    produto = models.ForengKey(Produto)
    nome = models.CharFiled(max_length=30)