"""urls.py — App progreso · Prefijo: /api/progreso/"""

from django.urls import path
from . import views

urlpatterns = [
    path('',         views.RegistroProgresoListView.as_view(),   name='progreso-lista'),
    path('<int:pk>/', views.RegistroProgresoDetailView.as_view(), name='progreso-detalle'),
]
