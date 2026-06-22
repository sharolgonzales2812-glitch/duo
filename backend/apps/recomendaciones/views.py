"""views.py — App recomendaciones"""

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analisis.models import Diagnostico
from .models import Rutina
from .serializers import RutinaSerializer
from .services.motor_recomendaciones import MotorRecomendaciones


class GenerarRecomendacionesView(APIView):
    """
    POST /api/recomendaciones/generar/
    Body: { "diagnostico_id": <int> }
    Ejecuta el motor de recomendaciones y retorna el resultado.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        diagnostico_id = request.data.get('diagnostico_id')
        if not diagnostico_id:
            return Response(
                {'error': 'Se requiere diagnostico_id.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            diagnostico = Diagnostico.objects.get(pk=diagnostico_id, usuario=request.user)
        except Diagnostico.DoesNotExist:
            return Response(
                {'error': 'Diagnóstico no encontrado.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        perfil = getattr(request.user, 'perfil_piel', None)
        motor = MotorRecomendaciones(diagnostico, perfil)
        resultado = motor.generar()
        return Response(resultado, status=status.HTTP_200_OK)


class RutinaView(APIView):
    """
    GET  /api/recomendaciones/rutina/  → rutina activa del usuario
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rutina = Rutina.objects.filter(usuario=request.user, activa=True).first()
        if not rutina:
            return Response({'mensaje': 'No tienes una rutina activa.'}, status=status.HTTP_200_OK)
        return Response(RutinaSerializer(rutina).data)
