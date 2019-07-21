from rest_framework import viewsets
from .serializers import PlacaVideoSerializer
from .models import PlacaVideo
# Create your views here.

class PlacaVideo(viewsets.ModelViewSet):
    queryset = PlacaVideo.objects.all()
    serializer_class = PlacaVideoSerializer 
