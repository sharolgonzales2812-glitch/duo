"""urls.py — App recomendaciones · Prefijo: /api/recomendaciones/"""

from django.urls import path
from . import views

urlpatterns = [
    path('generar/', views.GenerarRecomendacionesView.as_view(), name='recomendaciones-generar'),
    path('rutina/',  views.RutinaView.as_view(),                 name='recomendaciones-rutina'),
]
