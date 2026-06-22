"""urls.py — App productos · Prefijo: /api/productos/"""

from django.urls import path
from . import views

urlpatterns = [
    path('',               views.ProductoListView.as_view(),    name='productos-lista'),
    path('<int:pk>/',      views.ProductoDetailView.as_view(),  name='productos-detalle'),
    path('tratamientos/',  views.TratamientoListView.as_view(), name='tratamientos-lista'),
]
