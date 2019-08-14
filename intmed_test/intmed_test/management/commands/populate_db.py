from django.core.management.base import BaseCommand, CommandError
from memoria_ram.factories import MemoriaRamFactory
from processador.factories import ProcessadorFactory
from placa_mae.factories import PlacaMaeFactory
from placa_video.factories import PlacaVideoFactory

class Command(BaseCommand):
    help = 'Seeds the database.'
    def create_class(self):
        for i in range(2):
            ProcessadorFactory().create_processador()
            PlacaMaeFactory().create_placa_mae()
            PlacaVideoFactory().create_placa_videos()
            MemoriaRamFactory().create_placa_videos()
            

    def handle(self, *args, **options):
        self.create_class()