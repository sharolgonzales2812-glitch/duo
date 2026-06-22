"""views.py — App productos"""

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Producto, Tratamiento
from .serializers import ProductoSerializer, TratamientoSerializer


class ProductoListView(ListAPIView):
    """GET /api/productos/ — Lista de productos activos con filtro opcional por tipo_piel."""
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Producto.objects.filter(activo=True).prefetch_related('ingredientes')
        tipo_piel = self.request.query_params.get('tipo_piel')
        if tipo_piel:
            qs = qs.filter(tipo_piel_objetivo__in=[tipo_piel, 'todos'])
        return qs


class ProductoDetailView(RetrieveAPIView):
    """GET /api/productos/<pk>/ — Detalle de un producto."""
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Producto.objects.filter(activo=True).prefetch_related('ingredientes')


class TratamientoListView(ListAPIView):
    """GET /api/productos/tratamientos/ — Lista de tratamientos activos."""
    serializer_class = TratamientoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Tratamiento.objects.filter(activo=True)
