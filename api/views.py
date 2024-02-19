from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from logistics.models import Paquete, Transportista
from .serializers import PaqueteSerializer, TransportistaSerializer

@api_view(['POST'])
def asignar_paquete_a_transportista(request):
    if request.method == 'POST':
        paquete_id = request.data.get('paquete_id')
        transportista_id = request.data.get('transportista_id')

        try:
            paquete = Paquete.objects.get(pk=paquete_id)
            transportista = Transportista.objects.get(pk=transportista_id)
        except (Paquete.DoesNotExist, Transportista.DoesNotExist):
            return Response({'error': 'Paquete o transportista no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        paquete.transportista = transportista
        paquete.save()

        return Response({'message': 'Paquete asignado correctamente al transportista'}, status=status.HTTP_200_OK)

    else:
        return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def actualizar_estado_de_entrega(request, paquete_id):
    if request.method == 'PUT':
        try:
            paquete = Paquete.objects.get(pk=paquete_id)
        except Paquete.DoesNotExist:
            return Response({'error': 'Paquete no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        nuevo_estado = request.query_params.get('estado')

        if nuevo_estado is None:
            return Response({'error': 'Parámetro "estado" no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

        paquete.estado_entrega = nuevo_estado
        paquete.save()

        return Response({'message': 'Estado de entrega actualizado correctamente'}, status=status.HTTP_200_OK)

    else:
        return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
