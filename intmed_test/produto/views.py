from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProdutoSerializer
from .models import Produto
# Create your views here.

class Produto(viewsets.ModelViewset):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer 
