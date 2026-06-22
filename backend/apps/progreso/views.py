"""views.py — App progreso"""

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RegistroProgreso
from .serializers import RegistroProgresoSerializer


class RegistroProgresoListView(APIView):
    """
    GET  /api/progreso/          → historial completo del usuario
    POST /api/progreso/          → agrega nuevo registro de progreso
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        registros = RegistroProgreso.objects.filter(usuario=request.user)
        serializer = RegistroProgresoSerializer(registros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistroProgresoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistroProgresoDetailView(APIView):
    """GET /api/progreso/<pk>/ — Detalle de un registro."""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            registro = RegistroProgreso.objects.get(pk=pk, usuario=request.user)
        except RegistroProgreso.DoesNotExist:
            return Response(
                {'error': 'Registro no encontrado.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(RegistroProgresoSerializer(registro).data)
