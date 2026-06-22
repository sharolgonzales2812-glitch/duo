"""
views.py — App analisis
Vista principal: AnalizarFacialView
"""

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Diagnostico
from .serializers import DiagnosticoSerializer, ImagenFacialSerializer
from .services.vision_service import VisionService
from .services.metricas_service import MetricasService


class AnalizarFacialView(APIView):
    """
    POST /api/analisis/analizar/
    Recibe imagen facial, ejecuta el análisis con IA y retorna el diagnóstico.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ImagenFacialSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Guardar imagen en disco
        diagnostico = Diagnostico(
            usuario=request.user,
            imagen_original=serializer.validated_data['imagen_original'],
        )
        diagnostico.save()

        # Ejecutar análisis de visión artificial
        servicio_vision = VisionService()
        resultados = servicio_vision.analizar(diagnostico.imagen_original.path)

        # Actualizar diagnóstico con resultados
        for campo, valor in resultados.items():
            if campo != 'tiempo_procesamiento_ms' and valor is not None:
                setattr(diagnostico, campo, valor)
        diagnostico.tiempo_procesamiento_ms = resultados.get('tiempo_procesamiento_ms', 0)
        diagnostico.save()

        # Extraer y guardar métricas
        MetricasService(diagnostico).extraer_y_guardar(resultados)

        return Response(
            DiagnosticoSerializer(diagnostico).data,
            status=status.HTTP_201_CREATED,
        )


class HistorialDiagnosticosView(APIView):
    """
    GET /api/analisis/historial/
    Retorna todos los diagnósticos del usuario autenticado.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        diagnosticos = Diagnostico.objects.filter(
            usuario=request.user
        ).prefetch_related('metricas')
        serializer = DiagnosticoSerializer(diagnosticos, many=True)
        return Response(serializer.data)


class DetalleDiagnosticoView(APIView):
    """
    GET /api/analisis/<pk>/
    Retorna el detalle de un diagnóstico específico del usuario.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            diagnostico = Diagnostico.objects.prefetch_related('metricas').get(
                pk=pk, usuario=request.user
            )
        except Diagnostico.DoesNotExist:
            return Response(
                {'error': 'Diagnóstico no encontrado.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(DiagnosticoSerializer(diagnostico).data)
