"""
urls.py — App analisis
Prefijo base: /api/analisis/
"""

from django.urls import path
from . import views

urlpatterns = [
    path('analizar/',          views.AnalizarFacialView.as_view(),      name='analisis-analizar'),
    path('historial/',         views.HistorialDiagnosticosView.as_view(), name='analisis-historial'),
    path('<int:pk>/',          views.DetalleDiagnosticoView.as_view(),  name='analisis-detalle'),
]
