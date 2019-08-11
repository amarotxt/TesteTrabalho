from .models import Pedido
from memoria_ram.models import MemoriaRam
from processador.models import Processador
from placa_mae.models import PlacaMae
from placa_video.models import PlacaVideos
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# def validar_processador(instance):
#     processador = Processador.objects.filter(id=instance.processado.id).first()
#     placa_mae = PlacaMae.objects.filter(processador=instace.placa_mae.id).first()
#     if processador is not None and placa_mae is not None:
#         placa_mae_processadores_list = placa_mae.processador.all()
#         for p in placa_mae_processador_lis:
#             if p == processador:
#                 return True
#     return ValidationError({'detail': 'Processador Não é compativel com esta Placa Mãe'})


def validar_memoria_ram(instance):
    memorias_rams = instance.memoria_ram    
    placa_mae = PlacaMae.objects.filter(processador=instace.placa_mae.id).first()
    if memoria_ram is not None  and placa_mae is not None:
        count_memoria_ram = memorias_rams.count()
        qtd_memoria_ram = 0
        for m in memorias_rams:
            qtd_memoria_ram += m.tamanho
        if placa_mae.qtd_memoria_ram_slots >= count_memoria_ram and qtd_memoria_ram_total > qtd_memoria_ram :
            return True

    raise ValidationError({'detail': 'Memoria ram não é compativel com esta Placa Mãe'})


def validar_placa_mae(instance):
    processador = Processador.objects.filter(id=instance.processado.id).first()
    placa_mae = PlacaMae.objects.filter(processador=instace.placa_mae.id).first()
    if processador is not None and placa_mae is not None:
        placa_mae_processadores_list = placa_mae.processador.all()
        if processador in placa_mae_processadores_list:
            return True
        # for p in placa_mae_processador_lis:
        #     if p == processador:
        #         return True
    raise ValidationError({'detail': f'Placa mãe não é compativel com este Processador:{processador.nome}'})


def validar_placa_video(instance):
    placa_mae = PlacaMae.objects.filter(processador=instace.placa_mae.id).first()
    placa_videos = PlacaVideo.objects.filter(processador=instace.placa_video.id).first()
    if placa_mae is not None:
        if not placa_mae.video_integrado:
            if placa_video is not None:
                return True
            else:
                raise ValidationError({'detail': f'Placa de video não foi adicionada'})

            if 
            return True    
    

class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(
    read_only=True, 
    default=serializers.CurrentUserDefault()
    ) 
    class Meta:
        model = Pedido
        fields = ('__all__')
  
    def validate(self, data):
        if validar_placa_mae(data):

        if validar_processador(data):
             
        if validar_placa_video(data):

