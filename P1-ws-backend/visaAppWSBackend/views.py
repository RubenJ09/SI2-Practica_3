from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarjeta, Pago
from .serializers import PagoSerializer

class TarjetaView(APIView):
    def post(self, request):
        try:
            # El test envía todos los campos para validar
            Tarjeta.objects.get(
                numero=request.data.get('numero'),
                nombre=request.data.get('nombre'),
                fechaCaducidad=request.data.get('fechaCaducidad'),
                codigoAutorizacion=request.data.get('codigoAutorizacion')
            )
            return Response({'message': 'Datos encontrados en la base de datos'}, status=status.HTTP_200_OK)
        except Tarjeta.DoesNotExist:
            return Response({'message': 'Datos no encontrados en la base de datos'}, status=status.HTTP_404_NOT_FOUND)

class PagoView(APIView):
    def post(self, request):
        # El test envía 'tarjeta_id' en el JSON, pero el modelo usa 'tarjeta'
        data = request.data.copy()
        numero_tarjeta = data.pop('tarjeta_id', None)
        try:
            tarjeta = Tarjeta.objects.get(numero=numero_tarjeta)
            pago = Pago.objects.create(tarjeta=tarjeta, **data)
            serializer = PagoSerializer(pago)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tarjeta.DoesNotExist:
            return Response({"error": "Tarjeta no existe"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            pago = Pago.objects.get(pk=pk)
            pago.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pago.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ComercioView(APIView):
    def get(self, request, comercio_id):
        pagos = Pago.objects.filter(idComercio=comercio_id)
        serializer = PagoSerializer(pagos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
